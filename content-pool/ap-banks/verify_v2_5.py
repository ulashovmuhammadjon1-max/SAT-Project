"""Structural gate for AP U.S. Government 2.5 Checks on the Presidency.

ANCHORS, GROUNDING and the notation check via usgov_anchor, then usgov_check
with the six data items recomputed from their own tables.

THREE CLAIMS THAT MUST NOT DRIFT, AND HOW EACH IS HELD
-------------------------------------------------------
1. EK 2.5.A.1.iii says SOME positions within the Executive Office of the
   President are subject to confirmation. Not all, not none. Item 5's keyed
   choice is the word "some", and _some_positions below asserts that no key and
   no rationale in this module generalises it in either direction. A paraphrase
   that drops the quantifier is the ordinary way a bank turns a careful CED
   sentence into a false one.

2. EK 2.5.A.2's claim is about DURATION -- judicial appointments are the
   president's "longest lasting influence" -- not about importance. Item 13
   exists to make a student refuse the stronger reading, and the GROUNDING
   entries for items 10 to 14 all say "duration" so a later editor can see at a
   glance that the module never upgraded the claim.

3. EK 2.5.A.3 supplies the CED's own definition of the congressional agenda:
   "the formal list of policies Congress is considering at any given time."
   Item 16 keys on that phrase and _some_positions also checks it survives.

THE CONFOUND IN THE EXECUTIVE-ORDER TABLE IS DELIBERATE
--------------------------------------------------------
Items 24 to 26 use a table where unified control occupies Years 1 and 2 and
divided control Years 3 and 4. That is a perfect confound between party control
and time in office, and item 26 is the item that asks a student to see it. A
table built to be clean would have made item 26 impossible; a table built to be
confounded without an item pointing at the confound would be a defect. The
check below confirms the confound is exactly as described -- that the divided
years really are the later ones -- so the item cannot be quietly broken by
reordering rows.
"""
import usgov_anchor as ua
import usgov_check as uc
import v2_5

ANCHORS = {
 1: "an important check on the president's appointment powers",
 2: "personal household staff",
 3: "with conflict arising from who was chosen",
 4: "Court of Appeals judges and District Court judges are all subject",
 5: "Some of them are subject to Senate confirmation",
 6: "by inaction as effectively as by a vote against it",
 7: "The president chooses the nominee and the Senate decides",
 8: "even when doing so obstructs a president of their own party",
 9: "also slows the staffing of the executive branch",
 10: "In life-tenured judicial appointments",
 11: "may serve for decades after the appointing president has left office",
 12: "That the president's longest lasting influence lies in life-tenured",
 13: "a claim about duration rather than about importance",
 14: "an error cannot be corrected at the next election",
 15: "the formal list of policies Congress is considering at any given time",
 16: "Use executive orders and directives to the bureaucracy",
 17: "only what existing law and existing appropriations already permit",
 18: "has led the president to act through the bureaucracy instead",
 19: "removes or narrows the authority the orders rest on",
 20: "requirement of good government, not a threat to it",
 21: "the only category on which the Senate always acted",
 22: "Inaction, not rejection",
 23: "a single presidency",
 24: "more executive orders in each divided-control year",
 25: "can lead a president to use executive orders to address his own agenda items",
 26: "time in office and party control cannot be separated",
 27: "senators of the president's own party may object",
 28: "where their legislative proposals have failed",
 29: "makes a nominee's views a legitimate subject of the check",
 30: "give each side a decision the other cannot make alone",
}

GROUNDING = {
 1: "EK 2.5.A.1 and EK 2.5.A.2 both open with it: 'Senate confirmation is an important check "
    "on appointment powers.' The House has no role; U.S. Constitution Art. II Sec. 2.",
 2: "EK 2.5.A.1's four-item list, tested by exclusion. Household staff appear nowhere on it.",
 3: "EK 2.5.A.1: conflict arises 'based on who is chosen by the president for appointments.'",
 4: "EK 2.5.A.1.iv names Supreme Court Justices, Court of Appeals judges AND District Court "
    "judges in one item, so the check reaches the whole federal bench.",
 5: "EK 2.5.A.1.iii: 'SOME positions within the Executive Office of the President.' The "
    "quantifier is the framework's own and both generalisations are false.",
 6: "EK 2.5.A.1 read for what a check is: an instrument that prevents the appointment, "
    "whether by rejection or by never scheduling a vote.",
 7: "U.S. Constitution Art. II Sec. 2, the Appointments Clause, quoted verbatim. The split "
    "between nomination and appointment is what makes confirmation a check.",
 8: "Federalist No. 51 (required document), 'Ambition must be made to counteract ambition,' "
    "quoted verbatim; the CED attaches Federalist No. 51 to 2.5.A.",
 9: "EK 2.5.A.1's 'potential for conflict' seen as a cost: the same check that screens "
    "nominees also delays staffing. Nothing requires the Senate to act within a period.",
 10: "EK 2.5.A.2, verbatim: 'the president's longest lasting influence lies in life-tenured "
     "judicial appointments.' A claim about DURATION.",
 11: "EK 2.5.A.2's reason, life tenure, supplied by U.S. Constitution Art. III Sec. 1, office "
     "held during good behavior. Judicial appointments DO require confirmation (EK 2.5.A.1.iv).",
 12: "EK 2.5.A.2 shown as a contrast in DURATION: revoked orders against sitting judges.",
 13: "EK 2.5.A.2 read precisely. 'Longest lasting' is duration; reading it as a ranking of "
     "importance imports a claim the framework does not make.",
 14: "EK 2.5.A.1's check plus EK 2.5.A.2's life tenure: the Senate's decision on a judge is "
     "close to final because no election revisits it. No supermajority is required.",
 15: "EK 2.5.A.3's own parenthesis: the congressional agenda is 'the formal list of policies "
     "Congress is considering at any given time.' Congress's list, not the president's.",
 16: "EK 2.5.A.3, verbatim: policy conflicts 'can lead the president to use executive orders "
     "and directives to the bureaucracy to address the president's own agenda items.'",
 17: "EK 2.5.A.3's instruments bounded by EK 2.4.A.2.iv: an order rests on vested or "
     "delegated power and cannot create authority or appropriations Congress withheld.",
 18: "EK 2.5.A.3's sequence exactly: conflict with what Congress is considering, then "
     "executive action. An order does not become a statute.",
 19: "EK 2.4.A.2.iv: orders rest on vested or delegated power, so withdrawing the delegation "
     "strikes the source. Federal courts issue no advisory opinions.",
 20: "Federalist No. 70 (required document), quoted verbatim; the CED attaches Federalist "
     "No. 70 to 2.5.A. Hamilton argues against a PLURAL executive, not against checks.",
 21: "Data item; the zero in the Cabinet no-action cell is recomputed below.",
 22: "Data item; the totals for inaction against rejection are recomputed below.",
 23: "Data item, CED skill 3.E: one administration supplies no baseline for calling a "
     "pattern unusual.",
 24: "Data item; every divided year is compared with every unified year below.",
 25: "EK 2.5.A.3 seen as data: more executive orders under divided control, which is when "
     "policy conflict with the congressional agenda is likeliest.",
 26: "Data item, CED skill 3.E: unified control occupies Years 1 and 2 and divided control "
     "Years 3 and 4, so party control and time in office are perfectly confounded here.",
 27: "EK 2.5.A.1 locates conflict in WHO IS CHOSEN rather than in party control, so a "
     "unified Senate can still balk at a nominee.",
 28: "EK 2.5.A.3 operationalized: compare executive action across subjects where the "
     "legislative route succeeded and failed.",
 29: "EK 2.5.A.1: the potential for conflict arises from who is chosen, which makes the "
     "nominee's views rather than competence alone a legitimate subject of the check.",
 30: "U.S. Constitution Art. II Sec. 2's split between nomination and consent, which "
     "EK 2.5.A.1 identifies as the site of confrontation.",
}

CONF, REJ, NONE = "Confirmed", "Rejected or withdrawn", "No action taken"
CAB, AMB, COA, DIST = ("Cabinet members", "Ambassadors", "Court of Appeals judges",
                       "District Court judges")
CONTROL, ORDERS = "Party control of Congress", "Executive orders issued"


def _control(t, year):
    j = t["headers"].index(CONTROL)
    for row in t["rows"]:
        if row[0] == year:
            return row[j]
    raise KeyError(year)


TABLE_CHECKS = {
 21: [
  ("the Cabinet row is the only one with no lapsed nominations",
   lambda t: uc.cell(t, CAB, NONE) == 0
   and sum(1 for lab in uc.labels(t) if uc.cell(t, lab, NONE) == 0) == 1),
  ("in the other three rows inaction OUTNUMBERS rejection, so 'more rejected than "
   "left without action' is false in every category but the Cabinet",
   lambda t: all(uc.cell(t, lab, NONE) > uc.cell(t, lab, REJ)
                 for lab in (AMB, COA, DIST))),
  ("District Court confirmations exceed Court of Appeals confirmations, so that "
   "distractor reverses the table",
   lambda t: uc.cell(t, DIST, CONF) > uc.cell(t, COA, CONF)),
  ("every category records at least two rejections or withdrawals, so 'no nomination "
   "was rejected' is false",
   lambda t: min(uc.col(t, REJ)) >= 2),
 ],
 22: [
  ("100 nominations lapsed against 20 rejected or withdrawn, so inaction defeats five "
   "times as many nominees as rejection",
   lambda t: sum(uc.col(t, NONE)) == 100 and sum(uc.col(t, REJ)) == 20
   and sum(uc.col(t, NONE)) == 5 * sum(uc.col(t, REJ))),
  ("confirmations exceed rejections and lapses combined in every row, so 'rejects more "
   "than it confirms' is false everywhere",
   lambda t: all(uc.cell(t, lab, CONF) > uc.cell(t, lab, REJ) + uc.cell(t, lab, NONE)
                 for lab in uc.labels(t))),
  ("judicial rows show both rejections and lapses, so 'confirms every judicial nominee "
   "it considers' is false",
   lambda t: uc.cell(t, COA, REJ) > 0 and uc.cell(t, DIST, REJ) > 0),
  ("the Cabinet row differs from the judicial rows on inaction, so 'treats them "
   "identically' is false",
   lambda t: uc.cell(t, CAB, NONE) != uc.cell(t, DIST, NONE)),
 ],
 23: [
  ("two judicial categories and a confirmed column are present, so those two "
   "distractors are false on the table's face",
   lambda t: {COA, DIST} <= set(uc.labels(t)) and CONF in t["headers"]),
  ("every cell is a whole count rather than a percentage. Note that the no-action "
   "column happens to total exactly 100 -- a coincidence, not a distribution, and "
   "the reason this check does NOT test 'no column sums to 100' the way the other "
   "count tables in this bank do",
   lambda t: all(c.isdigit() for row in t["rows"] for c in row[1:])
   and sum(uc.col(t, NONE)) == 100 and sum(uc.col(t, CONF)) == 296),
 ],
 24: [
  ("every divided-control year exceeds every unified-control year",
   lambda t: min(uc.cell(t, y, ORDERS) for y in uc.labels(t)
                 if _control(t, y) == "Divided")
   > max(uc.cell(t, y, ORDERS) for y in uc.labels(t)
         if _control(t, y) == "Unified")),
  ("the four years differ, so 'the same in every year' is false",
   lambda t: len(set(uc.col(t, ORDERS))) == 4),
  ("the final year is the highest, so 'fewer in the final year than in the first' is "
   "false",
   lambda t: uc.cell(t, "Year 4", ORDERS) == max(uc.col(t, ORDERS))),
  ("both control conditions appear, so 'divided in every year' is false",
   lambda t: {"Unified", "Divided"} == {_control(t, y) for y in uc.labels(t)}),
 ],
 25: [
  ("the divided years average roughly twice the unified years, which is the pattern "
   "EK 2.5.A.3 would predict",
   lambda t: sum(uc.cell(t, y, ORDERS) for y in uc.labels(t)
                 if _control(t, y) == "Divided")
   > 1.8 * sum(uc.cell(t, y, ORDERS) for y in uc.labels(t)
               if _control(t, y) == "Unified")),
  ("no column reports confirmations, judicial appointments or vetoes, so those "
   "distractors cite data the table does not carry",
   lambda t: [h for h in t["headers"][1:]] == [CONTROL, ORDERS]),
 ],
 26: [
  ("the confound is exactly as the key describes: the two unified years are the FIRST "
   "two and the two divided years the LAST two, so control and tenure move together",
   lambda t: [_control(t, y) for y in uc.labels(t)]
   == ["Unified", "Unified", "Divided", "Divided"]),
  ("the orders column also rises monotonically, which is why time in office is as good "
   "an explanation as party control for these four points",
   lambda t: uc.col(t, ORDERS) == sorted(uc.col(t, ORDERS))),
  ("both variables and four years are present, and the counts are not percentages",
   lambda t: len(t["rows"]) == 4 and ORDERS in t["headers"]
   and sum(uc.col(t, ORDERS)) != 100),
 ],
}


def _quantifiers(module):
    """The CED's careful wording must survive in the text students are told is true."""
    bad = []
    for i, item in enumerate(module.QUESTIONS, 1):
        for label, s in (("key", item["choices"][item["ans"]]), ("why", item["why"])):
            low = s.lower()
            if "executive office of the president" in low:
                if "some" not in low:
                    bad.append(f"q{i} {label}: names the Executive Office of the President "
                               "without EK 2.5.A.1.iii's quantifier 'some'")
            # Narrow on purpose. An earlier version flagged any co-occurrence of
            # "longest lasting" and "importan", and fired on two rationales whose
            # whole job is to SAY the claim is not about importance. What must
            # never appear is the upgraded claim itself.
            if "longest lasting" in low and "most important" in low:
                if not any(n in low for n in ("rather than", "not the most important",
                                              "does not", "is not")):
                    bad.append(f"q{i} {label}: upgrades EK 2.5.A.2's duration claim into "
                               "a claim about importance")
    agenda = module.QUESTIONS[14]
    if "formal list of policies Congress is considering" not in agenda["choices"][agenda["ans"]]:
        bad.append("q15: the keyed choice no longer carries EK 2.5.A.3's own definition "
                   "of the congressional agenda")
    if bad:
        print(f"FAIL {module.__name__} quantifiers")
        for b in bad:
            print("  -", b)
        raise SystemExit(1)
    print(f"OK  {module.__name__} quantifiers: EK 2.5.A.1.iii's 'some', EK 2.5.A.2's "
          "duration claim and EK 2.5.A.3's definition all intact in the keys")


ua.shape(v2_5)
ua.check(v2_5, ANCHORS, GROUNDING)
ua.notation(v2_5)
_quantifiers(v2_5)
uc.check(v2_5, TABLE_CHECKS)

# WHAT THE REVIEW FOUND
# ---------------------
# No wrong key. The decision worth recording is the executive-order table in
# items 24 to 26, which is deliberately CONFOUNDED: unified control occupies the
# first two years and divided control the last two, so party control and time in
# office cannot be separated in it. That would be a defect in a table whose
# items all asked what the data show. Here item 26 asks the student to find the
# confound, which is CED skill 3.E, and the check above asserts the row order is
# exactly what that item claims -- so reordering the rows to "clean up" the table
# fails this file rather than silently making item 26 unanswerable.
#
# A table can be honest in two ways: by supporting the inference, or by making
# the reason it does not support the inference the thing being taught. What it
# may never be is confounded with no item saying so.
#
# Two smaller things, both caught by running the file rather than by reading:
#
#   * Item 22's second choice originally read "Rejection is the Senate's most
#     common way of defeating a nomination," which is the keyed choice minus its
#     first two words -- usgov_check's superset test caught it. A choice wholly
#     contained in another is unanswerable, because a student who believes the
#     shorter one must also believe the longer.
#   * The no-action column of the confirmation table happens to total exactly
#     100 (0 + 37 + 19 + 44). It is a coincidence, not a distribution, and a
#     boilerplate "no column sums to 100" check fired on it. The check now
#     asserts the real totals instead, and says why, so the next module's author
#     does not copy a check that is wrong here.
