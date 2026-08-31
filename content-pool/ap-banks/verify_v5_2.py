"""Structural gate for AP U.S. Government 5.2 Voter Turnout.

gov345_check plus the four usgov_anchor helpers, plus two content gates.

  _turnout_vs_choice
              This topic answers TWO questions and the whole module is built
              against running them together. EK 5.2.A.1 to 3 concern WHETHER a
              person votes; EK 5.2.A.4 concerns WHOM they vote for. The two
              lists even share an item -- demographics is in both -- which is
              exactly what makes the conflation easy, and it means a checker
              cannot simply forbid an overlap. What it can do is refuse the
              specific crossings: a key may not offer political efficacy,
              structural barriers, polling hours or registration procedures as
              an explanation of CHOICE, and may not offer party identification,
              candidate characteristics or contemporary issues as an explanation
              of TURNOUT. Neither list contains the other's distinctive items,
              so those crossings are unambiguous where demographics is not.

              The gate also counts how many keys turn on the distinction. Below
              four, the module has quietly become a turnout-only topic and has
              dropped EK 5.2.A.4.

  _definitions
              Two definitions carry this topic and both are droppable.
              POLITICAL EFFICACY is "the belief that an individual's
              participation in the political process will make a difference" --
              a BELIEF, not actual influence, not knowledge and not interest,
              which is why a person may have high efficacy and little influence.
              And EK 5.2.A.2.iii states the one DIRECTION the framework commits
              to in this topic: more turnout for presidential than midterm
              elections. Everything else is a list of things that CAN influence
              turnout, with no direction and no magnitude, so a key asserting
              that any of them always raises or lowers turnout would be adding a
              claim. The gate pins both and refuses the added direction.
"""
import gov345_check as gc
import usgov_anchor as ua
import v5_2

ANCHORS = {
 1: "Structural barriers, political efficacy, and demographics",
 2: "Polling hours and the availability of absentee ballots",
 3: "The belief that an individual's participation in the political process will make a",
 4: "whatever their actual influence turns out to be",
 5: "Political efficacy, since it is a belief the individual holds",
 6: "Differences in state-controlled elections and variations in voter registration laws",
 7: "The hours polls are open, Voter ID laws, funding for polling places and workers",
 8: "Voting by mail, absentee voting, and early voting",
 9: "Registering in person, online, or automatically",
 10: "There is more turnout for presidential elections than for midterm elections",
 11: "without stating how much each matters or in which direction",
 12: "Differences in state-controlled elections, and variations in voter registration laws",
 13: "Predict the likelihood of whether an individual will vote",
 14: "a probabilistic expectation about an individual rather than a certainty",
 15: "not only to explain differences in turnout across groups",
 16: "Voter choice",
 17: "Party identification and ideological orientation, candidate characteristics",
 18: "Demographic characteristics",
 19: "and it says nothing about whom those who vote support",
 20: "since it concerns whom voters support rather than whether they turn out",
 21: "are different decisions that different factors bear on",
 22: "and every age group turned out at a higher rate in the presidential election",
 23: "together with EK 5.2.A.1's inclusion of demographics among the influences on turnout",
 24: "so a campaign has less electoral incentive to prioritize its issues",
 25: "while more days of early voting did not always mean higher turnout",
 26: "and EK 5.2.A.2.ii's variations in registration procedures",
 27: "so no single policy's effect can be isolated",
 28: "rises with its reported level of political efficacy, from 34 percent to 83 percent",
 29: "use of political efficacy to predict the likelihood of whether an individual will vote",
 30: "and the framework treats the factors influencing voter choice separately",
}

GROUNDING = {
 1: "EK 5.2.A.1, verbatim: 'Structural barriers..., political efficacy..., and demographics can "
    "influence differences in voter turnout in the U.S.' Two are features of the system and one "
    "is a belief, which is why LO 5.2.A pairs state laws with individual choice.",
 2: "EK 5.2.A.1's own parenthesis for structural barriers: polling hours and the availability "
    "of absentee ballots.",
 3: "EK 5.2.A.1's parenthesis for political efficacy, verbatim. The framework's noun is a "
    "BELIEF.",
 4: "EK 5.2.A.1's definition read against EK 5.2.A.3's use of it to predict voting. A belief "
    "can motivate an action whether or not it is accurate.",
 5: "LO 5.2.A's INDIVIDUAL CHOICE half mapped onto EK 5.2.A.1's three influences. Structural "
    "barriers are features of how elections are run and demographics are characteristics.",
 6: "LO 5.2.A's STATE LAWS half mapped onto EK 5.2.A.2.i and ii, both of which describe rules "
    "a state sets.",
 7: "EK 5.2.A.2.i's parenthesis, verbatim: the hours polls are open, Voter ID laws, variations "
    "in funding for polling places and workers, and variations in types of voting allowed.",
 8: "EK 5.2.A.2.i's three named types of voting: voting by mail, absentee voting, early voting.",
 9: "EK 5.2.A.2.ii's parenthesis: registering in person, online, or automatically. A separate "
    "item from the types of voting in EK 5.2.A.2.i.",
 10: "EK 5.2.A.2.iii, verbatim: 'more turnout for presidential elections than midterm "
     "elections.' One of the few directional facts the framework states outright here.",
 11: "The verb CAN INFLUENCE across EK 5.2.A.1 and EK 5.2.A.2, which claims possibility rather "
     "than magnitude or direction. EK 5.2.A.2.iii is the stated exception.",
 12: "EK 5.2.A.2.i and ii applied: polling hours in the first parenthesis, online registration "
     "in the second, so the two changes fall under two different items of one list.",
 13: "EK 5.2.A.3, verbatim: these characteristics 'are used to predict the likelihood of "
     "whether an individual will vote.' Whether, not whom.",
 14: "EK 5.2.A.3's noun LIKELIHOOD, which supports an expectation rather than a rule about any "
     "individual.",
 15: "EK 5.2.A.1's claim about DIFFERENCES across groups against EK 5.2.A.3's individual-level "
     "prediction, which is a use of the first rather than a repetition of it.",
 16: "EK 5.2.A.4's own words: 'Factors influencing VOTER CHOICE include'. A different question "
     "from the one EK 5.2.A.1 to 3 answer.",
 17: "EK 5.2.A.4's four items. The distractors list turnout influences, EK 5.1.B.1's models of "
     "voting behavior, and EK 5.3.B.1's party functions.",
 18: "EK 5.2.A.1's demographics against EK 5.2.A.4.iv's demographic characteristics -- the one "
     "factor appearing in both lists, and the reason the two questions are easy to run "
     "together.",
 19: "EK 5.2.A.1 and EK 5.2.A.3: a rate of voting is a turnout measure. That demographics also "
     "appear in EK 5.2.A.4 does not convert a turnout finding into one about choice.",
 20: "EK 5.2.A.4.i, party identification, which appears nowhere in EK 5.2.A.1 to 3.",
 21: "EK 5.2.A.1 to 3 against EK 5.2.A.4: separate statements, mostly different items, and two "
     "different decisions.",
 22: "Data item, CED skill 3.C. Both columns and every row comparison are recomputed below.",
 23: "EK 5.2.A.2.iii's stated comparison as the gap between the columns, and EK 5.2.A.1's "
     "demographics as the gradient down each one.",
 24: "Data item, CED skill 3.C -- and the conclusion the CED's own sample activity for this "
     "topic draws. The reasoning runs through how many votes a group casts; the table reports "
     "turnout only, and nothing about what any group wants.",
 25: "Data item, CED skill 3.C. Both policies are compared against turnout below.",
 26: "EK 5.2.A.2.i's types of voting and EK 5.2.A.2.ii's registration procedures located as the "
     "table's two policy columns.",
 27: "CED skill 3.C, drawing a conclusion and stopping where the data does: the two policies "
     "vary together across these states, which is recomputed below.",
 28: "Data item, CED skill 3.C. Every voting share is recomputed below.",
 29: "EK 5.2.A.3's prediction located in the table, with the stem's description of efficacy "
     "matching EK 5.2.A.1's definition.",
 30: "EK 5.2.A.4 against a table whose columns both measure participation. The framework's "
     "list of factors influencing choice does not include political efficacy.",
}

PRES, MID = "Presidential election turnout (%)", "Midterm election turnout (%)"
DAYS, ONLINE, TURNOUT = ("Days of early voting offered", "Online registration available",
                         "Turnout (%)")
SAMPLE, VOTED = "Share of the sample (%)", "Share of the group who voted (%)"
LEVEL = "Reported level of political efficacy"


def _col(t, header):
    j = t["headers"].index(header)
    return [r[j] for r in t["rows"]]


def _num(t, header):
    return [gc.num(c) for c in _col(t, header)]


def q22(t):
    """Both columns rise with age, and presidential exceeds midterm in every row."""
    pres, mid = _num(t, PRES), _num(t, MID)
    assert pres == sorted(pres) and len(set(pres)) == len(pres), f"presidential column {pres}"
    assert mid == sorted(mid) and len(set(mid)) == len(mid), f"midterm column {mid}"
    assert all(p > m for p, m in zip(pres, mid)), "a row has midterm turnout at or above presidential"
    assert pres[-1] - pres[0] > 20, "the youngest and oldest groups are close in the presidential column"
    return (f"presidential {', '.join(f'{x:.0f}' for x in pres)}; midterm "
            f"{', '.join(f'{x:.0f}' for x in mid)}; presidential above midterm in all "
            f"{len(pres)} rows")


def q23(t):
    """Two patterns present: the column gap, and the gradient down each column."""
    pres, mid = _num(t, PRES), _num(t, MID)
    gaps = [p - m for p, m in zip(pres, mid)]
    assert all(g > 0 for g in gaps), f"the column gap is not positive throughout: {gaps}"
    assert pres[-1] > pres[0] and mid[-1] > mid[0], "no age gradient in one of the columns"
    return (f"column gaps {', '.join(f'{g:.0f}' for g in gaps)}; age gradient "
            f"{pres[-1] - pres[0]:.0f} points presidential, {mid[-1] - mid[0]:.0f} midterm")


def q24(t):
    """The youngest group is lowest in both columns, and far below the oldest at midterm."""
    pres, mid = _num(t, PRES), _num(t, MID)
    labels = _col(t, "Age group")
    assert pres[0] == min(pres) and mid[0] == min(mid), "the youngest group is not lowest in both"
    assert "18" in labels[0], f"the first row is {labels[0]!r}, not the youngest group"
    assert mid[0] < mid[-1] / 2, \
        f"the youngest midterm rate {mid[0]:.0f} is not far below the oldest {mid[-1]:.0f}"
    for h in t["headers"]:
        assert "issue" not in h.lower() and "favor" not in h.lower(), \
            f"column {h!r} reports preferences; this table must report turnout only"
    return (f"youngest lowest in both columns at {pres[0]:.0f} and {mid[0]:.0f}, against "
            f"{mid[-1]:.0f} for the oldest at midterm; no column reports a preference")


def q25(t):
    """Online-registration states lead both others; early voting days do not order turnout."""
    days, online, turn = _num(t, DAYS), _col(t, ONLINE), _num(t, TURNOUT)
    yes = [x for o, x in zip(online, turn) if o.strip().lower() == "yes"]
    no = [x for o, x in zip(online, turn) if o.strip().lower() == "no"]
    assert yes and no, "the online registration column does not take both values"
    assert min(yes) > max(no), f"online states {yes} do not all exceed the others {no}"
    ranked = [x for _, x in sorted(zip(days, turn))]
    assert ranked != sorted(ranked), \
        "turnout rises monotonically with early voting days, which the key denies"
    return (f"online registration states {yes} against {no}; turnout by ascending early voting "
            f"days {ranked} -- not monotonic")


def q26(t):
    """The two policy columns are a voting type and a registration procedure."""
    heads = [h.lower() for h in t["headers"]]
    assert any("early voting" in h for h in heads), f"no early voting column: {heads}"
    assert any("registration" in h for h in heads), f"no registration column: {heads}"
    assert any("turnout" in h for h in heads), f"no turnout column: {heads}"
    return "columns are early voting days, online registration, and turnout"


def q27(t):
    """The two policies vary together, so neither is isolated."""
    days, online, turn = _num(t, DAYS), _col(t, ONLINE), _num(t, TURNOUT)
    yes_days = [d for o, d in zip(online, days) if o.strip().lower() == "yes"]
    no_days = [d for o, d in zip(online, days) if o.strip().lower() == "no"]
    assert min(yes_days) > min(no_days), \
        "the two policies do not move together, so the stated confound does not hold"
    assert len(t["rows"]) == 4, f"{len(t['rows'])} states, not four"
    for h in t["headers"]:
        for other in ("population", "income", "region", "party"):
            assert other not in h.lower(), \
                f"column {h!r} controls for {other!r}, weakening the stated limitation"
    return (f"online states offer {yes_days} early voting days against {no_days} for the "
            "others -- the two policies move together, and no column reports anything else")


def q28(t):
    """Voting share rises with efficacy across the three levels."""
    levels, sample, voted = _col(t, LEVEL), _num(t, SAMPLE), _num(t, VOTED)
    assert levels == ["High", "Moderate", "Low"], f"the levels are {levels}"
    assert voted[0] > voted[1] > voted[2], f"the voting shares do not fall with efficacy: {voted}"
    assert sum(sample) == 100, f"the sample shares total {sum(sample):.0f}, not 100"
    assert voted[0] - voted[2] > 40, f"the range is only {voted[0] - voted[2]:.0f} points"
    biggest = sample.index(max(sample))
    assert voted[biggest] != max(voted), \
        "the largest group also voted at the highest rate, which the key's distractor denies"
    return (f"voting shares {', '.join(f'{x:.0f}' for x in voted)} across high, moderate and "
            f"low efficacy; sample shares total {sum(sample):.0f}")


def q29(t):
    """The table pairs a reported belief with whether people voted."""
    heads = [h.lower() for h in t["headers"]]
    assert any("efficacy" in h for h in heads), f"no efficacy column: {heads}"
    assert any("voted" in h for h in heads), f"no voting column: {heads}"
    return "a reported efficacy level beside whether the group voted -- EK 5.2.A.3's pairing"


def q30(t):
    """Both data columns measure participation; none reports a preference."""
    for h in t["headers"]:
        low = h.lower()
        for pref in ("candidate", "party", "supported", "chose", "preference"):
            assert pref not in low, \
                f"column {h!r} reports a preference, so the key's correction would not hold"
    assert any("voted" in h.lower() for h in t["headers"]), "no participation column"
    return f"columns are {', '.join(t['headers'])} -- participation only, no preference"


# --- module-specific content gates -------------------------------------------

# Items distinctive to ONE of the two lists. Demographics is deliberately absent
# from both sets, because EK 5.2.A.1 and EK 5.2.A.4.iv both name it -- that
# overlap is real content (item 18 is about it), so a gate forbidding it would
# be forbidding the framework.
_TURNOUT_ONLY = ("political efficacy", "structural barrier", "polling hours",
                 "hours polls are open", "registration procedure", "registering online",
                 "voter id law", "early voting", "absentee ballot")
_CHOICE_ONLY = ("party identification", "ideological orientation",
                "candidate characteristics", "contemporary political issues")


def _turnout_vs_choice(module):
    """Neither list's distinctive items may explain the other question."""
    bad = []
    for i, item in enumerate(module.QUESTIONS, 1):
        key = item["choices"][item["ans"]].lower()
        stem = item["q"].lower()
        # An item may legitimately NAME the wrong pairing in order to refuse it.
        refusing = any(w in key for w in ("rather than", "says nothing about", "separately",
                                          "does not include", "not"))
        if "voter choice" in key or "whom" in key:
            for t_ in _TURNOUT_ONLY:
                if t_ in key and not refusing:
                    bad.append(f"q{i} key: offers {t_!r}, a turnout factor, as bearing on "
                               "voter CHOICE. EK 5.2.A.1 to 3 concern whether a person votes; "
                               "EK 5.2.A.4 lists the factors influencing whom they vote for")
        if "turnout" in key:
            for c in _CHOICE_ONLY:
                if c in key and not refusing:
                    bad.append(f"q{i} key: offers {c!r}, an EK 5.2.A.4 choice factor, as "
                               "bearing on TURNOUT. That item appears nowhere in EK 5.2.A.1 "
                               "to 3")
        del stem
    q16 = module.QUESTIONS[15]
    if "voter choice" not in q16["choices"][q16["ans"]].lower():
        bad.append("q16: the key no longer identifies EK 5.2.A.4's subject as VOTER CHOICE")
    q13 = module.QUESTIONS[12]
    if "whether an individual will vote" not in q13["choices"][q13["ans"]].lower():
        bad.append("q13: the key no longer identifies EK 5.2.A.3's subject as WHETHER an "
                   "individual will vote")
    turn = sum(1 for item in module.QUESTIONS
               if "voter choice" in item["choices"][item["ans"]].lower()
               or "whom" in item["choices"][item["ans"]].lower())
    if turn < 4:
        bad.append(f"only {turn} keys turn on voter choice; EK 5.2.A.4 is half of this topic "
                   "and a module without it has quietly become a turnout-only one")
    if bad:
        print(f"FAIL {module.__name__} turnout vs choice")
        for b in bad:
            print("  -", b)
        raise SystemExit(1)
    print(f"OK  {module.__name__} turnout vs choice: no key crosses EK 5.2.A.1 to 3's turnout "
          f"factors with EK 5.2.A.4's choice factors, and {turn} keys turn on the distinction")


_ADDED_DIRECTION = (
    "always increases turnout", "always raises turnout", "always lowers turnout",
    "guarantees higher turnout", "every additional day of early voting",
)


def _definitions(module):
    """Efficacy stays a belief, and no direction is added beyond EK 5.2.A.2.iii's."""
    bad = []
    q3 = module.QUESTIONS[2]
    k3 = q3["choices"][q3["ans"]].lower()
    if "belief" not in k3 or "make a difference" not in k3:
        bad.append("q3: the key no longer carries EK 5.2.A.1's definition of political "
                   "efficacy as a BELIEF that participation will make a difference")
    for i, item in enumerate(module.QUESTIONS, 1):
        key = item["choices"][item["ans"]].lower()
        at = key.find("political efficacy")
        if at >= 0:
            seg = key[at:at + 120]
            for wrong in ("actual influence over policy", "level of knowledge",
                          "degree of interest"):
                if wrong in seg:
                    bad.append(f"q{i} key: redefines political efficacy as {wrong!r}; EK "
                               "5.2.A.1 defines it as a belief about one's own participation")
        for d in _ADDED_DIRECTION:
            if d in key:
                bad.append(f"q{i} key: asserts {d!r}. EK 5.2.A.1 and EK 5.2.A.2 say these "
                           "things CAN influence turnout, with no direction or magnitude; EK "
                           "5.2.A.2.iii is the only direction the framework states")
    q10 = module.QUESTIONS[9]
    k10 = q10["choices"][q10["ans"]].lower()
    if "presidential" not in k10 or "midterm" not in k10:
        bad.append("q10: the key no longer carries EK 5.2.A.2.iii's stated comparison, more "
                   "turnout for presidential than midterm elections")
    q11 = module.QUESTIONS[10]
    if "direction" not in q11["choices"][q11["ans"]].lower():
        bad.append("q11: the key no longer records that the framework's CAN INFLUENCE claims "
                   "state no direction")
    if bad:
        print(f"FAIL {module.__name__} definitions")
        for b in bad:
            print("  -", b)
        raise SystemExit(1)
    print(f"OK  {module.__name__} definitions: political efficacy stays a BELIEF, EK "
          "5.2.A.2.iii's presidential-over-midterm comparison survives, and no key adds a "
          "direction to a factor the framework only says CAN influence turnout")


ua.shape(v5_2)
ua.check(v5_2, ANCHORS, GROUNDING)
ua.notation(v5_2)
_turnout_vs_choice(v5_2)
_definitions(v5_2)
gc.check(v5_2, arith={22: q22, 23: q23, 24: q24, 25: q25, 26: q26, 27: q27,
                      28: q28, 29: q29, 30: q30})
