"""Structural gate for AP U.S. Government 4.6 Evaluating Public Opinion Data.

gov345_check plus the four usgov_anchor helpers, plus two content gates.

  _two_factors  EK 4.6.A.1 names two factors that affect the relationship
                between scientific polling and outcomes:
                    i.  the IMPORTANCE OF PUBLIC OPINION as a source of
                        political influence IN A GIVEN election or debate
                    ii. the RELIABILITY AND VERACITY of the data
                Only the second is about the poll. The first is about the
                political setting -- how much opinion actually bears on the
                decision at issue -- and it is the half that disappears, because
                topic 4.5 was entirely about how polls are produced and a reader
                arrives here primed to evaluate data. Collapsing 4.6 into more
                data quality is the error the whole module is written against.

                So the gate does two things. It refuses any key that assigns a
                poll-and-outcome mismatch to the data alone, since EK 4.6.A.1
                makes that mismatch equally consistent with opinion not being
                decisive. And it pins both halves of "reliability AND veracity",
                which are not synonyms: a leading question reliably produces the
                same distorted answer, which is consistent and not truthful.

  _no_named_election
                The CED lists three elections against this topic and marks all
                three ILLUSTRATIVE EXAMPLES (NOT REQUIRED). Naming one would put
                content the exam cannot ask about beside content it can -- the
                same refusal 3.13 makes about its four cases. The temptation is
                stronger here than anywhere else in the bank, because the famous
                polling misses are the first thing anyone reaches for when the
                subject is whether polls can be trusted, and they would make
                vivid items. The gate refuses any year from 1900 onward and any
                real candidate surname, and item 16 makes the required-versus-
                illustrative distinction the question instead.

WHY THE FIRST TWO TABLES ARE A MATCHED PAIR
-------------------------------------------
The polls-and-outcomes table varies only the DATA question: did the polling hold
up. The support-and-adoption table stipulates that the polls were well conducted
and varies the INFLUENCE question: did majority support decide anything. Item 27
is the hinge of the topic -- accurate data still failed to predict adoption, and
EK 4.6.A.1 names that as a separate factor rather than as evidence the poll was
wrong. The arithmetic checks assert that each table really does isolate its own
factor, which is what makes the pair mean anything.
"""
import re

import gov345_check as gc
import usgov_anchor as ua
import v4_6

ANCHORS = {
 1: "The importance of public opinion as a source of political influence in a given case",
 2: "The importance of public opinion as a source of political influence in a given election",
 3: "varies from case to case rather than being fixed",
 4: "which may be limited whatever the data show",
 5: "Whether the same procedure applied again would produce the same result",
 6: "as when a leading question reliably produces the same distorted answer",
 7: "and whether public opinion is the kind of influence that bears on the outcome",
 8: "so the natural reading of this one is more about data quality",
 9: "because accuracy concerns the second factor and relevance to the outcome concerns",
 10: "The importance of public opinion as a source of influence in that particular debate",
 11: "and that public opinion carries weight in the case at issue",
 12: "neither poll is thereby shown to lack reliability or veracity",
 13: "and the two possibilities have to be distinguished",
 14: "The extent to which the decision at issue is responsive to what the public wants",
 15: "the exam will not require knowledge of them the way it requires the content",
 16: "Which particular elections illustrate the limits of polling",
 17: "while this topic concerns what may be concluded from polling in a particular political",
 18: "Assessed whether public opinion is an important source of influence in the case",
 19: "and is public opinion the kind of influence that would shape the outcome",
 20: "without stating how much weight either carries in any case",
 21: "which requires connecting the numbers to a claim about influence or about the data",
 22: "and lost the one in which it did not",
 23: "The reliability and veracity of public opinion data",
 24: "which is precisely where the polling never claimed a lead",
 25: "and one proposal was adopted without majority support",
 26: "The importance of public opinion as a source of political influence in a given policy",
 27: "as a factor separate from the data's reliability",
 28: "because they contacted very different numbers of people",
 29: "The reliability and veracity of public opinion data",
 30: "the lowest in the table",
}
# Items 23 and 29 both key on EK 4.6.A.1.ii's own phrase, so they carry the same
# anchor string. usgov_anchor checks an anchor against its own question's five
# choices rather than across the module, so identical anchors on different items
# are fine -- and here they are the right ones, since the framework's wording is
# what each item is testing.

GROUNDING = {
 1: "EK 4.6.A.1, verbatim: the relationship 'is affected by the: i. Importance of public "
    "opinion as a source of political influence in a given election or policy debate; ii. "
    "Reliability and veracity of public opinion data.' Only the second concerns the poll.",
 2: "EK 4.6.A.1.i read against EK 4.5.A.2's elements of methodology. Sampling and wording are "
    "properties of a poll; the weight opinion carries is a property of the political setting.",
 3: "EK 4.6.A.1.i's phrase IN A GIVEN election or policy debate, which makes the factor vary "
    "by case rather than holding in general.",
 4: "EK 4.6.A.1.i applied to a poll satisfying every element of EK 4.5.A.2. With the data "
    "question stipulated as settled, the remaining factor is the framework's first.",
 5: "EK 4.6.A.1.ii's first word. Reliability concerns consistency of the procedure, as "
    "distinct from truthfulness about what the result claims to describe.",
 6: "EK 4.6.A.1.ii's pairing read for why both words are needed: EK 4.5.A.2.ii's biased "
    "wording would produce the same slanted result every time, which is reliable and not "
    "veracious.",
 7: "LO 4.6.A's pairing of QUALITY with CREDIBILITY, answered by EK 4.6.A.1's two factors. A "
    "claim can fail either test independently.",
 8: "The order of the framework's own topics: 4.5 is entirely about how polls are produced, "
    "which is what primes a reader to read 4.6 as more of the same.",
 9: "EK 4.6.A.1's separation of the two factors, which allows them to point in different "
    "directions for a single claim.",
 10: "EK 4.6.A.1.i as the step a support-to-enactment inference skips without examining.",
 11: "LO 4.6.A's word CREDIBILITY against EK 4.6.A.1's two factors: a full showing covers "
     "both, and sample size, recency and agreement bear only on the second.",
 12: "EK 4.5.A.2.i's margin of error, which makes some divergence between sound polls "
     "expected, read against EK 4.6.A.1.ii's question about reliability and veracity.",
 13: "EK 4.6.A.1's two-part structure applied to a mismatch between a poll and an outcome, "
     "which is consistent with a failure of either factor.",
 14: "EK 4.6.A.1.i's own phrase, 'a source of POLITICAL INFLUENCE', which is a question about "
     "how the decision gets made rather than about the poll or its coverage.",
 15: "The CED's distinction between required course content and ILLUSTRATIVE EXAMPLES marked "
     "NOT REQUIRED, of which this topic lists three elections.",
 16: "EK 4.6.A.1 read for what it omits: two factors, and no election named inside the "
     "essential knowledge itself.",
 17: "EK 4.5.A.1 and EK 4.5.A.2 against EK 4.6.A.1. Both topics mention elections and policy "
     "debates, so that is not what separates them.",
 18: "EK 4.5.A.2's three elements answer EK 4.6.A.1's second factor and leave the first "
     "untouched, which LO 4.6.A's word CREDIBILITY still covers.",
 19: "LO 4.6.A's object, the quality and credibility of claims, answered by both factors.",
 20: "EK 4.6.A.1's limit: two factors named, no weight assigned, and the first factor's own "
     "wording refusing a general answer by attaching it to a GIVEN case.",
 21: "CED skill 3.D for this topic, which asks what data IMPLIES OR ILLUSTRATES rather than "
     "what it says -- a further step than description, and one that lands on EK 4.6.A.1's "
     "two kinds of claim.",
 22: "Data item, CED skill 3.D. Every lead is compared with its own margin below.",
 23: "EK 4.6.A.1.ii located in a table whose every column concerns the polling and the result.",
 24: "EK 4.5.A.2.i's margin of error applied: the one loss falls where the polling never "
     "established a leader. Recomputed below.",
 25: "Data item, CED skill 3.D. Support and adoption are cross-tabulated below.",
 26: "EK 4.6.A.1.i located in a table that stipulates sound polling and varies only whether "
     "opinion carried the debate.",
 27: "EK 4.6.A.1's two-part structure against the collapse it is written to prevent. The "
     "table's independence of support and adoption is recomputed below.",
 28: "Data item, CED skill 3.D. Every response rate is recomputed from contacts and "
     "interviews below.",
 29: "EK 4.6.A.1.ii: a response rate describes who among those contacted answered, which is a "
     "property of how the data were produced.",
 30: "Data item: ranking on attempts rather than on data. Recomputed below.",
}

LEAD, MOE, OUTCOME = ("Final lead for the polling leader (percentage points)",
                      "Reported margin of error (percentage points)",
                      "Outcome for the polling leader")
SUPPORT, ADOPTED = "Public support for the proposal (%)", "Proposal adopted?"
CONTACTED, COMPLETED, RATE = ("People contacted", "Completed an interview", "Response rate (%)")


def _col(t, header):
    j = t["headers"].index(header)
    return [r[j] for r in t["rows"]]


def _num(t, header):
    return [gc.num(c) for c in _col(t, header)]


def q22(t):
    """The leader wins exactly where the lead exceeds the margin."""
    lead, moe = _num(t, LEAD), _num(t, MOE)
    out = [o.lower() for o in _col(t, OUTCOME)]
    for l, m, o in zip(lead, moe, out):
        won = o.startswith("won")
        assert won == (l > m), \
            f"a lead of {l:.0f} against a margin of {m:.0f} produced {o!r}, breaking the pattern"
    assert any(o.startswith("lost") for o in out), "no contest was lost, so the key overstates"
    assert sum(1 for o in out if o.startswith("won")) == 3, "not three wins"
    return ("leads " + ", ".join(f"{l:.0f}" for l in lead) + " against margins "
            + ", ".join(f"{m:.0f}" for m in moe)
            + "; the leader wins exactly where the lead exceeds the margin")


def q23(t):
    """Every column concerns polling or the result, so the table isolates factor ii."""
    heads = [h.lower() for h in t["headers"]]
    assert any("lead" in h for h in heads) and any("margin" in h for h in heads), \
        f"the polling columns are missing: {heads}"
    assert any("outcome" in h for h in heads), f"no outcome column: {heads}"
    for h in heads:
        assert "support" not in h and "adopted" not in h, \
            f"column {h!r} measures influence, which belongs to the other table"
    return "columns are lead, margin and outcome -- the data question only"


def q24(t):
    """The one loss is the one contest whose lead sits inside its margin."""
    lead, moe = _num(t, LEAD), _num(t, MOE)
    out = [o.lower() for o in _col(t, OUTCOME)]
    losses = [i for i, o in enumerate(out) if o.startswith("lost")]
    assert len(losses) == 1, f"{len(losses)} losses, not one"
    i = losses[0]
    assert lead[i] < moe[i], \
        f"the loss occurred with a lead of {lead[i]:.0f} outside a margin of {moe[i]:.0f}"
    inside = [k for k in range(len(lead)) if lead[k] < moe[k]]
    assert inside == losses, f"leads inside a margin at {inside} but losses at {losses}"
    return (f"the single loss is contest {i + 1}, lead {lead[i]:.0f} inside margin "
            f"{moe[i]:.0f} -- the only contest where polling claimed no leader")


def q25(t):
    """Support and adoption do not line up, in both directions."""
    sup = _num(t, SUPPORT)
    adopted = [a.strip().lower() == "yes" for a in _col(t, ADOPTED)]
    high_not = [s for s, a in zip(sup, adopted) if s > 50 and not a]
    low_yes = [s for s, a in zip(sup, adopted) if s < 50 and a]
    assert high_not, "no majority-supported proposal failed, so the key's first clause fails"
    assert low_yes, "no minority-supported proposal passed, so the key's second clause fails"
    assert sum(adopted) == 2, f"{sum(adopted)} proposals adopted, not two"
    return (f"support {', '.join(f'{s:.0f}' for s in sup)}; majority support without adoption "
            f"at {high_not[0]:.0f}, adoption without majority support at {low_yes[0]:.0f}")


def q26(t):
    """The table measures influence, not data quality: no polling column."""
    heads = [h.lower() for h in t["headers"]]
    for h in heads:
        assert "margin" not in h and "sample" not in h and "response" not in h, \
            f"column {h!r} measures the poll, which belongs to the other tables"
    assert any("adopted" in h for h in heads), f"no outcome column: {heads}"
    return "columns are support and adoption -- the influence question only"


def q27(t):
    """Support does not order adoption, which is what makes the two factors separable."""
    sup = _num(t, SUPPORT)
    adopted = [a.strip().lower() == "yes" for a in _col(t, ADOPTED)]
    yes = [s for s, a in zip(sup, adopted) if a]
    no = [s for s, a in zip(sup, adopted) if not a]
    assert min(no) < max(yes) and min(yes) < max(no), \
        f"adoption is perfectly ordered by support ({yes} against {no}), so the item's " \
        "premise that accurate data failed to predict the outcome does not hold"
    return (f"adopted at {', '.join(f'{s:.0f}' for s in yes)} percent, not adopted at "
            f"{', '.join(f'{s:.0f}' for s in no)} -- the two ranges overlap")


def q28(t):
    """Every stated response rate recomputes; two polls tie on interviews and not on rate."""
    con, comp, rate = _num(t, CONTACTED), _num(t, COMPLETED), _num(t, RATE)
    for c, k, r in zip(con, comp, rate):
        assert abs(gc.pct(k, c) - r) < 0.5, \
            f"{k:.0f} of {c:.0f} is {gc.pct(k, c)} percent, not the stated {r:.0f}"
    ties = [i for i in range(len(comp)) for j in range(i + 1, len(comp)) if comp[i] == comp[j]]
    assert ties, "no two polls complete the same number of interviews, so the key's contrast fails"
    assert con[rate.index(min(rate))] == max(con), \
        "the lowest response rate does not belong to the largest contact pool"
    return ("response rates recompute: "
            + ", ".join(f"{k:.0f} of {c:.0f} is {r:.0f} percent"
                        for c, k, r in zip(con, comp, rate)))


def q29(t):
    """A response rate is a property of data production, not of the political setting."""
    heads = [h.lower() for h in t["headers"]]
    assert any("response rate" in h for h in heads), f"no response rate column: {heads}"
    for h in heads:
        assert "adopted" not in h and "support" not in h, \
            f"column {h!r} measures influence, which belongs to the other table"
    return "columns are contacts, interviews and response rate -- the data question only"


def q30(t):
    """The largest contact pool carries the lowest rate."""
    con, comp, rate = _num(t, CONTACTED), _num(t, COMPLETED), _num(t, RATE)
    i = con.index(max(con))
    assert rate[i] == min(rate), \
        f"the largest contact pool has rate {rate[i]:.0f}, not the minimum {min(rate):.0f}"
    assert max(con) == 20000 and comp[i] == 1000 and rate[i] == 5, \
        f"the key's figures are {max(con):.0f}, {comp[i]:.0f}, {rate[i]:.0f}"
    assert comp[i] != max(comp) or comp.count(max(comp)) > 1, \
        "the largest contact pool also completed the most interviews outright"
    return (f"largest contact pool {max(con):.0f} completed {comp[i]:.0f} interviews for "
            f"{rate[i]:.0f} percent -- the lowest rate in the table")


# --- module-specific content gates -------------------------------------------

_DATA_ONLY = (
    "the poll was certainly inaccurate",
    "the polls must have been inaccurate",
    "the data must have been flawed",
    "one of the two organizations must have fabricated",
    "must not have had majority support",
)


def _two_factors(module):
    """Both of EK 4.6.A.1's factors survive, and a mismatch is not blamed on the data."""
    bad = []
    for i, item in enumerate(module.QUESTIONS, 1):
        key = item["choices"][item["ans"]].lower()
        for phrase in _DATA_ONLY:
            if phrase in key:
                bad.append(f"q{i} key: assigns a poll-and-outcome mismatch to the data "
                           f"({phrase!r}). EK 4.6.A.1 makes that mismatch equally consistent "
                           "with public opinion not being decisive in the given case, which is "
                           "its FIRST factor")
    q1 = module.QUESTIONS[0]
    k1 = q1["choices"][q1["ans"]].lower()
    if "importance of public opinion" not in k1 or "reliability" not in k1:
        bad.append("q1: the key no longer names both of EK 4.6.A.1's factors")
    q6 = module.QUESTIONS[5]
    k6 = q6["choices"][q6["ans"]].lower()
    if "consistent" not in k6 or "truthful" not in k6:
        bad.append("q6: the key no longer distinguishes RELIABILITY from VERACITY; EK "
                   "4.6.A.1.ii names both because consistency and truthfulness come apart")
    # At least four items must turn on the first factor, or the module has
    # collapsed into topic 4.5 whatever any single key says.
    first = sum(1 for item in module.QUESTIONS
                if "importance of public opinion" in item["choices"][item["ans"]].lower()
                or "source of influence" in item["choices"][item["ans"]].lower())
    if first < 4:
        bad.append(f"only {first} keys turn on EK 4.6.A.1's FIRST factor; the module has "
                   "collapsed into an account of data quality, which is topic 4.5")
    if bad:
        print(f"FAIL {module.__name__} two factors")
        for b in bad:
            print("  -", b)
        raise SystemExit(1)
    print(f"OK  {module.__name__} two factors: both of EK 4.6.A.1's factors survive, {first} "
          "keys turn on the first, reliability and veracity stay distinct, and no key blames "
          "a poll-and-outcome mismatch on the data alone")


# A four-digit year from 1900 on, or a real candidate surname. The CED marks
# every election it lists for this topic NOT REQUIRED, and the famous polling
# misses are the first thing anyone reaches for when the subject is whether
# polls can be trusted -- which is exactly why the refusal needs a gate rather
# than an intention.
_YEAR = re.compile(r"(?<![0-9])(19[0-9]{2}|20[0-9]{2})(?![0-9])")
_SURNAMES = ("carter", "reagan", "obama", "romney", "clinton", "trump", "truman", "dewey",
             "biden", "bush", "gore", "kerry", "mccain")


def _no_named_election(module):
    """No real election, year or candidate may be named."""
    bad = []
    for i, item in enumerate(module.QUESTIONS, 1):
        strings = [("stem", item["q"]), ("why", item["why"])]
        strings += [(f"choice {'ABCDE'[k]}", c) for k, c in enumerate(item["choices"])]
        t = item.get("table")
        if t:
            strings += [("table header", h) for h in t["headers"]]
            strings += [("table cell", c) for r in t["rows"] for c in r]
        for label, s in strings:
            m = _YEAR.search(s)
            if m:
                bad.append(f"q{i} {label}: names the year {m.group(0)}. The CED marks every "
                           "election it lists for 4.6 an ILLUSTRATIVE EXAMPLE, NOT REQUIRED")
            low = s.lower()
            for name in _SURNAMES:
                if re.search(rf"(?<![a-z]){name}(?![a-z])", low):
                    bad.append(f"q{i} {label}: names {name!r}, a real candidate. This topic's "
                               "elections are illustrative examples the exam will not require")
    if bad:
        print(f"FAIL {module.__name__} named election")
        for b in bad:
            print("  -", b)
        raise SystemExit(1)
    print(f"OK  {module.__name__} named election: no real election, year or candidate is named "
          "anywhere in the module, and item 16 makes the required-versus-illustrative "
          "distinction the question instead")


ua.shape(v4_6)
ua.check(v4_6, ANCHORS, GROUNDING)
ua.notation(v4_6)
_two_factors(v4_6)
_no_named_election(v4_6)
gc.check(v4_6, arith={22: q22, 23: q23, 24: q24, 25: q25, 26: q26, 27: q27,
                      28: q28, 29: q29, 30: q30})
