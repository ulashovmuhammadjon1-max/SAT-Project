"""Key audit for AP HUMAN GEOGRAPHY 4.8 Defining Devolutionary Factors.

Units 4-7 verify against `geo_check`, which takes a flat ANCHORS list plus
TABLE_NOTES. The CLAIMS list below is the audit trail -- one (anchor, claim) pair
per item, in module order -- and ANCHORS is derived from it so the two cannot
drift apart. Claims are checked here for length and for letter references, which
geo_check does not see.

WHAT MAY BE CITED. This topic has one learning objective and one essential
knowledge statement, and that statement is a closed list of six:

    SPS-4.A   Define factors that lead to the devolution of states.
    SPS-4.A.1 Factors that can lead to the devolution of states include the
              division of groups by physical geography, ethnic separatism,
              ethnic cleansing, terrorism, economic and social problems, and
              irredentism.

Everything keyed in this module traces to that sentence. Nothing else in the
CED belongs here: the definition of devolution itself is SPS-4.B.1, which is
Topic 4.9's statement, so this module asks only what CAUSES devolution and never
what devolution is. Items 14, 22 and 24 come closest to that line and each is
keyed to a property of SPS-4.A.1's own wording rather than to an outcome.

TWO FEATURES OF SPS-4.A.1 THAT DECIDE HOW THIS MODULE IS BUILT.

First, "CAN LEAD TO". The statement is probabilistic, not causal, and it makes
no factor sufficient. Items 16, 22 and 30 rest on that: many states contain
several of the six and do not devolve, so the honest reading is that these are
conditions that raise the likelihood. A module keyed as though any one factor
produced devolution would be overstating the sentence.

Second, the list is CLOSED and it is a list of six. Item 1 tests the boundary of
it, and the distractor there -- supranational trade agreements -- is a real CED
term drawn from SPS-4.B.3, which is exactly the neighbouring statement a student
is likely to blend in. Items 12, 21, 23 and 30 all depend on the membership of
the list being fixed.

THE DIRECTION OF IRREDENTISM is the reversal this topic exists to catch, and it
is the single most common error on it. Separatism is INTERNAL -- a group inside
a state wants out. Irredentism is EXTERNAL -- a state or group across a border
claims territory inhabited by people it regards as its own. Items 4, 5, 8, 12,
20, 21 and 27 turn on that direction, and items 5 and 27 ask for it directly.
Both can act on one border at once, which is item 8.

WHAT THE CED DOES NOT DEFINE. None of the six. The definitions this module uses
are written out in the module header and are the ordinary ones; where a
definition does any work in a key, the claim below states it. Ethnic cleansing is
named accurately -- the forced removal of a population from a territory -- and no
item asks a student to evaluate it or describes an atrocity.

NO REAL COUNTRY IS NAMED ANYWHERE IN THIS MODULE. SPS-4.A.1 names none, several
real cases are politically live, and describing a situation and asking which
factor it illustrates tests the same understanding without asserting a contested
claim about a real place.

The three table items (26, 27, 28) are the computational gate:

  26  the count of factors per region, plus the assertion that exactly one
      region's unemployment ratio is materially above the national rate
  27  who advances each claim -- the one variable that separates separatism
      from irredentism, recomputed from the record rather than read off
  28  both share columns sum to 100, so the item can only be a claim about
      composition; the recompute pins the 54-to-96 rise and the collapse of the
      other two groups to four percent between them

REVIEW NOTE. All 30 keys were derived from the questions before this file was
written and none needed correcting. Question 29 was written in this session --
the module was committed with 29 items and the exporter requires 30 -- and is a
scale-of-analysis item, the axis SOCIAL_BRIEF.md asks for and the one thing
SPS-4.A.1's regional factors most obviously support.
"""
import re

import geo_check
import g4_8


def q26_count_factors(table):
    """Count the framework's conditions recorded for each region."""
    counts = {}
    unemployment = {}
    for row in table["rows"]:
        region, terrain, ethnic, unemp, claim = row
        ratio = float(unemp.split()[0])
        unemployment[region] = ratio
        n = 0
        n += terrain == "Yes"
        n += ethnic == "Yes"
        n += ratio > 1.5          # materially above the national rate
        n += claim == "Yes"
        counts[region] = n
    best = max(counts, key=counts.get)
    assert best == "Region 1", counts
    assert counts["Region 1"] == 4, counts
    others = [v for k, v in counts.items() if k != best]
    # No other region records more than one, so the key is not merely the
    # largest of several close cases.
    assert max(others) <= 1, counts
    # Exactly one region is materially above the national unemployment rate,
    # and it is above THREE times it, which is what the keyed choice asserts.
    high = [k for k, v in unemployment.items() if v > 1.5]
    assert high == ["Region 1"], unemployment
    assert unemployment["Region 1"] > 3, unemployment
    return "more than three times the national rate"


def q27_who_advances(table):
    """The classifying variable is who advances the claim, not what is claimed."""
    rows = {r[0]: (r[1], r[2]) for r in table["rows"]}
    by1, aim1 = rows["Claim 1"]
    by2, aim2 = rows["Claim 2"]
    # Claim 1 comes from inside the state whose territory is at stake.
    assert "inside State A" in by1, by1
    assert "Independence" in aim1, aim1
    # Claim 2 comes from a government across the border.
    assert "neighbouring State B" in by2, by2
    assert "Transfer" in aim2 and "State B" in aim2, aim2
    # Both claims concern the same province, so the aim cannot separate them --
    # only the origin can, which is the whole point of the item.
    assert "province" in aim1 and "province" in aim2, (aim1, aim2)
    return "ethnic separatism and the second is irredentism"


def q28_composition_shift(table):
    """Shares sum to 100 both times, so only composition can be read."""
    before = after = 0.0
    rows = {}
    for row in table["rows"]:
        b, a = float(row[1]), float(row[2])
        rows[row[0]] = (b, a)
        before += b
        after += a
    assert before == after == 100, (before, after)
    b1, a1 = rows["Group 1"]
    assert b1 == 54 and a1 == 96, rows
    # The other two groups together fall to four percent, so this is a change in
    # who lives there rather than ordinary demographic drift.
    rest_before = sum(v[0] for k, v in rows.items() if k != "Group 1")
    rest_after = sum(v[1] for k, v in rows.items() if k != "Group 1")
    assert rest_before == 46 and rest_after == 4, (rest_before, rest_after)
    assert all(v[1] < v[0] for k, v in rows.items() if k != "Group 1"), rows
    return "96 percent of a region it had held 54 percent of"


CLAIMS = [
 ("Supranational trade agreements",
  "EK SPS-4.A.1 lists exactly six factors -- division of groups by physical geography, ethnic separatism, ethnic cleansing, terrorism, economic and social problems, and irredentism -- and trade agreements are not among them. They belong to EK SPS-4.B.3 on supranationalism, which is the adjacent statement a student is most likely to blend into this one."),

 ("division of groups by physical geography",
  "EK SPS-4.A.1 names the division of groups by physical geography first among its factors. A barrier that makes routine contact with the state's own core harder than contact across a border weakens the everyday connection on which cohesion rests, and the stem supplies both halves of that."),

 ("a group within the state is seeking autonomy",
  "EK SPS-4.A.1 names ethnic separatism as a factor, and what identifies it in a case is the direction of the demand. The movement described originates inside the state and seeks to loosen or sever its own tie to it, which is separatism and not the outward claim irredentism describes."),

 ("a claim is made from outside",
  "EK SPS-4.A.1 names irredentism as a factor, and it is the only outward-facing member of the list. The claim in the stem is advanced by a neighbouring state for territory inhabited by people it regards as its own, which is the definition, and no movement inside the claimed state is described at all."),

 ("originates inside the state whose territory is at stake",
  "EK SPS-4.A.1 lists ethnic separatism and irredentism as separate factors, and the difference between them is direction rather than method, scale or terrain. Either can be violent or peaceful and either can involve a large or a small group, so none of those tests would separate them."),

 ("concentrated in one region",
  "EK SPS-4.A.1 names economic and social problems among the devolutionary factors. What makes them devolutionary rather than merely difficult is their concentration in one place, which converts a national problem into a regional grievance directed at the centre."),

 ("which the framework lists as a factor",
  "EK SPS-4.A.1 names terrorism among the factors that can lead to devolution. Violence against civilians for a political aim is listed separately from the separatism it may serve, so the CED treats the means as a factor in its own right and not merely as a symptom."),

 ("from inside and irredentism from outside",
  "EK SPS-4.A.1 lists separatism and irredentism as distinct factors and nothing in the statement prevents both from acting on one territory. The stem describes a minority inside State A seeking to join State B while State B claims the same province, which is one instance of each."),

 ("the forced removal of a group from a territory",
  "EK SPS-4.A.1 names ethnic cleansing among the factors, and the defining act is the forced removal of a population rather than any change in its beliefs or allegiance. The stem specifies removal carried out so that one ethnic group alone will inhabit the territory."),

 ("Forcibly changing who lives in a territory",
  "EK SPS-4.A.1 places ethnic cleansing among the factors that CAN LEAD TO devolution rather than only among its results. Altering who lives in a place manufactures the homogeneity a territorial claim rests on and makes any later accommodation with the displaced population far harder."),

 ("makes routine contact with the centre difficult",
  "EK SPS-4.A.1 names the division of groups by physical geography, and distance across water is one of its plainest forms. Nine hundred kilometres and a weekly ferry reduce the trade, schooling, administration and family contact through which a state is experienced as a single place."),

 ("Irredentism",
  "EK SPS-4.A.1 lists six factors, five of which describe conditions or movements within the state whose territory is at issue. Irredentism alone is advanced from across the border, by a state or group acting on behalf of people it regards as its own."),

 ("distinct ethnic identity and economic conditions far worse",
  "EK SPS-4.A.1 lists physical division, ethnic distinctiveness and economic and social problems as separate factors, and nothing prevents them from coinciding in one region. Where they do, each reinforces the others: distance limits contact, identity supplies a claim, and grievance supplies a motive."),

 ("satisfy the demand short of separation",
  "Learning objective SPS-4.A concerns the factors leading to devolution, and a state facing them may concede part of what is demanded. Granting a region real authority converts a demand to leave into a question of how much authority it should hold, which is negotiable in a way that independence is not."),

 ("because it is governed from elsewhere",
  "EK SPS-4.A.1 names economic and social problems among the factors, but hardship by itself occurs in every state and is not devolutionary. What makes it devolutionary is the causal account attached to it, in which distant government is the cause and regional control is the remedy."),

 ("frequently occur together and reinforce one another",
  "EK SPS-4.A.1 presents six factors in a single list without ordering them, ranking them or making any of them sufficient. Physical separation, distinct identity, economic grievance and violence commonly appear in the same case, and their coincidence is what makes devolution likely."),

 ("is now present alongside the ethnic separatism",
  "EK SPS-4.A.1 lists separatism and terrorism as separate factors, so a change of method adds a factor rather than substituting one for another. The aim in the stem is unchanged; only the means have changed, and the CED counts the means separately."),

 ("how easily a centre can administer",
  "EK SPS-4.A.1 names the division of groups by physical geography among political factors, and the mechanism runs through administration rather than terrain producing attitudes directly. A region the state cannot easily reach, supply or communicate with is one the state governs weakly."),

 ("leave large minorities on the wrong side",
  "EK SPS-4.A.1 names ethnic separatism, and the geography of a group determines whether a boundary can be drawn around it at all. Intermingled settlement means any line leaves substantial minorities on both sides, which is why such cases are the hardest to settle by partition."),

 ("a loss of territory driven by a claim from outside",
  "EK SPS-4.A.1 names irredentism among the factors that can lead to devolution, and the devolutionary effect falls on the state whose territory is claimed rather than on the claimant. The claiming state grows while the state losing the province fragments."),

 ("impassable desert",
  "EK SPS-4.A.1 names six factors and only one pairing in this item matches a case to the factor whose definition it satisfies. A province cut off by a desert is division by physical geography; each of the other pairings swaps two of the CED's own categories."),

 ("without devolving",
  "EK SPS-4.A.1's wording is that these are factors that CAN LEAD TO devolution, which stops short of asserting that they do. Reading the six as conditions that raise the likelihood rather than as causes that produce the outcome is exactly what that phrasing licenses."),

 ("the division of groups by physical geography",
  "EK SPS-4.A.1's six factors are not all ethnic: terrain and material conditions require no cultural difference at all. A remote and poor region of an ethnically uniform state can therefore develop a devolutionary movement on regional grounds alone."),

 ("concessions that would once have satisfied it",
  "EK SPS-4.A.1 lists terrorism alongside separatism, which implies a process able to escalate from one to the other. A demand met while it is still a demand for a voice is settled on different terms from the same demand met after it has become a demand for a separate state."),

 ("better governed and better off on its own",
  "EK SPS-4.A.1 names economic and social problems as a factor in their own right rather than as a consequence of cultural difference. Both poor regions blaming neglect and wealthy regions resenting transfers have produced devolutionary movements on purely material grounds."),

 ("more than three times the national rate",
  "Recomputed from the record: one region records four of the framework's conditions -- terrain separation, a distinct ethnic majority, unemployment at 3.1 times the national rate and an external claim -- while no other region records more than one. The verifier also checks that exactly one region is materially above the national unemployment rate, so the ratio in the keyed choice is not a coincidence of rounding.",
  ),

 ("ethnic separatism and the second is irredentism",
  "Recomputed from the record: the first claim is advanced by a minority living inside the state whose province is at stake and the second by the government of the neighbouring state. Both aim at the same province, so the aim cannot classify them and only the origin can, which is the distinction EK SPS-4.A.1 draws between its two directional factors.",
  ),

 ("96 percent of a region it had held 54 percent",
  "Recomputed from the figures: both share columns sum to 100, so the record can only be a claim about composition, and the largest group rises from 54 to 96 percent while the other two fall from 46 percent between them to 4. EK SPS-4.A.1 names ethnic cleansing as a factor and the stem specifies forced displacement, which is the mechanism the shares record.",
  ),

 ("national averages can conceal",
  "EK SPS-4.A.1's factors are regional in form -- one region cut off by terrain, one group's separatism, one area's unemployment -- so every one of them is invisible in a national aggregate. A state whose national unemployment rate is unremarkable may still contain a region at three times that rate, which is the condition the statement names."),

 ("raise the likelihood that a state will fragment",
  "EK SPS-4.A.1 lists exactly six factors and says they CAN LEAD TO the devolution of states. Both halves of that matter: the list is closed, so a summary naming only economic or only ethnic causes is short, and the claim is probabilistic, so a summary promising fragmentation overstates it."),
]

# --- checks geo_check does not perform, because it takes bare anchors ---------
assert len(CLAIMS) == 30, f"{len(CLAIMS)} claims, expected 30"
LETTER_REF = re.compile(
    r"(?<![A-Za-z])(?:[Cc]hoice|[Oo]ption|[Aa]nswer)\s+\(?([A-E])\)?(?![A-Za-z])")
for n, entry in enumerate(CLAIMS, 1):
    anchor, claim = entry[0], entry[1]
    assert len(claim.split()) >= 8, f"4.8 q{n}: claim too thin to audit: {claim!r}"
    m = LETTER_REF.search(claim)
    assert not m, (
        f"4.8 q{n}: claim names an option by letter ({m.group(0)!r}); "
        "export_units.py shuffles the choices -- name the option by its content")

ANCHORS = [entry[0] for entry in CLAIMS]

TABLE_NOTES = {
    26: q26_count_factors,
    27: q27_who_advances,
    28: q28_composition_shift,
}

geo_check.check(g4_8, ANCHORS, TABLE_NOTES)
