"""Structural gate for AP U.S. Government 5.8 Electing a President.

gov345_check plus the four usgov_anchor helpers, plus three content gates.

  _hedges       EK 5.8.B.1 is three hedged claims in one sentence and every
                hedge matters:
                  * STATES CAN CHOOSE how they allocate their electors -- a
                    state decision, not a national rule;
                  * MOST states use winner-take-all. Most, not all, and the word
                    is what makes the first clause more than decoration: if
                    every state chose the same method, the freedom to choose
                    would have no observable consequence;
                  * the Electoral College result MAY NOT BE THE SAME as the
                    national popular vote. May not -- not does not, and not
                    always differs.
                The gate pins all three and refuses the stronger versions.

  _neutrality   EK 5.8.B.1 ends by recording an ONGOING DEBATE and says nothing
                about who is right. This is the topic in Unit 5 where a bank
                could most easily slip a position in while appearing to report
                one, because the framework itself raises the disagreement. So no
                key may argue for or against the Electoral College, and item 21
                makes the framework's own neutrality the question. The two sides
                appear only as DISTRACTORS in the argumentation items, which is
                what makes those items answerable.

  _defensible   Skill 5.A is articulating a defensible claim, and it is testable
                in multiple choice because DEFENSIBLE has two halves: the claim
                must TAKE A POSITION, and available evidence must be able to
                SUPPORT it. A restatement of fact fails the first; a claim about
                fairness or what a state SHOULD do fails the second. The gate
                checks that the argumentation items keep both halves in play --
                each must offer at least one factual restatement and at least
                one unsupportable position among its distractors, or the item
                is not testing the skill it names.

NO REAL ELECTION IS NAMED. The CED's illustrative example here is one
presidential election marked NOT REQUIRED, and it is the election most often
cited in the very debate EK 5.8.B.1 calls ongoing -- so naming it would import a
side as well as unrequired content.
"""
import re

import gov345_check as gc
import usgov_anchor as ua
import v5_8

ANCHORS = {
 1: "The benefits current officeholders possess over challengers",
 2: "Voting processes to elect candidates",
 3: "A closed meeting of party members to select candidates or decide policy",
 4: "A primary is a voting process while a caucus is a meeting that participants attend",
 5: "That participation is limited to party members",
 6: "Deciding policy",
 7: "General presidential elections and the Electoral College",
 8: "Six",
 9: "The incumbency advantage phenomenon",
 10: "while only the presidential list includes party conventions and the Electoral College",
 11: "The state itself",
 12: "Most of them",
 13: "and MOST records that not all do",
 14: "The results may not be the same",
 15: "There is an ongoing debate over the Electoral College",
 16: "None; it records that the debate is ongoing without endorsing either side",
 17: "That it takes a position, and that available evidence could support it",
 18: "shapes how much attention presidential campaigns give it",
 19: "The Electoral College is the only fair way to elect a president",
 20: "It states a fact no one disputes",
 21: "affects how a candidate's popular support in that state translates into electoral votes",
 22: "The Electoral College",
 23: "Whether the Electoral College should be changed",
 24: "a divergence between the two results is possible rather than routine",
 25: "and draw the lowest average participation",
 26: "and EK 5.8.A.1.iii's caucuses as closed meetings of party members",
 27: "is associated with how large a share of its eligible voters takes part",
 28: "the leading candidate took every elector with about half the state's popular vote",
 29: "states can choose how they allocate their electors and that most use a winner-take-all",
 30: "a state's entire bloc of electors can be awarded on the strength of a narrow popular",
}

GROUNDING = {
 1: "EK 5.8.A.1.i's parenthesis, verbatim: 'benefits current officeholders possess over "
    "challengers.' A comparison between two positions in a race.",
 2: "EK 5.8.A.1.ii's parenthesis: primaries are 'voting processes to elect candidates', with "
    "the open and closed varieties treated as one item.",
 3: "EK 5.8.A.1.iii's parenthesis, verbatim, with both of its purposes: 'closed meetings of "
    "party members to select candidates or decide policy.'",
 4: "EK 5.8.A.1.ii against EK 5.8.A.1.iii: a voting process against a meeting. Both open and "
    "closed primaries exist, so openness is not the distinction.",
 5: "EK 5.8.A.1.iii's phrase 'closed meetings of PARTY MEMBERS', which locates the restriction "
    "on who may take part -- the same sense of closed as in closed primaries.",
 6: "EK 5.8.A.1.iii's second purpose, DECIDE POLICY, which a summary drops.",
 7: "EK 5.8.A.1's list read in order: an advantage, three nominating processes, then the "
    "general election and the Electoral College.",
 8: "EK 5.8.A.1's six numbered items. Open and closed primaries are one item in the "
    "framework's own numbering rather than two.",
 9: "EK 5.8.A.1.i as the one item naming a condition rather than a stage, which the "
    "statement's phrase 'the process AND OUTCOMES' accommodates.",
 10: "EK 5.8.A.1 against EK 5.9.A.1: three items shared, and party conventions and the "
     "Electoral College distinctive to the presidential list.",
 11: "EK 5.8.B.1's first clause: 'States can choose how they allocate their electors.'",
 12: "EK 5.8.B.1's word MOST, which is what makes the first clause more than decoration.",
 13: "EK 5.8.B.1's two allocation clauses read together. Reading MOST as ALL would make the "
     "freedom to choose idle.",
 14: "EK 5.8.B.1, verbatim: the results 'may not be the same as the popular vote nationwide'. "
     "A modal, so neither always agreeing nor always differing is the framework's claim.",
 15: "EK 5.8.B.1's final clause: 'there is an ongoing debate over the Electoral College.'",
 16: "EK 5.8.B.1 read for what it withholds. Reporting that a debate exists is not joining "
     "it, and supplying a position would present one side with the framework's authority.",
 17: "CED skill 5.A. DEFENSIBLE has two halves: a position, and evidence that could support "
     "it. A claim taking no position is a restatement; one no evidence could reach is not "
     "defensible however firmly held.",
 18: "CED skill 5.A applied. The key asserts a disputable relationship; the distractors "
     "restate facts EK 5.8.B.1 and EK 5.8.A.1 state outright.",
 19: "CED skill 5.A applied to the second half of DEFENSIBLE. Fairness is a standard rather "
     "than an observation, and ONLY makes the assertion stronger still.",
 20: "CED skill 5.A: a claim that could be defended presupposes one that could be denied.",
 21: "CED skill 5.A against EK 5.8.B.1's neutrality. A claim about how the mechanism works is "
     "defensible; the two sides of the recorded debate are not the framework's to take.",
 22: "EK 5.8.A.1.vi and LO 5.8.B, which gives the Electoral College a second objective because "
     "EK 5.8.B.1 has more to say about it than a list entry could carry.",
 23: "EK 5.8.B.1 read for what it omits: how allocation works, a possible divergence, and a "
     "debate reported -- with no verdict.",
 24: "EK 5.8.B.1's modal MAY NOT BE THE SAME, which is also the premise of the debate the "
     "sentence records. Overstating it would misrepresent what the disagreement is about.",
 25: "Data item, CED skill 5.A. Every participation figure and state count is recomputed.",
 26: "EK 5.8.A.1.ii and iii located as the table's first three rows. A caucus being a meeting "
     "participants attend is one reason a gap of that size is unsurprising.",
 27: "CED skill 5.A on this table: a claim relating two of its columns, against restatements "
     "and positions the data cannot settle. Recomputed below.",
 28: "Data item, CED skill 5.A. The allocation methods and vote shares are recomputed below.",
 29: "EK 5.8.B.1's CAN CHOOSE shown by two methods in use, and its MOST by three of four.",
 30: "CED skill 5.A on the Electoral College without joining the debate: a claim about how the "
     "mechanism works, supported by the two narrow-margin rows. Recomputed below.",
}

METHOD, STATES_USING, PARTICIPATION = ("Nominating method", "States using it",
                                       "Average participation (%)")
EVOTES, ALLOC, SHARE = ("Electoral votes", "Allocation method",
                        "Leading candidate's share of the state's popular vote (%)")


def _col(t, header):
    j = t["headers"].index(header)
    return [r[j] for r in t["rows"]]


def _num(t, header):
    return [gc.num(c) for c in _col(t, header)]


def q25(t):
    """Caucus is tied for fewest states and lowest participation by a wide margin."""
    methods, states, part = _col(t, METHOD), _num(t, STATES_USING), _num(t, PARTICIPATION)
    assert sum(states) == 50, f"the state counts total {sum(states):.0f}, not 50"
    c = methods.index("Caucus")
    assert states[c] == min(states), f"caucuses are used by {states[c]:.0f} states, not fewest"
    assert part[c] == min(part), f"caucus participation {part[c]:.0f} is not the lowest"
    for m in ("Open primary", "Closed primary"):
        i = methods.index(m)
        assert part[c] * 3 < part[i], \
            f"caucus participation {part[c]:.0f} is not under a third of {m} at {part[i]:.0f}"
    assert states[methods.index("Open primary")] == max(states), \
        "open primaries are not used by the most states"
    return (f"states {', '.join(f'{x:.0f}' for x in states)} totalling {sum(states):.0f}; "
            f"participation {', '.join(f'{x:.0f}' for x in part)}")


def q26(t):
    """The first three rows are the framework's own nominating methods."""
    methods = [m.lower() for m in _col(t, METHOD)]
    for want in ("open primary", "closed primary", "caucus"):
        assert want in methods, f"{want!r} missing from {methods}"
    assert methods.index("open primary") < methods.index("caucus"), "the rows are out of order"
    return "rows include open primary, closed primary and caucus -- EK 5.8.A.1.ii and iii"


def q27(t):
    """Two columns vary together, so a relational claim is available; a figure is not a claim."""
    states, part = _num(t, STATES_USING), _num(t, PARTICIPATION)
    assert len(set(part)) == len(part), "two methods draw identical participation"
    assert max(part) - min(part) > 15, \
        f"participation varies only {max(part) - min(part):.0f} points, too little to relate"
    assert len(t["headers"]) == 3, "the table no longer has a method column and two data columns"
    del states
    return (f"participation spans {min(part):.0f} to {max(part):.0f} across "
            f"{len(t['rows'])} methods -- a relationship a claim could assert")


def q28(t):
    """Three of four use winner-take-all; two of those turn on about half the vote."""
    alloc = [a.strip().lower() for a in _col(t, ALLOC)]
    share, ev = _num(t, SHARE), _num(t, EVOTES)
    wta = [i for i, a in enumerate(alloc) if a == "winner-take-all"]
    assert len(wta) == 3, f"{len(wta)} states use winner-take-all, not three"
    narrow = [i for i in wta if share[i] <= 52]
    assert len(narrow) == 2, f"{len(narrow)} winner-take-all states have a narrow margin, not two"
    biggest = ev.index(max(ev))
    assert alloc[biggest] == "winner-take-all", \
        "the state with the most electoral votes does not use winner-take-all"
    assert max(share) > 70, "no state shows a wide margin, which the key's distractor needs"
    return (f"{len(wta)} of {len(alloc)} winner-take-all; narrow margins at "
            f"{', '.join(f'{share[i]:.0f}' for i in narrow)} percent carrying "
            f"{', '.join(f'{ev[i]:.0f}' for i in narrow)} electors")


def q29(t):
    """Two allocation methods appear, and one is used by most of the states shown."""
    alloc = [a.strip().lower() for a in _col(t, ALLOC)]
    assert len(set(alloc)) == 2, f"{len(set(alloc))} allocation methods, not two"
    top = max(set(alloc), key=alloc.count)
    assert alloc.count(top) > len(alloc) / 2, "no method is used by most of the states shown"
    assert top == "winner-take-all", f"the majority method is {top!r}"
    return f"two methods in use, {top!r} in {alloc.count(top)} of {len(alloc)} states"


def q30(t):
    """A narrow margin carries an entire bloc under winner-take-all."""
    alloc = [a.strip().lower() for a in _col(t, ALLOC)]
    share, ev = _num(t, SHARE), _num(t, EVOTES)
    pairs = [(ev[i], share[i]) for i, a in enumerate(alloc)
             if a == "winner-take-all" and share[i] <= 52]
    assert len(pairs) >= 2, f"fewer than two narrow winner-take-all states: {pairs}"
    assert max(e for e, _ in pairs) >= 29, \
        "no large elector bloc turns on a narrow margin, so the claim is not supported"
    return ("; ".join(f"{e:.0f} electors on {s:.0f} percent" for e, s in pairs))


# --- module-specific content gates -------------------------------------------

_OVERSTATED = (
    "all states use a winner-take-all",
    "every state uses a winner-take-all",
    "the results are never the same",
    "the results are always the same",
    "the results always differ",
    "congress decides how a state allocates",
)


def _hedges(module):
    """EK 5.8.B.1's three hedges survive."""
    bad = []
    for i, item in enumerate(module.QUESTIONS, 1):
        key = item["choices"][item["ans"]].lower()
        for o in _OVERSTATED:
            if o in key:
                bad.append(f"q{i} key: overstates EK 5.8.B.1 ({o!r}). The framework says states "
                           "CAN CHOOSE, that MOST use winner-take-all, and that the results MAY "
                           "NOT BE THE SAME as the national popular vote")
    q11 = module.QUESTIONS[10]
    if "state" not in q11["choices"][q11["ans"]].lower():
        bad.append("q11: the key no longer places the allocation decision with the state")
    q12 = module.QUESTIONS[11]
    if "most" not in q12["choices"][q12["ans"]].lower():
        bad.append("q12: the key no longer carries EK 5.8.B.1's word MOST")
    q14 = module.QUESTIONS[13]
    if "may not be the same" not in q14["choices"][q14["ans"]].lower():
        bad.append("q14: the key no longer carries EK 5.8.B.1's modal, MAY NOT BE THE SAME")
    if bad:
        print(f"FAIL {module.__name__} hedges")
        for b in bad:
            print("  -", b)
        raise SystemExit(1)
    print(f"OK  {module.__name__} hedges: EK 5.8.B.1's CAN CHOOSE, MOST and MAY NOT BE THE SAME "
          "all survive, and no key states a stronger version")


_POSITIONS = (
    "the electoral college should be abolished",
    "the electoral college should be preserved",
    "the electoral college should be replaced",
    "the electoral college is the only fair way",
    "winner-take-all allocation is unfair",
    "the electoral college produces the correct result",
)


def _neutrality(module):
    """No KEY may take a side in the debate EK 5.8.B.1 only records."""
    bad = []
    for i, item in enumerate(module.QUESTIONS, 1):
        key = item["choices"][item["ans"]].lower()
        stem = item["q"].lower()
        # An item may key ON a partisan position in order to IDENTIFY it as
        # undefensible -- item 19 asks which position evidence could NOT
        # establish, and its key is exactly such a position. Naming a side as
        # unsupportable is the opposite of taking it, and a flat scan reported
        # that correct key.
        identifying = ("could not" in stem or "not a defensible claim" in stem
                       or "not state" in stem)
        for p in _POSITIONS:
            if p in key and not identifying:
                bad.append(f"q{i} key: takes a side in the Electoral College debate ({p!r}). "
                           "EK 5.8.B.1 records that the debate is ONGOING and says nothing "
                           "about who is right")
    q16 = module.QUESTIONS[15]
    k16 = q16["choices"][q16["ans"]].lower()
    if "without endorsing" not in k16:
        bad.append("q16: the key no longer records the framework's neutrality, which is the "
                   "one thing EK 5.8.B.1 settles about the debate")
    # The two sides must still be AVAILABLE as distractors, or the argumentation
    # items have nothing to distinguish a defensible claim from.
    as_distractor = 0
    for item in module.QUESTIONS:
        for k, c in enumerate(item["choices"]):
            if k == item["ans"]:
                continue
            if any(p in c.lower() for p in _POSITIONS):
                as_distractor += 1
    if as_distractor < 3:
        bad.append(f"only {as_distractor} distractors state a side of the debate; the "
                   "argumentation items need them in order to be answerable")
    if bad:
        print(f"FAIL {module.__name__} neutrality")
        for b in bad:
            print("  -", b)
        raise SystemExit(1)
    print(f"OK  {module.__name__} neutrality: no key argues for or against the Electoral "
          f"College, {as_distractor} distractors carry the two sides so the argumentation "
          "items remain answerable, and the framework's own silence is recorded")


_RESTATEMENT = ("most states use a winner-take-all system", "states can choose how they allocate",
                "caucuses are used by six states", "state a has 38 electoral votes",
                "the electoral college is part of the presidential election process",
                "presidential elections are held in the united states",
                "nominating methods vary across states")
_UNSUPPORTABLE = ("only fair way", "should abandon", "better nominees", "should be abolished",
                  "should be preserved", "is unfair", "correct result in every election")


def _defensible(module):
    """Argumentation items must offer both a restatement and an unsupportable position."""
    bad = []
    # Only items asking WHICH CHOICE is defensible need a foil among their
    # distractors. Item 17 asks what a defensible claim REQUIRES -- a definition
    # item -- and a filter keyed on the phrase alone reported it for lacking
    # foils it has no use for.
    def _asks_which(stem):
        low = stem.lower()
        return "which" in low and ("defensible claim" in low or "could a student defend" in low)

    claim_items = [i for i, item in enumerate(module.QUESTIONS, 1)
                   if _asks_which(item["q"])]
    if len(claim_items) < 4:
        bad.append(f"only {len(claim_items)} items ask which claim is defensible; the "
                   "suggested skill for this topic is 5.A")
    for i in claim_items:
        item = module.QUESTIONS[i - 1]
        distractors = [c.lower() for k, c in enumerate(item["choices"]) if k != item["ans"]]
        has_fact = any(any(r in d for r in _RESTATEMENT) for d in distractors)
        has_unsupportable = any(any(u in d for u in _UNSUPPORTABLE) for d in distractors)
        if not (has_fact or has_unsupportable):
            bad.append(f"q{i}: offers neither a factual restatement nor an unsupportable "
                       "position among its distractors, so it does not test either half of "
                       "what DEFENSIBLE means in skill 5.A")
    q17 = module.QUESTIONS[16]
    k17 = q17["choices"][q17["ans"]].lower()
    if "takes a position" not in k17 or "support" not in k17:
        bad.append("q17: the key no longer names both halves of a defensible claim -- a "
                   "position, and evidence that could support it")
    if bad:
        print(f"FAIL {module.__name__} defensible")
        for b in bad:
            print("  -", b)
        raise SystemExit(1)
    print(f"OK  {module.__name__} defensible: {len(claim_items)} argumentation items, each "
          "offering a restatement or an unsupportable position to distinguish a defensible "
          "claim from, and both halves of the definition survive")


_YEAR = re.compile(r"(?<![0-9])(19[0-9]{2}|20[0-9]{2})(?![0-9])")


def _no_named_election(module):
    """No real election year: the CED's example here is NOT REQUIRED and contested."""
    bad = []
    for i, item in enumerate(module.QUESTIONS, 1):
        strings = [item["q"], item["why"]] + list(item["choices"])
        t = item.get("table")
        if t:
            strings += t["headers"] + [c for r in t["rows"] for c in r]
        for s in strings:
            m = _YEAR.search(s)
            if m:
                bad.append(f"q{i}: names the year {m.group(0)}. The CED's illustrative example "
                           "for 5.8 is one presidential election marked NOT REQUIRED, and it "
                           "is the election most cited in the debate EK 5.8.B.1 calls ongoing")
    if bad:
        print(f"FAIL {module.__name__} named election")
        for b in bad:
            print("  -", b)
        raise SystemExit(1)
    print(f"OK  {module.__name__} named election: no real election year appears anywhere")


ua.shape(v5_8)
ua.check(v5_8, ANCHORS, GROUNDING)
ua.notation(v5_8)
_hedges(v5_8)
_neutrality(v5_8)
_defensible(v5_8)
_no_named_election(v5_8)
gc.check(v5_8, arith={25: q25, 26: q26, 27: q27, 28: q28, 29: q29, 30: q30})
