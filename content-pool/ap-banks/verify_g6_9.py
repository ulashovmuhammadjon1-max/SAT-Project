"""Key audit for AP HUMAN GEOGRAPHY 6.9 Urban Data.

Units 4-7 verify against `geo_check`, which takes a flat ANCHORS list plus
TABLE_NOTES. The CLAIMS list below is the audit trail -- one (anchor, claim) pair
per item, in module order -- and ANCHORS is derived from it so the two cannot
drift apart.

WHAT MAY BE CITED. Learning objective IMP-6.E, suggested skill 3.E, and two
statements:

    IMP-6.E.1 Quantitative data from census and survey data provide information
              about changes in population composition and size in urban areas.
    IMP-6.E.2 Qualitative data from field studies and narratives provide
              information about individual attitudes toward urban change.

THE TWO STATEMENTS ANSWER DIFFERENT QUESTIONS and the topic is knowing which
question each can answer. Quantitative sources give HOW MANY and WHO; qualitative
sources give HOW IT IS REGARDED and WHY. A census can establish that a district's
median income doubled and its renting households fell by a third, and it cannot
say whether the people who left chose to or had to. Items 13 and 14 sit on either
side of that boundary -- one question only qualitative data can answer and one
only quantitative data can -- and item 15 is what the learning objective actually
asks for, since causes and effects generally need both at once.

THE CED'S OWN WORDS ARE SPECIFIC and the module keys on two of them. IMP-6.E.1
says composition AND SIZE, which move independently: item 7 describes a district
whose total is unchanged while its median age falls twelve years, and item 26's
table has size rising 21 percent while income more than doubles. IMP-6.E.2 says
INDIVIDUAL attitudes, and that word is why qualitative evidence is strong on
meaning and weak on generalization, which item 21 keys on directly.

THE OVERLAP WITH TOPIC 1.2 IS BOUNDED DELIBERATELY. That topic covers geographic
data in general -- field observation, remote sensing, geographic information
systems, policy documents, travel narratives. This module keeps to the four
sources THIS statement names and to what they show about URBAN change, so the two
topics do not become one module written twice.

LIMITATIONS ARE PART OF THIS TOPIC rather than an appendix, because the suggested
skill is explaining what data imply. Items 17 to 21 and 29 cover the four that
matter in urban work: an area figure is not a statement about any individual in
it; hard-to-count populations are undercounted exactly where they concentrate; a
census is already old when published; and a sample is only as good as who
answered. Item 29 adds the one specific to this subject -- a survey of a
gentrifying district cannot reach the households the change already moved out, so
the sample is selected by the very process being measured.

NO REAL CITY IS NAMED ANYWHERE IN THIS MODULE.

The three table items (26, 27, 28) are the computational gate:

  26  size and composition are computed separately and the verifier asserts they
      changed at DIFFERENT rates, since the key's claim is that composition moved
      far more than size
  27  each row checked to sum to 100 and the two groups' positions checked to be
      near mirror images, which is what the key asserts
  28  the two answer counts checked to sum to the number surveyed, and both
      shares derived -- the majority verdict and the concentration inside the
      minority, since the key rests on the two together

REVIEW NOTE. All 30 keys were derived from the questions before this file was
written and none needed correcting. THREE ITEMS HAD TO BE REPAIRED before this
file could be run: they were written with a malformed token in place of `ans=0`,
the same defect class SOCIAL_RESUME.md records from a stopped predecessor's
`july := None`. It is worth recording how it was caught -- not by reading, but by
importing the module and asserting every `ans` was present and in range before
writing a single claim. A module that merely parses is not a module that is
well formed.
"""
import re

import geo_check
import g6_9

# The repair described above, made permanent: a malformed answer token leaves
# `ans` missing rather than wrong, which reads as a KeyError deep inside the
# shared checker instead of as a defect in this file. Check it here, where the
# message can say what actually happened.
for _n, _item in enumerate(g6_9.QUESTIONS, 1):
    assert "ans" in _item, f"6.9 q{_n}: no `ans` key -- malformed answer token?"
    assert isinstance(_item["ans"], int), f"6.9 q{_n}: `ans` is {_item['ans']!r}"


def q26_composition_against_size(table):
    """Size and composition move at different rates -- that is the item's point."""
    rows = {r[0]: (float(r[1].replace(",", "")), float(r[2].replace(",", "")))
            for r in table["rows"]}
    pop_b, pop_a = rows["Population"]
    inc_b, inc_a = rows["Median household income (thousands)"]
    rent_share_b, rent_share_a = rows["Share of households renting (%)"]
    rent_b, rent_a = rows["Median monthly rent"]
    pop_growth = 100 * (pop_a - pop_b) / pop_b
    assert 20 < pop_growth < 22, pop_growth
    assert inc_a > 2 * inc_b, (inc_b, inc_a)
    assert 2.7 < rent_a / rent_b < 3.0, (rent_b, rent_a)
    assert rent_share_b - rent_share_a == 27, (rent_share_b, rent_share_a)
    # Composition must move far more than size, or the key does not follow.
    # Compare GROWTH, not the raw ratios: income grows 119 percent against the
    # population's 21, so income growth is about 5.6 times as large. My first
    # draft compared 68/31 with 5100/4200 -- two ratios that both start at 1 --
    # and failed. The record was right and the check was wrong.
    inc_growth = 100 * (inc_a - inc_b) / inc_b
    assert inc_growth > 5 * pop_growth, (pop_growth, inc_growth)
    return f"about {pop_growth:.0f} percent while median income more than doubled"


def q27_mirrored_responses(table):
    """Each row sums to 100 and the two groups are near mirror images."""
    rows = {r[0]: [float(c) for c in r[1:]] for r in table["rows"]}
    for group, vals in rows.items():
        assert sum(vals) == 100, (group, vals)
    own_yes, own_no, _ = rows["Homeowners"]
    rent_yes, rent_no, _ = rows["Renters"]
    assert own_yes == 68 and rent_yes == 24, (own_yes, rent_yes)
    assert own_no == 22 and rent_no == 64, (own_no, rent_no)
    # Near mirror images: each group's approval is close to the other's
    # opposition, which is what "almost exactly reversed" asserts.
    assert abs(own_yes - rent_no) <= 5 and abs(own_no - rent_yes) <= 5, rows
    return (f"{own_yes:.0f} percent of owners approving against "
            f"{rent_yes:.0f} percent of renters")


def q28_majority_and_minority(table):
    """Counts must reconcile, and both shares are derived from them."""
    counts = {r[0]: float(r[1].replace(",", "")) for r in table["rows"]}
    surveyed = counts["Households surveyed"]
    better = counts["Said the neighbourhood had improved"]
    worse = counts["Said the neighbourhood had worsened"]
    renters = counts["Of those saying it had worsened, number who rent"]
    assert better + worse == surveyed, (better, worse, surveyed)
    assert better > worse, (better, worse)
    share_better = round(100 * better / surveyed)
    share_renters = round(100 * renters / worse)
    assert share_better == 65, share_better
    assert share_renters == 84, share_renters
    return f"{share_renters} percent of those saying it had worsened were renters"


CLAIMS = [
 ("changes in population composition and size in urban areas",
  "EK IMP-6.E.1 states that quantitative data from census and survey data provide information about changes in population composition and size in urban areas. Attitudes belong to EK IMP-6.E.2's qualitative sources, which is the division this whole topic rests on."),

 ("individual attitudes toward urban change",
  "EK IMP-6.E.2 states that qualitative data from field studies and narratives provide information about individual attitudes toward urban change. Counts and medians are what EK IMP-6.E.1's quantitative sources supply instead."),

 ("how many and who, against how the change is regarded",
  "EK IMP-6.E.1 and EK IMP-6.E.2 assign the two kinds of data to different subjects, and learning objective IMP-6.E asks how both are used to show causes and effects. A count establishes that something happened; an account establishes what it meant to the people it happened to."),

 ("by age, household type, tenure and income changed between the two counts",
  "EK IMP-6.E.1 says quantitative data from census and survey data provide information about changes in population composition and size in urban areas. A census counts everyone and records characteristics, so comparing two counts measures what changed and by how much."),

 ("at the cost of covering only a sample rather than everyone",
  "EK IMP-6.E.1 names census AND survey data together as quantitative sources. A census is complete and infrequent while a survey is partial and frequent, so the two answer questions at different resolutions in time and in space."),

 ("What the population consists of",
  "EK IMP-6.E.1 names changes in population composition AND size as what quantitative data reveal. Composition is the internal make-up of a population, which is a different thing from its total and can change while the total does not move at all."),

 ("composition has changed substantially while its size has not",
  "EK IMP-6.E.1 names changes in population composition AND size as two separate things quantitative data reveal. A district can replace much of its population without changing its total, and a study reporting only the total would record no change whatever."),

 ("falling share of households renting and a falling share of long-tenure residents",
  "EK IMP-6.E.1 says quantitative data show changes in population composition and size in urban areas. The signature of this kind of change is several measures moving consistently together rather than any single one of them moving alone."),

 ("moved by choice or were pushed out",
  "EK IMP-6.E.1 confines quantitative data to changes in composition and size, and EK IMP-6.E.2 assigns attitudes and accounts to qualitative sources. A difference between two counts is compatible with several quite different stories about how it came about."),

 ("Direct observation and interviewing carried out in the place being studied",
  "EK IMP-6.E.2 names field studies among the qualitative sources providing information about individual attitudes toward urban change. Being present is the method: what is observed and what people say in the place itself is evidence a returned form cannot supply."),

 ("an interview, an oral history, a written recollection",
  "EK IMP-6.E.2 names narratives alongside field studies as qualitative sources on individual attitudes toward urban change. What a narrative supplies is a person's own account, including reasons and meanings that no count records."),

 ("whether change is supported, resisted or reversed",
  "EK IMP-6.E.2 names individual attitudes toward urban change as the subject of qualitative data, and enduring understanding IMP-6 says a population's attitudes and values are reflected in the built landscape. What residents accept or oppose feeds back into what is built."),

 ("Why long-term residents describe a redeveloped district as no longer theirs",
  "EK IMP-6.E.2 assigns individual attitudes toward urban change to qualitative sources, and a question about why a person describes something a particular way is a question about meaning. The four rejected options are counts and comparisons of counts."),

 ("By how much the district's share of households renting fell",
  "EK IMP-6.E.1 says quantitative data from census and survey data provide information about changes in population composition and size. A magnitude is what a count supplies, and no number of interviews can establish by how much a share changed across a whole district."),

 ("supply the reasons people give and the effects they report",
  "Learning objective IMP-6.E asks how qualitative AND quantitative data are used to show the causes and effects of geographic change within urban areas. Cause and effect are the joint product: one source locates and sizes the change and the other accounts for it."),

 ("a city-wide figure can conceal opposite changes in different districts",
  "EK IMP-6.E.1 says quantitative data provide information about change IN URBAN AREAS, and the suggested skill for this topic is explaining what data imply. A city whose median income is flat may contain districts that doubled and districts that halved."),

 ("individuals within the area vary around it",
  "The suggested skill for this topic is explaining what data imply, and this is the commonest fallacy in reading area data. A district with a high median income contains poor households, and inferring an individual's characteristics from an area's is an error the aggregation itself creates."),

 ("so the undercount is spatially uneven",
  "EK IMP-6.E.1 makes the census a source on population composition and size, so a systematic undercount distorts both. Because hard-to-count groups cluster geographically, the error falls hardest on precisely the districts whose numbers most need to be right."),

 ("so it can be years out of date",
  "EK IMP-6.E.1 names census data as a quantitative source on changes in composition and size. A complete enumeration is expensive and therefore infrequent, and the price of completeness is that the picture is always of a moment already past."),

 ("since a sample that over-represents some groups will misdescribe it",
  "EK IMP-6.E.1 names survey data among the quantitative sources on population composition and size. A sample stands in for a population only if it resembles it, so who did not answer matters as much as who did."),

 ("cannot establish how widely a view is held",
  "EK IMP-6.E.2 says qualitative data provide information about INDIVIDUAL attitudes toward urban change, and that word carries the limitation. Depth and generalization trade against each other, which is exactly why the framework pairs this statement with a quantitative one."),

 ("A single count describes a state",
  "EK IMP-6.E.1 says quantitative data provide information about CHANGES in population composition and size. A change is a difference between two observations, so the comparison rather than either count is what carries the information."),

 ("rather than which are currently rich or poor",
  "EK IMP-6.E.1 makes CHANGES in population composition the subject of quantitative urban data, and the suggested skill is explaining what maps or data imply. A level map and a change map can look nothing alike, since a poor district rising fast and a rich one standing still are opposite on one and similar on the other."),

 ("the account produced is shaped by the encounter",
  "EK IMP-6.E.2 names field studies among the qualitative sources on individual attitudes toward urban change. An attitude is elicited rather than measured, so the circumstances of the asking are part of what produced the answer and belong in the account of it."),

 ("How many households left the district between two censuses, answered by quantitative data",
  "EK IMP-6.E.1 assigns changes in composition and size to quantitative sources and EK IMP-6.E.2 assigns individual attitudes to qualitative ones. Only one pairing here matches a question to the kind of data the framework says can answer it."),

 ("about 21 percent while median income more than doubled",
  "Recomputed from the record: population rises from 4,200 to 5,100, about 21 percent, while median income rises from 31 to 68, rent from 640 to 1,780, and the renting share falls exactly 27 points. The verifier asserts composition moved far more than size, which is what EK IMP-6.E.1's naming them separately is for.",
  ),

 ("68 percent of owners approving against 24 percent of renters",
  "Recomputed from the record: each row sums to 100, approval runs 68 percent among owners against 24 among renters, and opposition runs 22 against 64, so each group's approval is within five points of the other's opposition. EK IMP-6.E.1 names survey data among the quantitative sources, and disaggregating by tenure is what makes a city-wide figure readable.",
  ),

 ("84 percent of those saying it had worsened were renters",
  "Recomputed from the record: the two answers sum to the 480 households surveyed, 312 of them about 65 percent, and 141 of the 168 negative answers, about 84 percent, came from renters. Learning objective IMP-6.E asks how data show causes and effects of urban change, and a majority verdict concealing a concentrated minority experience is why both readings are needed.",
  ),

 ("cannot be surveyed in it",
  "EK IMP-6.E.1 names survey data among the quantitative sources on urban change, and a survey reaches whoever is present to answer it. Where the change under study is one that moved people out, the sample is selected by the very process being measured."),

 ("while field studies and narratives record what individuals think",
  "EK IMP-6.E.1 assigns size and composition to quantitative sources, EK IMP-6.E.2 assigns individual attitudes to qualitative ones, and learning objective IMP-6.E asks how both are used to show causes and effects. Each rejected summary either swaps the two assignments or discards one of them."),
]

# --- checks geo_check does not perform, because it takes bare anchors ---------
assert len(CLAIMS) == 30, f"{len(CLAIMS)} claims, expected 30"
LETTER_REF = re.compile(
    r"(?<![A-Za-z])(?:[Cc]hoice|[Oo]ption|[Aa]nswer)\s+\(?([A-E])\)?(?![A-Za-z])")
for n, entry in enumerate(CLAIMS, 1):
    anchor, claim = entry[0], entry[1]
    assert len(claim.split()) >= 8, f"6.9 q{n}: claim too thin to audit: {claim!r}"
    m = LETTER_REF.search(claim)
    assert not m, (
        f"6.9 q{n}: claim names an option by letter ({m.group(0)!r}); "
        "export_units.py shuffles the choices -- name the option by its content")

ANCHORS = [entry[0] for entry in CLAIMS]

TABLE_NOTES = {
    26: q26_composition_against_size,
    27: q27_mirrored_responses,
    28: q28_majority_and_minority,
}

geo_check.check(g6_9, ANCHORS, TABLE_NOTES)
