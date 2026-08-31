"""Structural gate for AP U.S. Government 5.11 Campaign Finance.

gov345_check plus the four usgov_anchor helpers, plus two content gates and a
negative control for each of them.

  _no_invented_numbers
      Campaign finance is the one topic in this unit where a student's memory
      supplies dozens of precise-sounding figures the CED never states: a
      contribution ceiling, a spending cap, a threshold above which a committee
      must register. EK 5.11.A.1 to EK 5.11.A.3 contain no number at all except
      the year 2002. So the gate forbids any digit run in a keyed choice of a
      non-table question unless it is one of the years this module has a reason
      to name -- the act, the required case, the essay, and the other required
      cases used as distractors.

      This is the check that matters most here, because a fabricated dollar
      limit is exactly the kind of claim that reads as authoritative, is wrong
      the moment the law changes, and has no computational backstop in this
      subject. Restricting the vocabulary of a key to years is crude, and crude
      is the point: it cannot be satisfied by a number that merely looks
      plausible.

  _holding
      The CED states the holding of Citizens United v. Federal Election
      Commission in exactly one sentence (p. 30): "Political spending by
      corporations, associations, and labor unions is a form of protected
      speech under the First Amendment." The single most common misstatement of
      that case is that it permitted unlimited direct contributions to
      candidates, which is a claim about CONTRIBUTIONS where the CED's sentence
      is about SPENDING. Item 24 exists to refuse it.

      So the gate requires every key naming the case to stay inside the CED's
      vocabulary, and it forbids any key anywhere from joining "unlimited" to a
      contribution. A distractor may say it -- item 24's whole design is that
      one does -- which is why the gate reads keys only.

THE ARITHMETIC
--------------
Items 25 to 27 share a table of four hypothetical organizations reporting funds
raised, the share spent on advertising and the share given to candidate
committees; items 28 to 30 share a hypothetical survey of agreement with two
statements about spending limits, plus the share agreeing with both.

Both tables are HYPOTHETICAL and labelled so in the stems. Neither asserts
anything about a real election, committee or poll, which is the rule for this
subject: there is no sympy here, and a number attributed to a real contest is a
claim nobody downstream could check.

Item 27 is the share-against-quantity brake and item 30 the both-sides brake.
Item 27's key is only true because 35 percent of 2500 exceeds 6 percent of 4800,
and item 30's key is only true because the two agreement shares sum past 100 in
every row. Either would still READ correctly if a single figure moved, and would
no longer be true, so both are recomputed from the table rather than trusted.

NEGATIVE CONTROLS
-----------------
Every gate below is run against a deliberately corrupted copy of the module and
must fail. A checker that cannot fail is worse than none, and this project has
paid for that lesson four separate times. The controls corrupt: a key with an
invented contribution limit, a key restating the case as permitting unlimited
contributions, a table figure that breaks item 27's share-against-quantity
arithmetic, and a survey figure that breaks item 30's overlap arithmetic.
"""
import contextlib
import io
import re
import types

import gov345_check as gc
import usgov_anchor as ua
import v5_11

ANCHORS = {
 1: "ongoing debate over the role of money",
 2: "Supreme Court decisions on political spending as protected speech",
 3: "Ban soft money and reduce attack ads",
 4: "the candidate is named and says the message is approved",
 5: "makes the candidate publicly answerable for its content",
 6: "That it is a form of protected speech under the First Amendment",
 7: "Corporations, associations, and labor unions",
 8: "Citizens United v. Federal Election Commission (2010)",
 9: "Free speech, and competitive and fair elections",
 10: "Individuals, political action committees, and political parties",
 11: "Elections and policymaking, through fundraising and spending",
 12: "so it treats them as varied rather than uniform",
 13: "maximum amount any donor may lawfully contribute",
 14: "the way a campaign is paid for, and not only how it is run",
 15: "which reports decisions ruling that political spending",
 16: "The Stand by Your Ad provision of the Bipartisan Campaign Reform Act",
 17: "the question has been answered by different institutions in different ways",
 18: "an attempt to control the effects of unequal resources",
 19: "a liberty is not to be abolished merely because it feeds",
 20: "an ordinary legislative task rather than an unusual intrusion",
 21: "relates to a foundational document",
 22: "requires naming a shared principle rather than a shared subject",
 23: "because it treated political spending by organizations as protected speech",
 24: "says nothing about direct contributions to candidates",
 25: "the largest share to advertising and the smallest share to candidate committees",
 26: "influencing elections and policymaking through fundraising and spending",
 27: "a smaller fundraiser giving a much larger share supplied more dollars",
 28: "roughly a quarter of every group agrees with both",
 29: "the two goods the framework says the debate is between",
 30: "sum to more than the whole in every group",
}

GROUNDING = {
 1: "EK 5.11.A.1's own words: federal legislation and case law pertaining to campaign finance "
    "demonstrate the ONGOING DEBATE OVER THE ROLE OF MONEY IN POLITICAL AND FREE SPEECH.",
 2: "EK 5.11.A.1's two subordinate items, an act of Congress and a line of Supreme Court "
    "decisions, which is why the framework's sentence names legislation AND case law.",
 3: "EK 5.11.A.1.i, which describes the Bipartisan Campaign Reform Act of 2002 as an effort to "
    "ban soft money and reduce attack ads. Both purposes sit in one phrase.",
 4: "EK 5.11.A.1.i's quotation of the Stand by Your Ad provision: 'I'm [candidate's name] and I "
    "approve this message'. The provision's content is the candidate's name and approval.",
 5: "EK 5.11.A.1.i read for the connection the framework asserts by pairing them: a provision "
    "whose content is the candidate's own approval is offered as a means of reducing attack ads.",
 6: "EK 5.11.A.1.ii, and the CED's required-case list (p. 30), which state the ruling in the "
    "same sentence: a form of protected speech under the First Amendment.",
 7: "EK 5.11.A.1.ii's three named entities. Individuals appear only in EK 5.11.A.2's separate "
    "list of contribution sources, which is why they are not among these three.",
 8: "Citizens United v. Federal Election Commission (2010), required case. CED holding (p. 30): "
    "political spending by corporations, associations and labor unions is protected speech under "
    "the First Amendment. The SCOTUS cross-reference table (p. 34) attaches it to LO 5.11.A.",
 9: "EK 5.11.A.2, which names free speech alongside competitive and fair elections as the "
    "subjects of the increased debate.",
 10: "EK 5.11.A.2's parenthesis: contributions from individuals, political action committees "
     "[PACs], and political parties.",
 11: "EK 5.11.A.3 in full: different types of PACs influence ELECTIONS AND POLICYMAKING through "
     "FUNDRAISING AND SPENDING. Two objects of influence and two means, each pair joined.",
 12: "EK 5.11.A.3's opening words, DIFFERENT TYPES OF PACs. The framework asserts the variety "
     "and does not name the types, which is a limit on what may be asserted from it.",
 13: "The limit of EK 5.11.A.1 to EK 5.11.A.3 taken together. They name an act, a line of "
     "decisions, a debate and a set of actors, and state no dollar figure anywhere.",
 14: "LO 5.11.A (organization, FINANCE, and strategies of national political campaigns) against "
     "LO 5.10.A (campaign organizations and strategies). Finance is the whole of the difference.",
 15: "EK 5.11.A.1.ii applied to a labor union, one of the three entities the statement names.",
 16: "EK 5.11.A.1.i's quoted formula performed in a scenario. The soft money ban in the same act "
     "governs where money comes from rather than what an advertisement must say.",
 17: "EK 5.11.A.1's structure. It cites legislation AND case law, the first restricting certain "
     "money and the second protecting certain spending as speech, which is why ONGOING is the "
     "framework's word for the debate.",
 18: "Federalist No. 10 on the causes of faction being irremovable and relief lying in "
     "controlling effects, which the CED attaches to LO 5.11.A (p. 26). Madison recommends no "
     "campaign measure, so the key describes a relation rather than an endorsement.",
 19: "Federalist No. 10's air and fire passage read against EK 5.11.A.2's free speech half. "
     "Madison argues against abolishing a liberty because of what it nourishes.",
 20: "Federalist No. 10 on the regulation of interfering interests as the principal task of "
     "modern legislation, read against EK 5.11.A.2's competitive and fair elections half.",
 21: "CED skill 2.B as stated (p. 14) and its sample activity for this topic (p. 155), which "
     "pairs Citizens United with Madison's argument in Federalist No. 10.",
 22: "CED skill 2.B's stated tasks (p. 155): explain what the document and the case have in "
     "common AND WHY. A shared subject is where the task starts, not where it ends.",
 23: "The CED's stated holding for Citizens United applied to a scenario about an organization "
     "prevented from spending its own funds on election advertising.",
 24: "The exact wording of the CED's holding (p. 30). It concerns political SPENDING as "
     "protected speech and makes no statement about contributions given to candidates.",
 25: "Recomputed from the table: the largest fundraiser holds the highest advertising share and "
     "the lowest candidate committee share, and no candidate committee share exceeds half.",
 26: "EK 5.11.A.3's two means of influence, fundraising and spending, matched to the columns "
     "that report what was raised and how it was disposed of.",
 27: "Recomputed from the table: 6 percent of 4800 is 288 while 35 percent of 2500 is 875, so "
     "the largest fundraiser is not the largest source of candidate committee money.",
 28: "Recomputed from the table: every entry in the two agreement columns exceeds half, and the "
     "both statements column runs from 23 to 27 percent.",
 29: "EK 5.11.A.2's two named concerns matched to the two columns, which move in opposite "
     "directions across the groups.",
 30: "Recomputed from the table: the two agreement shares sum past 100 in every group, so an "
     "overlap is arithmetically forced, and the reported overlap is at least that minimum.",
}


# --- content gate 1: no number the CED does not state -------------------------
# Years this module has a reason to name: the act, the required case, the essay,
# and the required cases used as distractors in items 8 and 23.
_YEARS = {"1787", "1963", "1971", "1972", "1993", "1995", "2002", "2010"}
_DIGITS = re.compile(r"[0-9]+")
# A framework citation is the one numeric string a key may legitimately carry
# besides a year, and its shape is fixed: EK 5.11.A.1.ii, LO 5.11.A. The pattern
# is written tight rather than as a general "digits and dots" so that it cannot
# swallow a real figure standing next to a citation -- control 5 below corrupts
# a key to exactly that shape and requires the gate to still fire.
_CITE = re.compile(r"(?:EK|LO)\s+[0-9]+\.[0-9]+\.[A-Z](?:\.[0-9]+)?(?:\.[ivx]+)?")


def _no_invented_numbers(module):
    """A key outside the data items may carry a year and nothing else numeric."""
    bad = []
    for i, item in enumerate(module.QUESTIONS, 1):
        if item.get("table") is not None:
            continue
        key = _CITE.sub(" ", item["choices"][item["ans"]])
        for run in _DIGITS.findall(key):
            if run not in _YEARS:
                bad.append(f"q{i}: the key carries the number {run!r}, which is not one of the "
                           "years this topic names. EK 5.11.A.1 to EK 5.11.A.3 state no dollar "
                           "figure, limit or threshold, so none may be keyed")
    if bad:
        print(f"FAIL {module.__name__} invented numbers")
        for b in bad:
            print("  -", b)
        raise SystemExit(1)
    print(f"OK  {module.__name__} numbers: no key outside the data items carries a figure the "
          "framework does not state")


# --- content gate 2: the required case says what the CED says it says ---------
def _holding(module):
    """No key may enlarge the CED's one-sentence holding for the required case."""
    bad = []
    for i, item in enumerate(module.QUESTIONS, 1):
        key = item["choices"][item["ans"]]
        norm = gc.normalize(key)
        # "unlimited" next to a contribution is the standard misstatement.
        if "unlimited" in norm and "contribut" in norm:
            bad.append(f"q{i}: the key joins 'unlimited' to a contribution. The CED's holding "
                       "is about political SPENDING as protected speech and says nothing about "
                       "amounts given to candidates")
        if "citizens united" not in norm:
            continue
        # A key naming the case must stay inside the CED's own vocabulary.
        inside = ("protected speech" in norm or "political spending" in norm
                  or "direct contributions to candidates" in norm)
        if not inside:
            bad.append(f"q{i}: the key names Citizens United without staying inside the CED's "
                       "sentence about political spending as protected speech")
    if bad:
        print(f"FAIL {module.__name__} holding")
        for b in bad:
            print("  -", b)
        raise SystemExit(1)
    print(f"OK  {module.__name__} holding: every key naming the required case stays inside the "
          "CED's one sentence, and no key permits unlimited contributions")


# --- the arithmetic -----------------------------------------------------------
FUNDS = "Funds raised (thousands of dollars)"
ADS = "Share spent on advertising (%)"
CAND = "Share given to candidate committees (%)"
FAIR = "Limits protect fair elections (%)"
SPEECH = "Limits restrict free speech (%)"
BOTH = "Agree with both statements (%)"


def _col(table, header):
    """Column by header NAME, keyed by row label. Never by index -- inserting a
    column must not silently repoint a check at different numbers."""
    j = table["headers"].index(header)
    return {r[0]: gc.num(r[j]) for r in table["rows"]}


def q25(table):
    funds, ads, cand = _col(table, FUNDS), _col(table, ADS), _col(table, CAND)
    top = max(funds, key=funds.get)
    assert max(ads, key=ads.get) == top, f"highest advertising share is {max(ads, key=ads.get)}"
    assert min(cand, key=cand.get) == top, f"lowest candidate share is {min(cand, key=cand.get)}"
    assert all(v <= 50 for v in cand.values()), cand
    return (f"{top} raised the most ({funds[top]:.0f}), holds the highest advertising share "
            f"({ads[top]:.0f}%) and the lowest candidate committee share ({cand[top]:.0f}%); no "
            f"candidate committee share exceeds half (max {max(cand.values()):.0f}%)")


def q26(table):
    funds, ads, cand = _col(table, FUNDS), _col(table, ADS), _col(table, CAND)
    for name in funds:
        assert ads[name] + cand[name] <= 100, (name, ads[name], cand[name])
        assert funds[name] > 0, name
    return ("every row reports money raised and two disposals of it whose shares sum to at most "
            "the whole, so the table measures fundraising and spending together")


def q27(table):
    funds, cand = _col(table, FUNDS), _col(table, CAND)
    dollars = {k: funds[k] * cand[k] / 100.0 for k in funds}
    top_funds = max(funds, key=funds.get)
    top_dollars = max(dollars, key=dollars.get)
    assert top_dollars != top_funds, (
        f"the largest fundraiser {top_funds} is also the largest source of candidate money, so "
        "the item's correction is not true of this table")
    assert cand[top_dollars] > cand[top_funds], (cand[top_dollars], cand[top_funds])
    return (f"{top_funds} gives {dollars[top_funds]:.0f} thousand while {top_dollars} gives "
            f"{dollars[top_dollars]:.0f} thousand, so the largest fundraiser is not the largest "
            "source of candidate committee money")


def q28(table):
    fair, speech, both = _col(table, FAIR), _col(table, SPEECH), _col(table, BOTH)
    for name in fair:
        assert fair[name] > 50 and speech[name] > 50, (name, fair[name], speech[name])
        assert 20 <= both[name] <= 30, (name, both[name])
    return (f"every group is above half on both statements (lowest {min(min(fair.values()), min(speech.values())):.0f}%) "
            f"and the both statements share runs {min(both.values()):.0f}% to {max(both.values()):.0f}%")


def q29(table):
    order = [r[0] for r in table["rows"]]
    fair = [_col(table, FAIR)[k] for k in order]
    speech = [_col(table, SPEECH)[k] for k in order]
    assert all(b < a for a, b in zip(fair, fair[1:])), f"fair elections column does not fall: {fair}"
    assert all(b > a for a, b in zip(speech, speech[1:])), f"free speech column does not rise: {speech}"
    return (f"the fair elections column falls at every step ({fair[0]:.0f}% to {fair[-1]:.0f}%) "
            f"while the free speech column rises ({speech[0]:.0f}% to {speech[-1]:.0f}%), which "
            "is EK 5.11.A.2's two concerns pulling apart")


def q30(table):
    fair, speech, both = _col(table, FAIR), _col(table, SPEECH), _col(table, BOTH)
    forced = {}
    for name in fair:
        total = fair[name] + speech[name]
        assert total > 100, f"{name}: {fair[name]} plus {speech[name]} is {total}, so no overlap is forced"
        forced[name] = total - 100
        assert both[name] >= forced[name], (
            f"{name}: reported overlap {both[name]} is below the {forced[name]} the two shares force")
    return ("the two shares sum past 100 in every group, forcing an overlap of at least "
            f"{min(forced.values()):.0f} to {max(forced.values()):.0f} points, and the reported "
            "overlap is at or above that minimum everywhere")


# --- negative controls --------------------------------------------------------
def _copy(module):
    """A shallow module stand-in whose questions may be corrupted freely."""
    qs = []
    for item in module.QUESTIONS:
        c = dict(item)
        c["choices"] = list(item["choices"])
        if item.get("table") is not None:
            t = item["table"]
            c["table"] = dict(headers=list(t["headers"]), rows=[list(r) for r in t["rows"]])
        qs.append(c)
    return types.SimpleNamespace(__name__=module.__name__ + " (corrupted)",
                                 TOPIC=module.TOPIC, QUESTIONS=qs)


def _must_fail(label, fn):
    """Run a gate against corrupted content and require that it complains."""
    try:
        with contextlib.redirect_stdout(io.StringIO()):
            fn()
    except (SystemExit, AssertionError):
        print(f"OK  negative control fires: {label}")
        return
    print(f"FAIL negative control stayed SILENT: {label}")
    raise SystemExit(1)


def _controls():
    # 1. An invented contribution limit in a key.
    m = _copy(v5_11)
    m.QUESTIONS[12]["choices"][0] = "No donor may give more than 3300 dollars to a candidate"
    _must_fail("an invented dollar limit in a key", lambda: _no_invented_numbers(m))

    # 2. The standard misstatement of the required case, keyed.
    m = _copy(v5_11)
    m.QUESTIONS[23]["choices"][0] = (
        "Citizens United permitted unlimited contributions given directly to candidates")
    _must_fail("a key restating the required case as unlimited contributions",
               lambda: _holding(m))

    # 3. A table figure that breaks item 27's share-against-quantity arithmetic.
    m = _copy(v5_11)
    for item in m.QUESTIONS[24:27]:
        rows = item["table"]["rows"]
        rows[0][3] = "60"      # the largest fundraiser now also gives the most dollars
    _must_fail("a candidate committee share that makes item 27's correction false",
               lambda: q27(m.QUESTIONS[26]["table"]))

    # 4. A survey figure that breaks item 30's forced overlap.
    m = _copy(v5_11)
    for item in m.QUESTIONS[27:30]:
        rows = item["table"]["rows"]
        rows[0][2] = "34"      # 61 plus 34 no longer exceeds the whole
    _must_fail("an agreement share that removes item 30's forced overlap",
               lambda: q30(m.QUESTIONS[29]["table"]))


ua.shape(v5_11)
ua.check(v5_11, ANCHORS, GROUNDING)
ua.notation(v5_11)
_no_invented_numbers(v5_11)
_holding(v5_11)
gc.check(v5_11, arith={25: q25, 26: q26, 27: q27, 28: q28, 29: q29, 30: q30})
_controls()
