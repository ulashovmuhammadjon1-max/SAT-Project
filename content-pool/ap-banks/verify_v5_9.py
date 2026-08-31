"""Structural gate for AP U.S. Government 5.9 Congressional Elections.

gov345_check plus the four usgov_anchor helpers, plus two content gates.

  _congressional_list
              EK 5.9.A.1 is EK 5.8.A.1's list with two items REMOVED and one
              CHANGED, and both differences are the content of this topic.

                * PARTY CONVENTIONS and THE ELECTORAL COLLEGE are absent. They
                  belong to choosing a president, so a module that carried them
                  over would be describing the wrong contest. Item 14 makes that
                  the correction and the gate refuses either in a congressional
                  key.
                * EK 5.8.A.1.v reads "General (presidential) elections"; EK
                  5.9.A.1.iv reads "General (PRESIDENTIAL AND MIDTERM)
                  elections". One added word, and it is what places
                  congressional elections in both kinds of year -- which is the
                  link to EK 5.2.A.2.iii's statement that turnout is higher in
                  presidential elections than in midterm ones. The gate refuses
                  a congressional list that drops MIDTERM.

  _relevance  Skill 5.B is supporting a claim with RELEVANT evidence, and
              RELEVANT is the word doing the work: evidence can be true,
              interesting and about congressional elections while bearing on a
              different claim than the one being made. Relevance is a RELATION
              between a piece of evidence and a particular claim, not a property
              of the evidence -- which is why item 22 asks what two students
              arguing different claims from one table each owe.

              So the gate checks that the evidence items actually pose that
              discrimination: each must offer at least one distractor that is a
              true statement about congressional elections supporting some other
              claim. An item whose wrong answers are simply false would be
              testing recall rather than skill 5.B.
"""
import gov345_check as gc
import usgov_anchor as ua
import v5_9

ANCHORS = {
 1: "and general presidential and midterm elections",
 2: "Party conventions and the Electoral College",
 3: "it is the mechanism for choosing a president and has no role in electing members",
 4: "It names general PRESIDENTIAL AND MIDTERM elections",
 5: "The same office is contested under conditions that differ",
 6: "The benefits current officeholders possess over challengers",
 7: "shape how the election is conducted and also who wins it",
 8: "The incumbency advantage phenomenon",
 9: "naming of both presidential and midterm general elections",
 10: "and EK 5.2.A.2.iii states that turnout differs between them",
 11: "Turnout, which EK 5.2.A.2.iii says is higher in presidential elections",
 12: "The incumbency advantage phenomenon, open and closed primaries, and caucuses",
 13: "the definition supplied in the presidential list applies to the term in both",
 14: "Party conventions appear in the framework's presidential list and not in its",
 15: "not merely be true and on the same subject",
 16: "The share of incumbents seeking reelection who are reelected, across several cycles",
 17: "labeled by which kind of year each was",
 18: "A comparison of primary outcomes in states using open primaries",
 19: "The frequency of elections says nothing about how incumbents fare against challengers",
 20: "Congressional elections occur in both presidential and midterm years",
 21: "so the evidence bears on a different contest",
 22: "since the same table can support different claims through different figures",
 23: "How large the incumbency advantage is",
 24: "concern choosing a president and have no counterpart in a congressional election",
 25: "at least eighty-five percent of incumbents seeking reelection were reelected",
 26: "incumbency advantage phenomenon EK 5.9.A.1.i names operates in congressional elections",
 27: "The number of states that use open rather than closed primaries",
 28: "and more seats changed party in the midterm years",
 29: "naming of general presidential and midterm elections",
 30: "differ consistently by type of year rather than varying at random",
}

GROUNDING = {
 1: "EK 5.9.A.1's four items. The distractors import party conventions and the Electoral "
    "College, which EK 5.8.A.1 assigns to presidential elections and EK 5.9.A.1 omits.",
 2: "EK 5.8.A.1's six items against EK 5.9.A.1's four. The two dropped belong to choosing a "
    "president.",
 3: "EK 5.8.B.1's account of the Electoral College as allocating electors in a presidential "
    "election, against EK 5.9.A.1's omission of it. Members of Congress are elected directly.",
 4: "EK 5.8.A.1.v against EK 5.9.A.1.iv: 'General (presidential) elections' against 'General "
    "(presidential and midterm) elections'. One added word carries the whole difference.",
 5: "EK 5.9.A.1.iv's two kinds of year read with EK 5.2.A.2.iii's turnout comparison. The "
    "office and rules are the same; the electorate that turns out is not.",
 6: "EK 5.8.A.1.i's parenthetical definition, which EK 5.9.A.1.i names for congressional "
    "elections. A comparison between an officeholder and a challenger.",
 7: "EK 5.9.A.1's phrase 'the process and outcomes', which EK 5.8.A.1 also uses. Its items "
    "cover stages of the process and a condition bearing on who wins.",
 8: "EK 5.9.A.1.i as the one item naming a condition rather than a stage, the same asymmetry "
    "EK 5.8.A.1's longer list shows.",
 9: "EK 5.9.A.1.iv and EK 5.2.A.2.iii together, which is what reaches the claim. Neither alone "
    "does: the first names two years without comparing them, the second compares turnout "
    "without mentioning Congress.",
 10: "The two statements sharing a subject -- congressional elections held in both kinds of "
     "year -- which is how a turnout statement becomes relevant to this topic.",
 11: "EK 5.2.A.2.iii's stated comparison. The framework says nothing that would make terms, "
     "seat counts, primaries or the incumbency advantage differ between the two kinds of year.",
 12: "The three items common to EK 5.8.A.1 and EK 5.9.A.1.",
 13: "EK 5.9.A.1.iii names caucuses without a parenthesis and EK 5.8.A.1.iii defines them; the "
     "framework defines a term once and uses it in both lists.",
 14: "EK 5.8.A.1.iv against EK 5.9.A.1's four items. Studying the right content for the wrong "
     "contest is the error the difference between the lists exists to prevent.",
 15: "CED skill 5.B's word RELEVANT, which names a relation between evidence and a claim "
     "rather than a property of the evidence.",
 16: "CED skill 5.B applied to a claim about how incumbents fare against challengers. The "
     "distractors are true statements about congressional elections supporting other claims.",
 17: "CED skill 5.B: the claim relates turnout to the kind of year, so the evidence has to "
     "carry both variables.",
 18: "CED skill 5.B: the claim relates a nominating method to an outcome, so relevant evidence "
     "varies the method and observes the outcome.",
 19: "CED skill 5.B on an irrelevant citation. The fact is true and about congressional "
     "elections and does not touch the comparison the claim makes.",
 20: "EK 5.9.A.1.iv, which states this outright. The other options are empirical claims about "
     "magnitudes and trends no framework statement supplies.",
 21: "EK 5.8.A.1.vi against EK 5.9.A.1's omission of the Electoral College. Skill 5.B's "
     "relevance requirement is what the citation fails.",
 22: "CED skill 5.B: relevance is a relation to a particular claim, so one table can be "
     "relevant to several claims through different figures.",
 23: "EK 5.9.A.1 read for what it omits: four things named as affecting elections, with no "
     "magnitude for any of them.",
 24: "EK 5.8.A.1 against EK 5.9.A.1. The difference in length records a real difference "
     "between the two contests rather than an editorial choice.",
 25: "Data item, CED skill 5.B. Every reelection rate is recomputed below.",
 26: "EK 5.9.A.1.i located in the table: how incumbents fare when they seek reelection.",
 27: "CED skill 5.B: a count of nominating methods says nothing about how officeholders fare "
     "against challengers. The other options all make that comparison.",
 28: "Data item, CED skill 5.B. Both columns are recomputed by type of year below.",
 29: "EK 5.9.A.1.iv's distinction as the table's type-of-year column, and EK 5.2.A.2.iii's "
     "comparison as its turnout column.",
 30: "CED skill 5.B: the claim is about a systematic difference, so the relevant evidence is "
     "that it holds in both columns and both pairs. Recomputed below.",
}

SEEKING, REELECTED, RATE = ("Incumbents seeking reelection", "Incumbents reelected",
                            "Reelection rate (%)")
YEARTYPE, TURNOUT, SEATS = ("Type of year", "Congressional turnout (%)", "Seats changing party")


def _col(t, header):
    j = t["headers"].index(header)
    return [r[j] for r in t["rows"]]


def _num(t, header):
    return [gc.num(c) for c in _col(t, header)]


def q25(t):
    """Every stated rate recomputes and none falls below 85."""
    seek, re_, rate = _num(t, SEEKING), _num(t, REELECTED), _num(t, RATE)
    for s, r, x in zip(seek, re_, rate):
        assert abs(gc.pct(r, s, 0) - x) <= 1, \
            f"{r:.0f} of {s:.0f} is {gc.pct(r, s)} percent, not the stated {x:.0f}"
        assert r < s, f"{r:.0f} reelected of {s:.0f} seeking is not fewer"
    assert min(rate) >= 85, f"the lowest rate is {min(rate):.0f}, below 85"
    assert seek != sorted(seek, reverse=True), \
        "the number seeking reelection falls monotonically, which the key's last distractor denies"
    return (f"rates {', '.join(f'{x:.0f}' for x in rate)}, all recomputing from the counts; "
            f"lowest {min(rate):.0f}")


def q26(t):
    """The table measures incumbents against reelection and nothing else."""
    heads = [h.lower() for h in t["headers"]]
    assert all("incumbent" in h or "cycle" in h or "rate" in h for h in heads), \
        f"a column measures something other than incumbency: {heads}"
    for h in heads:
        for other in ("turnout", "primary", "convention", "elector"):
            assert other not in h, f"column {h!r} concerns a different framework item"
    return "columns are incumbents seeking, incumbents reelected and the rate -- EK 5.9.A.1.i"


def q27(t):
    """The table supports an incumbent-versus-challenger comparison; no primary column."""
    heads = [h.lower() for h in t["headers"]]
    for h in heads:
        assert "primary" not in h, \
            f"column {h!r} reports a nominating method, which would make the key's distractor "\
            "relevant after all"
    seek, re_ = _num(t, SEEKING), _num(t, REELECTED)
    assert all(s > r for s, r in zip(seek, re_)), "some incumbents are not defeated in any cycle"
    return "no nominating-method column, and every cycle has incumbents who were not reelected"


def _by_type(t):
    types = [x.strip().lower() for x in _col(t, YEARTYPE)]
    turn, seats = _num(t, TURNOUT), _num(t, SEATS)
    out = {}
    for ty, tu, se in zip(types, turn, seats):
        out.setdefault(ty, []).append((tu, se))
    return out


def q28(t):
    """Turnout higher in presidential years; more seats change in midterms."""
    by = _by_type(t)
    assert set(by) == {"presidential", "midterm"}, f"the year types are {set(by)}"
    pres_t = [tu for tu, _ in by["presidential"]]
    mid_t = [tu for tu, _ in by["midterm"]]
    pres_s = [se for _, se in by["presidential"]]
    mid_s = [se for _, se in by["midterm"]]
    assert min(pres_t) > max(mid_t), f"presidential turnout {pres_t} does not exceed {mid_t}"
    assert min(mid_s) > max(pres_s), f"midterm seat changes {mid_s} do not exceed {pres_s}"
    return (f"turnout presidential {pres_t} against midterm {mid_t}; seats changing "
            f"presidential {pres_s} against midterm {mid_s}")


def q29(t):
    """The table carries a year-type column and a turnout column."""
    heads = [h.lower() for h in t["headers"]]
    assert any("type of year" in h for h in heads), f"no year-type column: {heads}"
    assert any("turnout" in h for h in heads), f"no turnout column: {heads}"
    for h in heads:
        for other in ("elector", "interest group", "platform"):
            assert other not in h, f"column {h!r} concerns a different topic"
    return "a type-of-year column beside a turnout column and a seats column"


def q30(t):
    """Both measured columns split cleanly by year type, in both pairs."""
    by = _by_type(t)
    assert all(len(v) == 2 for v in by.values()), "the two year types are not both represented twice"
    pres_t = [tu for tu, _ in by["presidential"]]
    mid_t = [tu for tu, _ in by["midterm"]]
    pres_s = [se for _, se in by["presidential"]]
    mid_s = [se for _, se in by["midterm"]]
    assert min(pres_t) > max(mid_t) and min(mid_s) > max(pres_s), \
        "the split is not clean in both columns, so the claim of a systematic difference fails"
    return ("both columns split cleanly by year type across both pairs of elections -- no "
            "overlap in either")


# --- module-specific content gates -------------------------------------------

_PRESIDENTIAL_ONLY = ("party convention", "electoral college")


def _congressional_list(module):
    """EK 5.9.A.1's four items stay four, and MIDTERM survives."""
    bad = []
    q1 = module.QUESTIONS[0]
    k1 = q1["choices"][q1["ans"]].lower()
    for part in ("incumbency advantage", "primaries", "caucuses", "midterm"):
        if part not in k1:
            bad.append(f"q1: the key has dropped {part!r} from EK 5.9.A.1's four items")
    for p in _PRESIDENTIAL_ONLY:
        if p in k1:
            bad.append(f"q1: the key includes {p!r}, which EK 5.8.A.1 assigns to presidential "
                       "elections and EK 5.9.A.1 does not list")
    q4 = module.QUESTIONS[3]
    k4 = q4["choices"][q4["ans"]].lower()
    if "midterm" not in k4 or "presidential" not in k4:
        bad.append("q4: the key no longer carries both halves of EK 5.9.A.1.iv's parenthesis, "
                   "PRESIDENTIAL AND MIDTERM")
    # No key may state that a presidential-only process affects congressional elections.
    for i, item in enumerate(module.QUESTIONS, 1):
        key = item["choices"][item["ans"]].lower()
        stem = item["q"].lower()
        refusing = ("not in" in key or "no role" in key or "different contest" in key
                    or "presidential list" in key or "not include" in key)
        if "congressional election" not in key:
            continue
        for p in _PRESIDENTIAL_ONLY:
            if p in key and not refusing:
                bad.append(f"q{i} key: brings {p!r} into congressional elections; EK 5.9.A.1 "
                           "omits it, and EK 5.8.A.1 assigns it to choosing a president")
    midterm = sum(1 for item in module.QUESTIONS
                  if "midterm" in item["choices"][item["ans"]].lower())
    if midterm < 4:
        bad.append(f"only {midterm} keys mention midterm elections; EK 5.9.A.1.iv's added word "
                   "is the one thing distinguishing this list's general elections from the "
                   "presidential list's")
    if bad:
        print(f"FAIL {module.__name__} congressional list")
        for b in bad:
            print("  -", b)
        raise SystemExit(1)
    print(f"OK  {module.__name__} congressional list: EK 5.9.A.1's four items survive, MIDTERM "
          f"appears in {midterm} keys, and no key brings party conventions or the Electoral "
          "College into a congressional election")


# True statements about congressional elections that support some OTHER claim.
# An evidence item whose wrong answers were simply false would be testing recall
# rather than skill 5.B, so each must offer at least one of these as a foil.
_TRUE_BUT_IRRELEVANT = (
    "number of states that use open", "number of states using caucuses",
    "share of eligible voters who turned out", "number of seats in the house",
    "reelection rate of incumbents", "turnout in presidential elections",
    "number of electoral votes", "share of voters who identify",
    "congressional elections are held every two years",
    "number of candidates who ran unopposed",
    # True facts about the TABLE that bear on no claim about conditions --
    # item 30's foils are of this kind rather than facts about elections.
    "four elections are reported", "reported as a percentage",
    "names no candidates", "are whole numbers",
)


def _relevance(module):
    """Evidence items must pose a relevance discrimination, not a recall one."""
    bad = []
    evidence_items = [i for i, item in enumerate(module.QUESTIONS, 1)
                      if "relevant" in item["q"].lower() and "which" in item["q"].lower()]
    if len(evidence_items) < 4:
        bad.append(f"only {len(evidence_items)} items ask which evidence is relevant; the "
                   "suggested skill for this topic is 5.B")
    for i in evidence_items:
        item = module.QUESTIONS[i - 1]
        # A NEGATIVE item inverts the burden: item 27 asks which evidence would
        # NOT be relevant, so its KEY is the true-but-irrelevant statement and
        # its distractors are all relevant. Checking its distractors for a foil
        # reported a correct item, which is the same over-match this build keeps
        # paying for -- the test has to follow the item's polarity.
        negative = "not be relevant" in item["q"].lower()
        pool = ([item["choices"][item["ans"]].lower()] if negative
                else [c.lower() for k, c in enumerate(item["choices"]) if k != item["ans"]])
        if not any(any(t in c for t in _TRUE_BUT_IRRELEVANT) for c in pool):
            where = "key" if negative else "distractors"
            bad.append(f"q{i}: the {where} contain no TRUE statement bearing on a different "
                       "claim, so the item tests recall rather than the relevance judgement "
                       "skill 5.B names")
    q15 = module.QUESTIONS[14]
    k15 = q15["choices"][q15["ans"]].lower()
    if "bear on the particular claim" not in k15:
        bad.append("q15: the key no longer defines RELEVANT as a relation between evidence and "
                   "the particular claim being made")
    q22 = module.QUESTIONS[21]
    if "different claims" not in q22["choices"][q22["ans"]].lower():
        bad.append("q22: the key no longer records that one table can be relevant to several "
                   "claims, which is what makes relevance a relation rather than a property")
    if bad:
        print(f"FAIL {module.__name__} relevance")
        for b in bad:
            print("  -", b)
        raise SystemExit(1)
    print(f"OK  {module.__name__} relevance: {len(evidence_items)} evidence items, each with a "
          "true-but-irrelevant foil, and relevance stays a relation between evidence and a "
          "particular claim")


ua.shape(v5_9)
ua.check(v5_9, ANCHORS, GROUNDING)
ua.notation(v5_9)
_congressional_list(v5_9)
_relevance(v5_9)
gc.check(v5_9, arith={25: q25, 26: q26, 27: q27, 28: q28, 29: q29, 30: q30})
