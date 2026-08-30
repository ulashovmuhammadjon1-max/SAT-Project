"""Structural gate for AP U.S. Government 1.1 Ideals of Democracy.

What this file can check is stated in usgov_check.py: shape, distinctness,
key-first, and -- the part that matters for a data question -- the arithmetic.
Every claim a table item's key makes about its own numbers is recomputed here
from that item's own `table`, so a number edited in the stem and forgotten in
the key cannot ship. It cannot check that Engel v. Vitale is an Establishment
Clause case; AP_US_GOV_CED.md carries the CED's own statement of every required
holding, and the module comment cites the essential-knowledge statement behind
each block of items.
"""
import usgov_check as uc
import v1_1

# Four data questions, indexes 24-27. Each entry recomputes, from the table
# alone, the claim its keyed choice makes -- and, where a distractor is
# tempting because it is *nearly* true, the negation of that distractor too.
AGE_COLS = ["Ages 18-29", "Ages 30-49", "Ages 50-64", "Ages 65 and older"]

TABLE_CHECKS = {
 24: [
  ("every row rises across the four age columns, which is the key's claim",
   lambda t: all(all(row[k] < row[k + 1] for k in range(3))
                 for row in [[uc.cell(t, lab, c) for c in AGE_COLS] for lab in uc.labels(t)])),
  ("no age group reaches 50 on 'Elected officials answer to voters', so the "
   "majority distractor is false",
   lambda t: all(uc.cell(t, "Elected officials answer to voters", c) < 50 for c in AGE_COLS)),
  ("the youngest column is the LOWEST in every row, so 'most positive' is false",
   lambda t: all(uc.cell(t, lab, "Ages 18-29") == min(uc.cell(t, lab, c) for c in AGE_COLS)
                 for lab in uc.labels(t))),
 ],
 25: [
  ("rights minus accountability is at least 17 points in every age group",
   lambda t: all(uc.cell(t, "Rights of citizens are protected", c)
                 - uc.cell(t, "Elected officials answer to voters", c) >= 17
                 for c in AGE_COLS)),
  ("that gap WIDENS with age (17, 19, 20, 21), so the narrowing distractor is false",
   lambda t: [uc.cell(t, "Rights of citizens are protected", c)
              - uc.cell(t, "Elected officials answer to voters", c)
              for c in AGE_COLS] == [17, 19, 20, 21]),
  ("rights minus limited government is under 20 points somewhere, so that "
   "distractor's 'every age group' fails",
   lambda t: any(uc.cell(t, "Rights of citizens are protected", c)
                 - uc.cell(t, "Government power is effectively limited", c) < 20
                 for c in AGE_COLS)),
 ],
 26: [
  ("consent falls exactly 7 points and the written Constitution rises exactly 5",
   lambda t: uc.cell(t, "The consent of the people", "2004 (%)")
   - uc.cell(t, "The consent of the people", "2024 (%)") == 7
   and uc.cell(t, "The Constitution as a written document", "2024 (%)")
   - uc.cell(t, "The Constitution as a written document", "2004 (%)") == 5),
  ("consent stays above 50 in 2024, so 'fell below half' is false",
   lambda t: uc.cell(t, "The consent of the people", "2024 (%)") > 50),
  ("elected officials rises 9 -> 11, which is not more than double",
   lambda t: uc.cell(t, "Elected officials once in office", "2024 (%)")
   < 2 * uc.cell(t, "Elected officials once in office", "2004 (%)")),
  ("'Not sure' does not change at all, so 'every category changed by 3+' is false",
   lambda t: uc.cell(t, "Not sure", "2004 (%)") == uc.cell(t, "Not sure", "2024 (%)")),
  ("each column still sums to 100, so the table is a complete distribution",
   lambda t: all(sum(uc.col(t, h)) == 100 for h in t["headers"][1:])),
 ],
 27: [
  ("the federal courts hold both the minimum agreement and the maximum disagreement",
   lambda t: uc.cell(t, "The federal courts", "Agree power is adequately limited (%)")
   == min(uc.col(t, "Agree power is adequately limited (%)"))
   and uc.cell(t, "The federal courts", "Disagree (%)") == max(uc.col(t, "Disagree (%)"))),
  ("three institutions, not one, have disagreement above agreement, so the "
   "'only institution' distractor is false",
   lambda t: sum(1 for lab in uc.labels(t)
                 if uc.cell(t, lab, "Disagree (%)")
                 > uc.cell(t, lab, "Agree power is adequately limited (%)")) == 3),
  ("the courts' own two figures differ by 30 points, not fewer than 10",
   lambda t: abs(uc.cell(t, "The federal courts", "Disagree (%)")
                 - uc.cell(t, "The federal courts",
                           "Agree power is adequately limited (%)")) == 30),
  ("every row sums to 100",
   lambda t: all(uc.cell(t, lab, "Agree power is adequately limited (%)")
                 + uc.cell(t, lab, "Disagree (%)") == 100 for lab in uc.labels(t))),
 ],
}

uc.check(v1_1, TABLE_CHECKS)
