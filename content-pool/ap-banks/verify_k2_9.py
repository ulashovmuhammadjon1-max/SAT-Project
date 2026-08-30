"""Key audit for AP COMPARATIVE GOVERNMENT 2.9 Independent Judiciaries.

One (anchor, claim) per item, in module order. The anchor must appear in the
keyed choice and in no distractor; the claim states what the key rests on.

WHAT THE KEYS REST ON
---------------------
  PAU-3.H.1  the DEGREE of a judiciary's independence depends on five things: the
             AUTHORITY to overrule executive and legislative actions, the PROCESS
             by which judicial officials acquire their jobs, the LENGTH of judicial
             terms, the professional and academic BACKGROUNDS expected of them, and
             the PROCESSES USED TO REMOVE judges from their posts
  PAU-3.H.2  independent judiciaries can strengthen democracy by MAINTAINING CHECKS
             AND BALANCES, PROTECTING RIGHTS AND LIBERTIES, ESTABLISHING THE RULE
             OF LAW, and MAINTAINING SEPARATION OF POWERS

Country applications are held to PAU-3.G.1 -- party control of most appointments
(.a), Sharia training for Iranian judges (.b), Mexico's transition and its 15-year
term (.c, .d), Nigeria's judicial council and its corruption-reduction effort (.e,
.f), Russia's constitutional review power that has not been used against the
governing branches (.g, .h). PAU-1.C.3 supplies the corruption link, PAU-1.B.1.a
the rule of law and PAU-1.B.2 the general point about branch independence.

Suggested skill 5.B is Argumentation, which is why items 19, 23, 24 and 26 ask
what evidence would support or weaken a claim rather than what the framework says.

AN HONEST GAP, KEYED RATHER THAN FILLED
---------------------------------------
PAU-3.H.1 names the PROCESSES USED TO REMOVE JUDGES as one of its five
determinants, and the framework gives NO country illustration of a judicial
removal process -- not in any of PAU-3.G.1's nine sub-points, not anywhere else.
Item 18 keys that absence. The alternative would have been to invent a removal
rule for one of the six, which SOCIAL_BRIEF.md forbids.

WHY THE MIXED CASE MATTERS
--------------------------
PAU-3.H.1 speaks of the DEGREE of independence, and PAU-3.G.1.g supplies the case
that makes the word necessary: a court with constitutional review authority that
has not used it against the governing branches. Items 13, 20 and 27 turn on that,
and the data table for items 20-22 is built so that one row is strong on some
determinants and weak on others.

FIVE choices per item (A-E); see AP_COMP_GOV_CED.md.
"""
import cg_check as cg
import k2_9

TERM = "Stated length of a judicial term"
POWER = "Authority to overrule executive and legislative acts"
REMOVAL = "Who decides the removal of a judge"
REVIEWED = "Executive acts reviewed, 2000-2020"
OVERRULED = "Executive acts overruled, 2000-2020"
REMOVED = "Judges removed by the executive, 2000-2020"


def _fact(table):
    return {str(r[0]): (cg.num(r[1]), str(r[2]), str(r[3])) for r in table["rows"]}


def q20(table, item):
    v = _fact(table)
    term, power, removal = v["Judiciary 2"]
    assert term == min(x[0] for x in v.values()), "the keyed row must have the shortest stated term"
    assert "never exercised" in power, f"the keyed row's power must be unexercised; it reads {power!r}"
    assert "head of government alone" in removal, f"the keyed row's removal route reads {removal!r}"
    for lab in ("Judiciary 1", "Judiciary 3"):
        assert "never exercised" not in v[lab][1], f"{lab} must exercise its power"
        assert "head of government alone" not in v[lab][2], f"{lab} must not be removable by the executive alone"
    return "one row is worst on all three of term length, exercise of the overruling power, and who decides removal"


def q21(table, item):
    v = _fact(table)
    term, power, removal = v["Judiciary 3"]
    assert term == max(x[0] for x in v.values()), "the keyed row must have the longest stated term"
    assert "regularly exercised" in power, f"the keyed row's power reads {power!r}"
    assert "senior judges" in removal, f"the keyed row's removal route reads {removal!r}"
    assert "legislature" in v["Judiciary 1"][2], \
        "the nearest rival's removal must be decided by another branch, which is what separates them"
    assert v["Judiciary 1"][0] < term, "the nearest rival must also have a shorter term"
    return "one row alone pairs the longest term and an exercised power with a removal decision kept inside the judiciary"


def q22(table, item):
    terms = [x[0] for x in _fact(table).values()]
    gap = max(terms) - min(terms)
    assert gap == 16, f"the keyed difference recomputes to {gap}"
    assert sorted(terms) == [4, 15, 20], f"the stated terms read {sorted(terms)}"
    assert 15 - 4 == 11 and 20 - 15 == 5, "the 11 and 5 distractors must be the other pairwise gaps"
    assert min(terms) == 4 and max(terms) == 20, "the 4 and 20 distractors must be single stated terms"
    return f"the stated terms are {sorted(terms)} and the largest difference is {gap:.0f}, with every distractor another gap or a single term"


def _over(table):
    return {lab: (cg.cell(table, lab, REVIEWED), cg.cell(table, lab, OVERRULED), cg.cell(table, lab, REMOVED))
            for lab in cg.labels(table)}


def q23(table, item):
    v = _over(table)
    share = {lab: o / r for lab, (r, o, _) in v.items()}
    assert max(share, key=share.get) == "Court A", f"the largest overrule share belongs to {max(share, key=share.get)}"
    assert v["Court A"][2] == 0, "the keyed row must show no judges removed by the executive"
    assert all(v[lab][2] > 0 for lab in v if lab != "Court A"), \
        "every other row must show at least one such removal, so the key is unique on that column too"
    assert v["Court C"][0] == min(x[0] for x in v.values()), \
        "the rejected 'fewest acts reviewed' option must name a different row"
    return f"the three overrule shares are {[round(share[l], 3) for l in v]} and only one row shows no judges removed by the executive"


def q24(table, item):
    v = _over(table)
    share = {lab: o / r for lab, (r, o, _) in v.items()}
    assert min(share, key=share.get) == "Court B", f"the smallest overrule share belongs to {min(share, key=share.get)}"
    assert share["Court B"] < 0.02, "the key says under two percent"
    assert v["Court B"][2] == 11 and v["Court B"][2] == max(x[2] for x in v.values()), \
        f"the keyed row must show the most executive removals; it shows {v['Court B'][2]}"
    assert v["Court A"][2] == 0, "'each had at least one judge removed' must be false"
    return "one row combines the smallest overrule share, under two percent, with by far the most removals by the executive"


def q25(table, item):
    v = _over(table)
    r, o, _ = v["Court C"]
    pct = o / r * 100
    assert abs(pct - 23) < 1.0, f"the keyed share recomputes to {pct:.1f} percent"
    assert abs(v["Court A"][1] / v["Court A"][0] * 100 - 27) < 1.0, "the 27 distractor must be another row's share"
    assert abs(v["Court B"][1] / v["Court B"][0] * 100 - 2) < 1.0, "the 2 distractor must be the third row's share"
    assert abs(100 - pct - 77) < 1.0, "the 77 distractor must be the complementary share"
    assert r == 95, "the 95 distractor must be the acts reviewed, read as a percentage"
    return f"{o:.0f} of {r:.0f} is {pct:.1f} percent, and every distractor is another row's share, the complement, or a raw count"


CLAIMS = [
 ("processes used to remove judges",
  "EK PAU-3.H.1 names the courts' authority to overrule executive and legislative actions, the process by which judicial officials acquire their jobs, the length of judicial terms, the backgrounds expected of them, and the processes used to remove judges as the five determinants of the degree of independence."),
 ("authority the courts have to overrule executive and legislative actions",
  "EK PAU-3.H.1 names this first among its five determinants. The other four concern how judges arrive, how long they stay, what they must have studied, and how they can be made to leave."),
 ("process by which judicial officials acquire their jobs",
  "EK PAU-3.H.1 names the process by which judicial officials acquire their jobs among its determinants, and EK PAU-3.G.1.a and EK PAU-3.G.1.f supply the two contrasting routes the item describes."),
 ("the length of judicial terms",
  "EK PAU-3.H.1 names the length of judicial terms among its determinants, and EK PAU-3.G.1.d prints one, Mexico's 15-year Supreme Court term. A judge facing frequent reappointment depends on whoever grants it."),
 ("professional and academic backgrounds",
  "EK PAU-3.H.1 names the professional and academic backgrounds judicial officials are expected to have among its determinants, and EK PAU-3.G.1.b gives the framework's instance, Iranian judges trained in Islamic Sharia law."),
 ("the processes used to remove judges from their posts",
  "EK PAU-3.H.1 names the processes used to remove judges from their posts among its determinants. Removal is separate from appointment and from term length, since a fixed term means little if the officeholder can be dismissed at will inside it."),
 ("maintaining checks and balances, protecting rights and liberties",
  "EK PAU-3.H.2 names maintaining checks and balances, protecting rights and liberties, establishing the rule of law, and maintaining separation of powers as the ways independent judiciaries strengthen democracy. Each limits or structures power rather than exercising it."),
 ("maintaining checks and balances",
  "EK PAU-3.H.2 names maintaining checks and balances among the contributions of an independent judiciary, and EK PAU-1.B.2 explains why it matters, since independence can prevent any one branch from controlling all governmental power."),
 ("protecting rights and liberties",
  "EK PAU-3.H.2 names protecting rights and liberties among the contributions of an independent judiciary, EK PAU-1.C.3 repeats that independent judiciaries protect individual liberties and civil rights, and EK PAU-3.G.1.i gives one country's Supreme Court that function explicitly."),
 ("establishing the rule of law",
  "EK PAU-3.H.2 names establishing the rule of law among the contributions of an independent judiciary, and EK PAU-1.B.1.a describes the rule of law as governance by law rather than by arbitrary decisions of individual officials. Applying the same published rules to everyone is that principle operating."),
 ("maintaining separation of powers",
  "EK PAU-3.H.2 names maintaining separation of powers among the contributions of an independent judiciary, and EK PAU-1.B.2 states that branch independence can prevent one branch from controlling all governmental power. Returning a power to the branch the constitution assigned it to is that function."),
 ("reducing political corruption",
  "EK PAU-1.C.3 states that political corruption inhibits democratization and that independent judiciaries can reduce it while protecting individual liberties and civil rights, and EK PAU-3.G.1.e connects this to Nigeria's effort to reestablish its judiciary's legitimacy and independence."),
 ("has not been used to limit the authority of the governing branches",
  "EK PAU-3.H.1 makes the authority to overrule executive and legislative actions a determinant of independence, and EK PAU-3.G.1.g states both that Russia's courts hold the power of judicial review constitutionally and that it has not been used to limit the governing branches. Both halves belong to the assessment."),
 ("governing party controls most judicial appointments",
  "EK PAU-3.H.1 makes the process by which judicial officials acquire their jobs a determinant of independence, and EK PAU-3.G.1.a states that the Chinese Communist Party controls most judicial appointments and that the judicial system is subservient to its decisions."),
 ("judicial council recommends candidates before the head of state appoints",
  "EK PAU-3.G.1.f states that Nigeria's Supreme Court judges are recommended by a judicial council and appointed by the president with confirmation by the Senate, and EK PAU-3.G.1.e records an effort to reestablish the judiciary's legitimacy and independence. The 15-year term belongs to Mexico under EK PAU-3.G.1.d."),
 ("Mexico",
  "EK PAU-3.G.1.d states that Mexican Supreme Court magistrates are approved for a term of 15 years, and no other statement in the framework gives a judicial term length for any course country."),
 ("trained in Islamic Sharia law",
  "EK PAU-3.H.1 names the professional and academic backgrounds judicial officials are expected to have among its determinants, and EK PAU-3.G.1.b states that Iranian judges must be trained in Islamic Sharia law because the judiciary's major function is a legal system based on religious law."),
 ("no country illustration",
  "EK PAU-3.H.1 lists the processes used to remove judges as a determinant, but none of EK PAU-3.G.1's nine sub-points describes a removal process for any course country and no other statement supplies one. Asserting a removal rule for any of the six would go beyond the framework."),
 ("chosen through a process no single branch controls",
  "EK PAU-3.H.1's determinants are the authority to overrule other branches, the acquisition process, term length, expected backgrounds and removal processes, and the keyed finding reports three of the five at once. Caseload, reputation, premises and geographic origin bear on none of them."),
 ("shortest stated term",
  "EK PAU-3.H.1 makes the authority to overrule, the length of terms and the removal process three of its five determinants. Recomputed in q20 above: one row is worst on all three, and EK PAU-3.G.1.g shows the framework treating an unexercised constitutional power as the weaker case."),
 ("removal decided by senior judges",
  "EK PAU-3.H.1's determinants include term length, the authority to overrule and the removal process. Recomputed in q21 above: one row has the longest term, a power actually used, and a removal decision kept inside the judiciary, whereas removal by the legislature is still a decision another branch makes."),
 ("16 years",
  "Recomputed in q22 above by subtracting the shortest stated term from the longest. Every distractor is another pairwise gap or a single stated term read as a difference."),
 ("no judge removed by the executive",
  "EK PAU-3.H.1 makes the authority to overrule and the processes used to remove judges two of its five determinants. Recomputed in q23 above: one row leads on the overrule share and is alone in showing no removals by the executive."),
 ("eleven of its judges were removed",
  "EK PAU-3.H.1 names the processes used to remove judges among its determinants, so removals by the executive bear directly on the claim. Recomputed in q24 above: one row combines the smallest overrule share with by far the most such removals, and another row shows none at all."),
 ("23 percent",
  "Recomputed in q25 above by dividing that court's overruled acts by the acts it reviewed. Every distractor is another row's share, the complementary share, or a raw count read as a percentage."),
 ("removed shortly afterwards by the officials whose acts they had annulled",
  "EK PAU-3.H.1 names the processes used to remove judges from their posts among its five determinants, so removal by the very officials a judge ruled against strikes at independence directly. Caseload, publication, a qualification requirement and location bear on none of the five."),
 ("strong on one determinant and weak on another",
  "EK PAU-3.H.1 speaks of the DEGREE of independence and lists five separate things it depends on, and EK PAU-3.G.1.g supplies the mixed case: a court holding constitutional review authority that has not used it against the governing branches."),
 ("only one of those chambers is elected",
  "EK PAU-3.G.1.d has Mexico's magistrates nominated by the president and approved by the elected Senate, EK PAU-3.G.1.h has Russia's judges approved by the appointed Federation Council, EK PAU-3.G.1.c calls Mexico's judiciary in transition toward independence, and EK PAU-3.G.1.g says Russia's review power has not been used against the governing branches."),
 ("prevent any one branch from controlling all governmental power",
  "EK PAU-1.B.2 states that the branches of national government in democratic regimes are more likely to be independent of one another than in authoritarian regimes and that such independence can prevent one branch from controlling all governmental power. EK PAU-3.H.2's checks and balances and separation of powers apply that to courts."),
 ("four named ways",
  "EK PAU-3.H.1 supplies five determinants of the DEGREE of independence and EK PAU-3.H.2 the four ways an independent judiciary can strengthen democracy: checks and balances, protection of rights and liberties, establishment of the rule of law, and separation of powers."),
]

cg.check(k2_9, CLAIMS, table_checks={20: q20, 21: q21, 22: q22, 23: q23, 24: q24, 25: q25})
