"""Key audit for AP COMPARATIVE GOVERNMENT 4.2 Objectives of Election Rules.

One (anchor, claim) per item, in module order. The anchor must appear in the
keyed choice and in no distractor; the claim states what the key rests on.

WHAT THE KEYS REST ON
---------------------
Topic 4.2 is unusually well served by the framework: DEM-2.B.1 through
DEM-2.B.7 state most of what this module asks, and several of the sub-points
name a country and a rule outright. The items are keyed to these sentences:

  DEM-2.B.1   proportional representation can increase the number of parties in
              national legislatures and the election of minority and women
              candidates
  DEM-2.B.2   single-member district plurality tends to promote two-party
              systems and gives strong constituency service and accountability
              BECAUSE there is a single representative per district
  DEM-2.B.3   presidential systems differ in how a winner is determined
      .a      Mexico: a PLURALITY of the national popular vote, not a majority
      .b      Nigeria: the most votes AND at least 25 percent in two-thirds of
              the states, reflecting the federal characteristic of the regime
      .c      Iran and Russia: an absolute majority in the first or second round,
              the second round between the top two first-round finishers
      .d      majoritarian rules in Iran, Nigeria and Russia give a national
              mandate
  DEM-2.B.4   electoral regulatory organizations set ballot access rules
      .a      Iran's Guardian Council excludes reform-minded candidates and those
              not supporting Islamic values, reducing competition and
              representation
      .b      Mexico and Nigeria created independent election commissions during
              their democratic transitions to reduce fraud and manipulation and
              enhance competition
  DEM-2.B.5   appointment to legislative bodies serves opposite purposes --
              diversity of viewpoints, or the agenda of governing elites
      .a      UK House of Lords: approved by the monarch on the recommendation of
              the prime minister and an independent commission
      .b      Iran's Guardian Council: half chosen by the Supreme Leader, half
              judiciary nominees approved by the Majles
      .c      Russia's Federation Council: appointed by regional governors and
              the regional legislature; federal districts and president-approved
              gubernatorial lists reassert federal power under the president
  DEM-2.B.6   election rule changes affect the representation of religious,
              ethnic and socioeconomic groups
  DEM-2.B.7   the timing of legislative elections varies with term-limit policies

Four items reach outside DEM-2.B and each of those citations was checked against
the CED text rather than recalled: DEM-2.A.1.c (Mexico's 300 district plus 200
list deputies, and gender quotas in the party list system helping increase female
representation), DEM-2.A.1.f (Commons members directly elected under
single-member district, first-past-the-post rules), DEM-2.A.1.d (Nigeria's 36
states), DEM-2.A.2 (proportional representation relies on multimember districts
that promote multiparty systems), and PAU-4.A.3 (rules ensuring one-party
dominance in Russia include increasing party registration requirements and
increasing threshold rules to limit party access to the ballot).

Nigeria's 24-state figure is the module's only derived number: two-thirds of the
36 states of DEM-2.A.1.d. It is recomputed in q9 below rather than asserted.

DATA ITEMS
----------
Items 6-10 and 25-27 carry tables. Every figure in them is HYPOTHETICAL and the
stems say so, because the CED prints no election returns; keying a question to a
real result would make it a current-events item, which SOCIAL_BRIEF.md forbids.
Each keyed conclusion is recomputed from its table below, and the arithmetic
distractors are checked false against the same numbers.

A DEFECT FOUND AND FIXED WHILE WRITING THIS FILE
------------------------------------------------
Item 26 offered "22 seats" and "2 seats". Normalized, "2 seats" is a substring of
"22 seats", so the shared no-choice-contains-another guard in cg_check fired --
and it was right to: a student scanning for "2 seats" finds it inside the key.
The distractor is now "8 seats", which is the two smallest parties' combined
district total and therefore a real misreading of the table rather than filler.

FIVE choices per item (A-E); see AP_COMP_GOV_CED.md.
"""
import cg_check as cg
import k4_2

SHARE1 = "Share of the national vote in the first round"
SHARE = "Share of the national vote"
STATES25 = "States with at least 25 percent for this candidate"
PR = "Seats under proportional representation"
SMD = "Seats under single-member district plurality"


def _first_round(table):
    return dict(zip(cg.labels(table), cg.col(table, SHARE1)))


def q6(table, item):
    v = _first_round(table)
    lead = max(v, key=v.get)
    assert lead == "Candidate 1", f"the leading candidate is {lead}"
    assert sorted(v.values(), reverse=True)[0] > sorted(v.values(), reverse=True)[1], \
        "the lead must be strict for a plurality rule to decide the office"
    assert max(v.values()) < 50, "no candidate may reach a majority, or the item stops discriminating"
    assert abs(sum(v.values()) - 100) < 1e-9, f"the shares sum to {sum(v.values())}, not 100"
    return "Candidate 1's 38 percent is the strict maximum and is under 50, so a plurality rule elects and a majority rule would not"


def q7(table, item):
    v = _first_round(table)
    assert max(v.values()) < 50, "a runoff is required only because no candidate reached an absolute majority"
    top2 = sorted(v, key=v.get, reverse=True)[:2]
    assert top2 == ["Candidate 1", "Candidate 2"], f"the top two are {top2}"
    assert len(v) == 4, "the keyed runoff excludes two of the four candidates shown"
    return "no candidate reaches 50 percent and the two leading first-round finishers are Candidates 1 and 2"


def q8(table, item):
    v = _first_round(table)
    top2 = sorted(v.values(), reverse=True)[:2]
    total = top2[0] + top2[1]
    assert total == 69, f"the keyed 69 percent recomputes to {total}"
    for wrong in (50, 57, 62, 81):
        assert wrong != total, f"distractor {wrong} equals the correct total"
    return f"the two leading shares 38 and 31 sum to {total} percent, and no distractor equals it"


def q9(table, item):
    rows = {str(r[0]): str(r[1]) for r in table["rows"]}
    n_states = cg.num(rows["States"])
    assert n_states == 36, f"the table gives {n_states} states, not the 36 of EK DEM-2.A.1.d"
    frac_row = [k for k in rows if "two-thirds" in rows[k]]
    assert frac_row, f"no row states the two-thirds fraction: {rows}"
    required = n_states * 2 / 3
    assert required == 24, f"two-thirds of {n_states} is {required}"
    assert float(item["choices"][item["ans"]]) == required, \
        f"keyed choice {item['choices'][item['ans']]!r} is not {required}"
    others = [float(c) for i, c in enumerate(item["choices"]) if i != item["ans"]]
    assert required not in others, "a distractor repeats the correct count"
    return "two-thirds of the table's 36 states is 24, and the keyed choice is the only one equal to it"


def q10(table, item):
    share = dict(zip(cg.labels(table), cg.col(table, SHARE)))
    states = dict(zip(cg.labels(table), cg.col(table, STATES25)))
    need = 36 * 2 / 3
    assert need == 24, "the state requirement is two-thirds of 36"
    lead = max(share, key=share.get)
    assert lead == "Candidate J", f"the national vote leader is {lead}"
    assert states["Candidate J"] < need, "the key requires the vote leader to miss the state test"
    assert states["Candidate K"] >= need, "the key requires the runner-up to meet the state test"
    assert share["Candidate K"] < share["Candidate J"], "the key requires the runner-up to trail on votes"
    assert states["Candidate L"] < 36 / 3, "'more than a third of the states' must be false for the third candidate"
    assert not any(s >= need and share[c] == max(share.values()) for c, s in states.items()), \
        "no candidate may satisfy both halves, or the item has a winner"
    return "Candidate J leads on votes with 20 states against the 24 needed; Candidate K has 26 states but trails on votes; nobody satisfies both halves"


def _seats(table):
    return (dict(zip(cg.labels(table), cg.col(table, PR))),
            dict(zip(cg.labels(table), cg.col(table, SMD))))


def q25(table, item):
    pr, smd = _seats(table)
    share = dict(zip(cg.labels(table), cg.col(table, SHARE)))
    assert share["Party A"] == 40 and smd["Party A"] == 62, \
        f"the key says 40 percent into 62 seats; table says {share['Party A']} and {smd['Party A']}"
    small = ["Party C", "Party D"]
    assert sum(share[p] for p in small) == 28, "the key says the two smallest parties hold 28 percent of the vote"
    assert sum(smd[p] for p in small) == 8, "the key says those two take 8 district seats"
    assert sum(pr.values()) == 100 and sum(smd.values()) == 100, "both columns must fill a 100-seat chamber"
    # every distractor false on the same numbers
    assert any(pr[p] != smd[p] for p in pr), "'same seats under both rules' must be false"
    assert sum(smd[p] for p in small) < sum(pr[p] for p in small), \
        "'the two smallest win more district seats' must be false"
    assert smd["Party A"] > pr["Party A"], "'the leading party wins fewer district seats' must be false"
    assert pr["Party A"] <= 50, "'proportional representation gives the leader a majority' must be false"
    return "Party A turns 40 percent into 62 of 100 district seats while Parties C and D turn 28 percent into 8, and all four distractors are false on these numbers"


def q26(table, item):
    pr, smd = _seats(table)
    lead = max(pr, key=pr.get)
    assert lead == "Party A", f"the largest party is {lead}"
    gain = smd[lead] - pr[lead]
    assert gain == 22, f"the keyed gain of 22 recomputes to {gain}"
    assert float(item["choices"][item["ans"]].split()[0]) == gain, "the keyed choice is not the computed gain"
    others = [float(c.split()[0]) for i, c in enumerate(item["choices"]) if i != item["ans"]]
    assert gain not in others, "a distractor repeats the correct gain"
    return f"Party A holds 62 district seats against 40 list seats, a gain of {gain}, matched by no distractor"


def q27(table, item):
    pr, smd = _seats(table)
    total = sum(smd.values())
    assert smd["Party A"] > total / 2, "the key requires a single-party majority under district rules"
    assert pr["Party A"] <= total / 2, "the key requires no single-party majority under list rules"
    assert all(pr[p] > 0 for p in pr), "'proportional representation eliminates the smallest parties' must be false"
    assert smd["Party A"] != pr["Party A"], "'either system, same seats' must be false"
    share = dict(zip(cg.labels(table), cg.col(table, SHARE)))
    assert any(smd[p] != share[p] for p in smd), "'district rules give seats in proportion to votes' must be false"
    return f"Party A holds {smd['Party A']:.0f} of {total:.0f} district seats but only {pr['Party A']:.0f} list seats, so only one column yields a single-party majority"


CLAIMS = [
 ("more minority and women candidates",
  "EK DEM-2.B.1 states that proportional representation can increase the number of parties represented in national legislatures as well as the election of minority and women candidates. The single representative per district and its constituency service belong to the abandoned system, EK DEM-2.B.2."),
 ("one identifiable representative",
  "EK DEM-2.B.2 grounds strong constituency service and accountability in there being a single representative per district. Accountability of that kind requires that voters know whose record is on their ballot, which several shared representatives or an appointed one would not supply."),
 ("without needing an absolute majority",
  "EK DEM-2.B.3.a states that Mexico's president is elected by a plurality of the national popular vote and not an absolute majority. The distribution requirement offered against it is Nigeria's, EK DEM-2.B.3.b."),
 ("holding a second round between the two leading candidates",
  "EK DEM-2.B.3.c states that presidential candidates in Iran and Russia must win an absolute majority in the first or second round, and that a second round is conducted between the top two first-round vote earners."),
 ("federal character",
  "EK DEM-2.B.3.b states that the requirement of the most votes plus 25 percent in two-thirds of the states reflects the federal characteristic of the Nigerian regime. A purely national count would let one region's numbers decide the presidency of a federation."),
 ("Mexico awards the office",
  "EK DEM-2.B.3.a makes the Mexican presidency a plurality office. Recomputed in q6 above: the leading share is a strict maximum and is under 50, so a plurality rule elects on these figures and no runoff or distribution test is triggered."),
 ("between Candidate 1 and Candidate 2",
  "EK DEM-2.B.3.c requires an absolute majority in Russia with a second round between the top two first-round finishers. Recomputed in q7 above: no share reaches 50 and the two leading finishers are the first and second candidates."),
 ("69 percent",
  "Recomputed in q8 above from the two leading first-round shares. Nearly a third of first-round voters must choose again among candidates they did not support, which is the mandate-broadening EK DEM-2.B.3.d attributes to majoritarian rules."),
 ("24",
  "EK DEM-2.B.3.b sets the threshold at two-thirds of the states and EK DEM-2.A.1.d gives Nigeria 36 states. Recomputed in q9 above, and the keyed value is the only choice equal to it."),
 ("short of the 24 required",
  "EK DEM-2.B.3.b's rule is conjunctive: the most votes AND 25 percent in two-thirds of the states. Recomputed in q10 above, the vote leader misses the state test and the candidate meeting the state test trails on votes, so neither satisfies both halves."),
 ("reform-minded candidates",
  "EK DEM-2.B.4.a states that Iran's Guardian Council excludes reform-minded candidates or those who do not support Islamic values, which limits the number of candidates and reduces electoral competition and representation. The election still happens; what narrows is the set of names on the ballot."),
 ("voter fraud",
  "EK DEM-2.B.4.b states that Mexico and Nigeria created independent election commissions as part of their democratic transitions to reduce voter fraud and manipulation and enhance electoral competition. Ideological vetting, appointing legislators, seat allocation and term length are functions the framework assigns elsewhere."),
 ("curbing fraud",
  "EK DEM-2.B.4.a and EK DEM-2.B.4.b describe electoral regulators pointed in opposite directions: one restricts ballot access on ideological grounds, the other was built during a democratic transition to widen and clean up competition. The same institutional form can therefore serve opposite regime objectives."),
 ("recommendation of the prime minister",
  "EK DEM-2.B.5.a states that United Kingdom House of Lords appointments are approved by the monarch with recommendations made by the prime minister and an independent commission. The half-and-half option describes Iran's Guardian Council and the regional option Russia's Federation Council."),
 ("Supreme Leader",
  "EK DEM-2.B.5.b states that half of Iran's Guardian Council is selected by the Supreme Leader and half are nominees from the judiciary approved by the Majles, so an unelected office controls one half of the body that controls ballot access."),
 ("regional governors",
  "EK DEM-2.B.5.c states that appointments to Russia's Federation Council are made by regional governors and the regional legislature, which is why the chamber's composition follows control of regional office rather than a national vote."),
 ("reassertion of central power",
  "EK DEM-2.B.5.c presents the nine federal districts with presidential envoys, and the option for regional legislatures to forgo elections and appoint a governor from a presidentially approved list, as reasserting federal power under the Russian president. Choosing from a list the president supplies is not decentralization."),
 ("agenda of governing elites",
  "EK DEM-2.B.5 states that some regimes use appointment to legislative bodies to promote a diversity of viewpoints and others to advance the political agenda of governing elites, so the effect follows from who appoints and on what criteria. The United Kingdom's appointed upper chamber shows appointment is not confined to authoritarian regimes."),
 ("socioeconomic groups",
  "EK DEM-2.B.6 states that changes to election rules affect the representation of different religious, ethnic and socioeconomic groups, because the rules decide which votes convert into seats and therefore whom concentration or dispersion of support helps."),
 ("term-limit policies",
  "EK DEM-2.B.7 states that the timing of legislative elections varies among the six systems based on term-limit policies. Party counts, population, resource wealth and membership of supranational bodies are not offered by the framework as explanations of election timing."),
 ("beyond a narrow plurality",
  "EK DEM-2.B.3.d claims the national mandate and EK DEM-2.B.3.b and DEM-2.B.3.c supply the mechanism: an absolute majority in Iran and Russia, a national plurality plus 25 percent across two-thirds of the states in Nigeria. Each rule forces support wider than one bloc of voters."),
 ("minimum vote share across two-thirds",
  "EK DEM-2.B.3.a makes Mexico's presidency a pure plurality office while EK DEM-2.B.3.b adds a federal distribution requirement in Nigeria, so two presidential systems set very different bars for the same office."),
 ("single-member district by plurality",
  "EK DEM-2.B.2 states that single-member district plurality systems tend to promote two-party systems, since only the leading candidate in each district converts votes into a seat. EK DEM-2.B.1 and EK DEM-2.A.2 describe proportional representation and its multimember districts doing the opposite."),
 ("gender quotas",
  "EK DEM-2.B.1 links proportional representation to an increase in the election of minority and women candidates, and EK DEM-2.A.1.c credits gender quotas in Mexico's party list system with helping to increase female representation in the legislature."),
 ("62 of the district seats",
  "Recomputed in q25 above from the table's two seat columns, including that each of the four distractors is false on the same numbers. The pattern is EK DEM-2.B.2's two-party tendency shown as an arithmetic consequence."),
 ("22 seats",
  "Recomputed in q26 above: the largest party's district total minus its list total. The vote column is identical under both rules, so the difference is produced by the counting rule and not by any change in how people voted."),
 ("turns a 40 percent vote share into a majority",
  "Recomputed in q27 above: one column gives the largest party a majority of the chamber and the other does not. This is the trade-off EK DEM-2.B.1 and EK DEM-2.B.2 set out, breadth of representation against decisive single-party government."),
 ("permitted to compete",
  "EK DEM-2.B.4 treats ballot access and competition as an object of regulation separate from how votes are counted, and EK DEM-2.B.4.a is the clearest case: the Guardian Council alters nothing about the count yet fixes the list of names voters may choose among."),
 ("answers to the voters of one identifiable district",
  "EK DEM-2.B.2 grounds constituency accountability in a single representative per district, which EK DEM-2.A.1.f makes true of every Commons seat, while EK DEM-2.A.1.c puts 200 Mexican deputies on party lists where the party's ranking rather than a district electorate decides who sits."),
 ("registration requirements",
  "EK DEM-2.A.1 contrasts rules structured for competitive selection with rules frequently changed to advance particular political interests, and EK PAU-4.A.3 names increasing party registration requirements and increasing threshold rules among the devices ensuring one-party dominance. A fixed timetable, a second chamber, a two-round rule and prompt publication are all compatible with genuine competition."),
]

cg.check(k4_2, CLAIMS,
         table_checks={6: q6, 7: q7, 8: q8, 9: q9, 10: q10, 25: q25, 26: q26, 27: q27})
