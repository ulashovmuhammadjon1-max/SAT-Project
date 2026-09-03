"""Key audit for AP BIOLOGY 7.7 Common Ancestry.

One (anchor, claim) per item, in module order. The anchor must appear in the
keyed choice and in no distractor, so an off-by-one key stops matching; the
claim states what the key rests on, for a human to audit.

WHAT THE KEYS REST ON, AND THE PROBLEM THIS TOPIC POSES
-------------------------------------------------------
7.7 has ONE essential knowledge statement, EK 7.7.A.1, listing three features
as evidence of common ancestry of all eukaryotes. Thirty questions on one
sentence is how the Comparative Government bank produced ten cross-topic
repeats, and SOCIAL_DEDUPE.md records the fix: chain the thin statement to
another the CED prints, so each item asks something neither topic can ask
alone. Every claim below therefore cites 7.7.A.1 plus one of

    2.9.A.1, 2.10.A.2, 2.10.A.3   what a membrane-bound organelle is and does
    6.1.A.1 i and ii, 6.1.A.2     circular against linear chromosomes; plasmids
    6.3.A.4 iii                   introns excised, exons spliced and retained

and every claim states which. Endosymbiosis (EK 2.10.A.1) is keyed NOWHERE in
this module: b2_10 asks it eight ways, and a ninth would be the repeat.

The framework's hedges are preserved. It writes that prokaryotes TYPICALLY lack
membrane-bound organelles and TYPICALLY have circular chromosomes, so no key
here states an absolute in their place, and no key says anything about introns
in prokaryotes, on which the CED is silent.

Items 18 to 22 carry a table and every numeric or structural claim their keys
make is RECOMPUTED below from that table alone, through cg_check's
header-and-label accessors. cg_check.check fails a table question with no such
callable.

NEGATIVE CONTROL. Moving any key or changing any table cell that the keys
depend on makes this file raise; confirmed by running exactly that.
"""
import re

import cg_check as cg
import b7_7

QS = b7_7.QUESTIONS
T_SURVEY = b7_7._T_SURVEY
T_CHROM = b7_7._T_CHROM

EXAMINED = "Number of species examined"
FEATURE_COLS = ["Number found to have membrane-bound organelles",
                "Number found to have linear chromosomes",
                "Number found to have genes that contain introns"]
FORM = "Form of the main chromosome"
N_CHROM = "Number of main chromosomes"


def keyed(item):
    return item["choices"][item["ans"]]


def raw(table, row_label, header):
    j = [cg.normalize(h) for h in table["headers"]].index(cg.normalize(header))
    i = [cg.normalize(lab) for lab in cg.labels(table)].index(cg.normalize(row_label))
    return str(table["rows"][i][j])


def _groups_numbered(table):
    """Group labels must read Group 1 upward in written order; the stem and the
    key for the percentage item both refer to a group by its number."""
    nums = [cg.num(lab) for lab in cg.labels(table)]
    assert nums == list(range(1, len(nums) + 1)), \
        f"group labels are {cg.labels(table)}; they must be numbered from one in row order"


def q18(table, item):
    _groups_numbered(table)
    total = sum(cg.col(table, EXAMINED))
    assert total == int(total), "a count of species must be a whole number"
    assert keyed(item) == str(int(total)), \
        f"q18 key {keyed(item)!r} but the examined column sums to {int(total)}"
    return f"the examined column reads {cg.col(table, EXAMINED)} and sums to {int(total)}"


def q19(table, item):
    _groups_numbered(table)
    named = [lab for lab in cg.labels(table) if cg.contains_phrase(item["q"], lab)]
    assert len(named) == 1, f"the stem names rows {named}; it must name exactly one"
    total = sum(cg.col(table, EXAMINED))
    pct = cg.cell(table, named[0], EXAMINED) / total * 100
    assert abs(pct - round(pct)) < 1e-9, "the percentage must be whole for a calculator-free item"
    assert keyed(item) == f"{int(round(pct))} percent", \
        f"q19 key {keyed(item)!r} but {named[0]} is {pct} percent of {int(total)}"
    return f"{named[0]} holds {int(cg.cell(table, named[0], EXAMINED))} of {int(total)} species, {int(round(pct))} percent"


def q20(table, item):
    _groups_numbered(table)
    for lab in cg.labels(table):
        n = cg.cell(table, lab, EXAMINED)
        for h in FEATURE_COLS:
            assert cg.cell(table, lab, h) == n, (
                f"{lab}: {h} reads {cg.cell(table, lab, h)} but {int(n)} species were examined, "
                "so the key's claim that every species carried every feature fails"
            )
    return (f"in all {len(cg.labels(table))} rows each of the {len(FEATURE_COLS)} feature columns "
            f"equals the number of species examined, so no species lacked any feature")


def q21(table, item):
    forms = {raw(table, lab, FORM) for lab in cg.labels(table)}
    assert len(forms) == 1, f"the key rests on a shared form; the column holds {forms}"
    assert cg.contains_phrase(keyed(item), forms.pop()), \
        f"q21 key {keyed(item)!r} does not name the form the column actually reports"
    counts = cg.col(table, N_CHROM)
    assert len(set(counts)) > 1, \
        f"the key contrasts a shared form with a varying number; the counts are {counts}"
    return f"the form column is constant while the number column varies across {counts}"


def q22(table, item):
    counts = cg.col(table, N_CHROM)
    assert len(set(counts)) == len(counts), \
        f"the key says the number differs among the cells; the counts are {counts}"
    forms = {raw(table, lab, FORM) for lab in cg.labels(table)}
    assert len(forms) == 1, "the contrast requires the other column to be constant"
    return f"the chromosome counts {counts} are all different while the form column is constant"


TABLE_CHECKS = {18: q18, 19: q19, 20: q20, 21: q21, 22: q22}


CLAIMS = [
 ("genes that contain introns",
  "EK 7.7.A.1 names membrane-bound organelles, linear chromosomes and genes that contain introns. A plasma membrane and ribosomes belong to every form of life, and circular chromosomes and plasmids are what EK 6.1.A.1 and EK 6.1.A.2 describe instead."),
 ("cellular and molecular levels",
  "Learning objective 7.7.A specifies structural and functional evidence on cellular and molecular levels. An organelle sits at the first level and a gene's introns at the second, which is why the objective names both."),
 ("descend from a common ancestor",
  "EK 7.7.A.1 states that this structural and functional evidence indicates common ancestry of all eukaryotes. One inheritance accounts for a feature being present in every descendant, which repeated independent origin does not."),
 ("Membrane-bound organelles",
  "EK 7.7.A.1 lists membrane-bound organelles first, and EK 2.10.A.3 describes eukaryotic cells as maintaining internal membranes that partition the cell into specialized regions, which is what the observation reports."),
 ("marks the eukaryotes off as a group",
  "EK 2.10.A.2 states that prokaryotes typically lack internal membrane-bound organelles BUT have internal regions with specialized structures and functions, so no option denying prokaryotes internal organization can stand. Evidence about a group must be general within it and not general outside it."),
 ("linear form of the chromosome is one of the features",
  "EK 7.7.A.1 names linear chromosomes as the second line of evidence, and EK 6.1.A.1 supplies the contrast that prokaryotes typically have circular chromosomes while eukaryotes typically have multiple linear ones. The framework names the form and not the number."),
 ("which is shared, and not the number",
  "EK 6.1.A.1 describes eukaryotes as typically having MULTIPLE linear chromosomes without fixing a count, and EK 7.7.A.1 names the linear form. A feature that varies across the group cannot be the shared feature that evidence of shared ancestry rests on."),
 ("further shared molecular feature",
  "EK 6.1.A.1 states that eukaryotic linear chromosomes are comprised of DNA and condensed using histones and associated proteins, so this is a molecular property of the very structure EK 7.7.A.1 names. It adds to that line of evidence rather than displacing it."),
 ("introns",
  "EK 6.3.A.4 states that the excision of introns, along with the splicing and retention of exons, generates the mature mRNA. The removed stretches are therefore introns, and EK 7.7.A.1 names genes containing them as the third line of evidence."),
 ("a feature general to a group is explained by inheritance",
  "EK 7.7.A.1 asserts something about ALL eukaryotes, which is a claim about a group rather than about a species. Generality within a group is what an inherited ancestral feature produces, which is what makes the observation evidence of ancestry."),
 ("in which none of the three features is present",
  "EK 7.7.A.1 is a claim about all eukaryotes, so only a eukaryote lacking the features bears on it. EK 2.10.A.2 already grants prokaryotes internal specialized regions and EK 6.1.A.2 already grants both groups plasmids, so neither observation surprises the framework."),
 ("investigate the loss as a change within the lineage",
  "EK 7.7.A.1 offers three lines of evidence rather than one, so losing a single feature leaves two standing. Treating one observation as decisive against converging evidence is the error the other options share."),
 ("found in the same pond",
  "EK 7.7.A.1 names structural and functional features of the cell and of its molecules. Where two species happen to live can be true of wholly unrelated organisms, so it is not evidence of the kind this objective describes."),
 ("plasma membrane surrounding the cell",
  "EK 7.7.A.1 names three features, and a plasma membrane is not among them. It bounds cells of every kind, so it separates no group from another and could not serve as evidence about eukaryotes specifically."),
 ("cannot distinguish eukaryotes from anything else",
  "EK 7.7.A.1's three features are offered as evidence about eukaryotes as a group, which requires that they mark that group off. A universal feature is compatible with every hypothesis about eukaryotes and so discriminates among none."),
 ("compartmentalizing metabolic processes inside it",
  "EK 2.9.A.1 states that membranes and membrane-bound organelles in eukaryotic cells compartmentalize intracellular metabolic processes and specific enzymatic reactions. That is the function of the structure EK 7.7.A.1 names, which is what the objective's phrase structural AND functional requires."),
 ("cellular feature and genes containing introns a molecular one",
  "Learning objective 7.7.A asks for evidence on cellular and molecular levels. An organelle is a component of a cell and an intron a stretch of sequence within a gene, so the two features sit at those two levels."),
 ("100",
  "Skill 4.B, identifying and combining specific data points. The table check above sums the examined column across the three rows, which is the denominator any statement about generality needs."),
 ("25 percent",
  "Skill 5.A includes percentages. The table check above locates the row the stem names, divides its species count by the total across all rows, and confirms the result is whole."),
 ("Every species examined carried all three features",
  "EK 7.7.A.1 makes the three features evidence of common ancestry of all eukaryotes. The table check above confirms every feature column equals the examined column in every row; the survey covers no prokaryotes and carries no dates, so neither of those conclusions is available."),
 ("linear form shared by the chromosomes of all three cells",
  "EK 7.7.A.1 names linear chromosomes. The table check above confirms the form column is constant across the three cells while the number column varies, and only a constant column reports a shared feature that inheritance would explain."),
 ("not the feature the framework names as evidence",
  "EK 6.1.A.1 describes eukaryotes as typically having multiple linear chromosomes without fixing a number, and EK 7.7.A.1 names the form. The table check above confirms the counts are all different, so that column cannot carry the shared-ancestry claim."),
 ("membrane-bound organelles, linear chromosomes, and genes containing introns",
  "EK 7.7.A.1 names those three features as the structural and functional evidence indicating common ancestry of eukaryotes, so looking for them is looking for the evidence the objective specifies. Growth rate, sample depth, abundance and oxygen tolerance are ecological or physiological facts."),
 ("already grants prokaryotes such regions",
  "EK 2.10.A.2 says in one sentence that prokaryotes typically lack internal membrane-bound organelles BUT have internal regions with specialized structures and functions. The observation is therefore part of the framework's account rather than a counterexample to it."),
 ("found in both groups does not mark",
  "EK 6.1.A.2 states that prokaryotes and eukaryotes can both contain plasmids, extra-chromosomal circular molecules of DNA. EK 7.7.A.1's evidence is about eukaryotes specifically, and a feature shared with the other group cannot serve that purpose."),
 ("the third remains to be examined",
  "EK 7.7.A.1 lists three features as evidence, not as a checklist all of which must be confirmed before any inference. Two observed features are evidence, and an unexamined third is missing data rather than evidence of absence."),
 ("open to test by further observation",
  "EK 7.7.A.1 says the structural and functional evidence INDICATES common ancestry, which is the language of a supported claim rather than of a definition. A claim resting on observations is one further observations can bear on."),
 ("shows the organization the framework attributes to eukaryotic cells",
  "EK 2.10.A.3 states that eukaryotic cells maintain internal membranes partitioning the cell into specialized regions, and EK 7.7.A.1 makes membrane-bound organelles the first line of evidence. Neither statement licenses a claim about age, reproductive rate or direct descent."),
 ("more simply explained by inheritance",
  "EK 2.9.A.1 confirms that eukaryotic cells compartmentalize metabolic processes, so the premise stands and only the conclusion fails. EK 7.7.A.1 treats the feature as evidence of common ancestry precisely because one inheritance accounts for its presence throughout the group."),
 ("Three independent lines of structural and functional evidence",
  "EK 7.7.A.1 lists three separate features under one claim of common ancestry of all eukaryotes. They concern different components of the cell, and the statement makes no claim about dates or about the features of all living cells."),
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
    return hits


def main():
    n_style = style()
    cg.check(b7_7, CLAIMS, table_checks=TABLE_CHECKS)
    print(f"    {n_style} notation checks clean (no LaTeX, no ranges, no slash fractions).")


main()
