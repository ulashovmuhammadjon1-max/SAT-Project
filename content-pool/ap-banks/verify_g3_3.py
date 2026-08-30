"""Key audit for AP HUMAN GEOGRAPHY 3.3 Cultural Patterns.

One (anchor, claim) per item, in module order; a third element recomputes the
item's arithmetic from its own table.

WHAT MAY BE CITED. PSO-3.D prints two essential-knowledge statements, and the
same three variables appear in both doing different jobs:

    PSO-3.D.1  Regional patterns of language, religion, and ethnicity contribute
               to a sense of place, enhance placemaking, and shape the global
               cultural landscape.
    PSO-3.D.2  Language, ethnicity, and religion are factors in creating
               centripetal and centrifugal forces.

PSO-3.D.1 is about MEANING -- character, deliberate place-shaping, and the
composition of the world's cultural landscape out of regional ones. Items 1-8,
15, 18, 21, 22, 26 and 30 are keyed to it.

PSO-3.D.2 is about COHESION -- whether the same distributions hold a state
together or pull it apart. Items 9-14, 16, 17, 19, 20, 23, 24, 25 and 27-29 are
keyed to it.

Item 17 asks why the CED lists the same three variables twice, which is the
point of the pairing: one map of who speaks, worships and identifies how
produces both a landscape of distinctive places and a politics of unity or
division.

WHAT THE CED DOES NOT DEFINE, and which every key therefore argues rather than
cites: centripetal force, centrifugal force, sense of place and placemaking. All
four definitions are set out in the module header. The one that matters most is
the symmetry -- the SAME variable acts in either direction depending on
distribution and on state policy -- and items 10, 11, 12, 16, 20 and 25 are
built on it. Items 10 and 11 are a deliberate pair: identical policies, opposite
effects, because the underlying distributions differ. Item 12 then asks for the
generalization, which is the only place in the module where a student is asked
to state the rule rather than apply it.

Two keys are worded to stop short of overclaiming, and their claims say so
explicitly: item 7 keys to a CAPACITY for centrifugal force rather than to a
prediction of division, and item 29 keys to data that FIT a reading rather than
proving it, because four regions cannot establish causation.

The five table items (26-30) are the computational gate:

  26  the two columns are shares of two different populations and do NOT sum to
      100 -- the recompute asserts that, since treating them as one composition
      would be the error the item invites
  27  both rows sum to 100; the divisive case is the one whose largest language
      is a minority
  28  all three rows sum to 100; near-parity between two traditions is the
      distribution that divides
  29  the recognized regions average 11 percent against 41, with no overlap
  30  attachment rises at every step, with no reversal anywhere

REVIEW NOTE, written while building the tables. Item 26 originally gave visitors
71 percent for landscape, which made two distractors false in their premises --
one claimed visitors named landscape most often (they named language most often)
and another claimed ethnic history showed the largest gap (landscape did). The
visitor figure was changed to 61 so that both distractors are true in premise and
wrong only in inference, and the recompute asserts both facts. No key was
changed.
"""
import hg_check
from hg_check import num, numcol, column, rowdict
import g3_3


def q26_two_populations(table):
    """Two independent samples, so the columns do not sum to 100."""
    res, vis, names = {}, {}, []
    for row in table["rows"]:
        d = rowdict(table, row)
        k = d["Named as making the region distinctive"]
        names.append(k)
        res[k] = num(d["Residents (%)"])
        vis[k] = num(d["Visitors (%)"])
    # This is the point of the item: neither column is a composition.
    assert sum(res.values()) != 100 and sum(vis.values()) != 100, (res, vis)
    both_high = [k for k in names if res[k] > 70 and vis[k] > 70]
    assert both_high == ["The regional language"], (res, vis)
    # Each distractor's premise must be TRUE and only its inference wrong.
    assert max(vis, key=vis.get) == "The regional language", vis
    assert vis["Landscape and scenery"] > res["Landscape and scenery"], (res, vis)
    gaps = {k: abs(res[k] - vis[k]) for k in names}
    assert max(gaps, key=gaps.get) == "Shared ethnic history", gaps
    assert vis["Religious observances and festivals"] > res["Religious observances and festivals"]
    assert min(res, key=res.get) == "Local economy" and min(vis, key=vis.get) == "Local economy"
    return "the only factor above 70 percent for both groups"


def q27_language_fragmentation(table):
    """Both rows sum to 100; one country's largest language is a minority."""
    rows = {}
    for row in table["rows"]:
        d = rowdict(table, row)
        vals = [num(d[h]) for h in table["headers"] if h != "Country"]
        assert sum(vals) == 100, (d["Country"], vals)
        rows[d["Country"]] = vals
    a, b = rows["Country A"], rows["Country B"]
    assert a[0] > 90, a
    assert b[0] < 50, b
    # Three languages OTHER than the largest are above 10 percent, which is
    # what the keyed choice claims.
    assert sum(1 for v in b[1:] if v > 10) == 3, b
    # The dominant country's non-dominant share is the distractor's true premise.
    assert sum(a[1:]) == 7, a
    return "spoken by only 41 percent"


def q28_religious_parity(table):
    """Every row sums to 100; near-parity is the divisive distribution."""
    gaps = {}
    for row in table["rows"]:
        d = rowdict(table, row)
        vals = [num(d[h]) for h in table["headers"] if h != "State"]
        assert sum(vals) == 100, (d["State"], vals)
        gaps[d["State"]] = vals[0] - vals[1]
    closest = min(gaps, key=gaps.get)
    assert closest == "State 2", gaps
    assert gaps["State 2"] == 3, gaps
    # The other two must have a decisive majority tradition.
    for s in gaps:
        if s != closest:
            assert gaps[s] > 40, (s, gaps[s])
    return "two traditions of nearly equal size"


def q29_recognition_and_separatism(table):
    """Recognized regions average 11 percent; unrecognized average 41."""
    yes, no = [], []
    for row in table["rows"]:
        d = rowdict(table, row)
        s = num(d["Support for separation (%)"])
        (yes if d["Minority language recognized in schools and courts"] == "Yes"
         else no).append(s)
    assert len(yes) == 2 and len(no) == 2, (yes, no)
    my, mn = sum(yes) / len(yes), sum(no) / len(no)
    assert my == 11 and mn == 41, (my, mn)
    # The two groups must not overlap, or the pattern is not clean.
    assert max(yes) < min(no), (yes, no)
    assert mn - my > 25, (my, mn)
    return "average 11 percent support against 41 percent"


def q30_placemaking_association(table):
    """Attachment rises at every step as projects increase."""
    pairs = sorted((num(rowdict(table, r)["Placemaking projects completed"]),
                    num(rowdict(table, r)["Residents describing the district as distinctive (%)"]))
                   for r in table["rows"])
    projects = [p for p, _ in pairs]
    attach = [a for _, a in pairs]
    assert projects == [0, 3, 7, 12], projects
    assert attach == [22, 41, 63, 78], attach
    assert all(attach[i] < attach[i + 1] for i in range(len(attach) - 1)), attach
    # The zero-project district must be the lowest, disposing of a distractor.
    assert attach[0] == min(attach), attach
    return "from 22 percent with none to 78 percent"


CLAIMS = [
 ("Language, religion, and ethnicity",
  "EK PSO-3.D.1 names exactly these three and EK PSO-3.D.2 names the same three again in a different role. The repetition is deliberate: the variables giving a region its character are the ones that can also unite or divide a state."),

 ("sense of place produced by regional patterns",
  "EK PSO-3.D.1 states that regional patterns of language, religion and ethnicity contribute to a sense of place. What the residents are describing is the character those patterns give a district, which is exactly the effect the statement names."),

 ("deliberate shaping of a place's character",
  "EK PSO-3.D.1 says regional patterns of language, religion and ethnicity ENHANCE PLACEMAKING. Signage, murals and a reopened hall are deliberate acts intended to make a district legible as belonging to a particular community."),

 ("together compose the world's cultural landscape",
  "EK PSO-3.D.1 says these regional patterns SHAPE the global cultural landscape, which is a statement about scale. The world's cultural map is the assembly of its regional ones rather than a separate thing sitting above them."),

 ("spoken there and almost nowhere else",
  "EK PSO-3.D.1 names language, religion and ethnicity as the sources of a sense of place. Temperature, distance, population and area describe a region without giving it a character anyone could recognize as belonging to a particular people."),

 ("Institutional placemaking",
  "EK PSO-3.D.1 says cultural patterns enhance placemaking without limiting who does the making. A municipality choosing which history to mark and fund is shaping meaning as deliberately as residents do, and with considerably more resources."),

 ("cultural variables capable of acting as centrifugal forces",
  "EK PSO-3.D.1 makes these patterns sources of a sense of place and EK PSO-3.D.2 makes the same variables factors in centrifugal forces. The key names a capacity rather than an outcome, because division is possible here and not guaranteed."),

 ("survive long after that group has gone",
  "EK PSO-3.D.1 makes regional patterns of language part of what shapes a cultural landscape, and a place name is language fixed to a location. Their durability is what makes them evidence, since a name can outlast the population that coined it."),

 ("draw a population together and factors that pull it apart",
  "EK PSO-3.D.2 names language, ethnicity and religion as factors in creating centripetal and centrifugal forces without defining the pair. The definitions used throughout are cohesion and division: what binds a population to a state, and what loosens that bond."),

 ("formalizes something almost everyone already shares",
  "EK PSO-3.D.2 makes language a factor in both kinds of force, and which one appears depends on distribution. Formalizing a language nearly the whole population already uses adds a symbol of unity without imposing a cost on many people."),

 ("majority is required to conduct public life in a language that is not its own",
  "EK PSO-3.D.2 makes language a factor in both directions, and the policy that unified in the previous item divides here because the distribution differs. Being required to use another group's language in court, school and administration is a standing grievance."),

 ("depending on how it is distributed and how the state handles it",
  "EK PSO-3.D.2 names the three variables as factors in BOTH kinds of force, which is why the pair is listed once rather than twice. Distribution and policy decide the direction; the variable by itself decides nothing at all."),

 ("common identity and shared institutions",
  "EK PSO-3.D.2 names religion among the factors in centripetal and centrifugal forces. A faith held in common supplies shared symbols, a shared calendar and institutions reaching every settlement, which is cohesion in its most tangible form."),

 ("division runs through the institutions the state depends on",
  "EK PSO-3.D.2 names religion as a factor in centrifugal as well as centripetal forces. Two communities of comparable size competing for the same institutions turns every institutional decision into a contest between them."),

 ("surnames, church denominations, and building styles still differ",
  "EK PSO-3.D.1 names ethnicity among the regional patterns that shape a cultural landscape. A shared founding population leaves traces in names, worship and building that persist as a visible band across the map."),

 ("recognition removes a grievance and gives the minority a stake",
  "EK PSO-3.D.2 makes language a factor in both directions, and accommodation moves it toward the centripetal one by converting an exclusion into a form of belonging. Asserting the opposite as an invariable rule is what makes the separatism option wrong."),

 ("two different consequences of one distribution",
  "EK PSO-3.D.1 assigns the three variables a role in meaning and EK PSO-3.D.2 assigns them a role in cohesion. One map of who speaks, worships and identifies how produces both a landscape of distinctive places and a politics of unity or division."),

 ("Residents and outsiders alike can describe what is distinctive",
  "EK PSO-3.D.1 makes sense of place a product of regional patterns of language, religion and ethnicity. Evidence must therefore concern recognizable character rather than size, administration or wealth, none of which produces distinctiveness."),

 ("taught in every school, matched to a centripetal force",
  "EK PSO-3.D.2 makes language a factor in both kinds of force, and a language everyone learns and shares supplies a medium for national life. The other four pairings attach a unifying condition to the dividing force, which reverses the relationship."),

 ("suppression turns a cultural difference into a grievance",
  "EK PSO-3.D.2 names language as a factor in centrifugal forces, and suppression is where it most reliably becomes one. A difference that might have been unremarkable is made into an identity worth defending, which is the opposite of what suppression intends."),

 ("used to erase one community's sense of place",
  "EK PSO-3.D.1 covers placemaking and sense of place while EK PSO-3.D.2 covers the resulting force on cohesion. Placemaking is not intrinsically benign: the same tools that build a community's character can be turned to removing it."),

 ("sharing a language but not a religion",
  "EK PSO-3.D.1 and EK PSO-3.D.2 both list the three variables separately, and separateness is demonstrated by cross-cutting cases. Where the three lines fall in different places, none of them can be standing in for the others."),

 ("sharpened by the group's concentration and its exclusion",
  "EK PSO-3.D.2 names language and ethnicity among the factors in centrifugal forces, and this case adds the two conditions that intensify them: territorial concentration, which makes separation thinkable, and exclusion, which removes the reason not to seek it."),

 ("widely used second language",
  "EK PSO-3.D.2 makes language a factor in centripetal forces, and a shared second language unifies without displacing anyone's first. Each of the other options names something confined to part of the population, which cannot bind the whole of it."),

 ("depends on how institutions accommodate it",
  "EK PSO-3.D.2 makes the three variables FACTORS in both kinds of force rather than causes of either. Counting languages predicts nothing on its own, because the same count is consistent with recognition and with suppression."),

 ("the only factor above 70 percent for both groups",
  "Recomputed from the table: only the language row exceeds 70 percent in both columns, and the verifier confirms the two columns are shares of two different populations rather than one composition. It also confirms every distractor's premise is true, so each fails on its inference rather than on its arithmetic.",
  q26_two_populations),

 ("spoken by only 41 percent",
  "Recomputed from the table: both rows sum to 100, one country's largest language covers 93 percent and the other's covers 41 with three further languages above 10. EK PSO-3.D.2 makes language a factor in both directions, and imposing a minority language on a majority is the case that divides.",
  q27_language_fragmentation),

 ("two traditions of nearly equal size",
  "Recomputed from the table: every row sums to 100, and one state pairs 49 percent with 46 while the others hold majorities of 88 and 71 percent. EK PSO-3.D.2 names religion among the factors in centrifugal forces, and near-parity makes every institutional question a contest.",
  q28_religious_parity),

 ("average 11 percent support against 41 percent",
  "Recomputed from the table: the two regions with recognition average 11 percent support and the two without average 41, with no overlap between the groups. Four regions cannot establish causation, which is why the key says the data fit accommodation acting centripetally rather than proving it.",
  q29_recognition_and_separatism),

 ("from 22 percent with none to 78 percent",
  "Recomputed from the table: projects run 0, 3, 7 and 12 while attachment runs 22, 41, 63 and 78 percent, rising at every step with no reversal. EK PSO-3.D.1 says cultural patterns enhance placemaking, and four districts show an association rather than establishing that the projects caused it.",
  q30_placemaking_association),
]

hg_check.check(g3_3, CLAIMS, per_topic=30, n_choices=5)
