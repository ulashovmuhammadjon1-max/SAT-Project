"""Key audit for AP HUMAN GEOGRAPHY 4.5 The Function of Political Boundaries.

Units 4-7 verify against `geo_check`, whose entry point takes a flat ANCHORS
list plus TABLE_NOTES. The per-question CLAIMS list below is the audit trail the
brief asks for -- one (anchor, claim) pair per item, in module order -- and
ANCHORS is derived from it so the two cannot drift apart. The claims are checked
here for what geo_check does not know to look for: a claim must be a real
sentence of at least eight words and may not name an option by letter, since
export_units.py reshuffles the choices.

WHAT MAY BE CITED. IMP-4.B contributes four essential-knowledge statements to
this topic; its fifth, on voting districts, belongs to Topic 4.6:

    IMP-4.B.1  Boundaries are defined, delimited, demarcated, and administered
               to establish limits of sovereignty, but they are often contested.
    IMP-4.B.2  Political boundaries often coincide with cultural, national, or
               economic divisions. However, some boundaries are created by
               demilitarized zones or policy, such as the Berlin Conference.
    IMP-4.B.3  Land and maritime boundaries and international agreements can
               influence national or regional identity and encourage or
               discourage international or internal interactions and disputes
               over resources.
    IMP-4.B.4  The United Nations Convention on the Law of the Sea defines the
               rights and responsibilities of nations in the use of
               international waters, established territorial seas, and
               exclusive economic zones.

This is an unusually citable topic. IMP-4.B.1's four verbs are printed IN ORDER
and item 2 keys to that order; its final clause about contestation is a separate
citable fact and items 3 and 22 use it. IMP-4.B.2's "however" clause names
demilitarized zones and the Berlin Conference explicitly, so items 5, 6 and 18
cite them. IMP-4.B.3 names three effects -- identity, interaction in both
directions, resource disputes -- and items 9, 10, 11, 15, 19, 20, 21 and 23 are
distributed across all three. IMP-4.B.4 names the convention and its two zone
types.

WHAT THE CED DOES NOT DEFINE. It names the four boundary verbs without saying
what each means, and it names the two maritime zones without stating their
extents or the rights attaching to them. Those definitions are set out in the
module header and every key using them is argued from there:

    defined / delimited / demarcated / administered
        legal text, then map, then physical markers, then day-to-day management
    territorial sea (to 12 nautical miles)   SOVEREIGNTY
    exclusive economic zone (to 200)         RESOURCE RIGHTS, not sovereignty

The sovereignty-versus-rights distinction is the one students collapse, and
items 12, 16, 20 and 28 all turn on it. The nautical-mile figures are standard
uncontested course content and appear only where an item needs them to classify
a point.

BOUNDARY TYPE IS NOT THIS TOPIC. Topic 4.4 owns antecedent, subsequent,
superimposed, relict, geometric and consequent boundaries, and no item here asks
a student to name one. 4.4 asks where a boundary came from; 4.5 asks what it
does.

REVIEW NOTE. All 30 keys were derived from the questions before this file was
written and none needed correcting.
"""
import re

import geo_check
import g4_5


def q26_incomplete_stage(table):
    """Exactly one of the four stages is recorded as not completed."""
    stages = {row[0]: row[1] for row in table["rows"]}
    assert len(stages) == 4, stages
    incomplete = [s for s, y in stages.items() if not y[:1].isdigit()]
    assert incomplete == ["Demarcated with physical markers"], stages
    # The other three must carry real years, and administration must postdate
    # delimitation -- a boundary administered without ever being marked is the
    # point of the item.
    years = {s: int(y) for s, y in stages.items() if y[:1].isdigit()}
    assert len(years) == 3, years
    assert years["Administered with staffed crossings"] > years["Delimited on an agreed map"]
    assert years["Defined by treaty"] < years["Delimited on an agreed map"]
    return "Demarcation"


def q27_created_by_policy(table):
    """Segments coinciding with nothing on the ground, and how they arose."""
    words = {0: "No", 1: "One", 2: "Two", 3: "Three", 4: "Four"}
    rows = [(r[0], r[1], r[2]) for r in table["rows"]]
    assert len(rows) == 4, rows
    by_policy = [r for r in rows if r[1] == "Nothing on the ground"]
    assert len(by_policy) == 2, rows
    # Their origins must be the two the CED names -- policy and a military line
    # -- rather than local negotiation.
    origins = {r[2] for r in by_policy}
    assert origins == {"Agreed at an international conference",
                       "Fixed by an armistice line"}, origins
    # And the two that DO coincide with a division must have been negotiated
    # locally, or the contrast the item rests on is not present.
    others = [r for r in rows if r not in by_policy]
    assert all(r[2] == "Negotiated locally" for r in others), others
    return f"{words[len(by_policy)]} segments"


def q28_maritime_zone(table):
    """The one point beyond the territorial sea and inside the resource zone."""
    TERRITORIAL, EEZ = 12, 200
    zones = {}
    for row in table["rows"]:
        d = float(row[1])
        if d <= TERRITORIAL:
            zones[row[0]] = "territorial sea"
        elif d <= EEZ:
            zones[row[0]] = "exclusive economic zone"
        else:
            zones[row[0]] = "high seas"
    rights_only = [p for p, z in zones.items() if z == "exclusive economic zone"]
    assert rights_only == ["Point 3"], zones
    # Each of the other three zones must be occupied, so every distractor names
    # a real classification and only one of them answers the question asked.
    assert sum(1 for z in zones.values() if z == "territorial sea") == 2, zones
    assert sum(1 for z in zones.values() if z == "high seas") == 1, zones
    return "Point 3"


CLAIMS = [
 ("establish the limits of sovereignty",
  "EK IMP-4.B.1 states that boundaries are defined, delimited, demarcated and administered to establish limits of sovereignty. The four steps are procedural stages, and the purpose the sentence attaches to all of them is a statement about where one state's authority stops."),

 ("Defined, delimited, demarcated, and administered",
  "EK IMP-4.B.1 prints the four verbs in exactly this order, and the scenario matches them one by one: a legal text, an agreed map, physical pillars, then customs posts. The CED does not define the verbs, so the meanings used here are the standard ones set out in the module header."),

 ("often contested even after they have been formally established",
  "EK IMP-4.B.1 ends by noting that boundaries are often contested, and it places that clause AFTER the four establishment steps rather than before them. Completing the procedure produces a line that can be argued about precisely, not one everybody accepts."),

 ("coincide with cultural, national, or economic divisions",
  "EK IMP-4.B.2 states that political boundaries often coincide with cultural, national or economic divisions. A line matching a language divide is the cultural case, and the word coincide leaves open whether the line followed the division or the division followed the line."),

 ("created by demilitarized zones",
  "EK IMP-4.B.2 says that although boundaries often coincide with cultural, national or economic divisions, some are created by demilitarized zones or policy. The 'however' in that sentence introduces exactly this case, where the line records a military settlement rather than a social division."),

 ("created by policy rather than by an existing",
  "EK IMP-4.B.2 names the Berlin Conference alongside demilitarized zones as an example of boundaries created by policy. Lines agreed at a conference table by parties who did not live there are the paradigm of a boundary that matches nothing on the ground."),

 ("Staffed crossing points",
  "EK IMP-4.B.1 lists administration as the last of four stages, after a line has been defined, mapped and marked. Pillars, texts, maps and surveys establish where a boundary is; administration is the continuing work of making it operate."),

 ("physical marking of the line on the ground",
  "EK IMP-4.B.1 names demarcation as a step distinct from definition and delimitation. A line can be legally settled and accurately mapped while nobody has placed a marker on it, and unmarked boundaries are among the most often disputed on the ground."),

 ("influence national or regional identity",
  "EK IMP-4.B.3 states that land and maritime boundaries and international agreements can influence national or regional identity. A line separating people from a neighbour and joining them to a capital becomes part of how they describe themselves over time."),

 ("discourage international interactions",
  "EK IMP-4.B.3 says boundaries and agreements can encourage OR discourage international and internal interactions. Which direction they work in depends on how the boundary is administered, which is why one line can be a channel in one decade and a barrier in the next."),

 ("produce disputes over resources",
  "EK IMP-4.B.3 names disputes over resources among the things boundaries and agreements can produce. A deposit spanning a line makes the exact position of that line worth money, which converts a cartographic question into a political one."),

 ("without full sovereignty over the waters",
  "EK IMP-4.B.4 says the convention defines rights and responsibilities in international waters and established both territorial seas and exclusive economic zones. The distinction between them is sovereignty close to shore and resource rights further out, which is why foreign vessels may still navigate the wider zone."),

 ("defines the rights and responsibilities of nations",
  "EK IMP-4.B.4 states that the convention defines the rights and responsibilities of nations in the use of international waters and established territorial seas and exclusive economic zones. It is a framework of rules rather than an allocation of equal shares."),

 ("negotiated or adjudicated division",
  "EK IMP-4.B.4 makes the convention a framework of rights rather than a self-executing map, and EK IMP-4.B.1's contestation clause applies at sea as on land. Where full zones would overlap, the two states must agree a line or refer the question to a tribunal."),

 ("encourage international interactions as well as discourage",
  "EK IMP-4.B.3 states that boundaries and agreements can encourage or discourage interaction, naming both directions. The line still marks the limit of each state's sovereignty; what changed is how it is administered, which is the fourth of EK IMP-4.B.1's stages."),

 ("confers resource rights over a much wider area",
  "EK IMP-4.B.4 names both zones as things the convention established, and they differ in the kind of authority each carries. Sovereignty applies near the coast while the wider zone grants rights to fish, minerals and energy without closing the water to navigation."),

 ("physical marking on the ground is being made continuous",
  "EK IMP-4.B.1 names demarcation as the physical marking of a boundary on the ground, and a continuous fence is a more emphatic version of a line of pillars. The legal text and the map are unchanged, and a fence supplements rather than replaces administration."),

 ("no population on either side of it",
  "EK IMP-4.B.2 says boundaries often coincide with cultural, national or economic divisions but that some are created by policy instead. A line drawn by parties with no local knowledge or interest has no mechanism by which it could match a division on the ground."),

 ("encourage interactions that boundaries would otherwise discourage",
  "EK IMP-4.B.3 names international agreements alongside boundaries as things that can encourage or discourage interaction. Enclosure by other states' territory is a barrier only an agreement can overcome, which makes this the clearest case of the encouraging direction."),

 ("fish stocks, seabed minerals, and energy deposits",
  "EK IMP-4.B.4 establishes exclusive economic zones as a category of right rather than of sovereignty, and EK IMP-4.B.3 names disputes over resources as a consequence of maritime boundaries. What two states argue over in such a zone is who may take what from it."),

 ("regardless of how they originated",
  "EK IMP-4.B.3 says boundaries can influence national or regional identity and attaches no condition about their origin. A line that shaped who governs, who is schooled together and who trades with whom becomes the container within which an identity forms."),

 ("internal as well as international, are often contested",
  "EK IMP-4.B's learning objective covers international AND internal boundaries, and EK IMP-4.B.1's contestation clause is limited to neither. Provincial lines decide revenue, representation and jurisdiction, which is enough to make them worth arguing over."),

 ("goods are inspected and taxed",
  "EK IMP-4.B.3 names encouraging and discouraging INTERNAL as well as international interaction among the effects of boundaries. Inspection and taxation at an internal line raise the cost of moving goods within one state, which is the discouraging case."),

 ("produces effects on identity, interaction, and resources",
  "EK IMP-4.B.1 supplies the establishment process and EK IMP-4.B.3 the consequences, which together make a boundary an institution rather than a graphic. Delimitation is only the second of four stages, and every effect the CED names follows from the stages after it."),

 ("must operate at much greater volume",
  "EK IMP-4.B.1 makes administration the ongoing management of a boundary, and its burden scales with the traffic crossing it. A line through empty desert may be legally identical and practically trivial, which is why demarcation and administration are separate stages."),

 ("the only stage the record shows as incomplete",
  "Recomputed from the record: exactly one of EK IMP-4.B.1's four stages carries no year while the other three do, and the boundary is administered despite never having been physically marked. The verifier also confirms the three completed stages fall in the order the CED prints them.",
  ),

 ("Two segments",
  "Recomputed from the record: two of the four segments coincide with nothing on the ground, and their origins are a conference and an armistice line, which are the two kinds EK IMP-4.B.2 names. The verifier confirms the other two were negotiated locally, so the contrast the item rests on is really present.",
  ),

 ("Point 3, at 140 nautical miles",
  "Recomputed from the distances: only one point lies beyond the 12-nautical-mile territorial sea and inside the 200-mile exclusive economic zone, which EK IMP-4.B.4 establishes as separate categories. The verifier confirms the other three zones are each occupied, so every distractor names a real classification.",
  ),

 ("coincide with cultural divisions, and the claim that they are often contested",
  "EK IMP-4.B.2 makes coincidence with cultural divisions a common property of boundaries rather than a requirement, and EK IMP-4.B.1 records that boundaries are often contested. An argument that a line SHOULD match a distribution is a contest about the line conducted in the vocabulary of coincidence."),

 ("remain frequently contested",
  "EK IMP-4.B.1 supplies the process and the contestation, EK IMP-4.B.2 the coincidence with divisions, EK IMP-4.B.3 the effects on identity, interaction and resources, and EK IMP-4.B.4 the maritime allocation. A summary keeping all four is what the statements together assert."),
]

# --- checks geo_check does not perform, because it takes bare anchors ---------
assert len(CLAIMS) == 30, f"{len(CLAIMS)} claims, expected 30"
LETTER_REF = re.compile(
    r"(?<![A-Za-z])(?:[Cc]hoice|[Oo]ption|[Aa]nswer)\s+\(?([A-E])\)?(?![A-Za-z])")
for n, entry in enumerate(CLAIMS, 1):
    anchor, claim = entry[0], entry[1]
    assert len(claim.split()) >= 8, f"4.5 q{n}: claim too thin to audit: {claim!r}"
    m = LETTER_REF.search(claim)
    assert not m, (
        f"4.5 q{n}: claim names an option by letter ({m.group(0)!r}); "
        "export_units.py shuffles the choices -- name the option by its content")

ANCHORS = [entry[0] for entry in CLAIMS]

TABLE_NOTES = {
    26: q26_incomplete_stage,
    27: q27_created_by_policy,
    28: q28_maritime_zone,
}

geo_check.check(g4_5, ANCHORS, TABLE_NOTES)
