"""Key audit for AP BIOLOGY 8.6 Biodiversity.

One (anchor, claim) per item, in module order. The anchor must appear in the
keyed choice and in no distractor, so an off-by-one key stops matching; the
claim states what the key rests on, for a human to audit.

WHAT THE KEYS REST ON
---------------------
Every conceptual item is keyed to one of this topic's three statements:
EK 8.6.A.1 (natural AND artificial ecosystems with fewer component parts and
little diversity among the parts are OFTEN less resilient), EK 8.6.A.2
(keystone species, producers, and essential abiotic and biotic factors
contribute to maintaining diversity) and EK 8.6.B.1 (the effects of keystone
species are DISPROPORTIONATE relative to their abundance, and the ecosystem
OFTEN collapses when they are removed), or to suggested skill 6.E, predicting
the causes or effects of a disruption to one or more components.

THE HEDGES. Both statements say OFTEN. Three items turn on that word and no key
anywhere in this module converts either into a certainty.

Items 20 to 29 carry a table, and every number and every comparison their keys
make is RECOMPUTED below from that table alone. The keystone table is checked to
run abundance and effect in OPPOSITE directions before any key resting on the
word disproportionate is accepted -- otherwise the item would be testing nothing.

NEGATIVE CONTROL. Moving any key, or changing any table cell the keys depend
on, makes this file raise; confirmed by running exactly that.
"""
import re

import cg_check as cg
import b8_6

QS = b8_6.QUESTIONS
T_ECO = b8_6._T_ECO
T_KEYSTONE = b8_6._T_KEYSTONE

N_SPECIES = "Number of component species present"
DIVERSITY = "Diversity among the component parts"
LOSS = "Percentage change in productivity after the same drought"
SHARE = "Percentage of the community's total biomass held by this species"
AFFECTED = "Number of other species whose abundance changed by more than half after the removal"

NUMBER_WORDS = ["Zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven",
                "Eight", "Nine", "Ten"]
_DIVERSITY_WORDS = {"low": 0, "moderate": 1, "high": 2}


def keyed(item):
    return item["choices"][item["ans"]]


def raw(table, row_label, header):
    j = [cg.normalize(h) for h in table["headers"]].index(cg.normalize(header))
    i = [cg.normalize(lab) for lab in cg.labels(table)].index(cg.normalize(row_label))
    return str(table["rows"][i][j])


def _eco(table):
    """Species counts, ranked diversity words and losses, checked for consistency."""
    nums = [cg.num(lab) for lab in cg.labels(table)]
    assert nums == list(range(1, len(nums) + 1)), \
        f"ecosystem labels are {cg.labels(table)}; they must be numbered from one in row order"
    counts = cg.col(table, N_SPECIES)
    losses = cg.col(table, LOSS)
    words = [cg.normalize(raw(table, lab, DIVERSITY)) for lab in cg.labels(table)]
    for w in words:
        assert w in _DIVERSITY_WORDS, f"the diversity column reads {w!r}, not one of {sorted(_DIVERSITY_WORDS)}"
    ranks = [_DIVERSITY_WORDS[w] for w in words]
    assert len(set(counts)) == len(counts), f"species counts must be distinct; they read {counts}"
    assert sorted(range(len(counts)), key=lambda i: counts[i]) == \
        sorted(range(len(ranks)), key=lambda i: ranks[i]), \
        f"the species counts {counts} and the diversity words {words} must rank the rows the same way"
    assert all(v < 0 for v in losses), f"every row must record a loss of productivity; {losses}"
    return counts, ranks, losses


def q20(table, item):
    counts, ranks, losses = _eco(table)
    order = sorted(range(len(counts)), key=lambda i: counts[i])
    by_count = [losses[i] for i in order]
    assert all(b > a for a, b in zip(by_count, by_count[1:])), (
        f"the key says richer ecosystems lost less; ordered by species count the losses are {by_count}"
    )
    return f"ordering the rows by species count {sorted(counts)} gives losses {by_count}, shrinking at every step"


def q21(table, item):
    counts, ranks, losses = _eco(table)
    worst = min(range(len(losses)), key=lambda i: losses[i])
    assert counts[worst] == min(counts) and ranks[worst] == min(ranks), (
        "the key names the row that is lowest on species count, lowest on diversity and largest on loss; "
        f"counts {counts}, ranks {ranks}, losses {losses}"
    )
    assert cg.contains_phrase(keyed(item), cg.labels(table)[worst]), \
        f"q21 key {keyed(item)!r} but the least resilient row is {cg.labels(table)[worst]}"
    return (f"{cg.labels(table)[worst]} holds the fewest species, the lowest diversity and the "
            f"largest loss, {losses[worst]}")


def q22(table, item):
    counts, ranks, losses = _eco(table)
    least, most = ranks.index(min(ranks)), ranks.index(max(ranks))
    gap = abs(losses[least]) - abs(losses[most])
    assert gap > 0, f"the least diverse row must have lost more; losses are {losses}"
    assert abs(gap - round(gap)) < 1e-9, "the difference must be whole for a calculator-free item"
    assert keyed(item) == f"{int(round(gap))} percentage points", \
        f"q22 key {keyed(item)!r} but the losses are {losses[least]} and {losses[most]}"
    return f"losses of {losses[least]} and {losses[most]} differ in size by {int(round(gap))} percentage points"


def q23(table, item):
    _eco(table)
    headers = [cg.normalize(h) for h in table["headers"]]
    assert not any("severity" in h for h in headers), \
        "the key asks for a column the table does not yet carry; severity must be absent"
    for h in table["headers"][1:]:
        words = cg.normalize(h).split()
        grams = [" ".join(words[i:i + 3]) for i in range(len(words) - 2)]
        assert not any(cg.contains_phrase(keyed(item), g) for g in grams), \
            f"q23 key {keyed(item)!r} names {h!r}, a column the table already carries"
    return f"the table's columns are {table['headers'][1:]}, none of which records the severity of the drought"


def q24(table, item):
    counts, ranks, losses = _eco(table)
    order = sorted(range(len(counts)), key=lambda i: counts[i])
    by_count = [losses[i] for i in order]
    assert all(b > a for a, b in zip(by_count, by_count[1:])), \
        "the key says the pattern matches the framework's expectation; it must actually match"
    assert len(losses) == 3, f"the key speaks of three cases; the table holds {len(losses)}"
    return f"all {len(losses)} rows match the expected direction, which is a tendency and not a proof"


def _keystone(table):
    share = {lab: cg.cell(table, lab, SHARE) for lab in cg.labels(table)}
    effect = {lab: cg.cell(table, lab, AFFECTED) for lab in cg.labels(table)}
    smallest = min(share, key=share.get)
    biggest = max(share, key=share.get)
    assert sorted(share.values())[1] > share[smallest], f"the smallest share must be unique; {share}"
    assert sorted(share.values())[-2] < share[biggest], f"the largest share must be unique; {share}"
    assert max(effect, key=effect.get) == smallest, (
        "the item rests on abundance and effect running in opposite directions; the largest effect "
        f"is not the smallest share. shares {share}, effects {effect}"
    )
    assert min(effect, key=effect.get) == biggest, (
        f"the largest share must record the smallest effect. shares {share}, effects {effect}"
    )
    return share, effect, smallest, biggest


def q25(table, item):
    share, effect, smallest, _ = _keystone(table)
    assert sorted(effect.values())[-2] < effect[smallest], \
        f"the largest effect must be unique; the effects are {effect}"
    assert cg.contains_phrase(keyed(item), smallest), \
        f"q25 key {keyed(item)!r} but the keystone pattern belongs to {smallest}"
    return f"{smallest} holds the smallest share {share[smallest]} and the largest effect {effect[smallest]}"


def q26(table, item):
    share, effect, _, biggest = _keystone(table)
    assert effect[biggest] == 0, \
        f"the key says the most abundant species changed no other population; its effect is {effect[biggest]}"
    assert cg.contains_phrase(keyed(item), biggest), \
        f"q26 key {keyed(item)!r} but the largest share belongs to {biggest}"
    assert cg.contains_phrase(keyed(item), "no other species"), \
        f"q26 key {keyed(item)!r} does not state the outcome the table records for that row"
    return f"{biggest} holds the largest share {share[biggest]} and its removal changed {int(effect[biggest])} others"


def q27(table, item):
    share, effect, smallest, _ = _keystone(table)
    named = [lab for lab in cg.labels(table) if cg.contains_phrase(item["q"], lab)]
    assert len(named) == 1, f"the stem names rows {named}; it must name exactly one"
    n = int(effect[named[0]])
    assert keyed(item) == NUMBER_WORDS[n], \
        f"q27 key {keyed(item)!r} but {named[0]} affected {n} other species"
    assert n == max(effect.values()), "the claim says this is the largest such number in the table"
    return f"{named[0]} records {n} other species changed, the largest number in the table"


def q28(table, item):
    share, effect, _, _ = _keystone(table)
    named = [lab for lab in cg.labels(table) if cg.contains_phrase(item["q"], lab)]
    assert len(named) == 2, f"the stem must name exactly two rows; it names {named}"
    # Order by where each row appears IN THE STEM, not by its position in the
    # table. "G held how many times the share of F" is a different quotient from
    # "F held how many times the share of G", and reading the rows in table order
    # silently computes the wrong one.
    stem = cg.normalize(item["q"])
    named.sort(key=lambda lab: stem.index(cg.normalize(lab)))
    a, b = named
    ratio = share[a] / share[b]
    assert abs(ratio - round(ratio)) < 1e-9, "the ratio must be whole for a calculator-free item"
    assert keyed(item) == f"{int(round(ratio))} times", \
        f"q28 key {keyed(item)!r} but {share[a]} divided by {share[b]} is {ratio}"
    assert effect[a] < effect[b], \
        "the claim notes the pair runs the other way on effect; it does not"
    return (f"{a} holds {share[a]} against {b}'s {share[b]}, a factor of {int(round(ratio))}, "
            f"while affecting {int(effect[a])} against {int(effect[b])} species")


def q29(table, item):
    share, effect, smallest, biggest = _keystone(table)
    assert effect[smallest] > effect[biggest], \
        "the key rests on the smallest share having the larger effect"
    return (f"the smallest share {share[smallest]} records {int(effect[smallest])} species affected "
            f"while the largest share {share[biggest]} records {int(effect[biggest])}")


TABLE_CHECKS = {20: q20, 21: q21, 22: q22, 23: q23, 24: q24,
                25: q25, 26: q26, 27: q27, 28: q28, 29: q29}


CLAIMS = [
 ("fewer component parts and little diversity among the parts",
  "EK 8.6.A.1 states that natural and artificial ecosystems with fewer component parts, and with little diversity among the parts, are often less resilient to changes in the environment. Area and age appear nowhere in the statement."),
 ("usually reduces resilience without guaranteeing it",
  "EK 8.6.A.1 writes OFTEN rather than always. A stated tendency describes the usual case and leaves room for exceptions, so an absolute reading overstates the sentence."),
 ("Both natural and artificial ecosystems",
  "EK 8.6.A.1 opens by naming natural AND artificial ecosystems, so a planted stand and an undisturbed wood are covered by the same sentence."),
 ("Keystone species, producers, and essential abiotic and biotic factors",
  "EK 8.6.A.2 names exactly those as contributing to maintaining the diversity of an ecosystem. Each distractor keeps one part of the list and discards the rest."),
 ("age of the rocks underlying the ecosystem",
  "EK 8.6.A.2 names keystone species, producers, and essential abiotic and biotic factors. Rock age is a dating consideration under EK 7.6.B.1 and appears nowhere in this topic."),
 ("disproportionate relative to its abundance",
  "EK 8.6.B.1 states that the effects of keystone species on the ecosystem are disproportionate relative to their abundance. Disproportionate means out of proportion, which is what the nearest distractor denies."),
 ("It often collapses",
  "EK 8.6.B.1 states that when keystone species are removed from the ecosystem, it often collapses. That is the consequence the statement attaches to their removal."),
 ("usual outcome without being certain",
  "EK 8.6.B.1 writes OFTEN rather than always, which states a strong tendency and leaves room for cases in which the ecosystem does not collapse."),
 ("effect disproportionate relative to the species' abundance",
  "EK 8.6.B.1 states that the effects of keystone species are disproportionate relative to their abundance. A large effect from a species of small abundance is exactly that mismatch."),
 ("effects of keystone species are disproportionate relative to their abundance",
  "EK 8.6.B.1 defines the keystone role by a mismatch between effect and abundance, so identifying it with the greatest abundance removes the feature the statement names. Nothing in the framework ties the role to biomass rank."),
 ("addition or removal of a component of an ecosystem affects its overall structure",
  "Learning objective 8.6.B asks students to explain how the addition or removal of any component of an ecosystem will affect its overall short-term and long-term structure, and EK 8.6.B.1 gives the keystone case as its most extreme version."),
 ("because producers are named among its contributors",
  "EK 8.6.A.2 names producers among the contributors to maintaining the diversity of an ecosystem, and skill 6.E asks for the predicted effect of a disruption to one or more components. Removing a named contributor removes its contribution."),
 ("few, similar parts is more likely to be the less resilient",
  "EK 8.6.A.1 states that ecosystems with fewer component parts and little diversity among the parts are often less resilient. Skill 6.E asks for the prediction that follows, and OFTEN makes it a likelihood rather than a certainty."),
 ("likely to be less resilient than a comparable ecosystem with more and more varied parts",
  "EK 8.6.A.1 covers artificial as well as natural ecosystems and attaches lower resilience to few, similar component parts. A planted stand of one species with few other organisms is that description at the ecosystem level."),
 ("because such factors are named among its contributors",
  "EK 8.6.A.2 names essential abiotic AND biotic factors among the contributors to maintaining diversity, so the two are not independent in the statement's own terms. Skill 6.E asks for the effect of a disruption to a component."),
 ("small share of the community's biomass, and its removal changes many other populations",
  "EK 8.6.B.1 makes the keystone role a mismatch between effect and abundance, so evidence for it must pair a small abundance with a large effect. Biomass rank, area and variability alone say nothing about the effect of removal."),
 ("leaves the other populations almost unchanged",
  "EK 8.6.B.1 rests the keystone role on a large effect out of proportion to abundance. A removal that changes little removes the effect half of that claim, whereas a small abundance is consistent with the role rather than against it."),
 ("likely to become more resilient",
  "EK 8.6.A.1 attaches lower resilience to few component parts and little diversity among them, so moving away from that condition moves away from the associated fragility. The same statement covers artificial ecosystems, so the last option misreads it."),
 ("out of proportion to its abundance, so its loss removes more than its share",
  "EK 8.6.B.1 states that the effects of keystone species are disproportionate relative to their abundance and that the ecosystem often collapses on their removal. Rarity is shared by both species in the comparison; the disproportion is not."),
 ("more and more varied parts lost less productivity",
  "Skill 4.B asks for the relationship between the variables. The table check above orders the rows by species count and confirms the loss shrinks at every step, and separately that the species counts and the diversity words rank the rows the same way."),
 ("Ecosystem 1",
  "EK 8.6.A.1 attaches lower resilience to fewer component parts and little diversity. The table check above confirms one row is simultaneously lowest on species count, lowest on diversity and largest on loss."),
 ("51 percentage points",
  "Skill 5.A includes percentages and percent changes. The table check above identifies the least and most diverse rows from the diversity column and recomputes the difference in the size of their losses."),
 ("severity of the drought at each ecosystem",
  "Skill 6.E asks for the effect of a disruption, and a comparison across ecosystems isolates the effect of their structure only if the disruption was comparable. The table check above confirms the table carries no such column and that the key does not name a column it already has."),
 ("the word often means a further case could depart from it",
  "EK 8.6.A.1 says such ecosystems are OFTEN less resilient, which is a tendency rather than a law. The table check confirms all three cases match the expected direction, which is consistent with the statement without converting it into a certainty."),
 ("Species F",
  "EK 8.6.B.1 states that the effects of keystone species are disproportionate relative to their abundance. The table check above confirms the smallest biomass share and the largest number of species affected belong to the same unique row."),
 ("Species H, whose removal changed the abundance of no other species",
  "EK 8.6.B.1 makes the keystone role a mismatch between effect and abundance. The table check above confirms the row with the largest biomass share records the smallest effect, which is zero."),
 ("Nine",
  "Skill 4.B, identifying a specific data point. The table check above reads the effect column for the row the stem names and confirms it is the largest such number in the table."),
 ("12 times",
  "Skill 5.A includes ratios. The table check above divides the biomass share of the first named species by that of the second, confirms the factor is whole, and confirms the same pair runs the other way on the number of species affected."),
 ("need not be proportional to how abundant it is",
  "EK 8.6.B.1 states that the effects of keystone species are disproportionate relative to their abundance. The table check above confirms the smallest share records the largest effect and the largest share the smallest, which is that disproportion measured directly."),
 ("keystone species has effects out of proportion to its abundance",
  "EK 8.6.A.1 supplies the resilience claim with its hedge, EK 8.6.A.2 the list of contributors to maintaining diversity, and EK 8.6.B.1 the disproportionate effect. Each distractor contradicts one of those three sentences."),
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
    r"(?<![A-Za-z])(the (?:graph|figure|diagram|chart|web|plot) (?:shown|above|below)|"
    r"in the (?:graph|figure|diagram|chart|web|plot) (?:shown|above|below)|"
    r"shown in the (?:graph|figure|diagram|chart|web|plot))(?![A-Za-z])",
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
    cg.check(b8_6, CLAIMS, table_checks=TABLE_CHECKS)
    print(f"    {n_style} notation and figure-reference checks clean.")


main()
