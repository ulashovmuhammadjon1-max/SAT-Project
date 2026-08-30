"""Key audit for AP HUMAN GEOGRAPHY 2.10 Causes of Migration.

One (anchor, claim) per item, in module order; a third element recomputes the
item's arithmetic from its own table.

WHAT MAY BE CITED. IMP-2.C prints two essential-knowledge statements:

    IMP-2.C.1  Migration is commonly divided into push factors and pull factors.
    IMP-2.C.2  Push/pull factors and intervening opportunities/obstacles can be
               cultural, demographic, economic, environmental, or political.

This is one of the most citable topics in the course, because IMP-2.C.2 is a
CLOSED LIST of five categories AND it names two further roles beyond push and
pull. Almost every key here traces to one or both statements:

  role fixed by IMP-2.C.1 (origin vs destination):  3, 4, 5, 9, 10, 11, 12, 13,
      15, 16, 19, 22, 25
  role fixed by IMP-2.C.2 (obstacle vs opportunity): 6, 7, 8, 14, 17, 20, 23,
      27, 29
  category fixed by IMP-2.C.2's list of five:        2, 3, 4, 9, 10, 11, 12, 16,
      17, 18, 22, 26, 30

WHAT THE STATEMENTS DO NOT DEFINE, and how the module handles it. The CED names
intervening opportunities and obstacles without saying how they differ, so the
distinction every key rests on is stated in the module header and repeated in
the claims: an OBSTACLE hinders or prevents the move, an OPPORTUNITY diverts the
migrant to a nearer destination. Both lie between origin and destination, so
position cannot separate them and only effect can. Item 8 asks about that
directly and item 14 supplies a case containing one of each.

Two further disciplines the module observes, both to keep keys defensible:

  * Push and pull are usually two descriptions of one difference, so any item
    asking which is operating supplies enough detail to locate the condition.
    Items 3, 4, 5, 22 and 24 are written that way deliberately.
  * IMP-2.C.2's five categories classify the FACTOR, not its consequences. Item
    16 is built on that: a war is a political factor with environmental and
    economic consequences, and classifying it by its consequences is the error.

The five table items (26-30) are the computational gate, and three of them
invert an obvious column:

  27  settlement shifts toward the NEAREST destination against stated
      intentions, which is what an intervening opportunity does
  28  the highest-wage destination is NOT the best first-year outcome once the
      cost of moving is subtracted
  29  an obstacle is a RATE, so the category refusing the largest NUMBER of
      applicants is not the hardest to pass

REVIEW NOTE, written while building the tables. Item 29's first draft gave
20,000 more applications to the humanitarian category, which made it -- not the
skilled-worker category -- the one refusing the largest number of applicants, so
a distractor stating otherwise was simply false rather than plausibly wrong. The
figures were changed so the distractor's premise is true and only its inference
fails, and the recompute asserts that separation. No key was changed.
"""
import hg_check
from hg_check import num, numcol, column, rowdict
import g2_10

# The five categories IMP-2.C.2 prints, mapped to the survey wording of item 26.
CATEGORY_OF_REASON = {
    "No work available locally": "economic",
    "Repeated crop failure and water shortage": "environmental",
    "Fear of violence or persecution": "political",
    "To join family already elsewhere": "cultural",
    "No one of my own age left in the village": "demographic",
}


def q26_dominant_category(table):
    """Each reason maps to one of the five categories; economic dominates."""
    counts = {}
    total = 0.0
    for row in table["rows"]:
        d = rowdict(table, row)
        reason = d["Main reason given for leaving"]
        assert reason in CATEGORY_OF_REASON, f"unmapped reason: {reason!r}"
        n = num(d["Respondents"])
        counts[CATEGORY_OF_REASON[reason]] = n
        total += n
    assert set(counts) == set(CATEGORY_OF_REASON.values()), counts
    assert total == 4000, total
    top = max(counts, key=counts.get)
    assert top == "economic" and counts["economic"] == 1840, counts
    runner_up = sorted(counts.values(), reverse=True)[1]
    assert counts["economic"] > 2 * runner_up, counts
    return "1,840 of 4,000 respondents"


def q27_intervening_opportunity(table):
    """Settlement shifts toward the nearest destination against intentions."""
    rows = sorted((num(rowdict(table, r)["Distance from origin (km)"]),
                   rowdict(table, r)["Destination"],
                   num(rowdict(table, r)["Intended to settle there"]),
                   num(rowdict(table, r)["Actually settled there"]))
                  for r in table["rows"])
    assert sum(r[2] for r in rows) == sum(r[3] for r in rows), rows
    nearest, farthest = rows[0], rows[-1]
    assert nearest[3] - nearest[2] > 1000, nearest
    assert farthest[3] - farthest[2] < -1000, farthest
    # The middle destination must barely move, or the shift is not toward the
    # nearest one in particular.
    middle = rows[1]
    assert abs(middle[3] - middle[2]) < 200, middle
    return "toward the nearest destination"


def q28_net_gain(table):
    """First-year net gain: wage premium minus the cost of the journey."""
    by_place = {rowdict(table, r)["Place"]: rowdict(table, r) for r in table["rows"]}
    origin = num(by_place["Origin"]["Annual wage (US$)"])
    gains, wages = {}, {}
    for place, d in by_place.items():
        if place == "Origin":
            continue
        w = num(d["Annual wage (US$)"])
        cost = num(d["One-off cost of moving there (US$)"])
        wages[place] = w
        gains[place] = w - origin - cost
    best = max(gains, key=gains.get)
    assert best == "Destination 3", gains
    assert gains == {"Destination 1": 1400, "Destination 2": 1000,
                     "Destination 3": 1900}, gains
    # The highest wage must belong to a different destination, or the cost of
    # moving -- an intervening obstacle -- changes nothing.
    assert max(wages, key=wages.get) != best, wages
    return "net gain of 1,900 dollars"


def q29_obstacle_is_a_rate(table):
    """Admission RATE identifies the obstacle; refusal COUNT does not."""
    rate, refused = {}, {}
    for row in table["rows"]:
        d = rowdict(table, row)
        apps = num(d["Applications"])
        adm = num(d["Admissions"])
        rate[d["Visa category"]] = 100 * adm / apps
        refused[d["Visa category"]] = apps - adm
    hardest = min(rate, key=rate.get)
    assert hardest == "Humanitarian protection", rate
    assert rate == {"Skilled worker": 55, "Seasonal agricultural": 90,
                    "Family reunification": 50, "Humanitarian protection": 12}, rate
    # The distractor's premise must be TRUE and its inference wrong: the largest
    # number refused belongs to a category that is not the hardest to pass.
    most_refused = max(refused, key=refused.get)
    assert most_refused == "Skilled worker", refused
    assert most_refused != hardest, (refused, rate)
    return "admits 12 percent of applicants"


def q30_wages_do_not_explain(table):
    """Three districts line up on wages; the fourth needs another factor."""
    rows = {}
    for row in table["rows"]:
        d = rowdict(table, row)
        rows[d["District"]] = (
            num(d["Average wage relative to national (%)"]),
            num(d["Years since last major flood"]),
            abs(num(d["Net migration rate (per 1,000)"])),
        )
    odd = "District C"
    others = [k for k in rows if k != odd]
    # Among the other three, a lower wage really does go with a bigger outflow.
    ranked_by_wage = sorted(others, key=lambda k: rows[k][0])
    outflows = [rows[k][2] for k in ranked_by_wage]
    assert all(outflows[i] > outflows[i + 1] for i in range(len(outflows) - 1)), \
        (ranked_by_wage, outflows)
    # The odd district has near-average wages and the largest outflow of all.
    assert rows[odd][2] == max(r[2] for r in rows.values()), rows
    assert rows[odd][0] >= 90, rows
    # ...and the most recent flood, which is the factor the wage column misses.
    assert rows[odd][1] == min(r[1] for r in rows.values()), rows
    return "wages are near the national average"


CLAIMS = [
 ("Into push factors and pull factors",
  "EK IMP-2.C.1 states that migration is commonly divided into push factors and pull factors. The other four divisions offered are real and appear elsewhere in this unit, but none of them is the division this statement names."),

 ("Cultural, demographic, economic, environmental, and political",
  "EK IMP-2.C.2 prints exactly this list of five and applies it to push and pull factors and to intervening opportunities and obstacles alike. Each distractor substitutes a plausible category the statement does not contain."),

 ("condition is at the origin and concerns the physical environment",
  "EK IMP-2.C.1's push factors are conditions at the origin and EK IMP-2.C.2 supplies environmental among the five categories. Repeated crop failure is a physical condition of the place being left, which settles both the role and the category at once."),

 ("condition at the destination that attracts migrants",
  "EK IMP-2.C.1 distinguishes push from pull by where the condition sits, and advertised work sits at the destination. EK IMP-2.C.2's economic category covers work and wages, which makes the classification complete on both axes."),

 ("condition at the place of origin; a pull factor is a condition at the destination",
  "EK IMP-2.C.1's division is spatial: the two terms name where a condition lies relative to the move. EK IMP-2.C.2 then applies all five categories to both, so neither term is tied to any particular kind of cause."),

 ("lies between origin and destination and hinders the move",
  "EK IMP-2.C.2 names intervening obstacles as a role alongside push and pull. What unites a mountain range, a paid sea crossing and an unobtainable visa is position -- between the two ends of the move -- and effect, which is to hinder rather than attract or repel."),

 ("ended the journey early",
  "EK IMP-2.C.2 names intervening opportunities as a distinct role, and the diagnostic is diversion rather than obstruction. The job did not prevent the move; it satisfied the reason for the move before the intended destination was reached."),

 ("obstacle hinders or prevents the move; an opportunity diverts",
  "Both roles lie between origin and destination, so position cannot separate them and only effect can. EK IMP-2.C.2 lists them as a pair because they are the two ways the space between two places can alter a migration."),

 ("state action at the origin drives people out",
  "EK IMP-2.C.2's political category covers the acts of states and EK IMP-2.C.1's push factors are conditions at the origin. That the consequences include economic and demographic effects does not change what kind of factor the revocation itself is."),

 ("composition of the origin's population is itself the reason",
  "EK IMP-2.C.2 lists demographic among the five categories, and this is what that category is for: the number and age composition of the people already present. Prior migration has thinned the cohort itself, which is a demographic condition rather than an economic one."),

 ("shared language and religion at the destination",
  "EK IMP-2.C.2's cultural category and EK IMP-2.C.1's pull role combine here, since the condition is at the destination and concerns language, religion and belonging. Choosing a further city over a nearer one is what shows the cultural factor outweighing distance."),

 ("An environmental push factor",
  "The condition is at the origin, which makes it a push under EK IMP-2.C.1, and it is a physical change in the environment, which places it in EK IMP-2.C.2's environmental category. Both axes must be answered and only one option is correct on each."),

 ("requires both something to leave and somewhere better to go",
  "EK IMP-2.C.1 divides the factors into two halves of a single comparison, and a comparison needs both terms. Unemployment at home is a reason to leave only if work exists somewhere reachable, which is why lists of causes rarely name only one side."),

 ("the cost, and an intervening opportunity, the nearby city",
  "EK IMP-2.C.2 names both roles, and this case contains one of each: the cost hinders the intended move while the nearer city absorbs the migrant instead. Separating them matters because they act on the same journey in opposite ways."),

 ("resources, obligations, and alternatives",
  "EK IMP-2.C.1's factors enter a decision rather than determine one, so the same drought or wage gap is weighed against different assets, ties and options in each household. That is why migration from a village is selective rather than total."),

 ("political push factor with environmental and economic consequences",
  "EK IMP-2.C.2's five categories classify the FACTOR rather than its consequences, and the factor here is organized violence, which is political. Naming the consequences separately is what makes the classification complete instead of confused."),

 ("state rule stands between them and the destination",
  "EK IMP-2.C.2 applies the five categories to intervening obstacles as well as to push and pull factors. A quota is a rule made by a state that sits between the migrant and the destination, which fixes both the role and the category."),

 ("shortage of workers in the ages the migrants belong to",
  "EK IMP-2.C.2's demographic category concerns the composition of a population rather than its wages or its culture. A gap in a destination's own age structure is a demographic condition at the destination, which makes it demographic and a pull at the same time."),

 ("Political persecution in the country a migrant is leaving",
  "This is an INCORRECT-pairing question, so the key is the one option that misclassifies. EK IMP-2.C.1 fixes push and pull by location, and persecution in the country being left is at the origin, which makes it a push factor rather than a pull one."),

 ("intervening obstacle has weakened",
  "EK IMP-2.C.2 makes obstacles a factor in their own right, and distance, cost and time are among the commonest of them. Nothing at either end of the move has changed in this case; what changed is what lies between them."),

 ("existing community supplies language, contacts, housing, and work information",
  "EK IMP-2.C.2's cultural category covers shared language, kinship and community, and the condition sits at the destination, which makes it a pull. An established community lowers the real cost of arriving, which is why later migrants concentrate where earlier ones did."),

 ("warm, dry climate that attracts retirees",
  "EK IMP-2.C.1 fixes the role by where the condition is, and only one option describes a physical condition at a place people are moving TO. The other four are physical conditions at places people are moving FROM, which makes each of them a push."),

 ("the thing standing in its way can each be cultural",
  "EK IMP-2.C.2 explicitly attaches the five categories to push and pull factors AND to intervening opportunities and obstacles. Treating obstacles as always physical is the misreading the statement forecloses, since a visa regime and a war zone are political obstacles."),

 ("the poorest people often cannot afford to move",
  "EK IMP-2.C.1 divides causes into two halves and EK IMP-2.C.2 adds what lies between, so a one-term account omits both. It also runs into the cost of the journey, an intervening obstacle whose importance rises exactly as income falls."),

 ("Deliberately created pull factors",
  "EK IMP-2.C.1's pull factors are conditions at the destination, and a grant, a house and a school place are exactly that for the district being moved to. EK IMP-2.C.2's economic category covers the money and the housing that make up most of the package."),

 ("1,840 of 4,000 respondents",
  "Recomputed from the table: the five stated reasons map one to one onto EK IMP-2.C.2's five categories, and 1,840 of 4,000 responses fall in the economic one against 760 for the next largest. The verifier asserts the economic share really does exceed twice the runner-up, which is what the key claims.",
  q26_dominant_category),

 ("toward the nearest destination",
  "Recomputed from the table: the nearest destination gains 1,600 settlers over intentions while the most distant loses 1,500, and the middle one barely moves. Migrants stopping short of an intended destination at a nearer place is the definition of an intervening opportunity.",
  q27_intervening_opportunity),

 ("net gain of 1,900 dollars",
  "Recomputed from the table: subtracting the origin wage and then the cost of moving gives first-year gains of 1,400, 1,000 and 1,900 dollars. The verifier confirms the highest-wage destination is not the best outcome, which is the cost of the journey acting as an intervening obstacle.",
  q28_net_gain),

 ("admits 12 percent of applicants",
  "Recomputed from the table: admission rates are 55, 90, 50 and 12 percent, so the category hardest to pass is the one admitting the smallest share. The verifier confirms separately that the category refusing the largest NUMBER of applicants is a different one, so that distractor is true in its premise and wrong in its inference.",
  q29_obstacle_is_a_rate),

 ("wages are near the national average",
  "Recomputed from the table: for three of the four districts a lower relative wage really does go with a larger outflow, and the fourth breaks the pattern with near-average wages and the largest outflow of all. Its flood in the previous year points to an environmental push factor no wage column can capture.",
  q30_wages_do_not_explain),
]

hg_check.check(g2_10, CLAIMS, per_topic=30, n_choices=5)
