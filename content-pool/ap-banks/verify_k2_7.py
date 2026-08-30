"""Key audit for AP COMPARATIVE GOVERNMENT 2.7 Independent Legislatures.

One (anchor, claim) per item, in module order. The anchor must appear in the
keyed choice and in no distractor; the claim states what the key rests on.

WHAT THE KEYS REST ON
---------------------
  PAU-3.F.1  legislative powers can be CONSTRAINED BY OTHER GOVERNMENTAL
             INSTITUTIONS, including .a China's Politburo Standing Committee, the
             ACTUAL CENTER OF POWER in the Chinese state; .b China's Standing
             Committee of the NPC, which assumes legislative duties most of the
             year when the NPC is not in session, sets its agenda, supervises its
             member elections and interprets the Constitution and laws; .c Iran's
             Expediency Council, selected by the Supreme Leader as an ADVISORY
             committee to resolve disputes between the Majles and the Guardian
             Council; .d Iran's Guardian Council, which VETS CANDIDATES and
             OVERSEES the Majles for compliance with Islamic law
  PAU-3.F.2  legislatures can REINFORCE LEGITIMACY AND STABILITY by responding to
             public demand, openly debating policy, facilitating compromise
             between factions, extending civil liberties, and restricting the
             power of the executive

THE DEFINITION COMES FROM THE SCORING GUIDELINES
------------------------------------------------
The framework never defines legislative independence, and the whole topic turns
on it. The CED's SCORING GUIDELINES for its sample comparative-analysis question
do: 'the degree to which a legislature is free to exercise its powers without
influence from other branches/institutions.' Item 1 keys that wording, and items
20, 21 and 28 apply it. The same guidelines supply why each of four course
countries constrains its legislature -- to give the Supreme Leader more power and
enforce theocratic rules in Iran; elections every five years in the United
Kingdom; the executive's wish for concentrated power in Nigeria; elections to
maintain stability and prevent corruption in Mexico -- and every item keyed to one
of those names the source in its claim.

TWO THINGS THE MODULE KEEPS APART
---------------------------------
PAU-3.F.1.a's Politburo Standing Committee and PAU-3.F.1.b's Standing Committee
of the National People's Congress have similar names and different roles; items
3, 4, 10, 24 and 27 depend on not confusing them. And PAU-3.F.1's four examples
come from only TWO course countries, which item 29 keys, because a student who
assumes the framework spreads its examples evenly will hunt for a third.

DATA ITEMS
----------
Items 20-22 use a hypothetical activity table whose three columns are all
exercises of a legislature's own powers, so the scoring guidelines' definition can
be applied to data. Items 23-25 use a four-row matrix of constraining bodies whose
FUNCTIONS, not names, have to be matched.

FIVE choices per item (A-E); see AP_COMP_GOV_CED.md.
"""
import cg_check as cg
import k2_7

AMEND = "Executive bills amended before passage (percent)"
OWNBILL = "Bills initiated by members rather than by the executive (percent)"
DAYS = "Days in session per year"
FUNC = "Function as described"


def _ind(table):
    return {lab: (cg.cell(table, lab, AMEND), cg.cell(table, lab, OWNBILL), cg.cell(table, lab, DAYS))
            for lab in cg.labels(table)}


def q20(table, item):
    v = _ind(table)
    for i, name in enumerate((AMEND, OWNBILL, DAYS)):
        assert max(v, key=lambda k: v[k][i]) == "Legislature P", f"the keyed row does not lead on {name}"
    assert v["Legislature P"] == (62, 41, 118), f"the keyed row reads {v['Legislature P']}"
    assert all(max(v, key=lambda k: v[k][i]) == "Legislature P" for i in range(3)), \
        "all three columns must point to the same row, or the key would rest on one of them"
    return "one row leads on all three columns at once -- 62 percent amended, 41 percent member-initiated, 118 sitting days"


def q21(table, item):
    v = _ind(table)
    assert v["Legislature Q"][2] == min(x[2] for x in v.values()), "the keyed row must sit on the fewest days"
    assert v["Legislature Q"][0] == min(x[0] for x in v.values()), "the keyed row must also amend the least"
    assert v["Legislature Q"] == (9, 4, 12), f"the keyed row reads {v['Legislature Q']}"
    assert v["Legislature Q"][2] * 5 < v["Legislature P"][2], \
        "the gap in sitting days should be large enough that 'most of the year elsewhere' is the natural reading"
    return "one row sits on 12 days against 118 and 74, and amends 9 percent of executive bills against 62 and 38"


def q22(table, item):
    col = cg.col(table, AMEND)
    gap = max(col) - min(col)
    assert gap == 53, f"the keyed gap recomputes to {gap}"
    v = _ind(table)
    assert v["Legislature P"][0] - v["Legislature R"][0] == 24, "the 24 distractor must be another pair's gap"
    assert v["Legislature R"][0] - v["Legislature Q"][0] == 29, "the 29 distractor must be the remaining pair's gap"
    own = cg.col(table, OWNBILL)
    assert max(own) - min(own) == 37, "the 37 distractor must be the corresponding gap in the other percentage column"
    assert max(col) == 62, "the 62 distractor must be the largest single value read as a difference"
    return f"the amendment column spans {min(col):.0f} to {max(col):.0f}, a gap of {gap:.0f}, and every distractor is a real figure from the wrong pair or column"


def _bodies(table):
    return {str(r[0]): str(r[1]) for r in table["rows"]}


def q23(table, item):
    v = _bodies(table)
    f = v["Body 1"]
    assert "vets candidates" in f and "religious law" in f, f"the keyed row reads {f!r}"
    for lab in ("Body 2", "Body 3", "Body 4"):
        assert not ("vets candidates" in v[lab] and "religious law" in v[lab]), \
            f"{lab} must not also pair vetting with a religious-law check"
    # Body 3 REFERS to the vetting body, which is why the check is on the pairing
    # rather than on the phrase: a substring test alone would have matched it.
    assert "vets candidates" in v["Body 3"] and "religious law" not in v["Body 3"], \
        "the advisory row should mention the vetting body without performing the vetting itself"
    return "one row alone both vets candidates for the legislature and checks its laws against religious law"


def q24(table, item):
    v = _bodies(table)
    f = v["Body 2"]
    for phrase in ("not in session", "sets its agenda", "supervises the election", "interprets the constitution"):
        assert phrase in f, f"the keyed row must include {phrase!r}; it reads {f!r}"
    for lab in ("Body 1", "Body 3", "Body 4"):
        assert "sets its agenda" not in v[lab], f"{lab} must not also set the legislature's agenda"
    return "one row alone carries all four of the framework's functions for that committee"


def q25(table, item):
    v = _bodies(table)
    f = v["Body 3"]
    assert "advisory" in f and "resolves disputes" in f, f"the keyed row reads {f!r}"
    assert "vets candidates" in v["Body 1"], \
        "the keyed row's description refers to the vetting body, which must be a different row"
    for lab in ("Body 1", "Body 2", "Body 4"):
        assert "resolves disputes" not in v[lab], f"{lab} must not also resolve disputes"
    return "one row alone is advisory and resolves disputes between the legislature and the separate vetting body"


CLAIMS = [
 ("without influence from other branches",
  "The CED's scoring guidelines for its sample comparative-analysis question define legislative independence as the degree to which a legislature is free to exercise its powers without influence from other branches or institutions. Output, selection method, structure and timetable are different matters."),
 ("other governmental institutions",
  "EK PAU-3.F.1 states that legislative powers can be constrained by other governmental institutions and then names four, while the CED's scoring guidelines add elections and the executive branch as further sources of constraint."),
 ("the Politburo Standing Committee",
  "EK PAU-3.F.1.a states that China's Politburo Standing Committee is the actual center of power in the Chinese state. EK PAU-3.E.1.a states only what the constitution RECOGNIZES about the National People's Congress, which is a claim about a text rather than about actual power."),
 ("interpreting the Constitution and laws",
  "EK PAU-3.F.1.b lists assuming legislative duties when the Congress is not in session, setting its legislative agenda, supervising its member elections, and interpreting the Constitution and laws. The rejected sets belong to Iran's two councils, Russia's Federation Council and the House of Lords."),
 ("for most of the year, when the full body is not in session",
  "EK PAU-3.F.1.b states that the Standing Committee assumes legislative duties most of the year when the National People's Congress is not in session. A body exercising the legislature's powers for most of the year is the constraint EK PAU-3.F.1 describes."),
 ("supervising the election of its members",
  "EK PAU-3.F.1.b names supervising National People's Congress member elections among the Standing Committee's functions. Agenda setting, interpretation and acting between sessions concern what the body does rather than who belongs to it, and approving the premier is the full Congress's function at EK PAU-3.E.1.a."),
 ("interpreting the Constitution and laws",
  "EK PAU-3.F.1.b names interpreting the Constitution and laws among the Standing Committee's functions, which is authority over what the law means rather than over who makes it or when. Legitimizing executive policies belongs to the full Congress at EK PAU-3.E.1.a."),
 ("advisory committee selected by the Supreme Leader",
  "EK PAU-3.F.1.c states that Iran's Expediency Council is selected by the Supreme Leader as an advisory committee to resolve disputes between the Majles and the Guardian Council, and EK PAU-3.C.2.b lists the Council among the Supreme Leader's appointments."),
 ("vets candidates and oversees the Majles",
  "EK PAU-3.F.1.d states that Iran's Guardian Council vets candidates and oversees the Majles to make sure laws comply with Islamic law, and EK PAU-3.E.1.b adds that the Majles acts under its supervision. Dispute resolution belongs to the Expediency Council instead."),
 ("actual center of power in the state, while the other exercises",
  "EK PAU-3.F.1.a identifies the Politburo Standing Committee as the actual center of power in the Chinese state, while EK PAU-3.F.1.b describes the Standing Committee of the National People's Congress acting for the legislature between sessions, setting its agenda, supervising its member elections and interpreting the law."),
 ("advises on disputes between the legislature and that vetting body",
  "EK PAU-3.F.1.d gives the Guardian Council the vetting and compliance role and EK PAU-3.F.1.c gives the Expediency Council the advisory dispute-resolving role. EK PAU-3.C.2.b has the Supreme Leader appointing the Expediency Council and half the Guardian Council, so neither stands apart from that office."),
 ("facilitating compromise between factions, extending civil liberties",
  "EK PAU-3.F.2 lists responding to public demand, openly debating policy, facilitating compromise between factions, extending civil liberties, and restricting the power of the executive. The last is the same function EK PAU-3.B.1 and EK PAU-3.B.2 describe comparatively."),
 ("openly debating policy",
  "EK PAU-3.F.2 names openly debating policy among the ways legislatures reinforce legitimacy and stability, and EK DEM-1.C.4 treats the open circulation of information about policy making as transparency. The debate itself, not its outcome, is this route."),
 ("facilitating compromise between factions",
  "EK PAU-3.F.2 names facilitating compromise between factions among the ways legislatures reinforce legitimacy and stability, and EK LEG-1.B.2 adds that peaceful resolution of conflicts reinforces legitimacy. A brokered agreement between rival blocs supplies both."),
 ("extending civil liberties",
  "EK PAU-3.F.2 names extending civil liberties among the ways legislatures reinforce legitimacy and stability, and EK LEG-1.C.3 describes reform pressure producing institutions or policies that protect them. Enacting the protection is that route."),
 ("restricting the power of the executive",
  "EK PAU-3.F.2 names restricting the power of the executive among the ways legislatures reinforce legitimacy and stability, and EK PAU-3.B.2 lists refusing to pass executive-proposed legislation among the parliamentary checks. Withholding a delegated power is that restriction operating."),
 ("theocratic rules",
  "The CED's scoring guidelines accept that the Iranian government constrains the Majles to give the Supreme Leader more power and to make sure all institutions abide by theocratic rules, and add that the Expediency Council can constrain the Majles to reduce its power. EK PAU-3.F.1.c and .d supply the mechanisms."),
 ("every five years",
  "The CED's scoring guidelines accept that in the United Kingdom the legislature is constrained by elections, that all members of the House of Commons are up for election every 5 years, and that this constrains lawmakers to work for their constituents. EK PAU-3.E.1.f gives the Lords a delaying rather than a veto role."),
 ("more concentrated power",
  "The CED's scoring guidelines accept that in Nigeria the House of Representatives is constrained by the executive branch because the president wants to have more concentrated power. The vetting body and the delaying chamber offered against it belong to Iran and the United Kingdom."),
 ("originates the largest share of bills itself",
  "The CED's scoring guidelines make legislative independence the degree to which a legislature exercises its powers free of outside influence, and amending the executive's bills, originating its own and sitting often are all such exercises. Recomputed in q20 above: all three columns point to the same row."),
 ("sits on twelve days a year",
  "EK PAU-3.F.1.b describes a standing committee assuming legislative duties most of the year when the full body is not in session, so the matching record is a chamber that sits rarely and changes little when it does. Recomputed in q21 above: one row sits on a tenth of the days of another and amends least."),
 ("53 percentage points",
  "Recomputed in q22 above by subtracting the smallest figure in the amendment column from the largest. Every distractor is a real figure from the wrong pair of rows, the wrong column, or a single value read as a difference."),
 ("vets candidates for the legislature and oversees it",
  "EK PAU-3.F.1.d states that Iran's Guardian Council vets candidates and oversees the Majles for compliance with Islamic law, and EK PAU-3.E.1.b confirms that supervision. Recomputed in q23 above: only one row carries both functions."),
 ("supervises the election of its members, and interprets",
  "EK PAU-3.F.1.b lists all four functions for the Standing Committee of the National People's Congress, and EK PAU-3.F.1 places it among the institutions constraining legislative powers. Recomputed in q24 above: only one row carries all four."),
 ("advisory committee that resolves disputes",
  "EK PAU-3.F.1.c states that the Expediency Council is selected by the Supreme Leader as an advisory committee to resolve disputes between the Majles and the Guardian Council. Recomputed in q25 above: one row alone is advisory and resolves disputes with a separate vetting body named in another row."),
 ("maintain stability and prevent corruption",
  "The CED's scoring guidelines accept that in Mexico the legislature is constrained by elections as a way to maintain stability and prevent corruption, and give a parallel account for the United Kingdom, where elections constrain lawmakers to work for their constituents."),
 ("standing committee that assumes the legislature's duties",
  "EK PAU-3.F.1.b describes a committee OF the National People's Congress exercising that body's duties, setting its agenda, supervising its member elections and interpreting the law, so this constraint runs from within. EK PAU-3.F.1.a, .c and .d name bodies outside the legislature they affect."),
 ("rejected or rewritten the executive's proposals",
  "The CED's scoring guidelines define legislative independence as freedom to exercise the legislature's powers without influence from other branches or institutions, so the evidence must show powers exercised against or apart from outside preference. Size, premises and party count say nothing about that."),
 ("two",
  "EK PAU-3.F.1.a and .b name two Chinese bodies and EK PAU-3.F.1.c and .d two Iranian ones, so the four examples come from two course countries. Constraints on the other four countries' legislatures appear in the CED's scoring guidelines rather than in this statement."),
 ("five named ways",
  "EK PAU-3.F.1 supplies the constraints and EK PAU-3.F.2 the five ways a legislature can reinforce legitimacy and stability, so the pair describes what limits a legislature and what it contributes when unlimited. The CED's scoring guidelines add elections and the executive as constraints in democratic cases too."),
]

cg.check(k2_7, CLAIMS, table_checks={20: q20, 21: q21, 22: q22, 23: q23, 24: q24, 25: q25})
