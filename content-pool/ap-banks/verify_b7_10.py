"""Key audit for AP BIOLOGY 7.10 Speciation.

One (anchor, claim) per item, in module order. The anchor must appear in the
keyed choice and in no distractor, so an off-by-one key stops matching; the
claim states what the key rests on, for a human to audit.

WHAT THE KEYS REST ON
---------------------
Every non-data item is keyed to a sentence the CED prints: EK 7.10.A.1
(speciation is reproductive isolation), EK 7.10.A.2 (the biological species
concept, for sexually reproducing organisms, requiring VIABLE and FERTILE
offspring), EK 7.10.B.1 (punctuated equilibrium against gradualism),
EK 7.10.B.2 (divergent evolution and adaptive radiation), EK 7.10.B.3
(convergent evolution), EK 7.10.C.1 (allopatry is geographic isolation,
sympatry is geographic overlap) and EK 7.10.C.2 (pre-zygotic and post-zygotic
mechanisms maintain isolation and prevent gene flow).

THE ONE PLACE THE CED IS SILENT, AND WHAT IS DONE ABOUT IT. EK 7.10.C.2 names
pre-zygotic and post-zygotic mechanisms and lists none. No key in this module
names a particular mechanism. The three data items about isolation are keyed
only on the division the two words themselves make -- before or after a zygote
forms -- and the check below reads that division out of the table's own
columns.

Items 20 to 26 carry a table, and every claim their keys make about it is
RECOMPUTED below from that table alone, through cg_check's header-and-label
accessors. cg_check.check fails a table question with no such callable.

NEGATIVE CONTROL. Moving any key, or changing any table cell the keys depend
on, makes this file raise; confirmed by running exactly that.
"""
import re

import cg_check as cg
import b7_10

QS = b7_10.QUESTIONS
T_CROSS = b7_10._T_CROSS
T_TRAITS = b7_10._T_TRAITS

MATE = "Individuals of the two populations mate"
ZYGOTE = "A zygote forms"
SURVIVE = "Offspring survive to adulthood"
FERTILE = "Offspring are fertile"
HABITAT = "Kind of habitat occupied"
FORM = "Body form"
ANCESTOR = "Most recent common ancestor"


def keyed(item):
    return item["choices"][item["ans"]]


def raw(table, row_label, header):
    j = [cg.normalize(h) for h in table["headers"]].index(cg.normalize(header))
    i = [cg.normalize(lab) for lab in cg.labels(table)].index(cg.normalize(row_label))
    return str(table["rows"][i][j])


def state(table, lab, header):
    """One cell as yes, no, or na. Any other wording is a defect, not a value."""
    v = cg.normalize(raw(table, lab, header))
    mapping = {"yes": "yes", "no": "no", "not applicable": "na"}
    assert v in mapping, f"{lab}/{header} reads {v!r}, not yes, no or not applicable"
    return mapping[v]


def _pairs_numbered(table):
    nums = [cg.num(lab) for lab in cg.labels(table)]
    assert nums == list(range(1, len(nums) + 1)), \
        f"pair labels are {cg.labels(table)}; they must be numbered from one in row order"


def _consistent(table):
    """A row must not record an outcome that a preceding column has ruled out."""
    for lab in cg.labels(table):
        m, z, s, f = (state(table, lab, h) for h in (MATE, ZYGOTE, SURVIVE, FERTILE))
        if m == "no":
            assert z == "no", f"{lab}: no mating but a zygote is recorded"
        if z == "no":
            assert s == "no", f"{lab}: no zygote but surviving offspring are recorded"
        if s == "no":
            assert f == "na", f"{lab}: no surviving offspring but a fertility result is recorded"


def q20(table, item):
    _pairs_numbered(table)
    _consistent(table)
    same_species = [lab for lab in cg.labels(table)
                    if all(state(table, lab, h) == "yes"
                           for h in (MATE, ZYGOTE, SURVIVE, FERTILE))]
    assert len(same_species) == 1, \
        f"exactly one row must meet the biological species concept; {same_species} do"
    assert cg.contains_phrase(keyed(item), same_species[0]), \
        f"q20 key {keyed(item)!r} but the row meeting the concept is {same_species[0]}"
    return f"only {same_species[0]} records yes in all four columns, so only it produces viable fertile offspring"


def q21(table, item):
    _pairs_numbered(table)
    _consistent(table)
    hits = [lab for lab in cg.labels(table)
            if state(table, lab, SURVIVE) == "yes" and state(table, lab, FERTILE) == "no"]
    assert len(hits) == 1, f"exactly one row must show surviving but infertile offspring; {hits} do"
    assert cg.contains_phrase(keyed(item), hits[0]), \
        f"q21 key {keyed(item)!r} but the row with surviving infertile offspring is {hits[0]}"
    return f"{hits[0]} is the only row recording offspring that survive to adulthood and are not fertile"


def q22(table, item):
    _pairs_numbered(table)
    _consistent(table)
    post = [lab for lab in cg.labels(table)
            if state(table, lab, ZYGOTE) == "yes"
            and (state(table, lab, SURVIVE) == "no" or state(table, lab, FERTILE) == "no")]
    assert len(post) == 2, f"the key names two post-zygotic rows; the table gives {post}"
    for lab in post:
        assert cg.contains_phrase(keyed(item), lab), \
            f"q22 key {keyed(item)!r} does not name the post-zygotic row {lab}"
    for lab in cg.labels(table):
        if lab not in post:
            assert not cg.contains_phrase(keyed(item), lab), \
                f"q22 key {keyed(item)!r} also names {lab}, which is not post-zygotic"
    return f"a zygote forms and the cross then fails only in {post}, so those are the post-zygotic rows"


def q23(table, item):
    _pairs_numbered(table)
    _consistent(table)
    pre = [lab for lab in cg.labels(table) if state(table, lab, MATE) == "no"]
    assert len(pre) == 1, f"exactly one row must show a barrier before a zygote can form; {pre} do"
    assert state(table, pre[0], ZYGOTE) == "no", "a row with no mating must record no zygote"
    assert cg.contains_phrase(keyed(item), pre[0]), \
        f"q23 key {keyed(item)!r} but the pre-zygotic row is {pre[0]}"
    return f"{pre[0]} is the only row in which no mating occurs, so no zygote forms for a later barrier to act on"


# The two rows must take OPPOSITE values in each descriptive column, drawn from
# a closed vocabulary. Matching a cell by substring instead would let extra text
# appended to a cell pass unnoticed -- an under-matching check, which this
# project has paid for repeatedly. Every cell is compared for equality after
# normalization, so any edit to a cell fails the check.
_VOCAB = {
    "Kind of habitat occupied": {"the same kind of habitat", "several different habitats"},
    "Body form": {"very similar", "very different"},
    "Most recent common ancestor": {"distant", "recent"},
}


def _vocabulary(table):
    for header, allowed in _VOCAB.items():
        seen = [cg.normalize(raw(table, lab, header)) for lab in cg.labels(table)]
        for v in seen:
            assert v in allowed, f"{header} holds {v!r}, which is not one of {sorted(allowed)}"
        assert set(seen) == allowed, \
            f"the two rows must take opposite values in {header}; they read {seen}"


def _group_with(table, habitat_word, form_word, ancestor_word):
    _vocabulary(table)
    wanted = {HABITAT: habitat_word, FORM: form_word, ANCESTOR: ancestor_word}
    hits = [lab for lab in cg.labels(table)
            if all(cg.normalize(raw(table, lab, h)) == cg.normalize(v)
                   for h, v in wanted.items())]
    assert len(hits) == 1, (
        f"exactly one row must read {habitat_word!r}, {form_word!r}, {ancestor_word!r}; {hits} do"
    )
    return hits[0]


def q24(table, item):
    # Convergence: one kind of habitat, similar form, distant ancestor.
    lab = _group_with(table, "the same kind of habitat", "very similar", "distant")
    assert cg.labels(table).index(lab) == 0, \
        f"the stem names the first group; the convergent pattern is in {lab}"
    assert cg.contains_phrase(keyed(item), "convergent evolution"), \
        f"q24 key {keyed(item)!r} does not name the process the first row's cells describe"
    return f"{lab} reads same habitat, very similar form, distant ancestor, which is the convergent pattern"


def q25(table, item):
    # Divergence: several habitats, very different form, recent ancestor.
    lab = _group_with(table, "several different habitats", "very different", "recent")
    assert cg.labels(table).index(lab) == 1, \
        f"the stem names the second group; the divergent pattern is in {lab}"
    assert cg.contains_phrase(keyed(item), "divergent evolution"), \
        f"q25 key {keyed(item)!r} does not name the process the second row's cells describe"
    return f"{lab} reads several habitats, very different form, recent ancestor, which is the divergent pattern"


def q26(table, item):
    _vocabulary(table)
    a, b = cg.labels(table)
    differing = [h for h in (HABITAT, FORM, ANCESTOR)
                 if cg.normalize(raw(table, a, h)) != cg.normalize(raw(table, b, h))]
    assert differing == [HABITAT, FORM, ANCESTOR], \
        f"all three descriptive columns must differ between the two groups; {differing} do"
    assert cg.contains_phrase(keyed(item), "common ancestor"), \
        f"q26 key {keyed(item)!r} does not name the ancestry column"
    return ("all three descriptive columns differ between the two groups, so the key must rest on "
            "which column decides the explanation rather than on which column varies")


TABLE_CHECKS = {20: q20, 21: q21, 22: q22, 23: q23, 24: q24, 25: q25, 26: q26}


CLAIMS = [
 ("two populations become reproductively isolated",
  "EK 7.10.A.1, near verbatim: speciation occurs when two populations become reproductively isolated from each other. Variation in phenotype and growth in numbers both occur within a single species and divide none."),
 ("viable, fertile offspring",
  "EK 7.10.A.2 defines a species as a group capable of interbreeding and exchanging genetic information to produce viable, fertile offspring. Both adjectives do work, so producing offspring of any kind is not sufficient."),
 ("Sexually reproducing organisms",
  "EK 7.10.A.2 introduces the biological species concept as a commonly used definition of a species FOR SEXUALLY REPRODUCING ORGANISMS. The definition turns on interbreeding, which an asexual lineage does not do."),
 ("separate species, because the offspring are not fertile",
  "EK 7.10.A.2 requires viable AND fertile offspring. Sterile offspring cannot pass genetic information to a further generation, so no exchange of genetic information occurs between the populations despite the mating."),
 ("rapidly after a long period of stasis",
  "EK 7.10.B.1 defines punctuated equilibrium as evolution occurring rapidly after a long period of stasis. The nearest distractor is the same statement's definition of gradualism."),
 ("slowly over hundreds of thousands or millions of years",
  "EK 7.10.B.1 defines gradualism as evolution occurring slowly over hundreds of thousands or millions of years. The nearest distractor is the same statement's definition of punctuated equilibrium."),
 ("Punctuated equilibrium",
  "EK 7.10.B.1's definition applied to a record: little change over a long run, then marked change over a short interval, is stasis followed by rapid evolution. The remaining options name a different rate or a different process."),
 ("Gradualism",
  "EK 7.10.B.1's definition applied to a record: small steady change across millions of years is evolution occurring slowly over that span, with no stasis interrupted by a rapid episode."),
 ("adaptation to new habitats results in phenotypic diversification",
  "EK 7.10.B.2, near verbatim, for divergent evolution. The nearest distractor is EK 7.10.B.3's definition of convergent evolution, which is the contrasting term."),
 ("During times of adaptive radiation",
  "EK 7.10.B.2 states that speciation rates can be especially rapid during times of adaptive radiation as new habitats become available. New habitat is what allows adaptation to diversify phenotypes in the same statement."),
 ("similar selective pressures result in similar phenotypic adaptations",
  "EK 7.10.B.3, near verbatim, for convergent evolution. The nearest distractor is EK 7.10.B.2's definition of divergent evolution."),
 ("Convergent evolution",
  "EK 7.10.B.3 defines convergent evolution as similar selective pressures producing similar adaptations in different populations or species. Separate continents and a distant relationship rule out inheritance of the trait from a recent shared ancestor."),
 ("Divergent evolution during an adaptive radiation",
  "EK 7.10.B.2 states both halves of the key: divergent evolution occurs when adaptation to new habitats results in phenotypic diversification, and speciation can be especially rapid during adaptive radiation as new habitats become available."),
 ("geographically isolated",
  "EK 7.10.C.1 states that allopatric speciation occurs in populations that are geographically isolated, and that sympatric speciation occurs in populations with geographic overlap. Geography is the whole of the distinction the statement draws."),
 ("have geographic overlap",
  "EK 7.10.C.1 states that sympatric speciation occurs in populations with geographic overlap. Populations that are already separate species are the outcome of speciation rather than its starting condition."),
 ("allopatric speciation",
  "EK 7.10.C.1 assigns speciation in geographically isolated populations to allopatry. A barrier that keeps the two groups from meeting is geographic isolation, whatever rate of change follows."),
 ("sympatric speciation",
  "EK 7.10.C.1 assigns speciation in populations with geographic overlap to sympatry. The two groups share the orchard, so their ranges overlap even though their use of the range differs."),
 ("maintain reproductive isolation and prevent gene flow",
  "EK 7.10.C.2, near verbatim: various pre-zygotic and post-zygotic mechanisms can maintain reproductive isolation and prevent gene flow between populations. Increasing the movement of alleles is the opposite of what the statement says."),
 ("before or after a zygote is formed",
  "EK 7.10.C.2 names the two categories and lists no particular mechanism, so the only division the framework itself supplies is the one the two names make, at the formation of the zygote. Geography, form and rate belong to EK 7.10.C.1, EK 7.10.B.3 and EK 7.10.B.1."),
 ("Pair 1",
  "EK 7.10.A.2 requires interbreeding producing viable, fertile offspring. The table check above confirms exactly one row records yes in all four columns and that no row records an outcome a previous column has ruled out."),
 ("Pair 2",
  "Skill 4.B, identifying specific data points. The table check above confirms exactly one row records offspring surviving to adulthood together with those offspring being infertile, which under EK 7.10.A.2 makes the populations separate species."),
 ("Pair 2 and Pair 3",
  "EK 7.10.C.2's two categories divide at the formation of the zygote. The table check above collects the rows in which a zygote forms and the cross then fails, confirms there are exactly two, and confirms the key names those two and no others."),
 ("Pair 4",
  "EK 7.10.C.2 names pre-zygotic mechanisms, which by the term's own division act before a zygote is formed. The table check above confirms exactly one row records no mating at all and that the same row records no zygote."),
 ("Convergent evolution",
  "EK 7.10.B.3 defines convergent evolution as similar selective pressures producing similar phenotypic adaptations in different populations or species. The table check above confirms the first row reads the same kind of habitat, very similar form and a distant common ancestor."),
 ("Divergent evolution",
  "EK 7.10.B.2 defines divergent evolution as adaptation to new habitats resulting in phenotypic diversification. The table check above confirms the second row reads several different habitats, very different form and a recent common ancestor."),
 ("how recently the members of the group shared a common ancestor",
  "EK 7.10.B.2 and EK 7.10.B.3 differ in what produces the pattern: recent shared ancestry with new habitats in one case, shared selective pressure without close relationship in the other. The table check confirms all three descriptive columns differ, so the key cannot rest on mere variation and must rest on which column settles the explanation."),
 ("had not become reproductively isolated",
  "EK 7.10.A.1 makes reproductive isolation the condition for speciation and EK 7.10.A.2 makes viable, fertile offspring the test of one species. Free interbreeding on contact shows the isolation was never completed; time spent apart is not itself the criterion."),
 ("Phenotypic diversification among the descendants",
  "EK 7.10.B.2 states that divergent evolution occurs when adaptation to new habitats results in phenotypic diversification, and that speciation rates can be especially rapid during adaptive radiation as new habitats become available. New varied habitat is exactly the scenario."),
 ("species that are not closely related",
  "EK 7.10.B.3 states that convergent evolution occurs when similar selective pressures result in similar phenotypic adaptations in different populations or species. Resemblance therefore admits two explanations, and the observation alone does not choose between them."),
 ("Allopatric speciation with geographic isolation",
  "EK 7.10.C.1 assigns geographic isolation to allopatry and geographic overlap to sympatry. Each remaining option reverses a pair of definitions drawn from EK 7.10.B.1, EK 7.10.B.2 and EK 7.10.B.3, or contradicts EK 7.10.A.1."),
]


# SCIENCE_BRIEF.md: Biology is exported untypeset, so a backslash macro or a
# dollar span would reach a student as literal characters, and a
# digit-hyphen-digit run reads as a subtraction. Explicit lookarounds, never \b.
_BANNED = [
    (re.compile(r"\\"), "a backslash: this bank carries no LaTeX"),
    (re.compile(r"\$"), "a dollar-delimited math span"),
    (re.compile(r"(?<![A-Za-z])\d+\s*-\s*\d+(?![A-Za-z])"), "a digit-hyphen-digit range"),
    (re.compile(r"\d\s*/\s*\d"), "a digit-slash-digit fraction"),
]

_FIGURE_TALK = re.compile(
    r"(?<![A-Za-z])(the (?:tree|cladogram|diagram|graph|figure|map) (?:shown|above|below)|"
    r"in the (?:tree|cladogram|diagram|figure|map) (?:shown|above|below)|"
    r"shown in the (?:tree|cladogram|diagram|figure|map))(?![A-Za-z])",
    re.IGNORECASE)


def style():
    hits = 0
    for i, item in enumerate(QS, 1):
        texts = [("stem", item["q"]), ("why", item["why"])]
        texts += [(f"choice {k}", c) for k, c in enumerate(item["choices"])]
        if item.get("table"):
            texts.append(("table", " | ".join(item["table"]["headers"])))
            texts += [("table", " | ".join(str(c) for c in r)) for r in item["table"]["rows"]]
        for where, text in texts:
            for pat, why_bad in _BANNED:
                m = pat.search(text)
                assert not m, f"q{i} {where} contains {m.group(0)!r}, {why_bad}"
                hits += 1
            m = _FIGURE_TALK.search(text)
            assert not m, (
                f"q{i} {where} says {m.group(0)!r}, promising a figure the bank cannot show"
            )
            hits += 1
    return hits


def main():
    n_style = style()
    cg.check(b7_10, CLAIMS, table_checks=TABLE_CHECKS)
    print(f"    {n_style} notation and figure-reference checks clean.")


main()
