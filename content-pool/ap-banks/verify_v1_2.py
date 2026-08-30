"""Structural gate for AP U.S. Government 1.2 Types of Democracy.

This file is the gate v1_2.py shipped without. It does three things on top of
the shared checks in usgov_check.py, in ascending order of how much a human had
to think to write them:

1. ANCHORS -- a per-question substring that must appear in the KEYED choice and
   in none of the four distractors. usgov_check enforces the key-first
   invariant (`ans == 0` everywhere), which guards the index; the anchor guards
   the TEXT. If someone reorders the choices, rewrites the key, or edits a
   distractor until it says the same thing the key says, the index is still 0
   and the shape checks still pass -- and this list is the only thing that
   notices. It is written against the choice text as it stands, so it is also a
   compact record of what each question is actually keyed on.

2. GROUNDING -- for every one of the thirty questions, the constitutional
   provision, required case, foundational document or essential-knowledge
   statement the key traces back to. SOCIAL_BRIEF.md's rule for these subjects
   is that a key must trace to the CED rather than to the author's memory, and
   an unwritten trace is not a trace. Writing thirty of them is the review: it
   cannot be done without reading every question and deciding, item by item,
   what makes the key true. Two defects were found doing it, both recorded at
   the bottom of this file.

3. TABLE_CHECKS -- the arithmetic of the four data-stimulus items (18-21),
   recomputed from each item's own `table`, in the same form verify_v1_1.py
   uses: the claim the key makes, and the negation of any distractor that is
   tempting because it is nearly true.

WHAT THIS FILE STILL CANNOT DO
------------------------------
It cannot tell you that Baker v. Carr is about justiciability of redistricting
rather than about school prayer, or that the Federalist No. 10 excerpts in
items 5, 6 and 7 are quoted accurately. Those were checked by reading, against
AP_US_GOV_CED.md's statement of the required holdings and against the text of
Federalist No. 10; the GROUNDING table below is that reading written down so
the next reader audits it rather than repeats it.
"""
import usgov_anchor as ua
import usgov_check as uc
import v1_2

# --- 1. anchors -------------------------------------------------------------
# One per question, 1-based. Each must be a substring of the keyed choice and
# of no distractor in the same question. Comparison is case-sensitive and
# literal on purpose: a normalised comparison would let a distractor edited to
# differ only in punctuation slip past.
ANCHORS = {
 1: "Pluralist",
 2: "broad participation by individual citizens",
 3: "organized nongovernmental interests compete for influence over policy",
 4: "emphasizes limited participation in politics",
 5: "control their effects rather than to abolish them",
 6: "cure of destroying liberty",
 7: "single majority faction is harder to assemble",
 8: "small, decentralized republic",
 9: "filtered participation of the pluralist and elite models",
 10: "senators by state legislatures",
 11: "electors rather than the voters formally choose the president",
 12: "broad direct involvement of ordinary citizens",
 13: "Thousands of registered organizations lobby Congress",
 14: "wealthier and better-educated",
 15: "spend in order to influence political outcomes",
 16: "Baker v. Carr",
 17: "group identity may be built into the design of representation",
 18: "highest in general elections and lowest in school board elections",
 19: "never exceeds 15 percent",
 20: "by 13 percentage points",
 21: "No single model commands majority support",
 22: "individual citizens in the participatory model, organized groups",
 23: "shape the terms on which elected officials debate policy",
 24: "Senate as originally designed",
 25: "bargaining among organized interests",
 26: "life tenure for federal judges",
 27: "regardless of who wins elections",
 28: "transferring the decision from a small body to the electorate",
 29: "filter between the people and the decision",
 30: "accountability through elections",
}

# --- 2. grounding -----------------------------------------------------------
# The trace for every key. Not decoration: SOCIAL_BRIEF.md requires that a key
# be defensible from the CED, and this is the claim being made about each one.
GROUNDING = {
 1: "EK 1.2.A.1, verbatim: pluralist democracy 'emphasizes group-based activism "
    "by nongovernmental interests striving for impact on political decision making.'",
 2: "EK 1.2.A.1: participatory democracy 'emphasizes broad participation in politics "
    "and civil society.' A ballot initiative removes the representative filter.",
 3: "EK 1.2.A.1 pluralist. The actors named are organizations, not individuals; that "
    "is the discriminator this topic turns on.",
 4: "EK 1.2.A.1: elite democracy 'emphasizes limited participation in politics and "
    "civil society.' Eight appointed experts is limited participation.",
 5: "Federalist No. 10 (required document), the definition of faction, quoted "
    "verbatim; Madison's next move is to control the EFFECTS, having rejected "
    "removing the causes.",
 6: "Federalist No. 10 (required document), the liberty/air-and-fire analogy, quoted "
    "verbatim; the conclusion drawn is that abolishing liberty would be folly.",
 7: "Federalist No. 10 (required document), 'Extend the sphere,' quoted verbatim; "
    "the extended-republic argument at EK 1.2.A.2.",
 8: "Brutus No. 1 (required document), DESCRIBED not quoted, per the module header. "
    "EK 1.3.A.2: Anti-Federalist writings emphasized a small, decentralized republic.",
 9: "EK 1.2.A.2, which states the Federalist No. 10 / Brutus No. 1 tension as broad "
    "participation against the filtered participation of the pluralist and elite models.",
 10: "Article I Section 3 as originally ratified: senators chosen by state "
     "legislatures. Apportionment by population (Art. I Sec. 2) runs the other way.",
 11: "Article II Section 1 and the Twelfth Amendment: electors, not voters, cast the "
     "formal presidential ballots. EK 1.2.A.3, contemporary institutions.",
 12: "EK 1.2.A.1 participatory; the open town meeting is the model's clearest "
     "institutional form. Turnout is a fact about uptake, not about which model applies.",
 13: "EK 1.2.A.3: the models remain visible in contemporary institutions and behavior. "
     "Organized lobbying is the pluralist model's contemporary evidence.",
 14: "The standard critique of pluralism -- unequal group mobilization -- attacks the "
     "model's fairness while conceding its accuracy, which is what the stem asks for.",
 15: "Citizens United v. FEC (2010), required case. CED holding: political spending by "
     "corporations, associations and labor unions is protected speech. Organizations, "
     "not individuals -- hence pluralist.",
 16: "Baker v. Carr (1962), required case. CED holding: redistricting issues do not "
     "present political questions and are justiciable in federal court.",
 17: "Shaw v. Reno (1993), required case. CED holding: majority-minority districts may "
     "be challenged if race was the only factor in drawing them.",
 18: "Data item; the key is an arithmetic reading of the table and is recomputed below "
     "from the table itself, not trusted from the prose.",
 19: "Data item supporting an EK 1.2.A.3 claim about where participation is weakest; "
     "the supporting figure is recomputed below.",
 20: "Data item; the 13-point gap is recomputed below, as is the falsity of each "
     "near-miss distractor.",
 21: "Data item read against EK 1.2.A.1's three models; the 'no majority' and "
     "'differs by age' claims are both recomputed below.",
 22: "EK 1.2.A.1 distinguishes the models by the IDENTITY OF THE ACTOR, not by how "
     "many people are involved -- which is why a mass-membership group is pluralist.",
 23: "EK 1.2.A.1 pluralist / EK 1.2.A.3 contemporary. Organizations supplying the "
     "material of a floor debate is group-based activism striving for impact.",
 24: "EK 1.2.A.1 applied to four institutions. Art. I Sec. 3 (original Senate) is the "
     "elite pairing; referendum, recall and open comment are participatory.",
 25: "EK 1.2.A.1 pluralist: the decisive influence was an agreement among organizations, "
     "and the model is identified by what moved the decision.",
 26: "EK 1.2.A.2's tension shown inside one document: Art. I Sec. 2 (direct popular "
     "election of the House) against Art. III Sec. 1 (judges hold office during good "
     "behavior).",
 27: "EK 1.2.A.1 elite: the model's empirical claim is that a small group decides, so "
     "its research question is about the size and continuity of that group.",
 28: "EK 1.2.A.1 participatory. The decision moves from a party caucus to the registered "
     "electorate, which widens who holds it.",
 29: "Federalist No. 10 (required document), the republic/democracy distinction, "
     "DESCRIBED not quoted; delegation to elected representatives is the filter of "
     "EK 1.2.A.2.",
 30: "EK 1.2.A.1 participatory against republicanism's electoral accountability "
     "(Art. IV Sec. 4, the guarantee of a republican form of government): sortition "
     "maximizes eligibility and forfeits removability.",
}

# --- 3. the four data items -------------------------------------------------
YEARS = ["2018 turnout (%)", "2020 turnout (%)", "2022 turnout (%)"]
GEN = "Presidential or midterm general"
PRI = "Statewide primary"
SCH = "Local school board"
COLS = ["All respondents (%)", "Under 35 (%)", "35 and older (%)"]
CIT = "Ordinary citizens voting directly"
GRP = "Organized interest groups and associations"
REP = "Elected representatives"
EXP = "Nonpartisan experts"

TABLE_CHECKS = {
 18: [
  ("the general row is the largest and the school board row the smallest in all "
   "three years, which is the key's claim",
   lambda t: all(uc.cell(t, GEN, y) > uc.cell(t, PRI, y) > uc.cell(t, SCH, y)
                 for y in YEARS)),
  ("every row FALLS from 2018 to 2022, so 'rose in every type' is false",
   lambda t: all(uc.cell(t, lab, YEARS[2]) < uc.cell(t, lab, YEARS[0])
                 for lab in uc.labels(t))),
  ("school board never exceeds primary, so that distractor's 'at least one year' fails",
   lambda t: all(uc.cell(t, SCH, y) < uc.cell(t, PRI, y) for y in YEARS)),
  ("the general figure is under five times the school board figure in EVERY year, "
   "not just in 2020",
   lambda t: all(uc.cell(t, GEN, y) < 5 * uc.cell(t, SCH, y) for y in YEARS)),
  ("primary is nearer school board than general in every year, so the 'closer to "
   "general' distractor is false",
   lambda t: all(abs(uc.cell(t, PRI, y) - uc.cell(t, SCH, y))
                 < abs(uc.cell(t, PRI, y) - uc.cell(t, GEN, y)) for y in YEARS)),
 ],
 19: [
  ("the school board row is the table minimum in every year and never reaches 15,"
   " which is the keyed evidence",
   lambda t: all(uc.cell(t, SCH, y) == min(uc.col(t, y)) for y in YEARS)
   and max(uc.cell(t, SCH, y) for y in YEARS) <= 15),
  ("the general row's spread is exactly 19 points -- the distractor is TRUE of the "
   "table and simply does not bear on local participation, so it must not be "
   "rejected as arithmetic",
   lambda t: max(uc.cell(t, GEN, y) for y in YEARS)
   - min(uc.cell(t, GEN, y) for y in YEARS) == 19),
  ("all three rows do peak in 2020, likewise true and likewise irrelevant",
   lambda t: all(uc.cell(t, lab, YEARS[1]) == max(uc.cell(t, lab, y) for y in YEARS)
                 for lab in uc.labels(t))),
 ],
 20: [
  ("direct citizen decision runs 13 points higher under 35 than at 35 and older",
   lambda t: uc.cell(t, CIT, COLS[1]) - uc.cell(t, CIT, COLS[2]) == 13),
  ("citizens, not organized groups, lead the under-35 column, so that distractor fails",
   lambda t: uc.cell(t, CIT, COLS[1]) == max(uc.col(t, COLS[1]))
   and uc.cell(t, GRP, COLS[1]) < uc.cell(t, CIT, COLS[1])),
  ("elected representatives draw 31 percent overall, which is not a majority",
   lambda t: uc.cell(t, REP, COLS[0]) < 50),
  ("older respondents prefer representatives to experts, so that distractor is false",
   lambda t: uc.cell(t, REP, COLS[2]) > uc.cell(t, EXP, COLS[2])),
  ("two actors draw LESS support under 35 than at 35 and older, so 'every actor' fails",
   lambda t: sum(1 for lab in uc.labels(t)
                 if uc.cell(t, lab, COLS[1]) < uc.cell(t, lab, COLS[2])) == 2),
 ],
 21: [
  ("no cell anywhere in the survey reaches 50, so no model commands a majority",
   lambda t: max(max(uc.col(t, c)) for c in COLS) < 50),
  ("the two age columns differ on ALL FOUR actors, by up to 13 points, which is "
   "the key's second clause -- the rationale originally said three of four",
   lambda t: sum(1 for lab in uc.labels(t)
                 if uc.cell(t, lab, COLS[1]) != uc.cell(t, lab, COLS[2])) == 4
   and max(abs(uc.cell(t, lab, COLS[1]) - uc.cell(t, lab, COLS[2]))
           for lab in uc.labels(t)) == 13),
  ("the two filtered-decision actors together take 48 percent of all respondents "
   "and at least 37 in either age group, so 'negligible' is false -- this is the "
   "figure the rationale originally got wrong",
   lambda t: uc.cell(t, REP, COLS[0]) + uc.cell(t, EXP, COLS[0]) == 48
   and min(uc.cell(t, REP, c) + uc.cell(t, EXP, c) for c in COLS) == 37),
  ("each column sums to 100, so the survey is a complete distribution and the "
   "shares are comparable across columns",
   lambda t: all(sum(uc.col(t, c)) == 100 for c in COLS)),
 ],
}


ua.shape(v1_2)
ua.check(v1_2, ANCHORS, GROUNDING)
uc.check(v1_2, TABLE_CHECKS)

# WHAT THE REVIEW FOUND, reading all thirty to write GROUNDING above
# ------------------------------------------------------------------
# No wrong key. Thirty of thirty keys are defensible from the CED, the
# Constitution's text, or the required holdings as AP_US_GOV_CED.md states them,
# and the three Federalist No. 10 excerpts (items 5, 6, 7) are verbatim; item 8
# describes Brutus No. 1 and item 29 describes Federalist No. 10 rather than
# quoting them, which is what SOCIAL_BRIEF.md asks for when the wording cannot
# be verified.
#
# Two arithmetic errors were found and fixed, both in the SAME explanation
# rather than in any key -- item 21's `why`:
#
#   * it said the elite-leaning categories "together draw 37 percent of all
#     respondents." In the All-respondents column they draw 31 + 17 = 48; 37 is
#     the figure for the under-35 column (24 + 13). It now states both.
#   * it said the two age columns "differ on three of the four actors." They
#     differ on all four; the smallest gap is the 3 points on organized groups,
#     which is what presumably got rounded away in the writing.
#
# Neither changed a key, and the keyed choice for item 21 is right either way.
# Both are now recomputed from the table by TABLE_CHECKS above, which is the
# point: a number in a rationale that nothing recomputes is a number that drifts
# away from its table the first time an author edits a cell.
