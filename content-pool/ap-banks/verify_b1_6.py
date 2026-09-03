"""Key audit for AP BIOLOGY 1.6 Nucleic Acids.

One (anchor, claim) per item, in module order. The anchor is a distinctive
substring that must appear in the KEYED choice and in no distractor, so an
off-by-one key or a reordered choice list fails here instead of reaching a
student. ``claim`` states what the key rests on, for a human to audit.

The structural gate is the shared one in ``cg_check.py``. It cannot tell whether
the biology is right; that is gated by the CLAIMS text and by the
SCIENCE_BRIEF.md rule that every key must trace to a sentence in the CED.

WHAT THE KEYS REST ON
---------------------
EK 1.6.A.1 (information is encoded in sequences of nucleotide monomers; each
nucleotide has a five-carbon sugar, a phosphate and a nitrogenous base) carries
items 1, 2, 3, 4, 29 and 30.

EK 1.6.A.2 (the ends are defined by the 3 prime hydroxyl and 5 prime phosphates
of the sugar; nucleotides are added to the 3 prime end, forming covalent bonds
between nucleotides) carries items 5, 6, 7, 23 and 26, and half of 25. Its
exclusion statement carries item 14.

EK 1.6.A.3 (antiparallel double helix, opposite 5 prime to 3 prime orientation,
adenine with thymine and cytosine with guanine via hydrogen bonds, adenine with
uracil in RNA) carries items 8, 9, 10, 22, 24 and the other half of 25, and it
is the rule every base-composition item below is solved with.

EK 1.6.A.4 (deoxyribose against ribose, thymine against uracil, typically double
against typically single stranded) carries items 11, 12, 13, 15, 27 and 28.

THE COMPOSITION ARITHMETIC, stated once. In a double-stranded DNA molecule every
adenine is paired with a thymine and every cytosine with a guanine, so the
adenine and thymine percentages must be equal and so must the cytosine and
guanine percentages, and all four sum to 100. Items 16 to 21 are that one rule
applied to the tables, and every one is recomputed below.

ITEM 22 IS RECOMPUTED FROM THE STEM. The complementary strand is derived here by
complementing and reversing the module's own ``_SEQ_TOP``; the keyed choice is
checked against the derived string rather than taken on trust, and the
pair-without-reversing distractor is checked to be the un-reversed complement.

NOTATION: the CED prints 3' and 5'. Biology is exported as prose with no
typesetting, so the module writes "3 prime" and "5 prime" in words.

NEGATIVE CONTROL: ``python3 verify_b1_6.py --selftest`` corrupts a key, an
anchor, a table cell, the sequence and the notation on purpose and confirms each
check fails.
"""
import re
import sys

import cg_check as cg

_BANNED = [
    (re.compile(r"\\"), "a backslash: Biology is not typeset, so LaTeX would print raw"),
    (re.compile(r"(?<![A-Za-z])\d+\s?-\s?\d"), "a digit-hyphen-digit range: write 'to' instead"),
    (re.compile(r"\d\s?/\s?\d"), "a digit-slash-digit fraction: write it out in words"),
    (re.compile(r"\$"), "a dollar sign, which a converter reads as inline math"),
]


def style(module):
    for i, item in enumerate(module.QUESTIONS, 1):
        texts = [item["q"], item["why"]] + list(item["choices"])
        t = item.get("table")
        if t:
            texts += [str(h) for h in t["headers"]] + [str(c) for r in t["rows"] for c in r]
        for text in texts:
            for pat, msg in _BANNED:
                hit = pat.search(text)
                assert not hit, f"{module.TOPIC[0]} q{i}: {msg} -- {hit.group(0)!r} in {text[:70]!r}"
    print(f"OK  {module.TOPIC[0]} notation: no typeset markup in "
          f"{len(module.QUESTIONS)} questions.")


A = "Adenine (percentage of all bases)"
T = "Thymine (percentage of all bases)"
G = "Guanine (percentage of all bases)"
C = "Cytosine (percentage of all bases)"
U = "Uracil (percentage of all bases)"

# EK 1.6.A.3's pairing rule, written once and used by every composition check.
PAIR = {"A": "T", "T": "A", "G": "C", "C": "G"}


def _is_ds_dna(table, lab):
    return (cg.cell(table, lab, U) == 0
            and cg.cell(table, lab, A) == cg.cell(table, lab, T)
            and cg.cell(table, lab, G) == cg.cell(table, lab, C))


def q15(table, item):
    # how many samples carry each base at all
    present = {name: sum(1 for lab in cg.labels(table) if cg.cell(table, lab, name) > 0)
               for name in (A, T, G, C, U)}
    rare = sorted(name for name, n in present.items() if n == 1)
    assert rare == [U], f"bases present in exactly one sample: {rare}"
    assert present[T] > 1, "thymine must appear in more than one sample, or the item has two answers"
    return (f"counts of samples containing each base are "
            f"{ {k.split(' ')[0]: v for k, v in present.items()} }; only uracil appears once")


def q16(table, item):
    ds = sorted(lab for lab in cg.labels(table) if _is_ds_dna(table, lab))
    assert ds == ["Sample 1", "Sample 3"], f"rows consistent with double-stranded DNA: {ds}"
    for lab in ds:
        total = sum(cg.cell(table, lab, h) for h in (A, T, G, C, U))
        assert total == 100, f"{lab} percentages sum to {total}, not 100"
    return f"exactly two rows satisfy adenine equals thymine and guanine equals cytosine with no uracil: {ds}"


def q17(table, item):
    bad = [lab for lab in cg.labels(table)
           if cg.cell(table, lab, U) == 0 and not _is_ds_dna(table, lab)]
    assert bad == ["Sample 4"], f"uracil-free rows that fail the pairing rule: {bad}"
    assert cg.cell(table, bad[0], A) != cg.cell(table, bad[0], T), \
        "the keyed reason must be the adenine and thymine mismatch"
    return (f"{bad[0]} carries no uracil yet has adenine {cg.cell(table, bad[0], A):.0f} "
            f"against thymine {cg.cell(table, bad[0], T):.0f}, which EK 1.6.A.3 forbids in a double helix")


def q18(table, item):
    hits = [lab for lab in cg.labels(table)
            if cg.cell(table, lab, A) == 18 and cg.cell(table, lab, T) == 18]
    assert len(hits) == 1, f"the stem's 18 percent row matched {hits}"
    lab = hits[0]
    gc = cg.cell(table, lab, G) + cg.cell(table, lab, C)
    assert gc == 64, f"guanine plus cytosine recomputes to {gc}"
    assert cg.cell(table, lab, G) == 32, "the 32 distractor must be the guanine share alone"
    return f"100 minus 18 minus 18 is {gc:.0f}; guanine alone is 32, which is the distractor"


def _from_adenine(pct):
    """Percentages of T, G and C implied by an adenine share in a double helix."""
    return pct, (100 - 2 * pct) / 2, (100 - 2 * pct) / 2


def q19(table, item):
    hits = [lab for lab in cg.labels(table) if cg.cell(table, lab, A) == 20]
    assert len(hits) == 1, f"the stem's 20 percent adenine sample matched {hits}"
    t, g, c = _from_adenine(20)
    assert g == 30 and c == 30 and t == 20, f"recomputed T {t}, G {g}, C {c}"
    assert g + c == 60, "the 60 distractor must be the guanine and cytosine total"
    return f"adenine 20 forces thymine 20, leaving 60 shared equally, so guanine is {g:.0f}"


def q20(table, item):
    cyt = {lab: _from_adenine(cg.cell(table, lab, A))[2] for lab in cg.labels(table)}
    most = max(cyt, key=cyt.get)
    assert most == "DNA Y", f"the largest cytosine share is {most}"
    assert list(cyt.values()).count(cyt[most]) == 1, "the maximum must be unique"
    assert len(set(cyt.values())) > 1, "'all four the same' must be false"
    return f"cytosine shares recompute to {cyt}; the unique maximum is {most}"


def q21(table, item):
    hits = [lab for lab in cg.labels(table) if cg.cell(table, lab, A) == 25]
    assert len(hits) == 1, f"the stem's 25 percent adenine sample matched {hits}"
    t, g, c = _from_adenine(25)
    assert t == g == c == 25, f"recomputed T {t}, G {g}, C {c}, which are not all 25"
    return "adenine 25 forces thymine 25 and leaves 50 shared equally, so all four bases are 25 percent"


def check_sequence(module):
    """Item 22's complementary strand, recomputed rather than trusted."""
    top = module._SEQ_TOP.split()
    assert all(b in PAIR for b in top), f"unexpected base in {top}"
    paired = [PAIR[b] for b in top]              # pairs base by base
    complement = " ".join(reversed(paired))      # antiparallel: read back the other way
    assert complement == module._SEQ_COMPLEMENT, \
        f"recomputed {complement!r}, module stores {module._SEQ_COMPLEMENT!r}"
    item = module.QUESTIONS[21]
    assert module._SEQ_TOP in item["q"], "item 22's stem must carry the sequence being complemented"
    assert item["choices"][item["ans"]] == complement, \
        f"item 22's key is {item['choices'][item['ans']]!r}, not the recomputed {complement!r}"
    unreversed = " ".join(paired)
    assert unreversed in item["choices"] and unreversed != complement, \
        "the pair-without-reversing distractor must be present and must differ from the key"
    assert module._SEQ_TOP in item["choices"], "the unchanged-sequence distractor must be present"
    print(f"OK  {module.TOPIC[0]} q22: {module._SEQ_TOP} complements and reverses to "
          f"{complement}; {unreversed} is the un-reversed distractor.")


CLAIMS = [
 ("five-carbon sugar, a phosphate, and a nitrogenous base",
  "EK 1.6.A.1 lists exactly these three components for every nucleotide. The carboxyl group, amine group and variable R group belong to an amino acid under EK 1.7.A.2, and a fatty acid tail to a lipid under EK 1.5.A.1."),
 ("Adenine, thymine, guanine, cytosine and uracil",
  "EK 1.6.A.1 gives the nitrogenous base as adenine, thymine, guanine, cytosine, or uracil. Ribose and deoxyribose are the sugars in the same sentence and phosphate is the third component, so none of them is a base."),
 ("Deoxyribose and ribose",
  "EK 1.6.A.1 gives the five-carbon sugar as deoxyribose or ribose. Glucose, fructose, cellulose, glycogen and starch belong to EK 1.4.A.1's carbohydrate topic and are not nucleotide components."),
 ("sequence of its nucleotide monomers",
  "EK 1.6.A.1 states that biological information is encoded in sequences of nucleotide monomers. Counts, ratios and lengths are properties two different sequences can share, so none of them can carry the information."),
 ("3 prime hydroxyl and the 5 prime phosphate",
  "EK 1.6.A.2 states that the ends are defined by the 3 prime hydroxyl and 5 prime phosphates of the sugar in the nucleotide. The rejected option swaps which group sits at which end and moves both onto the base."),
 ("The 3 prime end",
  "EK 1.6.A.2 states that during nucleic acid synthesis nucleotides are added to the 3 prime end of the growing strand. One direction is given, not a choice of ends."),
 ("A covalent bond",
  "EK 1.6.A.2 states that adding nucleotides to the 3 prime end results in the formation of covalent bonds between nucleotides. Hydrogen bonds are what EK 1.6.A.3 uses across the two strands, and a peptide bond joins amino acids under EK 1.7.A.1."),
 ("antiparallel double helix",
  "EK 1.6.A.3 states that DNA is structured as an antiparallel double helix with two strands running in opposite 5 prime to 3 prime orientation. Antiparallel is the explicit denial of the parallel arrangement."),
 ("Adenine with thymine and cytosine with guanine, held by hydrogen bonds",
  "EK 1.6.A.3 pairs adenine with thymine and cytosine with guanine via hydrogen bonds. Adenine with uracil is the RNA pairing in the same statement, and the covalent bonds of EK 1.6.A.2 run along a strand rather than across a pair."),
 ("Uracil",
  "EK 1.6.A.3 ends by stating that in RNA adenine pairs with uracil. Thymine is adenine's DNA partner in the same statement, and EK 1.6.A.4 ii places thymine in DNA and uracil in RNA."),
 ("DNA contains deoxyribose and RNA contains ribose",
  "EK 1.6.A.4 i, near verbatim. The rejected option reverses the assignment and one substitutes a carbohydrate that EK 1.4.A.1 treats as a monosaccharide rather than a nucleotide sugar."),
 ("Thymine is in DNA and uracil is in RNA",
  "EK 1.6.A.4 ii states that DNA contains thymine and RNA contains uracil. Adenine, guanine and cytosine occur in both under EK 1.6.A.1, so they cannot distinguish the two."),
 ("DNA is typically double stranded and RNA is typically single stranded",
  "EK 1.6.A.4 iii, near verbatim. The framework says typically rather than always, which is why the options asserting a universal rule overstate it."),
 ("molecular structure of specific nucleotides",
  "The exclusion statement printed under EK 1.6.A.2 puts the molecular structure of specific nucleotides beyond the scope of the AP Exam. The rejected options restate content EK 1.6.A.1 to EK 1.6.A.4 do require."),
 ("Uracil",
  "Recomputed in q15 above: of the five base columns only uracil is nonzero in a single sample, and thymine is checked to appear in more than one so the item has one answer. EK 1.6.A.4 ii is why uracil is the scarce one -- it places thymine in DNA and uracil in RNA, and only one sample is a nucleic acid of the second kind."),
 ("Sample 1 and Sample 3",
  "Recomputed in q16 above. EK 1.6.A.3 pairs every adenine with a thymine and every cytosine with a guanine, so a double-stranded DNA must show equal adenine and thymine shares and equal cytosine and guanine shares; exactly two rows do, and both sum to 100."),
 ("Sample 4, because its adenine and thymine",
  "Recomputed in q17 above: exactly one uracil-free row breaks the pairing equality, and it breaks it on adenine against thymine. Holding more guanine than adenine, or the most adenine of any sample, violates nothing in EK 1.6.A.3."),
 ("64 percent",
  "Recomputed in q18 above: the four shares sum to 100, so removing adenine and thymine leaves the guanine and cytosine total. The check confirms the 32 distractor is the guanine share alone, which is half the total because EK 1.6.A.3 makes guanine and cytosine equal."),
 ("30 percent",
  "Recomputed in q19 above from EK 1.6.A.3: adenine 20 forces thymine 20, leaving 60 shared equally between guanine and cytosine. The check confirms the 60 distractor is that shared total reported as one base's share."),
 ("DNA Y",
  "Recomputed in q20 above: the cytosine share is half of what remains after twice the adenine share, so it is largest where adenine is smallest, and the table's smallest adenine value is unique."),
 ("Each of the other three bases also makes up 25 percent",
  "Recomputed in q21 above: adenine 25 forces thymine 25 under EK 1.6.A.3 and leaves 50 to be shared equally by guanine and cytosine. The pairing rule is what makes the other three determinable, contrary to the option saying they cannot be."),
 ("T G A C C T",
  "Recomputed in check_sequence above by complementing the stem's own sequence base by base under EK 1.6.A.3 and then reversing it, because EK 1.6.A.3 makes the two strands antiparallel. Pairing without reversing gives the T C C A G T distractor, and substituting uracil would make the partner RNA."),
 ("join the 3 prime end and are attached by covalent bonds",
  "EK 1.6.A.2 puts both halves in one sentence: nucleotides are added to the 3 prime end of the growing strand, resulting in the formation of covalent bonds between nucleotides. Hydrogen bonds belong to base pairing under EK 1.6.A.3."),
 ("From right to left in the 5 prime to 3 prime direction",
  "EK 1.6.A.3 states that the two strands run in opposite 5 prime to 3 prime orientation, so if one reads left to right in that direction the other must read right to left. The strands are complementary rather than identical."),
 ("Covalent bonds join neighbouring nucleotides along a strand",
  "EK 1.6.A.2 gives covalent bonds between nucleotides as the result of extension at the 3 prime end, and EK 1.6.A.3 gives hydrogen bonds as what holds the base pairs across the two strands. The two statements put the two bond types in two different places."),
 ("Strands already present will not be extended",
  "EK 1.6.A.2 makes addition at the 3 prime end the way a strand is extended, so blocking it blocks extension. The framework offers no alternative growing end, and neither EK 1.6.A.3's pairing nor EK 1.6.A.4 i's sugar depends on that step."),
 ("differ in one nitrogenous base and in how many strands",
  "EK 1.6.A.4 lists three differences, not one: the sugar in i, thymine against uracil in ii, and typically double against typically single stranded in iii. Both molecules carry a phosphate under EK 1.6.A.1 and are joined covalently under EK 1.6.A.2."),
 ("RNA",
  "All three observations are the RNA side of EK 1.6.A.4: ribose in i, uracil in ii, single stranded in iii. A protein, a polysaccharide and a phospholipid contain none of the nucleotide components EK 1.6.A.1 lists."),
 ("The phosphate",
  "EK 1.6.A.1 gives a phosphate as a component of every nucleotide, and EK 1.6.A.4 lists what differs between DNA and RNA: the sugar, one base, and typical strandedness. The phosphate appears on neither side of that list."),
 ("encoded in the order of the nucleotides",
  "EK 1.6.A.1 states that biological information is encoded in sequences of nucleotide monomers, and a sequence is an order rather than a count. Two different orders of the same nucleotides therefore share every percentage while encoding different information."),
]

TABLE_CHECKS = {15: q15, 16: q16, 17: q17, 18: q18, 19: q19, 20: q20, 21: q21}


def _selftest():
    import copy
    import types

    def must_fail(label, mutate, seq=False):
        mod = types.ModuleType("b1_6_mutant")
        mod.TOPIC = b1_6.TOPIC
        mod.QUESTIONS = copy.deepcopy(b1_6.QUESTIONS)
        mod._SEQ_TOP = b1_6._SEQ_TOP
        mod._SEQ_COMPLEMENT = b1_6._SEQ_COMPLEMENT
        claims = list(CLAIMS)
        try:
            mutate(mod, claims)
            style(mod)
            check_sequence(mod)
            cg.check(mod, claims, table_checks=TABLE_CHECKS)
        except AssertionError as exc:
            print(f"  control OK  {label}: {str(exc)[:90]}")
            return
        raise SystemExit(f"CONTROL FAILED: {label} did not raise")

    def break_pairing(mod, claims):
        mod.QUESTIONS[15]["table"] = dict(
            headers=b1_6._T_BASES["headers"],
            rows=[[r[0], r[1], ("24" if r[0] == "Sample 3" else r[2])] + r[3:]
                  for r in b1_6._T_BASES["rows"]])

    def wrong_complement(mod, claims):
        # key the un-reversed complement instead of the antiparallel one
        mod.QUESTIONS[21] = copy.deepcopy(b1_6.QUESTIONS[21])
        mod.QUESTIONS[21]["ans"] = mod.QUESTIONS[21]["choices"].index("T C C A G T")

    def stale_stored_complement(mod, claims):
        mod._SEQ_COMPLEMENT = "T G A C C A"

    print("negative controls:")
    must_fail("key moved off its anchor", lambda m, c: m.QUESTIONS[9].__setitem__("ans", 1))
    must_fail("anchor no longer in the keyed choice",
              lambda m, c: c.__setitem__(7, ("no such phrase", c[7][1])))
    must_fail("a base percentage altered so a row breaks the pairing rule", break_pairing)
    must_fail("the un-reversed complement keyed instead of the antiparallel one", wrong_complement)
    must_fail("the stored complement no longer matching the recomputed one", stale_stored_complement)
    must_fail("a backslash macro in a stem",
              lambda m, c: m.QUESTIONS[0].__setitem__("q", "Which \\textbf{three} components?"))
    print("all negative controls raised as required.")


import b1_6  # noqa: E402

if __name__ == "__main__" and "--selftest" in sys.argv:
    _selftest()

style(b1_6)
check_sequence(b1_6)
cg.check(b1_6, CLAIMS, table_checks=TABLE_CHECKS)
