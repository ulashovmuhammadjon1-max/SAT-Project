"""Key audit for AP HUMAN GEOGRAPHY 3.1 Introduction to Culture.

One (anchor, claim) per item, in module order; a third element recomputes the
item's arithmetic from its own table.

WHAT MAY BE CITED. PSO-3.A prints three essential-knowledge statements:

    PSO-3.A.1  Culture comprises the shared practices, technologies, attitudes,
               and behaviors transmitted by a society.
    PSO-3.A.2  Culture traits include such things as food preferences,
               architecture, and land use.
    PSO-3.A.3  Cultural relativism and ethnocentrism are different attitudes
               toward cultural difference.

PSO-3.A.1 is the rare CED statement that is a genuine DEFINITION, so it can
carry keys directly. Its three load-bearing words are SHARED, TRANSMITTED and
the four-noun list, and items 1, 2, 3, 9, 12, 14, 20, 23 and 24 each turn on one
of them. Item 3 is a NOT question keyed to "shared" and item 2 to "transmitted",
which is the way to test a definition rather than to have it recited.

PSO-3.A.2 is NOT a closed list. It reads "include such things as", so the three
examples illustrate rather than exhaust. Item 4 asks about that phrasing
directly, and no key anywhere in this module says a thing is not a culture trait
because it is absent from the CED's three; that would misread the sentence and
would also be false of language, dress and kinship.

PSO-3.A.3 names two attitudes and defines neither, so the definitions every key
rests on are stated in the module header:
    ethnocentrism        judging another culture by one's own standards
    cultural relativism  understanding a practice on its own culture's terms
Item 8 exists specifically to hold relativism apart from the much stronger claim
that all practices are equally desirable. The CED calls it an ATTITUDE toward
difference, which is a stance toward understanding rather than a moral verdict,
and teaching the stronger claim as though the framework endorsed it would be a
wrong key on a contested question.

Items 10, 18 and 22 lean on PSO-3's enduring understanding -- cultural practices
vary because of physical geography and available resources -- which is a claim
about influence, not determination. Those claims say so, because reading it as
determination would resurrect the environmental determinism Unit 1 rejects.

The five table items (26-30) are the computational gate. All five carry
composition data where each column or row sums to 100, so the recomputes assert
that first: a share table supports statements about proportions and none at all
about totals. Beyond that:

  27  the two courtyard categories TOGETHER still hold 73 percent, so the
      inherited plan survives even as the purely traditional form collapses
  29  soil is identical and rainfall differs by about one percent while field
      size differs ninetyfold, so the physical columns cannot be the cause
  30  the most widely shared trait is the one that is BOTH high and consistent,
      which is a different question from which single figure is largest

REVIEW NOTE, written while building the tables. Item 30 carried a distractor
claiming the festival row "reaches the highest single figure in the table", which
is false -- the language row reaches 91. It was rewritten so its premise is true
and only its inference fails, and the recompute asserts the language row holds
the maximum. No key was changed.
"""
import hg_check
from hg_check import num, numcol, column, rowdict
import g3_1


def _rows_sum_to_100(table, label_col):
    """Every row of a composition table must sum to 100."""
    cols = [h for h in table["headers"] if h != label_col]
    for row in table["rows"]:
        d = rowdict(table, row)
        total = sum(num(d[c]) for c in cols)
        assert abs(total - 100) < 1e-9, (d[label_col], total)


def q26_regional_staple(table):
    """Three regions have a staple above 70 percent; one has none above 38."""
    _rows_sum_to_100(table, "Region")
    grains = [h for h in table["headers"] if h != "Region" and h != "Other (%)"]
    tops = {}
    for row in table["rows"]:
        d = rowdict(table, row)
        tops[d["Region"]] = max(num(d[g]) for g in grains)
    clear = [r for r, v in tops.items() if v > 70]
    mixed = [r for r, v in tops.items() if v <= 40]
    assert len(clear) == 3, tops
    assert len(mixed) == 1, tops
    assert set(clear) | set(mixed) == set(tops), tops
    return "exceeding 70 percent while one is mixed"


def q27_plan_survives(table):
    """The two courtyard categories together still hold most new building."""
    _rows_sum_to_100(table, "Period")
    trad, adapted, imported = [], [], []
    for row in table["rows"]:
        d = rowdict(table, row)
        trad.append(num(d["Traditional courtyard form (%)"]))
        adapted.append(num(d["Adapted courtyard with new materials (%)"]))
        imported.append(num(d["Imported style (%)"]))
    courtyard = [t + a for t, a in zip(trad, adapted)]
    assert courtyard == [96, 88, 73], courtyard
    # The purely traditional form collapses...
    assert trad[0] > 90 and trad[-1] < 25, trad
    # ...but the plan still accounts for most new houses, and imported styles
    # never become the majority, which disposes of two distractors.
    assert courtyard[-1] > 50, courtyard
    assert max(imported) < 50, imported
    return "73 percent"


def q28_relativism_in_survey(table):
    """The relativist response and the ethnocentric one are near-reversed."""
    a = numcol(table, "Group A (%)")
    b = numcol(table, "Group B (%)")
    assert sum(a) == 100 and sum(b) == 100, (sum(a), sum(b))
    resp = column(table, "Response given")
    ask = resp.index("Asked what the practice means to those who follow it")
    judge = resp.index("Judged it inferior to their own equivalent practice")
    assert b[ask] == 58 and a[ask] == 14, (a[ask], b[ask])
    assert a[judge] == 63 and b[judge] == 17, (a[judge], b[judge])
    # Group B must lead on the relativist response and trail on the other.
    assert b[ask] > a[ask] and b[judge] < a[judge], (a, b)
    return "58 percent sought the practice's meaning"


def q29_culture_not_environment(table):
    """Physical columns are near-identical; the cultural one differs enormously."""
    rows = {rowdict(table, r)["Feature"]: rowdict(table, r) for r in table["rows"]}
    f1 = num(rows["Mean field size (hectares)"]["District 1"])
    f2 = num(rows["Mean field size (hectares)"]["District 2"])
    r1 = num(rows["Mean annual rainfall (mm)"]["District 1"])
    r2 = num(rows["Mean annual rainfall (mm)"]["District 2"])
    soil1 = rows["Soil type"]["District 1"]
    soil2 = rows["Soil type"]["District 2"]
    assert soil1 == soil2, (soil1, soil2)
    rain_gap = abs(r2 - r1) / min(r1, r2)
    field_ratio = max(f1, f2) / min(f1, f2)
    assert rain_gap < 0.02, rain_gap
    assert field_ratio >= 90, field_ratio
    # The inheritance rows must genuinely differ, or nothing is left to explain it.
    assert (rows["Inheritance custom"]["District 1"]
            != rows["Inheritance custom"]["District 2"])
    return "ninetyfold difference in field size"


def q30_most_widely_shared(table):
    """High AND consistent, which is not the same as the single largest figure."""
    districts = [h for h in table["headers"] if h != "Trait named as central"]
    stats = {}
    for row in table["rows"]:
        d = rowdict(table, row)
        vals = [num(d[c]) for c in districts]
        stats[d["Trait named as central"]] = (min(vals), max(vals), max(vals) - min(vals))
    lang = stats["Language spoken at home"]
    assert lang[0] >= 84, stats
    assert lang[2] == min(s[2] for s in stats.values()), stats
    assert lang[0] == max(s[0] for s in stats.values()), stats
    # The language row must also hold the single largest figure in the table, so
    # the "highest single figure" reading cannot point anywhere else.
    assert lang[1] == max(s[1] for s in stats.values()), stats
    # And the festival row must genuinely exceed 75 in two districts, which is
    # the distractor's true premise.
    fest = [num(rowdict(table, r)[c]) for r in table["rows"]
            for c in districts if rowdict(table, r)["Trait named as central"] == "Festival calendar"]
    assert sum(1 for v in fest if v > 75) == 2, fest
    return "at least 84 percent in every district"


CLAIMS = [
 ("shared practices, technologies, attitudes, and behaviors transmitted",
  "EK PSO-3.A.1 gives this definition word for word. It is deliberately broad, covering tools and beliefs alike, and its load-bearing words are shared and transmitted, which exclude an individual's private habit and anything inherited biologically."),

 ("inherited biologically or reinvented independently",
  "EK PSO-3.A.1 makes transmission part of the definition of culture. What passes between generations by teaching, imitation and participation is cultural, while what each individual arrives at unaided, or carries in their body, is not."),

 ("never told anyone about and no one else holds",
  "This is a NOT question and the key is the option failing EK PSO-3.A.1's requirement that culture be SHARED. A preference held by one person and communicated to nobody cannot be part of what a society holds in common and passes on."),

 ("illustrative rather than exhaustive",
  "EK PSO-3.A.2 writes 'include such things as', which introduces examples rather than defining by enumeration. Language, dress, kinship, music and burial practice are all culture traits although none of them appears in that sentence."),

 ("terraced hillside fields worked by extended families",
  "EK PSO-3.A.2 names land use among its examples of culture traits, and what makes land use cultural is that it records a society's decisions about how to work the land. Rainfall, elevation, geology and latitude are physical conditions those decisions respond to."),

 ("judged by the standards of the visitor's own",
  "EK PSO-3.A.3 names ethnocentrism and cultural relativism as two attitudes toward cultural difference. Applying one's own standards to another society's practice and finding it wanting is exactly what the first of the two names."),

 ("understood in the context of the culture it belongs to",
  "EK PSO-3.A.3 pairs cultural relativism with ethnocentrism as attitudes toward difference. Relativism is a method of understanding: it asks what a practice means inside the system it belongs to before any judgement is passed on it."),

 ("not a claim that every practice is equally desirable",
  "EK PSO-3.A.3 calls relativism an ATTITUDE toward cultural difference, which is a stance toward understanding rather than a moral verdict. Reading it as the stronger claim that nothing may be criticized is the most common misunderstanding of the term and is not what the CED says."),

 ("names technologies alongside practices, attitudes, and behaviors",
  "EK PSO-3.A.1 lists technologies as one of the four things culture comprises. A tool is knowledge made physical: it has to be learned, taught and maintained, which is what makes it shared and transmitted."),

 ("constrain what is possible without determining what a society chooses",
  "PSO-3's enduring understanding says cultural practices vary because of physical geography and available resources, which is a claim about influence rather than determination. Identical environments producing different traits is what shows the remaining variation is cultural."),

 ("each of which is a shared and transmitted element",
  "EK PSO-3.A.2 offers food preferences, architecture and land use as examples of culture traits, and every item in the catalogue is a shared practice passed between generations. That is what makes the list cultural rather than physical or demographic."),

 ("learned from other members of a society and passed on",
  "EK PSO-3.A.1 names attitudes alongside practices, technologies and behaviors as things a society shares and transmits. A belief about what is respectful, edible or shameful is taught in exactly the way a technique is taught."),

 ("Ethnocentrism operating through a food preference",
  "EK PSO-3.A.2 names food preferences among culture traits and EK PSO-3.A.3 names ethnocentrism as an attitude toward difference. Judging without inquiry is what separates the ethnocentric response from an ordinary personal dislike."),

 ("material form while the transmitted rules organizing them persist",
  "EK PSO-3.A.1 makes transmission the defining mechanism, and what is transmitted here is the rule rather than the material. EK PSO-3.A.2 names architecture as a culture trait, and the trait survives a change in the substance it is built from."),

 ("Courtyard houses built inward around a private central space",
  "EK PSO-3.A.2 names architecture among its examples of culture traits. A repeated building form embodies shared ideas about privacy, family and the relation between household and street, and it is taught from builder to builder."),

 ("Ethnocentrism and cultural relativism",
  "EK PSO-3.A.3 introduces these two as different attitudes toward cultural DIFFERENCE, which makes them stances an observer adopts. The other options name components of culture itself, which is a different kind of thing entirely."),

 ("imports the writer's own standards as though they were universal",
  "EK PSO-3.A.3 names ethnocentrism as an attitude toward difference, and an unstated criterion is what makes a comparison ethnocentric rather than merely evaluative. A method well adapted to one environment fails in another, so 'advanced' has to be advanced for something."),

 ("similar environments make different choices",
  "PSO-3 makes physical geography and available resources sources of cultural variation without making them the only ones, which is Unit 1's possibilism applied to culture. Both halves of the evidence are needed: constant environments with varying culture and varying environments with shared culture."),

 ("bundle of traits rather than a single indivisible thing",
  "EK PSO-3.A.1's definition is a list of components and EK PSO-3.A.2 speaks of traits in the plural, so a culture is an assemblage rather than a unit. Groups can therefore overlap on some traits and diverge on others, which is the ordinary situation rather than an anomaly."),

 ("ordinary objects and arrangements record it directly",
  "EK PSO-3.A.1 defines culture as shared practices, technologies, attitudes and behaviors rather than as high art or ceremony. What people do every day, and the things they make in order to do it, is where a definition that broad actually lives."),

 ("evaluates another culture by one's own standards; relativism seeks to understand",
  "EK PSO-3.A.3 presents the two as different attitudes toward cultural difference, and the difference lies in whose standards supply the frame of reference. Both are available to any observer, insider or outsider, so the distinction is about method rather than position."),

 ("treats one region's traits as the standard for all",
  "EK PSO-3.A.2 names food preferences among culture traits, and elevating one region's traits to the national standard applies one group's standards to everyone. That move is the ethnocentric structure operating inside a country rather than across a border."),

 ("would exclude the ordinary practices, tools, and attitudes",
  "EK PSO-3.A.1 names four different kinds of thing in a single sentence, which is a choice rather than an accident. Restricting culture to art or to belief would leave a geographer unable to discuss the field patterns, house forms and diets that make regions visibly different."),

 ("expected of newcomers, and taught to children",
  "EK PSO-3.A.1's definition turns on sharing and transmission, so the evidence must show both at once. Prevalence, an expectation applied to newcomers, and deliberate teaching are exactly the marks of a practice held in common rather than by an individual."),

 ("adopted in order to understand a practice before assessing it",
  "EK PSO-3.A.3 names relativism as an attitude toward cultural difference, and the sequence described is what that attitude amounts to in practice. Understanding first does not forbid judgement later; it forbids judgement in place of understanding."),

 ("exceeding 70 percent while one is mixed",
  "Recomputed from the table: every row sums to 100 percent, three regions record a staple above 70 percent, and the fourth has no category above 38. EK PSO-3.A.2 names food preferences among culture traits, and a trait varying between regions of one country is what the table shows.",
  q26_regional_staple),

 ("73 percent",
  "Recomputed from the table: each row sums to 100, and the two courtyard categories together fall only from 96 to 88 to 73 percent while the purely traditional form falls from 94 to 22. The verifier also confirms imported styles never reach a majority, so the inherited plan is what is being transmitted.",
  q27_plan_survives),

 ("58 percent sought the practice's meaning",
  "Recomputed from the table: both columns sum to 100, and the two groups are near-reversed on the pair of responses that matter -- 58 against 14 on asking what the practice means, and 17 against 63 on judging it inferior. EK PSO-3.A.3's two attitudes are exactly that pair.",
  q28_relativism_in_survey),

 ("ninetyfold difference in field size",
  "Recomputed from the table: soil type is identical and rainfall differs by about one percent, while mean field size differs by a factor of ninety. A near-constant physical variable cannot explain an outcome varying that widely, so the transmitted inheritance rule is what remains.",
  q29_culture_not_environment),

 ("at least 84 percent in every district",
  "Recomputed from the table: language runs 88, 91, 84 and 90 percent, giving it both the highest minimum and the smallest range of any row. The verifier confirms it also holds the single largest figure, and that the festival row genuinely exceeds three quarters in two districts, so that distractor is true in premise and wrong in inference.",
  q30_most_widely_shared),
]

hg_check.check(g3_1, CLAIMS, per_topic=30, n_choices=5)
