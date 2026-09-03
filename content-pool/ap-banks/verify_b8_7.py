"""Key audit for AP BIOLOGY 8.7 Disruptions in Ecosystems.

One (anchor, claim) per item, in module order. The anchor must appear in the
keyed choice and in no distractor, so an off-by-one key stops matching; the
claim states what the key rests on, for a human to audit.

WHAT THE KEYS REST ON
---------------------
Every conceptual item is keyed to a sentence the CED prints: EK 8.7.A.1 (an
adaptation is a genetic variation favored by selection that manifests as a
trait providing an advantage in a particular environment), EK 8.7.A.2
(heterozygote advantage is higher relative fitness in the heterozygote than in
EITHER homozygote), EK 8.7.A.3 (mutations are NOT directed by specific
environmental pressures), EK 8.7.B.1 (intentional or unintentional
introduction; a new niche free of predators or competitors, or outcompeting
native species), EK 8.7.C.1 (human impact accelerates change at local AND
global levels, with exactly two named changes) and EK 8.7.D.1 (geological and
meteorological events affect habitat change and ecosystem distribution;
biogeographical studies illustrate them). The remaining items are keyed to
suggested skill 5.D, using data to evaluate a hypothesis or prediction,
including rejecting or FAILING TO REJECT the null hypothesis.

THE LIST OF TWO. EK 8.7.C.1 prints exactly two changes, biomagnification and
eutrophication. One item asks how many there are, and the check below counts
them from the module's own claims rather than letting a third be smuggled in.
The CED's illustrative examples are not assessable content, so no key depends
on recognising a named species or event.

Items 19 to 28 carry a table, and every number and every comparison their keys
make is RECOMPUTED below from that table alone.

NEGATIVE CONTROL. Moving any key, or changing any table cell the keys depend
on, makes this file raise; confirmed by running exactly that.
"""
import re

import cg_check as cg
import b8_7

QS = b8_7.QUESTIONS
T_HET = b8_7._T_HET
T_INVASIVE = b8_7._T_INVASIVE
T_BIOMAG = b8_7._T_BIOMAG

FITNESS = "Relative fitness measured in one hypothetical environment"
INTRODUCED = "Individuals of the introduced species counted per plot"
NATIVE = "Native species recorded per plot"
CONC = "Concentration of a persistent compound in tissue, in parts per million"

HET, HOM_DOM, HOM_REC = "Heterozygous", "Homozygous dominant", "Homozygous recessive"


def keyed(item):
    return item["choices"][item["ans"]]


def raw(table, row_label, header):
    j = [cg.normalize(h) for h in table["headers"]].index(cg.normalize(header))
    i = [cg.normalize(lab) for lab in cg.labels(table)].index(cg.normalize(row_label))
    return str(table["rows"][i][j])


def _fitness(table):
    for lab in (HET, HOM_DOM, HOM_REC):
        assert cg.normalize(lab) in [cg.normalize(x) for x in cg.labels(table)], \
            f"the table has no row {lab!r}; it holds {cg.labels(table)}"
    return {lab: cg.cell(table, lab, FITNESS) for lab in (HOM_DOM, HET, HOM_REC)}


def q19(table, item):
    f = _fitness(table)
    assert f[HET] > f[HOM_DOM] and f[HET] > f[HOM_REC], (
        f"the key says the data show heterozygote advantage; the fitness values are {f}"
    )
    assert f[HOM_DOM] != f[HOM_REC], \
        "a distractor turns on the two homozygotes differing; they must differ"
    return f"relative fitness runs {f}, with the heterozygote above both homozygotes"


def q20(table, item):
    f = _fitness(table)
    best = max(f, key=f.get)
    assert sorted(f.values())[-2] < f[best], f"the highest fitness must be unique; the values are {f}"
    assert cg.contains_phrase(keyed(item), best), \
        f"q20 key {keyed(item)!r} but the highest relative fitness belongs to the {best} genotype"
    return f"the fitness column reads {f} and its unique maximum is the {best} genotype"


def q21(table, item):
    f = _fitness(table)
    gap = f[HET] - f[HOM_DOM]
    other = f[HET] - f[HOM_REC]
    assert gap > 0, f"the stem asks by how much the heterozygote exceeds the homozygous dominant; {f}"
    assert keyed(item) == f"{gap:.2f}", \
        f"q21 key {keyed(item)!r} but {f[HET]} minus {f[HOM_DOM]} is {gap}"
    assert f"{other:.2f}" in item["choices"], \
        "the difference from the other homozygote should be offered as a distractor"
    return f"heterozygote {f[HET]} minus homozygous dominant {f[HOM_DOM]} is {gap:.2f}"


def _years_numbered(table):
    nums = [cg.num(lab) for lab in cg.labels(table)]
    assert nums == list(range(1, len(nums) + 1)), \
        f"year labels are {cg.labels(table)}; they must be numbered from one in row order"


def q22(table, item):
    _years_numbered(table)
    intro = cg.col(table, INTRODUCED)
    nat = cg.col(table, NATIVE)
    assert all(b > a for a, b in zip(intro, intro[1:])), \
        f"the key says the introduced species rose every year; the column reads {intro}"
    assert all(b < a for a, b in zip(nat, nat[1:])), \
        f"the key says native species fell every year; the column reads {nat}"
    return f"the introduced column {intro} rises at every step while the native column {nat} falls at every step"


def q23(table, item):
    _years_numbered(table)
    intro = cg.col(table, INTRODUCED)
    labs = cg.labels(table)
    best = max(range(len(intro)), key=lambda i: intro[i])
    assert sorted(intro)[-2] < intro[best], f"the largest count must be unique; the column is {intro}"
    assert cg.contains_phrase(keyed(item), labs[best]), \
        f"q23 key {keyed(item)!r} but the largest count is in {labs[best]}"
    nat = cg.col(table, NATIVE)
    assert min(range(len(nat)), key=lambda i: nat[i]) == best, \
        "the claim adds that the same year records the fewest native species; it does not"
    return f"{labs[best]} records the largest introduced count {int(intro[best])} and the fewest natives {int(nat[best])}"


def q24(table, item):
    _years_numbered(table)
    intro = cg.col(table, INTRODUCED)
    nat = cg.col(table, NATIVE)
    assert all(b > a for a, b in zip(intro, intro[1:])) and \
        all(b < a for a, b in zip(nat, nat[1:])), (
            f"the key rejects a null of no effect because the two columns move in opposite "
            f"directions; they read {intro} and {nat}"
        )
    assert nat[0] > nat[-1], "the native count must actually have fallen over the survey"
    return (f"native species fall {nat} while the introduced species rise {intro}, which is not what "
            "no effect predicts")


def q25(table, item):
    _years_numbered(table)
    intro = cg.col(table, INTRODUCED)
    nat = cg.col(table, NATIVE)
    assert intro[-1] > intro[0] and nat[-1] < nat[0], \
        "the key reads the pattern as the introduced species outcompeting natives; the columns must show that"
    return f"the introduced count rises from {int(intro[0])} to {int(intro[-1])} while natives fall from {int(nat[0])} to {int(nat[-1])}"


def q26(table, item):
    conc = cg.col(table, CONC)
    labs = cg.labels(table)
    best = max(range(len(conc)), key=lambda i: conc[i])
    assert sorted(conc)[-2] < conc[best], f"the highest concentration must be unique; the column is {conc}"
    assert cg.contains_phrase(keyed(item), labs[best]), \
        f"q26 key {keyed(item)!r} but the highest concentration is at {labs[best]}"
    assert best == len(conc) - 1, "the highest concentration should be the topmost level sampled"
    return f"the concentration column reads {conc} and its unique maximum is {labs[best]}"


def q27(table, item):
    conc = cg.col(table, CONC)
    ratios = [b / a for a, b in zip(conc, conc[1:])]
    assert len({round(r, 6) for r in ratios}) == 1, \
        f"a single factor can only be keyed if the column is a constant ladder; the ratios are {ratios}"
    r = ratios[0]
    assert abs(r - round(r)) < 1e-6, "the factor must be whole for a calculator-free item"
    assert keyed(item) == f"{int(round(r))} times", \
        f"q27 key {keyed(item)!r} but the constant factor up the column is {r}"
    return f"the concentration column reads {conc}, a constant factor of {int(round(r))} at every step"


def q28(table, item):
    conc = cg.col(table, CONC)
    assert all(b > a for a, b in zip(conc, conc[1:])), \
        f"biomagnification requires the concentration to rise with trophic level; the column is {conc}"
    labs = [cg.normalize(l) for l in cg.labels(table)]
    assert "producers" in labs[0], f"the first row should be the producers; it reads {labs[0]}"
    return f"the concentration rises at every trophic level from the producers upward, {conc}"


TABLE_CHECKS = {19: q19, 20: q20, 21: q21, 22: q22, 23: q23,
                24: q24, 25: q25, 26: q26, 27: q27, 28: q28}


CLAIMS = [
 ("genetic variation favored by selection that manifests as a trait",
  "EK 8.7.A.1 gives that definition in as many words. Every part does work: the variation must be genetic, it must be favored by selection, and the advantage it confers is relative to a particular environment."),
 ("requires a genetic variation, and this change is not one",
  "EK 8.7.A.1 defines an adaptation as a GENETIC VARIATION favored by selection that manifests as a trait. A change that is not heritable cannot be favored by selection across generations."),
 ("favored by selection and must manifest as a trait that provides an advantage",
  "EK 8.7.A.1 requires both: the variation is FAVORED BY SELECTION and it MANIFESTS AS A TRAIT providing an advantage in a particular environment. Frequency, dominance and recency form no part of the definition."),
 ("higher relative fitness than either homozygous genotype",
  "EK 8.7.A.2 states that heterozygote advantage is when the heterozygous genotype has a higher relative fitness than either the homozygous dominant or the homozygous recessive genotype. It is a claim about fitness, not about frequency."),
 ("exceeds that of both homozygotes",
  "EK 8.7.A.2 requires the heterozygote to exceed EITHER homozygote, which means both. The statement says nothing about how the two homozygotes compare with each other."),
 ("not directed by specific environmental pressures",
  "EK 8.7.A.3 states exactly that. Each distractor asserts some form of direction by need, which is what the sentence denies."),
 ("the pressure will cause the mutations needed to withstand it to arise",
  "EK 8.7.A.3 rules out a pressure producing the mutation that answers it. Selection acting on variation already present is a different claim, made by EK 8.7.A.1, and is not excluded."),
 ("selection can favour a variation that happens to be advantageous",
  "EK 8.7.A.3 denies direction of MUTATION by pressure and says nothing against selection, which EK 8.7.A.1 makes the process that favours advantageous variation. The four distractors all restate the direction the sentence rules out."),
 ("Intentionally or unintentionally",
  "EK 8.7.B.1 states that the INTENTIONAL OR UNINTENTIONAL introduction of an invasive species can allow it to exploit a new niche or outcompete native species. Both routes appear in the same sentence."),
 ("Exploit a new niche free of predators or competitors, or outcompete native species for resources",
  "EK 8.7.B.1 names exactly those two possibilities. Nothing in the statement suggests an increase in native species or a restoration of a damaged ecosystem."),
 ("Exploiting a new niche free of predators or competitors",
  "EK 8.7.B.1 names two routes and the scenario describes the first. Outcompeting native species would require the species to be taking resources from established populations, which the scenario rules out."),
 ("accelerates changes at local and global levels",
  "EK 8.7.C.1 states that human impact accelerates changes at local AND global levels. Both scales are named, so restricting the claim to one contradicts the sentence."),
 ("Biomagnification",
  "EK 8.7.C.1 names biomagnification and eutrophication as the two changes driven by human activities that can cause extinctions. Continental drift is a geological event under EK 8.7.D.1 and the rest are Unit 7 processes."),
 ("Eutrophication",
  "EK 8.7.C.1 lists exactly two such changes, and this is the second. Nitrogen fixation is a step of the nitrogen cycle in EK 8.2.B.6 and the remaining options are evolutionary processes from Unit 7."),
 ("Two",
  "EK 8.7.C.1 introduces its list with the words such as the following and prints two items, biomagnification and eutrophication. No key in this module adds a third."),
 ("Habitat change and ecosystem distribution",
  "EK 8.7.D.1 states that geological and meteorological events affect habitat change and ecosystem distribution. Directing mutation is what EK 8.7.A.3 explicitly denies of any environmental pressure."),
 ("Biogeographical studies",
  "EK 8.7.D.1 states that biogeographical studies illustrate these changes. Biogeography concerns where organisms are found, which is what habitat change and shifting distribution alter."),
 ("what would be observed if the proposed effect were absent",
  "Skill 5.D asks a student to use data to evaluate a hypothesis or prediction, including rejecting or failing to reject the null hypothesis. The null is the no-effect expectation the observations are judged against, which is why it is not the investigator's own prediction."),
 ("because the heterozygote's relative fitness exceeds that of both homozygotes",
  "EK 8.7.A.2 defines heterozygote advantage by that comparison. The table check above confirms the heterozygote exceeds both homozygotes and that the two homozygotes differ, which is what one distractor turns on."),
 ("The heterozygous genotype",
  "Skill 4.B, identifying a specific data point, applied to the comparison EK 8.7.A.2 turns on. The table check above confirms the largest relative fitness is unique and belongs to that genotype."),
 ("0.20",
  "Skill 5.A includes differences. The table check above recomputes the difference between the two rows the stem names, and confirms the difference from the other homozygote is present among the distractors."),
 ("rose in every year while the number of native species fell in every year",
  "Skill 4.B asks for the trend and the relationship between variables. The table check above confirms one column rises at every step and the other falls at every step."),
 ("Year 4",
  "Skill 4.B, identifying a specific data point. The table check above confirms the largest introduced count is unique, and separately that the same year records the fewest native species."),
 ("Rejecting the null hypothesis, because native species fell steadily",
  "Skill 5.D names rejecting or failing to reject the null hypothesis. The table check above confirms the two columns move in opposite directions across every interval, which is not what a null of no effect predicts; a rise in the introduced species alone would say nothing about the natives."),
 ("outcompeting native species for resources",
  "EK 8.7.B.1 gives two routes and the data fit the second: natives falling as the introduced species rises. The table check above confirms both directions. EK 8.7.A.3 rules out the option in which native species direct mutations."),
 ("Tertiary consumers",
  "Skill 4.B, identifying a specific data point. The table check above confirms the largest concentration is unique and belongs to the topmost trophic level the table samples."),
 ("10 times",
  "Skill 5.A includes ratios. The table check above divides each level's concentration by the level below it, confirms the factor is the same at every step before a single number may be keyed, and confirms it is whole."),
 ("Biomagnification",
  "EK 8.7.C.1 names biomagnification and eutrophication as changes driven by human activities that can cause extinctions. The table check above confirms the concentration rises at every step from the producers upward, which is what the first of the two names."),
 ("fail to reject the null hypothesis of no effect, which is not the same as proving there is none",
  "Skill 5.D names rejecting or FAILING TO REJECT the null hypothesis as the two outcomes. Failing to reject is a statement about what the data establish and leaves open that an effect exists but was not detected."),
 ("human activities such as biomagnification and eutrophication, and geological and meteorological events",
  "EK 8.7.B.1 supplies invasive species, EK 8.7.C.1 human impact with its two named changes, and EK 8.7.D.1 geological and meteorological events. EK 8.7.A.3 separately rules out any account in which the changes are directed by what organisms need."),
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
    r"(?<![A-Za-z])(the (?:graph|figure|diagram|chart|map|plot) (?:shown|above|below)|"
    r"in the (?:graph|figure|diagram|chart|map|plot) (?:shown|above|below)|"
    r"shown in the (?:graph|figure|diagram|chart|map|plot))(?![A-Za-z])",
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
    cg.check(b8_7, CLAIMS, table_checks=TABLE_CHECKS)
    print(f"    {n_style} notation and figure-reference checks clean.")


main()
