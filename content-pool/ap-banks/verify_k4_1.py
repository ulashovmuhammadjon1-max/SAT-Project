"""Structural gate for AP Comparative Government 4.1 Electoral Systems and Rules.

The politics is checked by a human against the CED; the citations are in the
module header. What is checked here is the shape of the module and, for the six
questions carrying a table, the arithmetic -- recomputed from the table's own
cells rather than from the number written in the keyed choice, so a typo in
either place is a disagreement rather than a matched pair of errors.

The six tables and what each recomputes:
    q4   200 of (300 + 200) party-list seats is 40 percent of Mexico's Chamber
         of Deputies.
    q5   3 senators from each of 36 Nigerian states is 108 members.
    q10  the four hypothetical party votes total 100,000 and the leader's
         41,000 is 41 percent, leaving 59 percent unrepresented in the district.
    q13  exactly one of the three rows describes indirect selection, and two
         name single-member districts -- a count, not a sum, but still a claim
         the key makes about the table.
    q21  (300 + 200) + (96 + 32) is 628 members of the Congress of the Union.
    q22  200/500 = 40 percent against 32/128 = 25 percent, so the Chamber of
         Deputies is the more proportional chamber.
"""
import k_verify_util as kv
import k4_1


def q4(item):
    t = item["table"]
    seats = [int(v.replace(",", "")) for v in kv.column(t, "Seats")]
    total = sum(seats)
    assert total == 500, f"seat total is {total}"
    pr = int(kv.cell(t, "Proportional representation party list", "Seats"))
    pct = 100 * pr / total
    assert abs(pct - 40) < 1e-9, f"party-list share is {pct}"
    assert "40 percent" == item["choices"][item["ans"]], "key is not the 40 percent choice"


def q5(item):
    t = item["table"]
    states = int(kv.cell(t, "States", "Number"))
    per_state = int(kv.cell(t, "Senators directly elected from each state", "Number"))
    assert states * per_state == 108, f"{states} x {per_state} is not 108"
    assert kv.nums(item["choices"][item["ans"]]) == [108.0], "key is not 108"


def q10(item):
    t = item["table"]
    votes = [int(v.replace(",", "")) for v in kv.column(t, "Votes")]
    total = sum(votes)
    assert total == 100000, f"votes total {total}"
    lead = max(votes)
    assert lead == 41000, f"leading party polled {lead}"
    assert votes.index(lead) == 0, "the leading party is not the first row"
    share = 100 * lead / total
    assert abs(share - 41) < 1e-9, f"leader's share is {share}"
    key = item["choices"][item["ans"]]
    assert kv.nums(key) == [41.0, 59.0], f"key states {kv.nums(key)}"
    assert abs((100 - share) - 59) < 1e-9, "the complement is not 59 percent"


def q13(item):
    t = item["table"]
    how = kv.column(t, "How members are chosen")
    assert len(how) == 3, f"{len(how)} rows, expected three"
    indirect = [h for h in how if h.lower().startswith("indirectly")]
    assert len(indirect) == 1, f"{len(indirect)} rows describe indirect selection"
    smd = [h for h in how if "single-member district" in h.lower()]
    assert len(smd) == 2, f"{len(smd)} rows name single-member districts"
    pr = [h for h in how if "proportional representation" in h.lower()]
    assert len(pr) == 1, f"{len(pr)} rows name proportional representation"


def _mexico(t):
    dep_d = int(kv.cell(t, "Chamber of Deputies", "Seats filled in districts"))
    dep_p = int(kv.cell(t, "Chamber of Deputies", "Seats filled by proportional representation"))
    sen_d = int(kv.cell(t, "Chamber of Senators", "Seats filled in districts"))
    sen_p = int(kv.cell(t, "Chamber of Senators", "Seats filled by proportional representation"))
    return dep_d, dep_p, sen_d, sen_p


def q21(item):
    dep_d, dep_p, sen_d, sen_p = _mexico(item["table"])
    total = dep_d + dep_p + sen_d + sen_p
    assert total == 628, f"the two chambers total {total}"
    assert kv.nums(item["choices"][item["ans"]]) == [628.0], "key is not 628"


def q22(item):
    dep_d, dep_p, sen_d, sen_p = _mexico(item["table"])
    dep_share = 100 * dep_p / (dep_d + dep_p)
    sen_share = 100 * sen_p / (sen_d + sen_p)
    assert abs(dep_share - 40) < 1e-9, f"deputies' list share is {dep_share}"
    assert abs(sen_share - 25) < 1e-9, f"senators' list share is {sen_share}"
    assert dep_share > sen_share, "the Chamber of Deputies is not the more proportional chamber"
    key = kv.nums(item["choices"][item["ans"]])
    assert key == [200.0, 500.0, 32.0, 128.0], f"key cites {key}"


kv.check(k4_1, tables={4: q4, 5: q5, 10: q10, 13: q13, 21: q21, 22: q22})
