"""Structural gate for AP U.S. Government 1.3 Government Power and Individual Rights.

Same three-part shape as verify_v1_2.py, and for the same reasons:

* ANCHORS pins each key to a distinctive substring of its own choice text, so a
  reordered or rewritten choice list fails here even though ``ans`` is still 0;
* GROUNDING records, for all thirty, the CED essential-knowledge statement,
  foundational document or required case the key traces to -- SOCIAL_BRIEF.md's
  rule for these subjects, written down so the next reader audits it instead of
  repeating the work;
* TABLE_CHECKS recomputes the arithmetic of the five data items from their own
  tables, including the negation of each distractor that is tempting because it
  is nearly true.

THE HISTORICAL FIGURES IN THE RATIFICATION TABLE
------------------------------------------------
Items 21 to 23 use the recorded convention votes: Delaware 30 to 0, Massachusetts
187 to 168, Virginia 89 to 79, New York 30 to 27, Rhode Island 34 to 32. Those
are real numbers, not invented ones, which is why item 23 is a data-LIMITATION
question rather than a third reading question -- a delegate vote is not a
measure of public opinion, and saying so is the honest use of the table.

The survey in items 24 and 25 is labelled hypothetical in the stem, as the
economics banks label theirs. Both of its columns sum to 100, which the last
check confirms, so the shares are a complete distribution and comparable across
columns.
"""
import usgov_anchor as ua
import usgov_check as uc
import v1_3

ANCHORS = {
 1: "Federalists supported ratification and a strong central government",
 2: "too distant from the people to be watched",
 3: "locating the danger to liberty in a distant central government",
 4: "written list of individual rights",
 5: "never be legislated out of existence",
 6: "too few and too distant to reflect the people",
 7: "reject both of them",
 8: "protects rights and rests on consent",
 9: "abandons a principle worth keeping",
 10: "harder for any single interest to capture",
 11: "level of government closest to the people affected",
 12: "reads national power broadly",
 13: "McCulloch v. Maryland (1819), which established the supremacy",
 14: "can still burden the liberty of a small community",
 15: "became an enforceable limit on government",
 16: "define the limits of its own authority",
 17: "Ninth Amendment",
 18: "treats distance between the people and their governors",
 19: "hard to represent",
 20: "whether the greater threat came from a distant central government",
 21: "carried by a margin of fewer than twenty votes",
 22: "the losing side drew more than forty percent",
 23: "selected under restrictive suffrage rules",
 24: "place the two subnational levels above the national government",
 25: "leads among rural respondents at 41 percent",
 26: "derives its just powers from the consent of the governed",
 27: "keeps any winning coalition from controlling everything at once",
 28: "cannot know or serve local circumstances",
 29: "enforced written guarantees against the national government itself",
 30: "left the balance between national power, state power and individual rights unresolved",
}

GROUNDING = {
 1: "EK 1.3.A.1 and EK 1.3.A.2, both quoted in the module header; the key pairs each "
    "side with the CED's own sentence about it.",
 2: "EK 1.3.A.2, verbatim: Anti-Federalist writings warned of 'the dangers to personal "
    "liberty from a large, centralized government.'",
 3: "EK 1.3.A.2. The discriminator is WHERE the speaker locates the danger, which the "
    "module header states as this topic's organizing distinction.",
 4: "EK 1.3.A.1 names exactly three focuses. A written enumeration of rights belongs to "
    "EK 1.5.A.1's ratification compromises, not to Federalist No. 10.",
 5: "Federalist No. 10 (required document), 'The latent causes of faction are thus sown "
    "in the nature of man,' quoted verbatim; it is the premise for controlling effects.",
 6: "Federalist No. 10 (required document), the democracy/republic distinction, quoted "
    "verbatim, set against EK 1.3.A.2's small-republic theory.",
 7: "Federalist No. 10 (required document), the two methods of removing causes, quoted "
    "verbatim; Madison introduces the pair in order to reject both.",
 8: "Declaration of Independence (required document), quoted verbatim; the CED attaches "
    "the Declaration to 1.3.A. It states a test of legitimacy, which both sides claimed.",
 9: "Articles of Confederation (required document), Article II, quoted verbatim; the CED "
    "attaches the Articles to 1.3.A. The contrast is with the Necessary and Proper Clause.",
 10: "EK 1.3.A.1: 'dispersing power between the states and national government' is the "
     "third of Madison's three focuses.",
 11: "EK 1.3.A.2: popular democratic theory emphasizing the benefits of a small, "
     "decentralized republic.",
 12: "McCulloch v. Maryland (1819), required case. CED holding: established supremacy of "
     "the U.S. Constitution and federal laws over state laws.",
 13: "McCulloch v. Maryland (1819), required case, as a SCOTUS comparison; the "
     "non-required case's facts are printed in the stem per CED p. 29.",
 14: "Wisconsin v. Yoder (1972), required case. CED holding: compelling Amish students to "
     "attend past the eighth grade violates the Free Exercise Clause. Read against "
     "EK 1.3.A.2's fear for the liberty of the unlike few.",
 15: "Tinker v. Des Moines (1969), required case. CED holding: banning black armbands "
     "violated students' First Amendment freedom of speech. Read against EK 1.5.A.1's "
     "Bill of Rights compromise.",
 16: "EK 1.3.A.2 read structurally: a central government with implied powers cannot police "
     "its own boundary, which is why the Anti-Federalists wanted the boundary written.",
 17: "Ninth Amendment, verbatim in substance: 'The enumeration in the Constitution, of "
     "certain rights, shall not be construed to deny or disparage others retained by the "
     "people.' It answers the Federalist objection to enumerating at all.",
 18: "EK 1.3.A.2. The Senate as originally designed (Art. I Sec. 3, legislative selection, "
     "six-year terms) is the institution the popular democratic theory objects to.",
 19: "EK 1.3.A.1 against EK 1.3.A.2: the strongest Anti-Federalist reply concedes the "
     "extended-republic mechanism and attacks its cost to representation.",
 20: "EK 1.3.A.1 and EK 1.3.A.2 together. Federalist No. 10 is an argument about managing "
     "a danger, so neither side is the party of trust in government.",
 21: "Data item on the recorded ratification votes; every claim in the key and in the "
     "near-miss distractors is recomputed below from the table.",
 22: "Data item; the four losing shares are recomputed below and all exceed forty percent.",
 23: "Data item, CED skill 3.E, explain limitations of the data. Delegates were chosen "
     "under restrictive suffrage, so the table cannot measure public opinion.",
 24: "Data item read against EK 1.3.A.2's decentralization preference; the row and column "
     "comparisons are recomputed below.",
 25: "Data item; the state-government row supplies the only level-by-level comparison that "
     "bears on the claim, and its two figures are recomputed below.",
 26: "Declaration of Independence (required document): 'deriving their just powers from the "
     "consent of the governed.' Common ground, which is why the other four were contested.",
 27: "EK 1.3.A.1's three focuses as one design -- scale multiplies interests, delegation "
     "refines them, dispersal limits what a winning coalition can seize.",
 28: "EK 1.3.A.2 applied to a modern scenario; the objection is about distance and local "
     "knowledge, not about an enumeration of rights.",
 29: "EK 1.3.A.2's prediction stated as falsifiable, then tested. Enforcement of written "
     "guarantees against the national government is what would weaken it.",
 30: "EK 1.5.A.3 and EK 1.5.A.4: the compromises left matters unresolved, and the balance "
     "of national power, state power and individual rights remains at the heart of "
     "present-day constitutional issues.",
}

FOR, AGAINST = "Votes for", "Votes against"
DE, MA, VA, NY, RI = "Delaware", "Massachusetts", "Virginia", "New York", "Rhode Island"
ALL, URB, RUR = "All adults (%)", "Urban (%)", "Rural (%)"
NAT, ST, LOC, NOP = ("The national government", "State government",
                     "Local government", "No opinion")


def _margin(t, state):
    return uc.cell(t, state, FOR) - uc.cell(t, state, AGAINST)


def _loser_share(t, state):
    total = uc.cell(t, state, FOR) + uc.cell(t, state, AGAINST)
    return 100.0 * uc.cell(t, state, AGAINST) / total


TABLE_CHECKS = {
 21: [
  ("exactly one state is unanimous, and EVERY other margin is under twenty -- the "
   "key says four, and 19 in Massachusetts counts",
   lambda t: sum(1 for s in uc.labels(t) if uc.cell(t, s, AGAINST) == 0) == 1
   and all(_margin(t, s) < 20 for s in uc.labels(t) if uc.cell(t, s, AGAINST) > 0)
   and sum(1 for s in uc.labels(t) if uc.cell(t, s, AGAINST) > 0) == 4),
  ("no margin reaches fifty, so 'at least fifty votes' is false",
   lambda t: all(_margin(t, s) < 50 for s in uc.labels(t))),
  ("Massachusetts holds the WIDEST contested margin and Rhode Island the narrowest, "
   "so the 'narrowest was Massachusetts' distractor is false",
   lambda t: _margin(t, MA) == max(_margin(t, s) for s in uc.labels(t)
                                   if uc.cell(t, s, AGAINST) > 0)
   and _margin(t, RI) == min(_margin(t, s) for s in uc.labels(t))),
  ("four of the five states do record votes against, so 'no state recorded any' fails",
   lambda t: sum(1 for s in uc.labels(t) if uc.cell(t, s, AGAINST) > 0) == 4),
  ("the totals for exceed the totals against, so that distractor is false",
   lambda t: sum(uc.col(t, FOR)) > sum(uc.col(t, AGAINST))),
 ],
 22: [
  ("in four conventions the losing side took more than forty percent, and in the "
   "fifth it took none",
   lambda t: sum(1 for s in uc.labels(t) if _loser_share(t, s) > 40) == 4
   and _loser_share(t, DE) == 0),
  ("each of those four losing shares is between 46 and 49 percent",
   lambda t: all(46 < _loser_share(t, s) < 49 for s in (MA, VA, NY, RI))),
  ("Massachusetts really does cast the most total votes and Delaware not the fewest "
   "tie -- both are true of the table and neither bears on how divided the "
   "conventions were, which is why they are distractors rather than errors",
   lambda t: uc.cell(t, MA, FOR) + uc.cell(t, MA, AGAINST)
   == max(uc.cell(t, s, FOR) + uc.cell(t, s, AGAINST) for s in uc.labels(t))
   and uc.cell(t, DE, FOR) + uc.cell(t, DE, AGAINST)
   == min(uc.cell(t, s, FOR) + uc.cell(t, s, AGAINST) for s in uc.labels(t))),
 ],
 23: [
  ("every state in the table ratified, so the 'no information about which ratified' "
   "distractor is false on the table's own face",
   lambda t: all(uc.cell(t, s, FOR) > uc.cell(t, s, AGAINST) for s in uc.labels(t))),
  ("delegate counts differ across states, so 'identical in every state' is false",
   lambda t: len({uc.cell(t, s, FOR) + uc.cell(t, s, AGAINST)
                  for s in uc.labels(t)}) > 1),
  ("the table does carry a year column, so 'reports votes rather than years' is false",
   lambda t: "Convention year" in t["headers"]),
 ],
 24: [
  ("among rural respondents state and local together outrank the national level, "
   "while among urban respondents the national level leads outright",
   lambda t: uc.cell(t, ST, RUR) + uc.cell(t, LOC, RUR) > uc.cell(t, NAT, RUR)
   and uc.cell(t, ST, RUR) > uc.cell(t, NAT, RUR)
   and uc.cell(t, NAT, URB) > max(uc.cell(t, ST, URB), uc.cell(t, LOC, URB))),
  ("the national government draws 38 percent of all adults, which is not a majority",
   lambda t: uc.cell(t, NAT, ALL) < 50),
  ("the largest urban-rural gap is 19 points, so 'more than twenty on every level' "
   "fails at the first row",
   lambda t: max(abs(uc.cell(t, lab, URB) - uc.cell(t, lab, RUR))
                 for lab in uc.labels(t)) == 19),
  ("state, not local, leads among rural respondents",
   lambda t: uc.cell(t, ST, RUR) > uc.cell(t, LOC, RUR)),
  ("the no-opinion share is identical in both columns, so neither group is more "
   "likely to have none",
   lambda t: uc.cell(t, NOP, URB) == uc.cell(t, NOP, RUR)),
  ("all three columns sum to 100, so the survey is a complete distribution",
   lambda t: all(sum(uc.col(t, c)) == 100 for c in (ALL, URB, RUR))),
 ],
 25: [
  ("state government leads the rural column at 41 and trails the national figure in "
   "the urban column, which is the keyed comparison",
   lambda t: uc.cell(t, ST, RUR) == 41
   and uc.cell(t, ST, RUR) == max(uc.col(t, RUR))
   and uc.cell(t, ST, URB) < uc.cell(t, NAT, URB)),
  ("local government's smallest figure is indeed the urban one -- true of the table, "
   "and silent on relative preference, which is what makes it a distractor",
   lambda t: uc.cell(t, LOC, URB) == min(uc.cell(t, LOC, c) for c in (ALL, URB, RUR))),
  ("the national government's 38 is the largest figure in the all-adults column -- "
   "also true, also silent on the rural/urban contrast",
   lambda t: uc.cell(t, NAT, ALL) == max(uc.col(t, ALL))),
  ("the no-opinion row does NOT differ across the two groups, so 'every category "
   "differs' is false",
   lambda t: uc.cell(t, NOP, URB) == uc.cell(t, NOP, RUR)),
 ],
}


ua.shape(v1_3)
ua.check(v1_3, ANCHORS, GROUNDING)
uc.check(v1_3, TABLE_CHECKS)

# WHAT THE REVIEW FOUND while writing GROUNDING and the table checks
# ------------------------------------------------------------------
# One defect, caught by the arithmetic rather than by reading: item 21's keyed
# choice originally said ratification was "decided by fewer than twenty votes in
# THREE others." Massachusetts carried by 19, which is also fewer than twenty, so
# the count was four and the key as written was false of its own table while
# still being the best of the five options -- the worst kind of near-miss. The
# key now says four, and the first check on item 21 counts the unanimous state
# and the sub-twenty margins from the table rather than from the sentence.
