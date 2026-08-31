"""Key audit for AP HUMAN GEOGRAPHY 5.12 Women in Agriculture.

Units 4-7 verify against `geo_check`, which takes a flat ANCHORS list plus
TABLE_NOTES. The CLAIMS list below is the audit trail -- one (anchor, claim) pair
per item, in module order -- and ANCHORS is derived from it so the two cannot
drift apart.

WHAT MAY BE CITED. Learning objective IMP-5.C, "Explain geographic variations in
female roles in food production and consumption", suggested skill 3.D, and ONE
essential knowledge statement:

    IMP-5.C.1 The role of females in food production, distribution, and
              consumption varies in many places depending on the type of
              production involved.

THE STATEMENT'S SUBJECT IS VARIATION, and that governs every key in the module.
The CED does not say what women's role in agriculture IS. It says the role
VARIES, and that it varies with the TYPE OF PRODUCTION. Three consequences, all
of them deliberate:

  1. NO KEY ASSERTS A UNIVERSAL ROLE. An item keyed "women do X in farming"
     would contradict the only sentence this topic contains. Items 1, 2, 22 and
     30 key against that directly, and items 2 and 30 offer the universal claim
     -- in both its inflated and its dismissive form -- as distractors.
  2. WHERE A KEY DESCRIBES A ROLE IT NAMES THE PRODUCTION TYPE it belongs to: a
     subsistence household (item 4), a mechanized commercial operation (item 5),
     an export horticulture business (item 20), a labour-exporting district
     (item 15). That is the variable the CED names, so it belongs in the stem
     and in the key rather than being left implicit.
  3. NO REAL COUNTRY OR REGION IS NAMED ANYWHERE IN THE MODULE. Gendered
     divisions of agricultural labour differ within countries as much as
     between them and they change over time; the CED names none, and a claim
     about a named place could be stale or contested in a way no verifier could
     detect. All three data items use lettered regions and countries.

THE THREE DOMAINS -- production, distribution, consumption -- are easy to
collapse into the first. Item 3 keys on all three, items 10 and 11 give
distribution and consumption an item each so they are not an afterthought, and
item 25 requires an activity to be sorted into the right one of the three.

THE MECHANISM the module teaches, and what items 7, 8, 9, 23 and 27 rest on: the
constraint is ACCESS TO RESOURCES -- secure tenure, credit, inputs, advice --
rather than skill or effort. Item 8 makes it explicit by holding soil and
district constant so that the institutional explanation is what remains. This is
a claim about institutions, it is measurable, and it is why the CED's suggested
skill for this topic is data analysis (item 17).

THE MEASUREMENT PROBLEM IS PART OF THE TOPIC, not an aside. Work that is unpaid,
seasonal and performed on a household's own holding falls outside what a labour
survey is built to count, so a participation figure can badly understate the role
it purports to measure. Items 12, 18 and 29 key on that, and item 29 states it as
a limitation of exactly the kind of figure items 26 to 28 use -- the module
supplies the data and then supplies the caution about it.

The three table items (26, 27, 28) are the computational gate:

  26  the GAP between labour share and recorded operator share is computed for
      every region, and the verifier asserts it widens as the labour share
      rises, since the key claims both facts
  27  the two rankings are computed and compared, and credit is checked to sit
      below landholding in every country -- one distractor asserts the reverse
  28  both rows are summed per group, and the verifier asserts that field and
      paid work alone would REVERSE the comparison, which is the reason the item
      exists

REVIEW NOTE. All 30 keys were derived from the questions before this file was
written. The module was drafted with 29 items and a thirtieth was added before
this file was finished -- an item separating the SHARE OF WORK a person performs
from the CONTROL that person has over its product, which is the distinction the
two data items on landholding and credit depend on and which nothing else in the
module had asked for directly.
"""
import re

import geo_check
import g5_12


def q26_labour_against_operators(table):
    """The gap between working the land and being recorded as operating it."""
    labour, operators, gap = {}, {}, {}
    for name, l, o in table["rows"]:
        labour[name] = float(l)
        operators[name] = float(o)
        gap[name] = float(l) - float(o)
    # In every region the labour share exceeds the recorded operator share.
    assert all(gap[k] > 0 for k in gap), gap
    order = sorted(labour, key=labour.get)
    gaps_in_order = [gap[k] for k in order]
    # The gap must widen as the labour share rises -- the key claims both.
    assert all(b > a for a, b in zip(gaps_in_order, gaps_in_order[1:])), gaps_in_order
    assert min(labour.values()) == 24 and max(labour.values()) == 62, labour
    assert 9 <= min(operators.values()) and max(operators.values()) <= 14, operators
    return f"far above the share of recorded operators"


def q27_credit_tracks_land(table):
    """Credit ranks with landholding and sits below it in every country."""
    land = {r[0]: float(r[1]) for r in table["rows"]}
    credit = {r[0]: float(r[2]) for r in table["rows"]}
    assert sorted(land, key=land.get) == sorted(credit, key=credit.get), (land, credit)
    # One distractor asserts credit exceeds landholding; it must not, anywhere.
    assert all(credit[k] < land[k] for k in land), (land, credit)
    assert min(land, key=land.get) == min(credit, key=credit.get), (land, credit)
    return "sits slightly below it in every country"


def q28_time_use(table):
    """Totals per group, and a check that field work alone reverses the result."""
    rows = {r[0]: (float(r[1]), float(r[2])) for r in table["rows"]}
    field_m, field_w = rows["Field and paid work"]
    home_m, home_w = rows["Food processing, water and fuel collection"]
    total_m = field_m + home_m
    total_w = field_w + home_w
    assert abs(total_m - 6.3) < 0.001, total_m
    assert abs(total_w - 8.5) < 0.001, total_w
    # The whole point: counting field work alone would reverse the comparison.
    assert field_m > field_w, (field_m, field_w)
    assert total_w > total_m, (total_m, total_w)
    assert abs((home_w - home_m) - 3.5) < 0.001, (home_m, home_w)
    assert abs((field_m - field_w) - 1.3) < 0.001, (field_m, field_w)
    return f"{total_w:.1f} hours across the two categories against {total_m:.1f} for men"


CLAIMS = [
 ("varies in many places depending on the type of production",
  "EK IMP-5.C.1 states that the role of females in food production, distribution and consumption varies in many places depending on the type of production involved. Variation is the claim itself, and the variable the statement names is the type of production."),

 ("the role varies, and that it varies with the type of production",
  "EK IMP-5.C.1 is a statement about variation, so a claim of uniformity contradicts the only sentence this topic contains. Learning objective IMP-5.C reinforces it by asking for GEOGRAPHIC VARIATIONS rather than for a description of one role."),

 ("food distribution, and food consumption",
  "EK IMP-5.C.1 names food production, distribution and consumption in that order. Land tenure and credit help explain the variation but are not domains the statement names, which is why they belong in the reasoning rather than in the list."),

 ("carry a large share of field labour together with processing",
  "EK IMP-5.C.1 says the role varies with the type of production, and a subsistence household is the type in which production, processing and consumption all occur in one place. Where the household is the productive unit, the same people perform tasks a commercial system would separate."),

 ("sorting, packing and horticulture",
  "EK IMP-5.C.1 makes the type of production the variable the role depends on. Mechanization and waged employment separate tasks a household performs together, and where the tasks separate the pattern of who does which one changes with them."),

 ("who has access to training, credit and the machine itself",
  "EK IMP-5.C.1 says the role varies depending on the type of production, and mechanization changes that type. The reallocation runs through access to the equipment and the training rather than through the task, which is why the outcome differs from place to place."),

 ("she cannot safely invest in improvements she may not keep",
  "EK IMP-5.C.1 places female roles in food production under an enduring understanding about opportunities and challenges varying by location. Tenure is an institution rather than a fact about a person, and it governs both the incentive to improve land and the ability to borrow against it."),

 ("access to inputs, credit, advice and secure land",
  "EK IMP-5.C.1 makes the role a matter of the production system a person works within. Holding soil and district constant leaves the institutional differences -- who can buy fertilizer, who can obtain a loan, who is visited by an extension officer -- as the available explanation."),

 ("adopt improved varieties and methods more slowly",
  "EK IMP-5.C.1 says the role in food production varies with the type of production involved, and information is one of the inputs a production system distributes. Where advice is delivered to a recorded landholder, whoever is not that landholder receives it late or not at all."),

 ("market trading of produce is substantially carried out by women",
  "EK IMP-5.C.1 names food distribution alongside production and consumption. Distribution covers the stages between the field and the household, and the CED's inclusion of it is a reminder that a role can be central in one domain and marginal in another."),

 ("deciding how it is allocated within a household",
  "EK IMP-5.C.1 names consumption as the third domain in which female roles vary. Allocation within a household is where a national food supply finally becomes an individual's diet, which is why the domain belongs in a geography of food and not only in a study of production."),

 ("performed on the household's own holding is frequently not recorded",
  "EK IMP-5.C.1 concerns roles across production, distribution and consumption, much of which falls outside the categories a labour survey is built around. A measurement rule counting paid employment will miss unpaid work on one's own holding however substantial it is."),

 ("control of the cash from the sold crop",
  "EK IMP-5.C.1 says the role varies depending on the type of production involved, and a system separating a cash crop from a food crop is one such type. Responsibility for feeding the household and control of its money can then rest with different people, which is a variation in role of exactly the kind the statement describes."),

 ("unavailable for cultivation, processing or paid work",
  "EK IMP-5.C.1 covers roles in production and consumption together, and a day contains a fixed number of hours. Where one person is responsible for provisioning tasks and for field work, an increase in one is necessarily a reduction in the other."),

 ("without a matching change in land rights",
  "EK IMP-5.C.1 says the role varies with the type of production involved, and a labour-exporting district is a distinct type. The additional responsibility ordinarily arrives well before any change in the institutions that record who holds the land."),

 ("Within a household, where tasks are divided between its members",
  "EK IMP-5.C.1 says the role varies in many PLACES depending on the TYPE OF PRODUCTION, which puts variation at both scales at once. A national average conceals the household division of labour, and a single household cannot demonstrate the regional differences the statement asserts."),

 ("variation can only be demonstrated by comparing measurements across places",
  "EK IMP-5.C.1 asserts that the role varies in many places, which is a comparative claim. One place, however carefully described, cannot establish variation, and the CED's suggested skill here is comparing patterns and trends in quantitative and geospatial data."),

 ("captures unpaid work on a household's own holding",
  "EK IMP-5.C.1 concerns roles in production, so the indicator has to measure work rather than residence or assets. The qualification matters because a measure restricted to paid employment omits most of the work the statement is actually about."),

 ("changing with the system they work within rather than as fixed",
  "EK IMP-5.C.1 makes the role depend on the type of production, and EK SPS-7.D.1 states that the roles of women change as countries develop economically. Both statements locate the explanation in the surrounding system rather than in any fixed characteristic of people."),

 ("a new pattern of paid work",
  "EK IMP-5.C.1 says the role varies depending on the type of production involved, and an export horticulture operation is a type with its own labour requirements. Recorded waged employment in packing is a different role from unrecorded field labour on a household holding, not a smaller one."),

 ("hours are fully committed across productive and household tasks",
  "EK IMP-5.C.1 covers roles across production, distribution and consumption, which for one person can fill a day before any new activity begins. A programme offering training or a new crop reaches such a household as a cost as well as an opportunity."),

 ("the role follows the system rather than being carried unchanged",
  "EK IMP-5.C.1 attaches the variation explicitly to the type of production involved, which is a causal claim as well as a descriptive one. It says where to look for the explanation of a difference: in the production system rather than in the people working within it."),

 ("Recording women as landholders in their own right",
  "EK IMP-5.C.1 places female roles in production under an enduring understanding about varying opportunities and challenges. Where tenure records decide who may borrow and who is advised, changing the record changes access to every resource attached to it, which the other options leave untouched."),

 ("Work is a matter of hours in a field while control is a matter of who owns the land",
  "EK IMP-5.C.1 spans production, distribution and consumption, which is exactly the span across which work and control can come apart. A person may perform most of the labour on a plot recorded in another name and sold by another hand, so a participation figure answers only the first of the two questions."),

 ("Selling produce at a weekly market town",
  "EK IMP-5.C.1 names production, distribution and consumption as three distinct domains. Only one pairing here matches an activity to the domain it belongs to; each of the others moves an activity into one of the statement's other two categories."),

 ("far above the share of recorded operators",
  "Recomputed from the record: the labour share exceeds the recorded operator share in every region, and the gap widens from 15 points where the labour share is lowest to 51 points where it is highest. EK IMP-5.C.1 makes the role depend on the type of production, and a gap between who works the land and who is recorded as operating it is a difference in institutions rather than in effort.",
  ),

 ("sits slightly below it in every country",
  "Recomputed from the record: ranking the four countries by women's share of landholders and by their share of agricultural credit gives the same order, and credit sits below landholding in every case. EK IMP-5.C.1 makes the role depend on the production system, and a lender requiring land as security ties one institution directly to the other.",
  ),

 ("8.5 hours across the two categories against 6.3 for men",
  "Recomputed from the record: the two rows sum to 6.3 hours for men and 8.5 for women, with a 3.5-hour difference in processing and collection against a 1.3-hour difference in field and paid work. The verifier also confirms that counting field and paid work alone would reverse the comparison, which is the reason the item exists.",
  ),

 ("may exclude unpaid work on a household's own holding",
  "EK IMP-5.C.1 concerns roles across production, distribution and consumption, much of which is unpaid and performed on a household's own land. A measure built around paid employment omits that work by construction, which is a defect of the instrument rather than of the people being counted."),

 ("differs from place to place, and what it depends on is the type of production",
  "EK IMP-5.C.1 asserts variation and names the type of production as what the variation depends on. Both universal claims contradict the statement, and the climate version replaces the CED's own variable with one the framework does not name here."),
]

# --- checks geo_check does not perform, because it takes bare anchors ---------
assert len(CLAIMS) == 30, f"{len(CLAIMS)} claims, expected 30"
LETTER_REF = re.compile(
    r"(?<![A-Za-z])(?:[Cc]hoice|[Oo]ption|[Aa]nswer)\s+\(?([A-E])\)?(?![A-Za-z])")
for n, entry in enumerate(CLAIMS, 1):
    anchor, claim = entry[0], entry[1]
    assert len(claim.split()) >= 8, f"5.12 q{n}: claim too thin to audit: {claim!r}"
    m = LETTER_REF.search(claim)
    assert not m, (
        f"5.12 q{n}: claim names an option by letter ({m.group(0)!r}); "
        "export_units.py shuffles the choices -- name the option by its content")

ANCHORS = [entry[0] for entry in CLAIMS]

TABLE_NOTES = {
    26: q26_labour_against_operators,
    27: q27_credit_tracks_land,
    28: q28_time_use,
}

geo_check.check(g5_12, ANCHORS, TABLE_NOTES)
