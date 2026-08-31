"""Structural gate for AP U.S. Government 5.10 Modern Campaigns.

gov345_check plus the four usgov_anchor helpers, plus one content gate.

  _both_sides EK 5.10.A.1 says its four features represent the BENEFITS AND
              DRAWBACKS of modern political campaigns. That conjunction is the
              whole content of the topic, and it is the one thing a module on
              this material can most easily get wrong, because all four
              features -- consultants, cost, cycle length, social media -- are
              in ordinary use as complaints. An author who restates them
              without the framework's framing has quietly written an editorial
              and keyed it as fact.

              So the gate refuses any key that asserts modern campaigns are
              worse (or better) than earlier ones, and it requires the items
              that pose the framing question to keep both halves of the
              conjunction. Items 1, 9, 13, 14, 18, 24 and 30 all turn on it;
              the gate checks the two that state it outright.

              This is a content check a person had to decide, not one a shape
              check could find: every one of those questions is structurally
              impeccable whichever way it is keyed.

THE ARITHMETIC
--------------
Items 25-27 share a four-cycle table of campaign cost, candidate time spent
fundraising, and the small-donation share; 28-30 share a table of four campaign
activities by usage, cost per voter contacted, and the share of contacted
voters calling the message unwanted.

Both tables are HYPOTHETICAL and labelled so in the stems. Neither asserts
anything about a real election, which is the rule for this subject -- there is
no sympy here, and a number attributed to a real contest is a claim nobody can
check.

Item 27 is the causal brake and item 30 the benefit/drawback brake: the second
table is built so that social media holds the BEST figure on two measures and
the WORST on the third, which is EK 5.10.A.1's conjunction expressed as data
rather than as a sentence. The gate recomputes that shape rather than trusting
the stem, because if an edit moved a single figure the item would still read
correctly and would no longer be true.
"""
import gov345_check as gc
import usgov_anchor as ua
import v5_10

ANCHORS = {
 1: "benefits and drawbacks",
 2: "Dependence on professional consultants, rising campaign costs",
 3: "Intensive fundraising efforts",
 4: "Campaign communication and fundraising",
 5: "The duration of election cycles",
 6: "paid specialists to run their operations",
 7: "how a campaign is organized and resourced",
 8: "named for campaign communication and fundraising",
 9: "presenting them as problems states a position the framework does not take",
 10: "a campaign built from scratch each cycle would lack",
 11: "cannot afford specialists compete on unequal terms",
 12: "a longer period during which money must be raised",
 13: "quietly endorses one side",
 14: "better or worse than earlier ones",
 15: "significance asks what it shows about the claim once it does",
 16: "a route to money that does not depend on existing wealth",
 17: "consistent with more contacts and higher total cost",
 18: "the feature has both benefits and drawbacks",
 19: "explaining what each column shows about the claim is the second",
 20: "different levels of prior recognition fare as cycle length varies",
 21: "unequal resources are a standing feature of politics",
 22: "could take in a greater variety of voices",
 23: "weighing evidence on both sides rather than describing a pattern",
 24: "declines to weigh for the student",
 25: "campaign costs more than tripling",
 26: "Rising campaign costs and intensive fundraising efforts",
 27: "small donations more than tripled over the same period",
 28: "costs least per voter contacted",
 29: "The impact of and reliance on social media",
 30: "the best figures on two measures and the worst on a third",
}

GROUNDING = {
 1: "EK 5.10.A.1's own words: the four features represent the BENEFITS AND DRAWBACKS of "
    "modern political campaigns. The framework states the conjunction and weighs neither side.",
 2: "EK 5.10.A.1's four items, in the order the framework lists them.",
 3: "EK 5.10.A.1's second item, which names rising campaign costs and intensive fundraising "
    "efforts together in one phrase rather than as two separate features.",
 4: "EK 5.10.A.1's fourth item, which names social media for campaign communication AND "
    "fundraising -- two purposes in one item.",
 5: "EK 5.10.A.1's third item. It is the only one of the four naming a property of time "
    "rather than of money, people or medium.",
 6: "EK 5.10.A.1's first item read plainly. A consultant is a paid specialist, and dependence "
    "is the framework's word for the relation.",
 7: "LO 5.10.A's phrase CAMPAIGN ORGANIZATIONS AND STRATEGIES against EK 5.10.A.1's four "
    "items, two of which describe how a campaign is put together and two the conditions it "
    "works in.",
 8: "EK 5.10.A.1's fourth item as the only one carrying two stated purposes.",
 9: "EK 5.10.A.1's word REPRESENT applied to benefits AND drawbacks. A summary that keeps only "
    "the drawbacks is not a shorter statement of the framework but a different one.",
 10: "EK 5.10.A.1's first item read for the benefit half of the conjunction the framework says "
     "its features represent. The framework does not name the benefit; it says there is one.",
 11: "The same item read for the drawback half.",
 12: "EK 5.10.A.1's third item read for both halves at once, which is what the conjunction "
     "requires of every one of the four.",
 13: "EK 5.10.A.1's framing against ordinary usage. All four features circulate as complaints, "
     "so neutral-sounding restatement is where the framework's position gets lost.",
 14: "The limit of EK 5.10.A.1. It names four features and says they represent benefits and "
     "drawbacks; it reaches no verdict, so no verdict can be keyed to it.",
 15: "CED skill 5.B against skill 5.C. Relevance is a yes-or-no relation between evidence and "
     "a claim; significance is what the evidence shows once relevance is settled.",
 16: "CED skill 5.C applied to the cost feature. Evidence that qualifies a claim is neither "
     "support nor refutation, which is the distinction the item turns on.",
 17: "CED skill 5.C on a per-unit against a total measure. A fall in the cost of one contact "
     "leaves total spending undetermined, so the evidence does not reach the claim as stated.",
 18: "EK 5.10.A.1's conjunction stated as a method: evidence pointing both ways about one "
     "feature is what the framework predicts, not a contradiction to be resolved.",
 19: "CED skill 5.C, both halves. Sorting evidence is preparation; saying what the sorting "
     "shows about the claim is the skill.",
 20: "CED skill 5.B on EK 5.10.A.1's third item. The claim relates recognition to cycle "
     "length, so relevant evidence has to vary the length and observe candidates who differ in "
     "recognition.",
 21: "Federalist 10 on the varied and unequal distribution of property as the most durable "
     "source of faction, read as background to EK 5.10.A.1's cost feature rather than as a "
     "statement about campaigns, which the document does not make.",
 22: "Federalist 10 on extending the sphere, read against EK 5.10.A.1's social media item for "
     "the benefit half of the conjunction.",
 23: "The CED's assignment of an argumentation skill to this topic, which follows from EK "
     "5.10.A.1 framing its features as two-sided rather than as a trend to be measured.",
 24: "EK 5.10.A.1 as a whole: four features, each two-sided, with the weighing left undone.",
 25: "Recomputed from the table: cost 1,200 to 3,900 is 3.25 times, the small-donation share "
     "12 to 41 is more than triple, and the fundraising-time share rises at every step.",
 26: "EK 5.10.A.1's second item matched to the two columns that move together. Cost and "
     "fundraising effort are one feature in the framework, not two.",
 27: "CED skill 5.C. The small-donation share more than tripled over the same cycles, which "
     "bears on who the money comes from and so qualifies a claim about access without "
     "refuting the cost figures.",
 28: "Recomputed from the table: social media is highest on usage, lowest on cost per voter, "
     "and highest on the unwanted share -- best on two measures, worst on the third.",
 29: "EK 5.10.A.1's fourth item matched to the row the table singles out.",
 30: "EK 5.10.A.1's conjunction recovered from data. One activity holding the best and the "
     "worst figures at once is the benefits-and-drawbacks claim in numeric form.",
}


def _both_sides(module):
    """EK 5.10.A.1's conjunction must survive in the items that state it."""
    bad = []
    q1 = module.QUESTIONS[0]
    k1 = gc.normalize(q1["choices"][q1["ans"]])
    if "benefits" not in k1 or "drawbacks" not in k1:
        bad.append("q1: the key drops one half of EK 5.10.A.1's 'benefits and drawbacks'")

    q18 = module.QUESTIONS[17]
    k18 = gc.normalize(q18["choices"][q18["ans"]])
    if "both" not in k18 or "benefits" not in k18 or "drawbacks" not in k18:
        bad.append("q18: the key no longer records that one feature carries both")

    # No key anywhere may reach the verdict the framework declines to reach.
    verdicts = ("are worse than", "are better than", "have made campaigns worse",
                "have made campaigns better")
    for i, item in enumerate(module.QUESTIONS, 1):
        key = gc.normalize(item["choices"][item["ans"]])
        for v in verdicts:
            if gc.normalize(v) in key:
                bad.append(f"q{i}: the key reaches a verdict EK 5.10.A.1 does not: {v!r}")

    if bad:
        print(f"FAIL {module.__name__} both-sides")
        for b in bad:
            print("  -", b)
        raise SystemExit(1)
    print(f"OK  {module.__name__} both-sides: EK 5.10.A.1's conjunction intact, no key "
          "reaches a verdict the framework declines to reach")


COST = "Average campaign cost (thousands of dollars)"
TIME = "Candidate time spent fundraising (%)"
SMALL = "Funds from small donations (%)"
USE = "Campaigns using it (%)"
PER = "Median cost per voter (dollars)"
UNWANTED = "Contacted voters calling it unwanted (%)"


def _col(table, header):
    """Column by header NAME, keyed by row label. Never by index -- inserting a
    column must not silently repoint a check at different numbers."""
    j = table["headers"].index(header)
    return {r[0]: gc.num(r[j]) for r in table["rows"]}


def q25(table):
    cost, time, small = _col(table, COST), _col(table, TIME), _col(table, SMALL)
    order = [r[0] for r in table["rows"]]
    for name, col in (("cost", cost), ("time", time), ("small", small)):
        vals = [col[k] for k in order]
        assert all(b > a for a, b in zip(vals, vals[1:])), f"{name} does not rise at every step: {vals}"
    first, last = order[0], order[-1]
    assert cost[last] > 3 * cost[first], f"cost {cost[first]}->{cost[last]} is not more than triple"
    assert small[last] > 3 * small[first], f"small share {small[first]}->{small[last]} is not more than triple"
    return (f"all three columns rise at every step; cost {cost[first]:,.0f}->{cost[last]:,.0f} "
            f"and small donations {small[first]:.0f}%->{small[last]:.0f}% both more than triple")


def q26(table):
    cost, time = _col(table, COST), _col(table, TIME)
    order = [r[0] for r in table["rows"]]
    assert cost[order[-1]] > cost[order[0]] and time[order[-1]] > time[order[0]], (cost, time)
    return ("cost and fundraising time both rise, which is the pair EK 5.10.A.1 names as one "
            "feature rather than two")


def q27(table):
    small = _col(table, SMALL)
    order = [r[0] for r in table["rows"]]
    assert small[order[-1]] > 3 * small[order[0]], small
    return (f"the small-donation share {small[order[0]]:.0f}%->{small[order[-1]]:.0f}% more than "
            "tripled, so the qualification the key states is true of this table")


def _media(table):
    use, per, unw = _col(table, USE), _col(table, PER), _col(table, UNWANTED)
    sm = "Social media"
    assert max(use, key=use.get) == sm, f"highest usage is {max(use, key=use.get)}"
    assert min(per, key=per.get) == sm, f"lowest cost per voter is {min(per, key=per.get)}"
    assert max(unw, key=unw.get) == sm, f"highest unwanted share is {max(unw, key=unw.get)}"
    return use, per, unw, sm


def q28(table):
    use, per, unw, sm = _media(table)
    return (f"{sm} is highest on usage ({use[sm]:.0f}%), lowest on cost per voter "
            f"({per[sm]}), and highest on the unwanted share ({unw[sm]:.0f}%)")


def q29(table):
    _media(table)
    return ("the row the table singles out on all three measures is social media, EK "
            "5.10.A.1's fourth feature")


def q30(table):
    use, per, unw, sm = _media(table)
    # The whole point of the item: best on two, worst on one, in one row.
    best = sum([max(use, key=use.get) == sm, min(per, key=per.get) == sm])
    worst = 1 if max(unw, key=unw.get) == sm else 0
    assert best == 2 and worst == 1, (best, worst)
    return ("one row holds the best figure on two measures and the worst on the third, which is "
            "EK 5.10.A.1's benefits-and-drawbacks conjunction expressed as data")


ua.shape(v5_10)
ua.check(v5_10, ANCHORS, GROUNDING)
ua.notation(v5_10)
_both_sides(v5_10)
gc.check(v5_10, arith={25: q25, 26: q26, 27: q27, 28: q28, 29: q29, 30: q30})
