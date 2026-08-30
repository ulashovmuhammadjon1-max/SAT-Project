"""Key audit for AP HUMAN GEOGRAPHY 4.4 Defining Political Boundaries.

Units 4-7 verify against `geo_check`, whose entry point takes a flat ANCHORS
list plus TABLE_NOTES. The per-question CLAIMS list below is the audit trail the
brief asks for -- one (anchor, claim) pair per item, in module order -- and
ANCHORS is derived from it, so the two can never drift apart. The claims are
checked here for the properties geo_check does not know to look for: a claim
must be a real sentence of at least eight words, and it may not name an option
by letter, because export_units.py reshuffles the choices on the way out.

WHAT THIS TOPIC MAY REST ON. Learning objective IMP-4.A prints exactly one
essential-knowledge statement:

    IMP-4.A.1  Types of political boundaries include relict, superimposed,
               subsequent, antecedent, geometric, and consequent boundaries.

That list is the entire content of the topic, and it is a list of names with no
definitions attached, so almost every claim below is a claim about what the term
actually picks out rather than a quotation of a framework sentence. The two axes
the module is built on are stated in the module header and repeated here because
they decide every key:

  * WHEN, relative to settlement: antecedent (before), subsequent (after),
    consequent (the subsequent case drawn deliberately to match a cultural
    division), superimposed (drawn by an outside power in disregard of one),
    relict (no longer functioning but still legible on the landscape).
  * SHAPE: geometric, which describes the form of the line and says nothing
    about its history -- which is why a boundary can be geometric and
    superimposed at once, the point items 9, 18 and 27 turn on.

Item 12 keys the Berlin Conference and the 1947 partition of India to
SUPERIMPOSED boundaries. That is the CED's own sample question 2 key, not a
reading of my own, and it is followed here for that reason.

Item 21 uses the defined / delimited / demarcated sequence, which is not in
IMP-4.A.1. It is standard course vocabulary for how a boundary is established
and the key rests on the ordinary meanings of the three verbs, so no EK is
cited for it -- an invented citation would be worse than none.

The three data items (15, 24, 29) are the computational gate. Item 24 is the
only one making an arithmetic claim in the strict sense, but 15 and 29 both
require a row-by-row reading that a typo in a cell would break, so all three get
a real recompute function rather than a "no arithmetic claim" note.

REVIEW NOTE. All 30 keys were re-derived from the questions before these anchors
were written, and none was changed.
"""
import re

import geo_check
import g4_4


def q15_relict_row(table):
    """Exactly one boundary is recorded as no longer administered."""
    heads = table["headers"]
    idx = heads.index("Still administered today")
    defunct = [row[0] for row in table["rows"] if row[idx] == "No"]
    assert defunct == ["Boundary 3"], f"rows no longer administered: {defunct}"
    # The two distractor readings must each pick a different row, or the item
    # would have more than one defensible answer.
    before = heads.index("Drawn before local settlement")
    outside = heads.index("Drawn by an outside power")
    antecedent = [row[0] for row in table["rows"] if row[before] == "Yes"]
    superimposed = [row[0] for row in table["rows"] if row[outside] == "Yes"]
    assert antecedent == ["Boundary 1"], antecedent
    assert superimposed == ["Boundary 2"], superimposed
    return "Boundary 3"


def q24_straight_share(table):
    """Share of boundary LENGTH on a straight survey line: 720 of 1,000 km."""
    heads = table["headers"]
    km = heads.index("Length (km)")
    straight = heads.index("Follows a straight survey line")
    total = sum(int(row[km]) for row in table["rows"])
    on_line = sum(int(row[km]) for row in table["rows"] if row[straight] == "Yes")
    pct = 100 * on_line / total
    assert pct == int(pct), f"share {pct} is not a whole percentage"
    # The stem specifies length precisely because counting segments differs.
    by_count = 100 * sum(1 for row in table["rows"] if row[straight] == "Yes") \
        / len(table["rows"])
    assert by_count != pct, "counting segments gives the same answer as length"
    return f"{int(pct)} percent"


def q29_antecedent_count(table):
    """Rows whose line was fixed before the first permanent settlement."""
    heads = table["headers"]
    fixed = heads.index("Year line fixed")
    settled = heads.index("Year first permanent settlement")
    words = {0: "None", 1: "One", 2: "Two", 3: "Three", 4: "Four"}
    n = sum(1 for row in table["rows"] if int(row[fixed]) < int(row[settled]))
    assert 0 < n < len(table["rows"]), "the count must not be all or nothing"
    return words[n]


CLAIMS = [
 ("antecedent",
  "An antecedent boundary is drawn before the cultural landscape develops around it, which is the sequence the stem states: the survey line first, farms and towns afterward. Every other type on IMP-4.A.1's list needs an already settled landscape for the line to respond to, ignore, or outlive."),

 ("subsequent",
  "A subsequent boundary forms after settlement and shifts as the cultural landscape changes, which is what centuries of negotiated adjustment between growing villages describe. An antecedent line would have been fixed before those villages existed and would not have moved with them."),

 ("superimposed",
  "A superimposed boundary is imposed by an external power over an existing cultural landscape it disregards, and splitting resident peoples between two new states is the diagnostic consequence. A consequent line would have been placed to follow those cultural divisions rather than to cut across them."),

 ("consequent boundary",
  "A consequent boundary is drawn to accommodate an existing cultural division rather than in spite of one, so a line laid along a language divide is the standard case. It presupposes that the culture existed first, which is what separates it from an antecedent line."),

 ("relict boundary",
  "A relict boundary no longer functions politically but remains legible on the landscape, and ruined watchtowers with a disused customs house are exactly that legibility. The surviving traces, not the lapsed legal line, are what make the category apply."),

 ("geometric",
  "Geometric describes the form of a line -- a straight segment following a meridian, a parallel, or an arc -- and asserts nothing about when or by whom it was drawn. The stem restricts itself to shape for that reason, since the same line will also belong to a history-based category."),

 ("Antecedent and subsequent",
  "Antecedent means the line preceded the cultural landscape and subsequent means it followed, so the pair differs purely in timing relative to settlement. Geometric is a statement about shape, relict about whether the line still functions, and superimposed about who imposed it on whom."),

 ("physical, because it follows a landform",
  "Classification tracks the human sequence rather than the age of the landform: settlement arrived after the line was agreed, which makes it antecedent, and the line's course follows a ridge crest, which makes it physical. Calling a mountain range ancient confuses geology with a boundary's political history."),

 ("geometric in shape and superimposed in origin",
  "Shape and history are independent axes, so both labels apply at once: the perfectly straight line is geometric, and a colonial administration drawing it across an inhabited region it never surveyed is superimposed. Insisting on one label per boundary is the error the item is built to expose."),

 ("Fortifications, border markers",
  "A relict boundary must be both defunct and legible, so surviving fortifications, markers or a cleared strip where no jurisdiction now changes is the evidence that separates it from a line merely forgotten. Difficult terrain, cartographic omission, internal position and straightness say nothing about surviving physical traces."),

 ("outside power's disregard",
  "A boundary is classified by its origin, and independence changes who administers a line rather than who drew it or why. The relict reading fails because the segments are still functioning international borders, which is precisely what a relict boundary is not."),

 ("superimposed boundaries",
  "In both cases an outside authority drew lines across long-settled regions without regard for the peoples they divided, which is the definition of a superimposed boundary; the CED's own sample question keys these two examples that way. The divided nations left on either side follow directly from that disregard."),

 ("each governs the area where its own religion predominates",
  "Consequent means the line was placed to correspond with a cultural division that already existed, so a boundary negotiated between two communities along their religious divide is the case. A parallel of latitude, an unsettled survey, ruins and an imposed military line each match a different type on the list."),

 ("antecedent, which records when the line appeared",
  "Antecedent, subsequent, consequent, superimposed and relict all say something about a boundary's history, while geometric alone describes its geometry. Keeping the process axis and the form axis apart is what allows one line to be both geometric and superimposed."),

 ("Boundary 3",
  "A relict boundary is one that has ceased to function, and the record shows exactly one line no longer administered. Preceding settlement makes a boundary antecedent and an outside origin makes it superimposed, so the other two flagged rows answer different questions.",
  ),

 ("may now differ from the physical feature",
  "A boundary defined by a moving feature raises the question of whether the line follows the channel or stays where the channel used to be, which is why such treaties specify one or the other. A shift in the river ends neither the boundary's function nor changes its shape to a straight line."),

 ("subsequent for the provincial lines",
  "The provincial lines followed settlement and were adjusted as populations grew, which is subsequent, while the treaty line preceded that settlement, which is antecedent. A government drawing its own internal boundaries is not an outside power, so superimposed cannot apply to either."),

 ("who drew it and over what",
  "The two categories answer different questions, so one line can carry an answer to each: a straight segment drawn by a colonial power across an inhabited region is geometric in form and superimposed in origin. They are not synonyms, and neither one implies a particular timing."),

 ("the trace of a relict boundary",
  "The wall no longer divides jurisdictions but remains legible on the landscape, which is what makes a boundary relict rather than active. Preservation as a monument is evidence of exactly the visibility the category requires, not evidence that the line still does political work."),

 ("omits that most were imposed from outside",
  "Geometric is accurate but incomplete: it captures the form of the line while leaving out the history that explains why so many African boundaries divide peoples. That omission is what makes the description useless for reasoning about the consequences."),

 ("defined and delimited but not demarcated",
  "Defining sets a boundary in a legal document, delimiting draws it on a map, and demarcating marks it on the ground, so a treaty line never surveyed or marked has completed only the first two steps. The sequence matters because unmarked boundaries are the ones most often disputed on the ground."),

 ("was consequent when drawn",
  "Classification records the circumstances at the time the line was drawn, and this line was drawn to place each nation wholly within one state. Superimposed would require an outside power to have imposed it against the cultural map, and relict would require the boundary to have stopped functioning, and neither has happened."),

 ("communities grew up on one side or the other",
  "Timing does the work here: a line that precedes settlement cannot split a community that does not yet exist, whereas one imposed on an already inhabited region routinely does. The claim that superimposed boundaries are drawn before settlement simply restates the antecedent definition and misapplies it."),

 ("72 percent",
  "Recomputed from the table: the straight segments total 720 kilometers of a 1,000 kilometer boundary, which is 72 percent. Counting segments instead of length would give 50 percent, which is why the stem specifies length and why that figure is offered as a distractor.",
  ),

 ("superimposed and active",
  "Relict turns on whether a line still does political work, not on the age of the decision or the survival of the authority that made it. A border that two governments still administer is active by definition, whatever its colonial origin."),

 ("harder to police",
  "A straight line laid across a landscape without reference to rivers, ridges or settlement creates practical problems of its own, independent of who drew it, which is why shape is worth recording as a separate category. Shape carries no information about timing, sovereignty, status or function."),

 ("superimposed in origin, because the line disregards",
  "Prior mapping by outside surveyors is not prior settlement: the territory was inhabited by indigenous nations, so a line drawn across it by a distant treaty is superimposed. Treating a survey as evidence that the land was empty is the assumption the antecedent reading depends on, and it is false."),

 ("different laws, currencies, and services",
  "A boundary is a difference in jurisdiction, so a line drawn through a settled community delivers two sets of rules, currencies and public services to one social unit. That mismatch is the local expression of the disregard that made the boundary superimposed in the first place."),

 ("Two, because in two cases",
  "Recomputed from the table: comparing the year each line was fixed with the year of first permanent settlement shows the line preceding settlement in two of the four rows. The other two lines were fixed centuries after settlement, which makes them subsequent or superimposed rather than antecedent.",
  ),

 ("cheaper to survey but more likely to divide",
  "A straight line is trivial to define and to mark, which is why administrations drawing boundaries from a distance favored them, but it takes no account of where fields, villages and routes already are. Ease of survey and disregard for the existing landscape are the same property seen from two sides."),
]

# --- checks geo_check does not perform, because it takes bare anchors ---------
assert len(CLAIMS) == 30, f"{len(CLAIMS)} claims, expected 30"
LETTER_REF = re.compile(
    r"(?<![A-Za-z])(?:[Cc]hoice|[Oo]ption|[Aa]nswer)\s+\(?([A-E])\)?(?![A-Za-z])")
for n, entry in enumerate(CLAIMS, 1):
    anchor, claim = entry[0], entry[1]
    assert len(claim.split()) >= 8, f"4.4 q{n}: claim too thin to audit: {claim!r}"
    m = LETTER_REF.search(claim)
    assert not m, (
        f"4.4 q{n}: claim names an option by letter ({m.group(0)!r}); "
        "export_units.py shuffles the choices -- name the option by its content")

ANCHORS = [entry[0] for entry in CLAIMS]

TABLE_NOTES = {
    15: q15_relict_row,
    24: q24_straight_share,
    29: q29_antecedent_count,
}

geo_check.check(g4_4, ANCHORS, TABLE_NOTES)
