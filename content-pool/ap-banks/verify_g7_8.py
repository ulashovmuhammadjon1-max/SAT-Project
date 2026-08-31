"""Key audit for AP HUMAN GEOGRAPHY 7.8 Sustainable Development.

Units 4-7 verify against `geo_check`, which takes a flat ANCHORS list plus
TABLE_NOTES. The CLAIMS list below is the audit trail -- one (anchor, claim) pair
per item, in module order -- and ANCHORS is derived from it so the two cannot
drift apart.

WHAT MAY BE CITED. Enduring understanding IMP-7, learning objective IMP-7.A,
suggested skill 5.D, three essential knowledge statements, and one further CED
sentence from the unit 7 overview:

    IMP-7     Environmental problems stemming from industrialization MAY BE
              REMEDIED through sustainable development strategies.
    IMP-7.A.1 Sustainable development policies ATTEMPT to remedy problems
              stemming from natural-resource depletion, mass consumption, the
              effects of pollution, and the impact of climate change.
    IMP-7.A.2 Ecotourism is tourism based in natural environments -- OFTEN
              environments that are threatened by LOOMING industrialization or
              development -- that FREQUENTLY helps to protect the environment in
              question WHILE ALSO providing jobs for the local population.
    IMP-7.A.3 The UN's Sustainable Development Goals HELP MEASURE progress in
              development, such as small-scale finance and public
              transportation projects.
    unit 7 overview, page 121 -- "Students explore strategies for sustainable
              development focused on women, children, health, education, the
              environment, and global cooperation."   (items 9 and 10)

THIS TOPIC IS BUILT OUT OF HEDGES AND THE HEDGES ARE THE CONTENT. Five of them,
each keyed on by its own item: MAY BE REMEDIED (item 1), ATTEMPT TO REMEDY
(item 3), OFTEN threatened (item 12), FREQUENTLY helps (item 14), HELP MEASURE
(item 21). A student who reads any of them flat has learned that sustainable
development works, which the framework nowhere says. The distractor sets in
those five items are deliberately symmetric: each carries the over-reading (it
always works) AND the under-reading (it never works), because both misreport the
statement equally and only one of them feels like the cautious answer. Item 30
does the same for all five at once.

NOTHING IS ASSERTED ABOUT ANY INDIVIDUAL SUSTAINABLE DEVELOPMENT GOAL. The CED
neither quotes nor numbers any of the seventeen, so no item here names, numbers
or quotes one. What the CED does say is that they HELP MEASURE progress, with
small-scale finance and public transportation projects as its examples, and
items 19 to 22 stay inside that.

TWO COLLISIONS WERE AVAILABLE IN THIS BANK AND BOTH WERE STEERED AROUND:

    g1_5 q8 already asks which definition of sustainability matches the way the
    course uses the concept. No item here defines sustainability.

    g6_11 covers urban sustainability in fifteen items -- sprawl, sanitation,
    air and water quality, ecological footprint, brownfields, growth boundaries,
    farmland protection -- every one of them inside the city. This topic's scale
    is the industrial economy and the world, and item 23 is the item that makes
    the difference explicit rather than papering over it. Nothing here repeats a
    g6_11 stem or a g6_11 key.

SUGGESTED SKILL 5.D ASKS FOR THE DEGREE TO WHICH SOMETHING WORKS ACROSS SCALES,
which is a stronger demand than asking what it is, and items 18, 23 and 24 are
that skill. Item 18 is the sharpest: EK IMP-7.A.2 credits ecotourism with
protecting the environment IN QUESTION, which is a claim about one place, while
EK IMP-7.A.1 names a global process. Saying so is not scepticism about
ecotourism; it is reporting the scale the CED's own words attach to it.

NO REAL COUNTRY, PLACE, SITE OR PROJECT IS NAMED ANYWHERE IN THIS MODULE. The
three data items carry hypothetical records attached to an unnamed protected
site, an unnamed district and four unnamed economies.

The three table items (27, 28, 29) are the computational gate:

  27  the money retained locally is DERIVED from a share and a total and appears
      nowhere in the record, as is revenue per visitor. Four distractors are
      each checked against directly -- most of the revenue leaving, the
      protected area shrinking, nobody employed, revenue per visitor above a
      thousand -- because a record that failed any of them would make a
      distractor true.
  28  the four indicator rows are found by keyword in the record's own first
      column rather than by position, and all four are checked to have MOVED,
      since a distractor says only one did. The directions are checked
      separately: two rises and two falls, and getting one backwards would make
      a different distractor true.
  29  income, consumption per person and emissions per person are each checked
      to rise at EVERY step, and the totals are checked NOT to, with the largest
      total checked to sit on a different economy from the largest per-person
      figure. That divergence is the whole point of the item; a record where the
      totals also rose in order would let a student reach the key while
      believing per-person and national figures say the same thing.

ROUNDING. Every returned string is built from the recomputed values and printed
the way a person would state them, with the exact value held by a bound beside
it. verify_g7_4.py had to be repaired for the opposite mistake: it recomputed
3,696 and demanded those digits appear in a choice that correctly said "about
3,700", so it failed a question whose arithmetic was right.

REVIEW NOTE. All 30 keys were derived from the questions before this file was
written. One drafted item was cut: "What is an ecological footprint?", which is
g6_11 q7 word for word. Its slot became item 26, on what a measured goal cannot
capture, which is EK IMP-7.A.3's own hedge and belongs to no other topic.
"""
import re

import geo_check
import g7_8

for _n, _item in enumerate(g7_8.QUESTIONS, 1):
    assert isinstance(_item.get("ans"), int), f"7.8 q{_n}: `ans` is {_item.get('ans')!r}"
    assert 0 <= _item["ans"] < len(_item["choices"]), f"7.8 q{_n}: ans out of range"


def _num(cell):
    return float(str(cell).replace(",", ""))


def q27_ecotourism_site(table):
    """Money retained locally derived from a share and a total."""
    vals = {r[0]: _num(r[1]) for r in table["rows"]}
    visitors = vals["Visitors a year"]
    revenue = vals["Revenue a year (currency units)"]
    share = vals["Share of revenue retained in the local economy (%)"]
    jobs = vals["Local residents employed at the site"]
    area_now = vals["Area under a protection agreement (hectares)"]
    area_then = vals[
        "Area under a protection agreement ten years earlier (hectares)"]
    retained = revenue * share / 100
    # A distractor says most of the revenue leaves the local economy.
    assert share > 50, share
    assert retained < revenue, (retained, revenue)
    # A distractor says the protected area has shrunk.
    assert area_now > area_then, (area_now, area_then)
    # A distractor says nobody local is employed.
    assert jobs > 0, jobs
    # A distractor says revenue per visitor exceeds a thousand.
    assert revenue / visitors < 1000, revenue / visitors
    shown = round(retained)
    assert abs(retained - shown) < 0.5, retained
    return (f"About {shown:,.0f} currency units of the revenue stays in the "
            "local economy")


def q28_transport_project(table):
    """Rows found by keyword, not by position; all four must have moved."""
    def row(word):
        hits = [r for r in table["rows"] if word in r[0].lower()]
        assert len(hits) == 1, (word, [r[0] for r in table["rows"]])
        return _num(hits[0][1]), _num(hits[0][2])

    access_b, access_a = row("scheduled service")
    time_b, time_a = row("journey time")
    school_b, school_a = row("attending school")
    car_b, car_a = row("private vehicle")
    # A distractor says only one indicator moved; another reverses each of
    # these directions in turn.
    assert access_a > access_b, (access_b, access_a)
    assert time_a < time_b, (time_b, time_a)
    assert school_a > school_b, (school_b, school_a)
    assert car_a < car_b, (car_b, car_a)
    gain = access_a - access_b
    saved = time_b - time_a
    for exact in (gain, saved):
        assert abs(exact - round(exact)) < 0.5, exact
    return (f"Access rose by {gain:.0f} percentage points and the journey to "
            f"the hospital fell by {saved:.0f} minutes")


def q29_consumption_and_totals(table):
    """Per-person figures rise at every step; the totals must NOT."""
    income = [_num(r[1]) for r in table["rows"]]
    consumption = [_num(r[2]) for r in table["rows"]]
    per_person = [_num(r[3]) for r in table["rows"]]
    total = [_num(r[4]) for r in table["rows"]]
    rising = lambda xs: all(b > a for a, b in zip(xs, xs[1:]))
    assert rising(income), income
    # Two distractors: consumption falling with income, emissions per person
    # about the same everywhere.
    assert rising(consumption), consumption
    assert rising(per_person), per_person
    assert max(per_person) / min(per_person) > 2, per_person
    # Two distractors: totals rising with income, and the largest total sitting
    # on the largest per-person figure. Both must be false, or the item teaches
    # that per-person and national figures answer the same question.
    assert not rising(total), total
    assert total.index(max(total)) != per_person.index(max(per_person)), (
        total, per_person)
    return (f"from {consumption[0]:g} to {consumption[-1]:g} tonnes and from "
            f"{per_person[0]:g} to {per_person[-1]:g} tonnes")


CLAIMS = [
 ("They may be remedied through sustainable development strategies",
  "Enduring understanding IMP-7 states that environmental problems stemming from industrialization MAY BE REMEDIED through sustainable development strategies. The modal claims possibility rather than certainty, and it is the frame every statement in this topic sits inside."),

 ("Natural-resource depletion, mass consumption, the effects of pollution",
  "EK IMP-7.A.1 names exactly these four. The rejected sets are real lists from elsewhere in this course -- the challenges to urban sustainability, the changes in the world economy, the measures of development -- which makes choosing between them a test of this statement rather than of memory in general."),

 ("without asserting that they succeed",
  "EK IMP-7.A.1 says sustainable development policies ATTEMPT to remedy the problems it lists. A statement of aim is not a statement of result, and leaving the result open is exactly what suggested skill 5.D then asks a student to assess in its phrase 'the degree to which'."),

 ("drawing down of a stock faster than it is replaced",
  "EK IMP-7.A.1 names natural-resource depletion first among the four, and enduring understanding IMP-7 attributes such problems to industrialization. Depletion is a relation between the rate of use and the rate of replacement, which is why the same withdrawal can be sustainable at one scale of production and not at another."),

 ("upstream of the waste and emissions that follow from meeting it",
  "EK IMP-7.A.1 lists mass consumption and the effects of pollution as separate items, and the stage models named in EK SPS-7.E.1 place high mass consumption as a condition an economy arrives at. Naming demand separately from waste means a policy can address either without addressing the other."),

 ("what pollution does to a place and to the people in it",
  "EK IMP-7.A.1 says the EFFECTS of pollution rather than pollution as such. Learning objective IMP-7.A asks how sustainability principles relate to SPATIAL development, and effects are where a chemical becomes a geographic fact, since the same emission produces different consequences in different places."),

 ("the impact falls unevenly across places",
  "EK IMP-7.A.1 names the IMPACT of climate change among the four problems, and learning objective IMP-7.A concerns spatial development. A globally produced process with locally variable consequences is the case suggested skill 5.D is built around, because the scale of the cause and the scale of the effect differ."),

 ("raised the scale at which materials are extracted, transformed and discarded",
  "Enduring understanding IMP-7 says environmental problems STEMMING FROM INDUSTRIALIZATION may be remedied, and enduring understanding SPS-7 says industrialization facilitated improvements in standards of living but contributed to geographically uneven development. The connection the framework draws is one of scale rather than of kind."),

 ("Women, children, health, education, the environment, and global cooperation",
  "The unit 7 overview states that students explore strategies for sustainable development focused on women, children, health, education, the environment, and global cooperation. Four of the six are social rather than environmental, which tells a student the framework does not treat this as an environmental programme only."),

 ("covers the social conditions of development as well as the environmental ones",
  "The unit 7 overview groups all six concerns in one sentence about strategies for sustainable development, and learning objective IMP-7.A asks how sustainability principles relate to industrialization AND spatial development. A gain in living standards a place cannot hold on to is not a durable gain, which is why both halves appear in one list."),

 ("Tourism based in natural environments that frequently helps to protect the environment",
  "EK IMP-7.A.2 defines ecotourism as tourism based in natural environments that frequently helps to protect the environment in question while also providing jobs for the local population. Setting, protection and employment are three parts of one definition, and dropping any leaves something the statement does not describe."),

 ("often environments threatened by looming industrialization or development",
  "EK IMP-7.A.2 says ecotourism is based in natural environments -- OFTEN environments threatened by looming industrialization or development. The word 'often' makes it a tendency rather than a defining condition, so a site under no such threat is still ecotourism."),

 ("Helps to protect the environment in question, while also providing jobs for the local population",
  "EK IMP-7.A.2 says ecotourism frequently helps to protect the environment in question WHILE ALSO providing jobs for the local population. The phrase asserts both together, which is why the practice appears in a topic about sustainable development rather than in one about conservation."),

 ("leaving room for cases in which the protection fails",
  "EK IMP-7.A.2 says ecotourism FREQUENTLY helps to protect the environment in question. A frequency claim is compatible with counterexamples and would be falsified only by their being the rule, which is what suggested skill 5.D's 'degree to which' asks a student to weigh."),

 ("the asset the visitors are paying to see",
  "EK IMP-7.A.2 says ecotourism frequently helps to protect the environment in question while also providing jobs for the local population, and the CED does not state the mechanism joining the two. Making the environment the source of the earnings gives protection a constituency, which is what separates it from protection imposed against local interests."),

 ("earnings that leave the area give them no stake in the site",
  "EK IMP-7.A.2 says ecotourism provides jobs FOR THE LOCAL POPULATION specifically. The people whose alternative uses of the land are given up are the local ones, so a benefit accruing anywhere else does not answer the cost the arrangement imposes on them."),

 ("marks the threat as prospective rather than accomplished",
  "EK IMP-7.A.2 says the environments are often threatened by LOOMING industrialization or development. A threat that has not yet arrived is one an alternative can still forestall, which is why the word matters to what ecotourism is being credited with."),

 ("it does not by itself reduce mass consumption",
  "EK IMP-7.A.2 credits ecotourism with protecting the environment IN QUESTION, a claim about one place, while EK IMP-7.A.1 names problems including a global process. Suggested skill 5.D asks for the degree to which something explains effects ACROSS SCALES, and an instrument effective at a site is not thereby effective at the scale of the world."),

 ("They help measure progress in development",
  "EK IMP-7.A.3 states that the UN's Sustainable Development Goals HELP MEASURE progress in development. The claim is about measurement rather than about compulsion, which is far narrower than what the goals are often taken to be."),

 ("Small-scale finance and public transportation projects",
  "EK IMP-7.A.3 names small-scale finance and public transportation projects as its examples. Both are concrete undertakings rather than statements of intent, which fits the statement's claim being about measuring progress rather than about declaring aims."),

 ("A goal with an indicator attached is a yardstick",
  "EK IMP-7.A.3 says the goals HELP MEASURE progress in development, such as small-scale finance and public transportation projects. Naming projects as the examples locates the doing in the projects, and the goals supply the terms in which the doing is judged."),

 ("One works at the scale of a household and the other at the scale of a settlement",
  "EK IMP-7.A.3 offers both as examples in one clause, and suggested skill 5.D asks about geographic effects across various geographic scales. A loan reaches one household and a bus network reaches a whole settlement, so the pairing demonstrates range rather than repeating a point."),

 ("made at one scale and the problem is generated at another",
  "Suggested skill 5.D asks for the degree to which a concept explains geographic effects across various geographic scales, and EK IMP-7.A.1 lists problems ranging from a depleted local stock to the impact of climate change. A remedy has to reach the level at which its problem is produced, and the four named problems are not all produced at one level."),

 ("the district's record improves while the total",
  "EK IMP-7.A.1 names both the effects of pollution and the impact of climate change among the problems policies attempt to remedy, and suggested skill 5.D asks for effects across scales. A displacement is a genuine improvement in one place and no improvement in the total, which is why the two scales have to be assessed separately."),

 ("tracked over enough years to separate it from the fluctuation",
  "EK IMP-7.A.1 says policies ATTEMPT to remedy the four problems and EK IMP-7.A.3 says the goals HELP MEASURE progress, so the framework itself separates the aim from the result. Spending and announcements are inputs, and only a change in the targeted condition speaks to whether the attempt succeeded."),

 ("a real gain that no indicator counts is invisible",
  "EK IMP-7.A.3 says the goals HELP MEASURE progress in development, and the verb concedes that measurement is an aid rather than the thing itself. EK SPS-7.C.1 names sectoral structure BOTH FORMAL AND INFORMAL among the measures of development, which is the same point: what is not counted is not thereby absent."),

 ("About 1,170,000 currency units of the revenue stays in the local economy",
  "Recomputed from the record: 65 percent of 1,800,000 currency units is about 1,170,000, revenue per visitor is 75, employment is 210, and the protected area has risen from 1,600 to 4,300 hectares. EK IMP-7.A.2 says ecotourism frequently helps to protect the environment in question WHILE ALSO providing jobs for the local population, and the record shows both halves at once.",
  ),

 ("Access rose by 43 percentage points and the journey to the hospital fell by 33 minutes",
  "Recomputed from the record: access rises from 38 to 81 percent, journey time falls from 74 to 41 minutes, attendance rises from 62 to 79 percent, and private vehicle trips fall from 96 to 72 thousand a week. EK IMP-7.A.3 names public transportation projects as an example of what the goals help measure, and the unit 7 overview names health, education and the environment among the concerns such strategies address.",
  ),

 ("from 4 to 26 tonnes and from 1.1 to 14.6 tonnes",
  "Recomputed from the record: material consumption per person runs 4, 9, 17 and 26 tonnes and emissions per person 1.1, 3.4, 7.2 and 14.6 tonnes, both rising at every step, while total emissions run 39, 520, 310 and 467 and so do not. EK IMP-7.A.1 names mass consumption among the problems policies attempt to remedy, and suggested skill 5.D asks about scales, since the per-person and the national totals answer different questions.",
  ),

 ("ecotourism frequently protects a site while also employing local people",
  "Enduring understanding IMP-7 says MAY BE REMEDIED, EK IMP-7.A.1 says ATTEMPT to remedy, EK IMP-7.A.2 says FREQUENTLY helps, and EK IMP-7.A.3 says HELP MEASURE. Every rejected summary either hardens one of those four hedges into a guarantee or collapses it into a denial, and both errors misreport the framework equally."),
]

# --- checks geo_check does not perform, because it takes bare anchors ---------
assert len(CLAIMS) == 30, f"{len(CLAIMS)} claims, expected 30"
LETTER_REF = re.compile(
    r"(?<![A-Za-z])(?:[Cc]hoice|[Oo]ption|[Aa]nswer)\s+\(?([A-E])\)?(?![A-Za-z])")
for n, entry in enumerate(CLAIMS, 1):
    anchor, claim = entry[0], entry[1]
    assert len(claim.split()) >= 8, f"7.8 q{n}: claim too thin to audit: {claim!r}"
    m = LETTER_REF.search(claim)
    assert not m, (
        f"7.8 q{n}: claim names an option by letter ({m.group(0)!r}); "
        "export_units.py shuffles the choices -- name the option by its content")

# The exporter does not typeset this subject, so hand-written LaTeX would ship
# as literal backslashes, and a range written with a hyphen between two digits
# reads as a minus sign to any converter ever pointed at the bank. Explicit
# lookarounds, never \b -- a digit and a letter are both word characters.
DIGIT_RANGE = re.compile(r"[0-9]\s*[-/]\s*[0-9]")
for n, item in enumerate(g7_8.QUESTIONS, 1):
    strings = [item["q"], item["why"], *item["choices"]]
    tbl = item.get("table")
    if tbl:
        strings += list(tbl["headers"]) + [c for row in tbl["rows"] for c in row]
    for s in strings:
        assert "\\(" not in s and "\\[" not in s and "$" not in s, (
            f"7.8 q{n}: math delimiter in a prose subject: {s!r}")
        m = DIGIT_RANGE.search(s)
        assert not m, f"7.8 q{n}: digit range {m.group(0)!r} in {s!r}"

ANCHORS = [entry[0] for entry in CLAIMS]

TABLE_NOTES = {
    27: q27_ecotourism_site,
    28: q28_transport_project,
    29: q29_consumption_and_totals,
}

geo_check.check(g7_8, ANCHORS, TABLE_NOTES)
