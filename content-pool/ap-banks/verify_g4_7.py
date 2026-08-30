"""Key audit for AP HUMAN GEOGRAPHY 4.7 Forms of Governance.

Units 4-7 verify against `geo_check`, which takes a flat ANCHORS list plus
TABLE_NOTES. The CLAIMS list below is the audit trail -- one (anchor, claim) pair
per item, in module order -- and ANCHORS is derived from it so the two cannot
drift apart. Claims are checked here for length and letter references, which
geo_check does not see.

WHAT MAY BE CITED. Two learning objectives contribute one statement each:

    IMP-4.C.1  Forms of governance include unitary states and federal states.
    IMP-4.D.1  Unitary states tend to have a more top-down, centralized form of
               governance, while federal states have more locally based,
               dispersed power centers.

IMP-4.C.1 supplies the categories (items 1, 18, 24, 25, 27) and IMP-4.D.1
supplies the contrast between them (items 2, 3, 6, 7, 8, 10, 12, 13, 14, 15, 16,
17, 20, 22, 23, 26, 28, 30).

TWO FEATURES OF IMP-4.D.1 THAT DECIDE HOW THIS MODULE IS BUILT.

First, the hedge. The CED writes that unitary states TEND TO have a more
centralized form, not that they always do. Items 5, 11, 19 and 29 all rest on
that word: a heavily devolved unitary state can be less centralized in practice
than a federal state with weak or penniless regions. Item 19 keys directly
against the overstatement, and item 29 supplies the usual mechanism by which
form and practice diverge, which is money.

Second, the phrase "dispersed power CENTERS". That is spatial vocabulary, and it
is what makes this a geography topic rather than a civics one. Items 6, 10, 17,
26 and 28 read the constitutional arrangement off the map -- how many cities
house a legislature, where government employment sits, how many bodies of law a
citizen can be under.

WHAT THE CED DOES NOT DEFINE. Neither term. So the operative test used
throughout is stated in the module header and repeated in the claims: not how
much power regions currently exercise, but WHERE IT COMES FROM and who can take
it back. Delegation by statute is unitary however generous; constitutional
division is federal however modest. Items 4, 7, 8, 9, 11, 20, 22, 27 and 29 all
turn on that test, and item 4 asks for it directly.

NO REAL COUNTRY IS NAMED ANYWHERE IN THIS MODULE. That is deliberate.
Constitutional arrangements change, several real states are genuinely hard to
classify, and the CED names none in this topic. Describing an arrangement and
asking which category it fits tests the same understanding without asserting a
fact about a real state that could be stale or contested -- which is the
discipline SOCIAL_BRIEF.md asks for.

The three table items (26, 27, 28) are the computational gate:

  26  nine legislatures in nine cities against one, plus the abolition row that
      settles delegation versus division
  27  exactly two of four states record a constitutional division the centre
      cannot revoke
  28  total government employment is unchanged while its distribution moves --
      the recompute asserts the total is constant, since a fall in the capital
      would otherwise be readable as a cut rather than a shift

REVIEW NOTE. All 30 keys were derived from the questions before this file was
written and none needed correcting.
"""
import re

import geo_check
import g4_7


def q26_dispersed_centres(table):
    """Nine law-making legislatures in nine cities, and unabolishable regions."""
    rows = {r[0]: (r[1], r[2]) for r in table["rows"]}
    leg1, leg2 = rows["Legislatures with power to make binding law"]
    city1, city2 = rows["Cities housing a legislature"]
    law1, law2 = rows["Bodies of law a citizen may be subject to"]
    ab1, ab2 = rows["Regional bodies the centre may abolish by ordinary law"]
    assert int(leg2) == 9 and int(leg1) == 1, (leg1, leg2)
    assert int(city2) == int(leg2), (city2, leg2)
    assert int(law2) > int(law1), (law1, law2)
    # The decisive row: one state's regional bodies are revocable, the other's
    # are not. Without it, nine legislatures could still be a unitary state's
    # branch offices.
    assert ab1 == "All of them" and ab2 == "None of them", (ab1, ab2)
    return "nine law-making legislatures in nine cities"


def q27_count_federal(table):
    """Federal states are the ones whose regional powers cannot be revoked."""
    words = {0: "No", 1: "One", 2: "Two", 3: "Three", 4: "Four"}
    federal, unitary = [], []
    for row in table["rows"]:
        state, source, revocable = row
        if source == "Constitutional division" and revocable == "No":
            federal.append(state)
        else:
            unitary.append(state)
            assert source == "Delegation by statute" and revocable == "Yes", row
    assert len(federal) == 2 and len(unitary) == 2, (federal, unitary)
    return f"{words[len(federal)]}, since two derive regional powers"


def q28_employment_shift(table):
    """Employment moves from the capital to regional capitals; the total is flat."""
    before = after = 0.0
    rows = {}
    for row in table["rows"]:
        b = float(row[1].replace(",", ""))
        a = float(row[2].replace(",", ""))
        rows[row[0]] = (b, a)
        before += b
        after += a
    # The total must NOT change, or the fall in the capital could be a cut.
    assert before == after == 500, (before, after)
    cap_b, cap_a = rows["National capital"]
    reg_b, reg_a = rows["Regional capitals combined"]
    assert cap_a < cap_b and reg_a > reg_b, rows
    assert reg_a / reg_b > 4, (reg_b, reg_a)
    fall = 100 * (cap_b - cap_a) / cap_b
    assert 41 < fall < 43, fall
    # The capital must still hold the most, so that distractor's premise is true.
    assert cap_a > reg_a and cap_a > rows["All other locations"][1], rows
    return "regional capitals more than quadrupled"


CLAIMS = [
 ("Unitary states and federal states",
  "EK IMP-4.C.1 states that forms of governance include unitary states and federal states. The other pairs offered are real distinctions used elsewhere in this course, but none of them is the one this statement draws."),

 ("more top-down, centralized form of governance",
  "EK IMP-4.D.1 uses exactly these words for unitary states, contrasting them with federal states that have more locally based, dispersed power centres. The word 'tend' signals a comparison of degree rather than an absolute rule."),

 ("more locally based, dispersed power centres",
  "EK IMP-4.D.1 describes federal states this way in contrast with the top-down organization it attributes to unitary states. Dispersal of the places where decisions are made is the spatial content of the term and the reason this is a geography topic."),

 ("powers the centre cannot simply withdraw",
  "EK IMP-4.C.1 names the two forms and EK IMP-4.D.1 describes their tendencies without defining either, so the test rests on where authority originates and who can take it back. A unitary state can delegate extensively and remain unitary."),

 ("differ by degree along a spectrum",
  "EK IMP-4.D.1's hedge is deliberate: unitary states TEND TO be more centralized. A unitary state that has devolved substantially may be less centralized in practice than a federal state whose regional governments are weak, so the comparison holds on average."),

 ("made in several places are now made in one",
  "EK IMP-4.D.1 contrasts dispersed power centres with top-down centralized governance, which is a claim about where decisions physically happen. Replacing legislatures with branch offices removes the alternative locations at which a decision could be taken."),

 ("delegation by the central government",
  "EK IMP-4.D.1 describes unitary governance as top-down, and the direction is the point: authority flows outward from the centre rather than upward from the regions. That is what makes local powers revocable in a unitary arrangement."),

 ("constitutional division of authority",
  "EK IMP-4.D.1 attributes locally based, dispersed power centres to federal states, and what makes them centres rather than offices is that their authority is entrenched. A power the centre may take back by ordinary legislation is delegation rather than division."),

 ("whether the centre can withdraw the powers",
  "EK IMP-4.C.1 names the two forms, and the standard test between them is the source and security of regional authority rather than its current extent. Identical functions can rest on entrenched division in one state and on revocable delegation in the other."),

 ("Multiple capitals, legislatures, and bodies of law",
  "EK IMP-4.D.1's phrase about locally based, dispersed power centres is a description of geography rather than of constitutional theory. Each regional government occupies a place, employs people there and makes law applying over a defined area."),

 ("the centre retains the authority to alter or reclaim them",
  "EK IMP-4.D.1's contrast turns on the location and security of authority, and devolution moves the exercise of power without moving its source. This is exactly why the CED hedges with 'tend to', since a heavily devolved unitary state can look federal from outside."),

 ("legislate for their own circumstances",
  "EK IMP-4.D.1 attributes dispersed power centres to federal states, and dispersal is a response to variety. Where the right answer differs from region to region, one central rule must be either wrong somewhere or too vague to decide anything."),

 ("simpler to administer and can deliver equal standards",
  "EK IMP-4.D.1 describes unitary governance as top-down and centralized, and uniformity is the advantage that follows. Where a service ought to be identical everywhere, dispersed decision making produces variation that is hard to justify."),

 ("usually through a court rather than by one side simply overruling",
  "EK IMP-4.D.1 attributes dispersed power centres to federal states, which means neither level can settle a boundary dispute by fiat. A written division of powers implies an interpreter of it, which is why federal systems characteristically have constitutional courts."),

 ("differ between regions, which complicates movement and business",
  "EK IMP-4.D.1's dispersed power centres are the source of both the advantages and the costs of federalism. If regions legislate separately, a firm or a family crossing a regional line meets a different rulebook, which is the price of local responsiveness."),

 ("poorly informed about distant regions",
  "EK IMP-4.D.1 describes unitary governance as top-down, and the flow of information runs against that direction. Distance from the capital tends to correlate with how little the capital knows about a place, which is the standing weakness of centralization at scale."),

 ("spread it among regional capitals as well",
  "EK IMP-4.D.1's dispersed power centres are places where people work as well as where decisions are made. A regional legislature needs a building, a bureaucracy and a professional class around it, so the constitutional arrangement marks the economic map."),

 ("divides authority between two levels rather than delegating",
  "EK IMP-4.C.1 names federal states as a form of governance, and a constitutional list assigning subjects to each level is the characteristic instrument of one. What matters is that the provincial powers come from the constitution rather than from the centre's permission."),

 ("a heavily devolved unitary state can be less centralized in practice",
  "EK IMP-4.D.1's hedge is doing real work, since practice and constitutional form can diverge in either direction. The categories describe where authority formally sits, while centralization in practice depends on what each level actually does."),

 ("funding conditional on regions adopting the standard",
  "EK IMP-4.D.1's dispersed power centres are secure against the centre in their own fields, which forecloses direct legislation there. Conditional funding works because the centre's spending power is not confined to the subjects it may legislate on."),

 ("size alone neither requires nor prevents either form",
  "EK IMP-4.C.1 names the two forms without attaching either to a size, so any connection has to be stated as a tendency. Very large unitary states and very small federal ones both exist, which is why the correlation cannot be given as a rule."),

 ("redraw, merge, or abolish regional governments by ordinary legislation",
  "EK IMP-4.D.1's top-down organization means regional bodies exist at the centre's discretion. The power to abolish is the sharpest form of that relationship, and none of the other features listed distinguishes the two forms at all."),

 ("already has a channel for regional demands",
  "EK IMP-4.D.1's dispersed power centres are institutions through which regional interests are already expressed. Where no such channel exists, a demand for regional authority is necessarily a demand to change the structure of the state itself."),

 ("entrenched in the constitution, matched to a federal state",
  "EK IMP-4.C.1 names the two forms and EK IMP-4.D.1 attributes locally based, dispersed power centres to the federal one. Only entrenched regional authority produces a power centre rather than an administrative outpost, and every other pairing describes a unitary arrangement."),

 ("Both are ways of organizing one sovereign state",
  "EK IMP-4.C.1 presents both as forms of governance of a state rather than as different kinds of entity, and EK IMP-4.D.1 locates the difference in where power sits. Sovereignty, regime type and the number of provinces are all independent of the distinction."),

 ("nine law-making legislatures in nine cities",
  "Recomputed from the record: one state records nine law-making bodies in nine cities against the other's single legislature, and its regional bodies cannot be abolished by ordinary law. The verifier treats that last row as decisive, since nine legislatures could otherwise be a unitary state's branch offices.",
  ),

 ("since two derive regional powers",
  "Recomputed from the record: exactly two of the four states derive regional powers from a constitutional division the centre cannot revoke, and the other two record revocable statutory delegation. EK IMP-4.C.1 names federal states as a form of governance and the source of regional authority is the test.",
  ),

 ("regional capitals more than quadrupled",
  "Recomputed from the figures: total government employment is unchanged at 500,000 while the national capital falls 42 percent and regional capitals rise more than fourfold. The verifier asserts the total is constant, since otherwise the capital's fall could be read as a cut rather than a shift.",
  ),

 ("raise almost no revenue of their own",
  "EK IMP-4.D.1's hedge allows practice and form to diverge, and money is the usual mechanism. A region with entrenched powers but no independent revenue must spend on the centre's terms, which converts constitutional authority into practical dependence."),

 ("act through a single chain of authority",
  "EK IMP-4.D.1's contrast between top-down governance and dispersed power centres is exactly a contrast in how a decision travels. Speed and uniformity favour the centralized arrangement, which is the counterpart of the responsiveness that favours the dispersed one."),
]

# --- checks geo_check does not perform, because it takes bare anchors ---------
assert len(CLAIMS) == 30, f"{len(CLAIMS)} claims, expected 30"
LETTER_REF = re.compile(
    r"(?<![A-Za-z])(?:[Cc]hoice|[Oo]ption|[Aa]nswer)\s+\(?([A-E])\)?(?![A-Za-z])")
for n, entry in enumerate(CLAIMS, 1):
    anchor, claim = entry[0], entry[1]
    assert len(claim.split()) >= 8, f"4.7 q{n}: claim too thin to audit: {claim!r}"
    m = LETTER_REF.search(claim)
    assert not m, (
        f"4.7 q{n}: claim names an option by letter ({m.group(0)!r}); "
        "export_units.py shuffles the choices -- name the option by its content")

ANCHORS = [entry[0] for entry in CLAIMS]

TABLE_NOTES = {
    26: q26_dispersed_centres,
    27: q27_count_federal,
    28: q28_employment_shift,
}

geo_check.check(g4_7, ANCHORS, TABLE_NOTES)
