"""Structural gate for AP U.S. Government 2.7 Presidential Communication.

ANCHORS, GROUNDING and the notation check via usgov_anchor, then usgov_check
with the six data items recomputed from their own tables.

THE SMALLEST CONTENT BASE IN THE UNIT, AND WHAT THE GROUNDING MAP IS FOR
--------------------------------------------------------------------------
2.7 has ONE essential-knowledge statement with two sub-items. Thirty questions
on one sentence becomes one question thirty times unless the module is
deliberately structured, and the GROUNDING map below is how that structure is
audited without re-reading the items. Read down it and the two-by-two is
visible: LO 2.7.A names two relationships (the national constituency, the other
branches) and EK 2.7.A.1 names two mechanisms (rapid response, agenda setting).
Roughly eight items on agenda setting toward the public, six on rapid response,
six on the OTHER BRANCHES -- the half of the learning objective a bank usually
drops -- six data items, and four on limits and testing.

If a later editor adds items, the map is where to check the balance has not
collapsed back onto the easy half.

AGENDA SETTING IS SALIENCE, NOT PERSUASION, AND NOT ENACTMENT
---------------------------------------------------------------
EK 2.7.A.1.ii's phrase is "influence public views about WHICH POLICIES ARE THE
MOST IMPORTANT." That is a claim about what the country is arguing about, not
about who wins the argument and not about what passes. Items 4, 5, 15 and 24
each separate the three, and _salience below asserts that no key or rationale
in the module defines agenda setting as agreement or as legislation. It is the
one substantive error this topic invites, and it is invited by the ordinary
English meaning of "influence."

WHAT THE MODULE DELIBERATELY OMITS
-----------------------------------
No living or recent president, no named platform beyond the CED's own "social
media," no contemporary controversy. The CED's illustrative example for this
topic is a 1981 address and is explicitly not required. A bank that names
current figures dates itself and makes claims that cannot be checked against
the framework, which SOCIAL_BRIEF.md forbids. _no_current below checks it.
"""
import usgov_anchor as ua
import usgov_check as uc
import v2_7

ANCHORS = {
 1: "increased with advances in communication technology",
 2: "agenda setting, using the media to influence public views",
 3: "which policies the public sees as most important",
 4: "it changed which issue the public treats as most important",
 5: "naming the address's subject as the nation's most important problem rose",
 6: "Respond rapidly to political issues",
 7: "an immediate response to events as they occur",
 8: "now reaches a national audience directly",
 9: "That modern technology allows for rapid responses",
 10: "without an intermediary deciding what to report",
 11: "cannot be unsaid and may commit the administration",
 12: "in the sustained attention to one issue",
 13: "split across many channels",
 14: "brings pressure to bear on members who must face those voters",
 15: "failed at legislating but succeeded at agenda setting",
 16: "Only indirectly, since courts decide cases on legal grounds",
 17: "define what the nation's central commitment is",
 18: "arising from the office's visibility",
 19: "prompting constituents in those states to contact their offices",
 20: "and did the share agreeing with the president's position change",
 21: "two channels that did not exist in the early era",
 22: "have changed how presidential messages reach the public",
 23: "may have received a message through more than one channel",
 24: "rose by seventeen points while every other category fell",
 25: "influencing which policies the public sees as most important",
 26: "Other events in the same week could have raised the subject's salience",
 27: "determines what is discussed but not what is enacted",
 28: "changes the president's leverage over Congress",
 29: "the occasion's authority and the guaranteed national audience are given up",
 30: "how much the public's ranking of the most important problem shifted",
}

GROUNDING = {
 1: "EK 2.7.A.1, verbatim: 'The impact of presidential communication has increased with "
    "advances in communication technology.'",
 2: "EK 2.7.A.1.ii, verbatim: State of the Union messages and the bully pulpit 'are tools "
    "for agenda setting that use the media to influence public views about which policies "
    "are the most important.'",
 3: "EK 2.7.A.1.ii's definition, isolated: agenda setting is about SALIENCE, not about the "
    "merits of a policy or the behavior of Congress.",
 4: "EK 2.7.A.1.ii applied. Divided opinion on the merits is consistent with successful "
    "agenda setting, because the two effects are distinct.",
 5: "EK 2.7.A.1.ii operationalized: the evidence for agenda setting is a change in what the "
    "public names as most important.",
 6: "EK 2.7.A.1.i, verbatim: 'Modern technology, such as social media, allows for rapid "
    "responses to political issues.'",
 7: "EK 2.7.A.1.i against EK 2.7.A.1.ii: immediacy against the scheduled set-piece. Both are "
    "informal instruments (EK 2.4.A.2 places persuasion among the informal powers).",
 8: "U.S. Constitution Art. II Sec. 3, the State of the Union clause, quoted verbatim. The "
    "duty runs to Congress; EK 2.7.A.1.ii's point is that broadcasting aims it at the public.",
 9: "EK 2.7.A.1.i: speed is the defining feature of the scenario.",
 10: "LO 2.7.A's first relationship, the NATIONAL CONSTITUENCY: the structural change is the "
     "removal of an editorial intermediary.",
 11: "EK 2.7.A.1.i read for its cost: what speed enables, it also exposes.",
 12: "EK 2.7.A.1.i and EK 2.7.A.1.ii combined -- rapid messages used in service of salience.",
 13: "EK 2.7.A.1's claim is about IMPACT, and audience fragmentation attacks impact while "
     "leaving reach intact. CED skill 5.D, rebuttal.",
 14: "LO 2.7.A's second relationship, THE OTHER BRANCHES, by the indirect route: attention "
     "among constituents becomes a legislator's problem.",
 15: "EK 2.7.A.1.ii against EK 2.2.A's legislative process: salience and enactment are "
     "separate outcomes, and collapsing them is this topic's central error.",
 16: "LO 2.7.A's other branches, answered honestly for the judiciary: the channel is indirect, "
     "since public argument is not a source of law.",
 17: "Gettysburg Address (required document), Bliss copy, quoted verbatim; the CED attaches it "
     "to 2.7.A. EK 2.7.A.1's claim is that technology INCREASED this impact, not created it.",
 18: "EK 2.7.A.1.ii lists the bully pulpit as a tool; EK 2.4.A.2 places instruments of "
     "persuasion among the INFORMAL powers. No clause of Article II mentions it.",
 19: "LO 2.7.A's other branches: the mechanism runs through the public back to the "
     "officeholder, which is what distinguishes it from a formal power.",
 20: "EK 2.7.A.1.ii's definition operationalized against persuasion -- the two must be "
     "measured separately or neither is measured.",
 21: "Data item on a labelled hypothetical; the era-by-era leaders are recomputed below.",
 22: "EK 2.7.A.1 seen as data: two channels appear from nothing and one nearly disappears.",
 23: "Data item, CED skill 3.E: the recent column sums to 124 percent, so the channels overlap "
     "and no total reach can be read off it.",
 24: "Data item on a labelled hypothetical; the rise and the four falls are recomputed below.",
 25: "EK 2.7.A.1.ii measured: a change in which problem is named most important, and nothing "
     "about agreement or about congressional action.",
 26: "Data item, CED skill 3.E: a before-and-after comparison with no control cannot separate "
     "the address from anything else that happened that week.",
 27: "EK 2.7.A.1.ii against EK 2.2.A.3's legislative process: salience does not enact.",
 28: "LO 2.7.A itself, which is why this topic sits in a unit on interactions among branches "
     "rather than in a unit about media.",
 29: "EK 2.7.A.1.i against EK 2.7.A.1.ii: two instruments with different properties, and the "
     "set-piece carries an audience and an authority the immediate message does not.",
 30: "EK 2.7.A.1 operationalized: measure the shift in the most-important-problem ranking "
     "across eras, since that is what EK 2.7.A.1.ii defines the impact as.",
}

EARLY, MID, RECENT = "Early era (%)", "Middle era (%)", "Recent era (%)"
PRINT_, BROAD = "Printed newspaper account", "Live radio or television broadcast"
CLIP, DIRECT = ("Recorded or streamed clip online",
                "Direct message from the president's own account")
BEFORE, AFTER = "Week before (%)", "Week after (%)"
INFRA, ECON = "Infrastructure", "The economy"

TABLE_CHECKS = {
 21: [
  ("a different channel leads in each era: newspapers, then live broadcast, then "
   "streamed clips",
   lambda t: uc.cell(t, PRINT_, EARLY) == max(uc.col(t, EARLY))
   and uc.cell(t, BROAD, MID) == max(uc.col(t, MID))
   and uc.cell(t, CLIP, RECENT) == max(uc.col(t, RECENT))),
  ("the two channels absent from the early era together carry 90 points of the recent "
   "era, which is the key's second clause",
   lambda t: uc.cell(t, CLIP, EARLY) == 0 and uc.cell(t, DIRECT, EARLY) == 0
   and uc.cell(t, CLIP, RECENT) + uc.cell(t, DIRECT, RECENT) == 90),
  ("newspapers FALL from 44 to 6, so 'reached more adults in the recent era' is false",
   lambda t: uc.cell(t, PRINT_, RECENT) < uc.cell(t, PRINT_, EARLY)),
  ("live broadcast peaks in the MIDDLE era, so 'largest share in the recent era' is "
   "false",
   lambda t: uc.cell(t, BROAD, MID) > uc.cell(t, BROAD, RECENT)),
  ("live broadcast reaches 63 in the middle era, so 'no channel above half in any "
   "era' is false",
   lambda t: max(max(uc.col(t, c)) for c in (EARLY, MID, RECENT)) > 50),
 ],
 22: [
  ("two channels rise from zero and one falls by 38 points, which is the change "
   "EK 2.7.A.1 describes",
   lambda t: uc.cell(t, CLIP, EARLY) == 0 and uc.cell(t, DIRECT, EARLY) == 0
   and uc.cell(t, PRINT_, EARLY) - uc.cell(t, PRINT_, RECENT) == 38),
  ("no row concerns the State of the Union, vetoes, confirmations or judicial "
   "appointments, so the four distractors cite statements these data cannot support",
   lambda t: len(t["rows"]) == 4
   and not any(k in lab.lower() for lab in uc.labels(t)
               for k in ("union", "veto", "confirm", "judicial"))),
 ],
 23: [
  ("the recent column sums to 124 percent, which is only possible if a respondent "
   "could name more than one channel -- the limitation the key states",
   lambda t: sum(uc.col(t, RECENT)) == 124),
  ("all three eras and four channels are present, so three of the distractors are "
   "false on the table's face",
   lambda t: len(t["rows"]) == 4
   and all(c in t["headers"] for c in (EARLY, MID, RECENT))),
 ],
 24: [
  ("infrastructure rises by exactly seventeen points and every other category falls",
   lambda t: uc.cell(t, INFRA, AFTER) - uc.cell(t, INFRA, BEFORE) == 17
   and all(uc.cell(t, lab, AFTER) < uc.cell(t, lab, BEFORE)
           for lab in uc.labels(t) if lab != INFRA)),
  ("infrastructure is still behind the economy afterward, so 'became the most "
   "frequently named' is false",
   lambda t: uc.cell(t, INFRA, AFTER) < uc.cell(t, ECON, AFTER)),
  ("the economy falls 7 points against infrastructure's rise of 17, so 'fell by more "
   "points than the subject rose' is false",
   lambda t: uc.cell(t, ECON, BEFORE) - uc.cell(t, ECON, AFTER)
   < uc.cell(t, INFRA, AFTER) - uc.cell(t, INFRA, BEFORE)),
  ("both weeks sum to 100, so each is a complete distribution and the shares are "
   "comparable",
   lambda t: all(sum(uc.col(t, c)) == 100 for c in (BEFORE, AFTER))),
 ],
 25: [
  ("the table measures which problem is named most important and nothing else -- no "
   "column reports agreement with the president or action by Congress",
   lambda t: [h for h in t["headers"][1:]] == [BEFORE, AFTER]
   and "most important problem" in t["headers"][0]),
  ("the subject of the address moves more than any other category, which is what "
   "makes it an agenda-setting table rather than a persuasion table",
   lambda t: abs(uc.cell(t, INFRA, AFTER) - uc.cell(t, INFRA, BEFORE))
   == max(abs(uc.cell(t, lab, AFTER) - uc.cell(t, lab, BEFORE))
          for lab in uc.labels(t))),
 ],
 26: [
  ("both weeks are present and both sum to 100, so three of the four distractors are "
   "false on the table's face",
   lambda t: all(sum(uc.col(t, c)) == 100 for c in (BEFORE, AFTER))),
  ("five categories appear, so 'covers a single category' is false",
   lambda t: len(t["rows"]) == 5),
  ("the table carries no column for any other event or variable, which is exactly the "
   "gap the key names",
   lambda t: len(t["headers"]) == 3),
 ],
}


def _salience(module):
    """Agenda setting must never be defined as agreement or as enactment."""
    bad = []
    for i, item in enumerate(module.QUESTIONS, 1):
        for label, s in (("key", item["choices"][item["ans"]]), ("why", item["why"])):
            low = s.lower()
            if "agenda setting" not in low and "set the agenda" not in low:
                continue
            for wrong in ("persuad", "came to agree", "enacted the", "passed the bill"):
                if wrong in low and "not " not in low and "rather than" not in low:
                    bad.append(f"q{i} {label}: defines agenda setting in terms of {wrong!r}; "
                               "EK 2.7.A.1.ii's effect is on which policies are seen as "
                               "MOST IMPORTANT")
    if bad:
        print(f"FAIL {module.__name__} salience")
        for b in bad:
            print("  -", b)
        raise SystemExit(1)
    print(f"OK  {module.__name__} salience: no key or rationale defines agenda setting as "
          "agreement or as legislation, per EK 2.7.A.1.ii")


def _no_current(module):
    """No named president, platform or controversy the CED does not supply."""
    banned = ("twitter", "facebook", "instagram", "tiktok", "youtube", "trump", "biden",
              "obama", "reagan", "clinton", "bush", "roosevelt", "nixon")
    allowed = {"lincoln"}  # the Gettysburg Address is a required document
    bad = []
    for i, item in enumerate(module.QUESTIONS, 1):
        blob = (item["q"] + " " + item["why"] + " " + " ".join(item["choices"])).lower()
        for word in banned:
            if word in blob:
                bad.append(f"q{i}: names {word!r}, which the CED does not require here")
    if bad:
        print(f"FAIL {module.__name__} currency")
        for b in bad:
            print("  -", b)
        raise SystemExit(1)
    print(f"OK  {module.__name__} currency: no named platform, president or controversy "
          f"beyond the CED's own wording (Lincoln excepted as a required document: "
          f"{sorted(allowed)[0].title()})")


ua.shape(v2_7)
ua.check(v2_7, ANCHORS, GROUNDING)
ua.notation(v2_7)
_salience(v2_7)
_no_current(v2_7)
uc.check(v2_7, TABLE_CHECKS)

# WHAT THE REVIEW FOUND
# ---------------------
# No wrong key. Two decisions recorded rather than left implicit:
#
#   * The reach table's recent column sums to 124 percent ON PURPOSE, and item 23
#     is the item that makes a student notice. Channels overlap, so the shares
#     are not a distribution and cannot be added into a total reach. The check
#     asserts the sum is 124, so anyone later "correcting" the column to 100
#     fails this file instead of quietly making item 23 unanswerable. Same
#     pattern as the multiple-response table in v1_9.
#   * _no_current exists because this is the topic where a bank naturally starts
#     naming platforms and presidents. The CED says "social media" and nothing
#     more; its own illustrative example is a 1981 address it marks as NOT
#     REQUIRED. Every item here is written so it will still be true in ten years,
#     and the check makes that a property rather than an intention.
