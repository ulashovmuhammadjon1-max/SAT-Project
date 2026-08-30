"""Key audit for AP HUMAN GEOGRAPHY 3.7 Diffusion of Religion and Language.

One (anchor, claim) per item, in module order; a third element recomputes the
item's arithmetic from its own table.

WHAT MAY BE CITED. IMP-3.B prints five essential-knowledge statements, the most
of any Unit 3 topic, and unusually for this course two of them ASSIGN REAL
RELIGIONS TO CATEGORIES BY NAME:

    IMP-3.B.1  Language families, languages, dialects, world religions, ethnic
               cultures, and gender roles diffuse from cultural hearths.
    IMP-3.B.2  Diffusion of language families, including Indo-European, and
               religious patterns and distributions can be visually represented
               on maps, in charts and toponyms, and in other representations.
    IMP-3.B.3  Religions have distinct places of origin from which they diffused
               to other locations through different processes. Practices and
               belief systems impacted how widespread the religion diffused.
    IMP-3.B.4  Universalizing religions, including Christianity, Islam,
               Buddhism, and Sikhism, are spread through expansion and
               relocation diffusion.
    IMP-3.B.5  Ethnic religions, including Hinduism and Judaism, are generally
               found near the hearth or spread through relocation diffusion.

The category assignments in B.4 and B.5 are therefore CITED rather than
inferred, which is why items 3, 4 and 18 can key to them directly. The
mechanism claims are cited too: universalizing religions get BOTH expansion and
relocation (item 5), ethnic religions get the hearth or relocation ONLY (item 6),
and IMP-3.B.3 supplies the reason -- belief systems decide which mechanisms are
open (items 7, 12, 19, 22).

WHAT THIS MODULE REFUSES TO ASSERT. Item 14 states the six hearths only at
region level -- eastern Mediterranean, Arabian Peninsula, South Asia -- because
that is where the fact is uncontested. Item 21 goes further and keys to the
DISPUTE itself: the Indo-European hearth is genuinely contested between an
Anatolian and a steppe origin, and the CED does not settle it. Keying to either
proposal would be exactly the guess SOCIAL_BRIEF.md forbids, so the key is that
the question is open. That is the single most important editorial decision in
this module.

IMP-3.B.2 names TOPONYMS among visual representations, which is easy to skip
past. Items 10, 17, 24, 25 and 28 use place names as evidence, and the reason
they work is durability: a name outlasts the population that coined it because
changing it takes deliberate effort.

The five table items (26-30) are the computational gate:

  26  the table carries an explicit Total row, so the recompute checks the
      component rows sum to it rather than double-counting
  27  conversion is 37 percent of one religion's growth and under one percent of
      the other's, while migration contributes almost the same absolute number
      to both -- the recompute asserts that second half, since it is what rules
      out a relocation explanation of the difference
  28  the older naming layer falls and the later one rises across four
      districts, crossing over in the second
  29  the largest branch holds under half the family's speakers
  30  exactly one region records zero conversions

REVIEW NOTE. All 30 keys were derived from the questions before this file was
written and none needed correcting.
"""
import hg_check
from hg_check import num, numcol, column, rowdict
import g3_7


def q26_universalizing_distribution(table):
    """Share outside the hearth, with the printed Total row checked not summed."""
    cols = ["Religion 1 (millions of adherents)", "Religion 2 (millions of adherents)"]
    parts = {c: {} for c in cols}
    totals = {}
    for row in table["rows"]:
        d = rowdict(table, row)
        label = d["Region"]
        for c in cols:
            if label == "Total":
                totals[c] = num(d[c])
            else:
                parts[c][label] = num(d[c])
    for c in cols:
        assert abs(sum(parts[c].values()) - totals[c]) < 1e-9, (c, parts[c], totals[c])
    r1, r2 = parts[cols[0]], parts[cols[1]]
    out1 = 100 * (totals[cols[0]] - r1["Hearth region"]) / totals[cols[0]]
    out2 = 100 * (totals[cols[1]] - r2["Hearth region"]) / totals[cols[1]]
    assert round(out1) == 85, out1
    assert out2 < 5, out2
    # The widely spread religion's largest single group must be off-continent.
    assert max(r1, key=r1.get) == "Other continents", r1
    # Total size must NOT be the criterion: assert the concentrated religion has
    # more adherents in its hearth than the spread one has in its own.
    assert r2["Hearth region"] > r1["Hearth region"], (r1, r2)
    return "85 percent of adherents outside the hearth region"


def q27_growth_by_source(table):
    """Conversion share separates the two; migration does not."""
    a, b = {}, {}
    for row in table["rows"]:
        d = rowdict(table, row)
        a[d["Source of new adherents over a decade"]] = num(d["Religion A"])
        b[d["Source of new adherents over a decade"]] = num(d["Religion B"])
    conv = "Conversion of previously unaffiliated people"
    mig = "Arrived through migration of adherents"
    share_a = a[conv] / sum(a.values())
    share_b = b[conv] / sum(b.values())
    assert share_a > 0.3 and share_b < 0.01, (share_a, share_b)
    assert a[conv] > 200 * b[conv], (a[conv], b[conv])
    # Migration must contribute a comparable ABSOLUTE amount to both, so it
    # cannot be what distinguishes them.
    assert 0.8 < a[mig] / b[mig] < 1.3, (a[mig], b[mig])
    return "26 million of its new adherents are converts"


def q28_toponym_gradient(table):
    """The older naming layer falls and the later one rises, crossing once."""
    old = numcol(table, "Place names of older linguistic origin")
    new = numcol(table, "Place names of later linguistic origin")
    assert all(old[i] > old[i + 1] for i in range(len(old) - 1)), old
    assert all(new[i] < new[i + 1] for i in range(len(new) - 1)), new
    crossings = [i for i in range(len(old)) if old[i] > new[i]]
    # The first two districts keep the older layer ahead, the last two reverse.
    assert crossings == [0, 1], (old, new)
    assert old[0] > 10 * new[0], (old[0], new[0])
    assert new[-1] > 20 * old[-1], (old[-1], new[-1])
    return "gradient from districts still dominated by the older naming layer"


def q29_largest_branch(table):
    """The largest branch holds well under half the family's speakers."""
    vals = {rowdict(table, r)["Branch"]: num(rowdict(table, r)["Speakers (millions)"])
            for r in table["rows"]}
    total = sum(vals.values())
    assert total == 3000, total
    biggest = max(vals.values())
    assert biggest == 1300, vals
    share = 100 * biggest / total
    assert 43 < share < 44, share
    assert share < 50, share
    return "1,300 of 3,000 million speakers"


def q30_relocation_only(table):
    """Exactly one region gained no adherents by conversion."""
    rows = {}
    for row in table["rows"]:
        d = rowdict(table, row)
        rows[d["Region"]] = (num(d["Adherents arriving as migrants"]),
                             num(d["Adherents gained by conversion"]),
                             num(d["Adherents today"]))
    no_conv = [r for r, v in rows.items() if v[1] == 0]
    assert no_conv == ["Region W"], rows
    # Its present community must be consistent with descent from the migrants.
    mig, _, today = rows["Region W"]
    assert today >= mig, rows["Region W"]
    assert today < 2 * mig, rows["Region W"]
    # Every other region must have gained more by conversion than by migration.
    for r, v in rows.items():
        if r != "Region W":
            assert v[1] > v[0], (r, v)
    return "every adherent traces to migration"


CLAIMS = [
 ("Each diffuses from a cultural hearth",
  "EK IMP-3.B.1 lists language families, languages, dialects, world religions, ethnic cultures and gender roles as things that diffuse from cultural hearths. Naming so varied a list under one mechanism is the point of the statement."),

 ("area in which a cultural trait originated",
  "EK IMP-3.B.1 makes cultural hearths the source areas from which these traits diffuse. Origin and present concentration are different things, and a trait can be almost absent from the region where it began."),

 ("Christianity, Islam, Buddhism, and Sikhism",
  "EK IMP-3.B.4 names exactly these four as universalizing religions. EK IMP-3.B.5 names Hinduism and Judaism as its ethnic examples, so any option mixing the two lists misassigns at least one religion the CED has assigned itself."),

 ("Hinduism and Judaism",
  "EK IMP-3.B.5 names Hinduism and Judaism as its examples of ethnic religions found near the hearth or spread through relocation diffusion. The other four religions in this topic appear in EK IMP-3.B.4's universalizing list."),

 ("Both expansion and relocation diffusion",
  "EK IMP-3.B.4 states that universalizing religions are spread through expansion AND relocation diffusion. Both channels are open because such a religion seeks adherents wherever it can reach them, whether by contact or by carriage."),

 ("Generally found near the hearth or spread through relocation diffusion",
  "This restates EK IMP-3.B.5 word for word. The qualifier GENERALLY matters: ethnic religions are found beyond the hearth wherever adherents have moved, but relocation rather than conversion is what brought them there."),

 ("tie it to a particular people, history, and place",
  "EK IMP-3.B.3 states that practices and belief systems impacted how widespread a religion diffused, and EK IMP-3.B.5 records the result for ethnic religions. Where membership is bound to descent and to a homeland, conversion is not how the faith grows."),

 ("faith travelled with the people who held it",
  "EK IMP-3.B.5 names relocation diffusion as how ethnic religions reach places beyond the hearth. The faith is present in the new location because its adherents are, which is precisely what relocation means."),

 ("spreads outward by contact while remaining at its source",
  "EK IMP-3.B.4 says universalizing religions spread through expansion as well as relocation diffusion. Conversion of a resident population is spread by contact from a source that keeps the faith, which is Topic 3.4's definition of expansion."),

 ("On maps, in charts and toponyms",
  "EK IMP-3.B.2 lists maps, charts, toponyms and other representations. Including toponyms among VISUAL representations is deliberate: a place name on a map is evidence about who named the place and in what language."),

 ("descended from a shared ancestral language",
  "EK IMP-3.B.1 names language families among the things that diffuse from cultural hearths and EK IMP-3.B.2 names Indo-European as an example. A family is defined by common descent, which is what makes it traceable to a hearth at all."),

 ("direct adherents to bring others in",
  "EK IMP-3.B.3 says practices and belief systems impacted how widespread a religion diffused, and EK IMP-3.B.4 and B.5 record the resulting difference in available mechanisms. A faith open to converts can grow without anyone moving, which a relocation-only faith cannot."),

 ("spread through expansion AND relocation diffusion",
  "EK IMP-3.B.4 names both mechanisms in a single sentence, and this case uses them in sequence: carriage by settlers is relocation and subsequent conversion is expansion. Naming both is what makes the answer complete."),

 ("Christianity and Judaism arose in the eastern Mediterranean",
  "EK IMP-3.B.3 states that religions have distinct places of origin, and these locations are standard uncontested course content stated at region level only. Two clusters of hearths, southwest Asia and South Asia, account for all six religions the CED names here."),

 ("generally found near the hearth or spread through relocation",
  "EK IMP-3.B.5 describes exactly this distribution: near the hearth plus communities formed where adherents moved. The absence of converted populations distant from the hearth is what separates it from a universalizing pattern."),

 ("where no substantial migration from the hearth ever occurred",
  "EK IMP-3.B.4 and B.5 differ on exactly this point, so the diagnostic has to separate carriage from conversion. Adherents where nobody migrated from the hearth can only have been converted, which relocation alone cannot account for."),

 ("speakers of that language once occupied the region",
  "EK IMP-3.B.2 names toponyms among the representations in which linguistic diffusion can be read. Names are durable because changing them takes deliberate effort, so they outlast the population that coined them and record an earlier layer."),

 ("Sikhism to universalizing and Judaism to ethnic",
  "EK IMP-3.B.4 names Sikhism among the universalizing religions and EK IMP-3.B.5 names Judaism among the ethnic ones. Every other pairing reverses at least one of the CED's own assignments, which are stated by name rather than inferred."),

 ("determines which diffusion mechanisms are available to it",
  "EK IMP-3.B.3 makes the content of a faith a cause of its geographic extent, which is an unusually specific claim for the CED to make. Whether a religion instructs adherents to seek converts decides whether expansion diffusion is open to it at all."),

 ("table of adherents by world region at three dates",
  "EK IMP-3.B.2 names maps, charts and toponyms as separate kinds of representation. A chart holds quantities and changes over time that a shaded map cannot show, which is why the statement lists more than one form."),

 ("genuinely disputed among scholars",
  "EK IMP-3.B.2 names Indo-European as its example of a language family whose diffusion can be represented, and EK IMP-3.B.1 places hearths behind such diffusion, but the CED does not locate this hearth. Keying to either the Anatolian or the steppe proposal would be a guess, so the key is that the question is open."),

 ("whether adherents should seek converts",
  "EK IMP-3.B.3 says practices and belief systems impacted how widespread a religion diffused, which denies that proximity of hearths determines extent. Holding geography roughly constant leaves the content of the faiths as the explanatory difference."),

 ("Gender roles and ethnic cultures",
  "EK IMP-3.B.1's list is language families, languages, dialects, world religions, ethnic cultures AND gender roles. Every distractor names physical features, which do not diffuse from hearths because nobody transmits them."),

 ("naming follows the arrival of the people",
  "EK IMP-3.B.2 names toponyms among the representations of religious and linguistic diffusion. Names concentrated along corridors are the diffusion channel made visible, since names are given where the naming population actually went."),

 ("same hearth-and-diffusion account applies at a finer scale",
  "EK IMP-3.B.1 lists language families, languages and dialects together, which places one process at three scales. A regional pronunciation spreads from where it arose exactly as a language family does, only over a smaller area."),

 ("85 percent of adherents outside the hearth region",
  "Recomputed from the table: one religion holds 310 million of 2,010 in its hearth, leaving 85 percent elsewhere with the largest single group on other continents, while the other holds over 95 percent at home. The verifier checks the component rows against the printed total and confirms that total size is not the criterion.",
  q26_universalizing_distribution),

 ("26 million of its new adherents are converts",
  "Recomputed from the table: conversion supplies 37 percent of one religion's growth and under one percent of the other's, a difference of more than two hundredfold in absolute terms. The verifier also confirms migration contributes almost the same absolute number to both, which is what rules out a relocation explanation of the gap.",
  q27_growth_by_source),

 ("gradient from districts still dominated by the older naming layer",
  "Recomputed from the table: the older naming layer falls from 184 to 9 across the four districts while the later layer rises from 12 to 213, crossing over in the second. EK IMP-3.B.2 names toponyms among the representations of linguistic diffusion, and a gradient like this is a diffusion front made visible.",
  q28_toponym_gradient),

 ("1,300 of 3,000 million speakers",
  "Recomputed from the table: the five rows total 3,000 million speakers and the largest branch holds 1,300, which is 43.3 percent. A branch holding well under half of a family's speakers is why a family cannot be described by its largest branch alone.",
  q29_largest_branch),

 ("every adherent traces to migration",
  "Recomputed from the table: exactly one region records zero adherents gained by conversion, and its present community is consistent with descent from the migrants who arrived. The verifier also confirms every other region gained more by conversion than by migration, so only one case is relocation alone.",
  q30_relocation_only),
]

hg_check.check(g3_7, CLAIMS, per_topic=30, n_choices=5)
