"""Key audit for AP ENVIRONMENTAL SCIENCE 2.1 Introduction to Biodiversity.

One (anchor, claim) per item, in module order. ``anchor`` is a distinctive
substring that must appear in the KEYED choice and in no distractor, so an
off-by-one key or a reordered choice list fails here rather than reaching a
student. ``claim`` states what the key rests on, for a human to audit.

WHAT THE KEYS REST ON
---------------------
Items 1, 16, 20, 24 and 28 rest on ERT-2.A.1: biodiversity in an ecosystem
includes genetic, species, and habitat diversity.

Items 3, 4, 11, 19, 22, 25, 30 rest on ERT-2.A.2: the more genetically diverse a
population is, the better it can respond to environmental stressors, and a
population bottleneck can lead to a loss of genetic diversity.

Items 5, 12, 18 and 23 rest on ERT-2.A.3: ecosystems that have a larger number of
species are more likely to recover from disruptions.

Items 6, 7, 13, 14, 15, 21, 26, 27 and 30 rest on ERT-2.A.4: loss of habitat
leads to a loss of specialist species, followed by a loss of generalist species,
and to reduced numbers of species that have large territorial requirements. The
ORDER is the framework's own and is what items 6, 13, 14 and 21 turn on.

Items 2, 8, 9, 17, 23 and 29 rest on ERT-2.A.5: species richness refers to the
number of different species found in an ecosystem.

BOUNDARIES. The island specialist-generalist case is ERT-2.E.1 (topic 2.3) and
the constant-versus-changing-habitat case is ERT-3.A.1 (topic 3.1). No item here
uses either. The framework does not define a population bottleneck's causes, so
no item asks for them; it gives no diversity index, so no item asks a student to
compute one.

DATA ITEMS: 8 to 17 carry tables. Each keyed conclusion is recomputed below from
that table alone, and each check also falsifies the distractors.

NEGATIVE CONTROL: ``python3 verify_e2_1.py --selftest`` corrupts a key, an
anchor, a table cell and the notation on purpose and confirms each check fires.
"""
import re
import sys

import cg_check as cg

_BANNED = [
    (re.compile(r"\\"), "a backslash: this subject is not typeset, so LaTeX prints raw"),
    (re.compile(r"(?<![A-Za-z])\d+\s?-\s?\d"), "a digit-hyphen-digit range: write 'to' instead"),
    (re.compile(r"\d\s?/\s?\d"), "a digit-slash-digit fraction: write it out in words"),
    (re.compile(r"\^"), "a bare caret, which prints raw outside a math span"),
    (re.compile(r"\$"), "a dollar sign, which the converter reads as inline math"),
]


def style(module):
    """No typeset notation anywhere in the module's student-facing text."""
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


NSPP = "Number of different species recorded"
NIND = "Total number of individuals recorded"
VARIANTS = "Number of different genetic variants present"
SURVIVE = "Percent of individuals surviving a severe drought"
NINDIV = "Number of individuals"
BEFORE_SPP = "Number of different species before a storm"
YEARS = "Years taken to return to the pre-storm community"
AREA = "Area remaining (hectares)"
SPECIALIST = "Number of specialist species present"
GENERALIST = "Number of generalist species present"
TERRITORY = "Territory one pair requires (hectares)"
FRAGSHARE = "Percent of small forest fragments in which it is still found"


def q8(table, item):
    spp = dict(zip(cg.labels(table), cg.col(table, NSPP)))
    ind = dict(zip(cg.labels(table), cg.col(table, NIND)))
    assert max(spp, key=spp.get) == "Plot 1", "Plot 1 must record the most species"
    assert max(ind, key=ind.get) != "Plot 1", \
        "the plot with the most species must NOT also hold the most individuals"
    assert len(set(spp.values())) == len(spp), "'all four have the same richness' must be false"
    return (f"the species counts are {spp} and the individual counts {ind}, so the two "
            "columns rank the plots differently and richness is read from the first")


def q9(table, item):
    spp = dict(zip(cg.labels(table), cg.col(table, NSPP)))
    ind = dict(zip(cg.labels(table), cg.col(table, NIND)))
    most_ind = max(ind, key=ind.get)
    assert most_ind == "Plot 4", f"Plot 4 must hold the most individuals; got {most_ind}"
    assert spp[most_ind] == min(spp.values()), \
        "the plot with the most individuals must hold the fewest species"
    return (f"{most_ind} holds the most individuals, {ind[most_ind]:.0f}, and the fewest "
            f"species, {spp[most_ind]:.0f}, so the two counts point opposite ways")


def q10(table, item):
    pairs = sorted(zip(cg.col(table, VARIANTS), cg.col(table, SURVIVE)))
    assert all(pairs[i + 1][1] > pairs[i][1] for i in range(len(pairs) - 1)), \
        f"survival must rise with genetic variants; got {pairs}"
    assert pairs[0][1] != max(s for _, s in pairs), \
        "'the least diverse population survived best' must be false"
    assert len(set(s for _, s in pairs)) == len(pairs), "'all survived equally' must be false"
    return (f"sorted by genetic variants the survival reads {[s for _, s in pairs]} percent, "
            "strictly increasing across the four populations")


def q11(table, item):
    n = dict(zip(cg.labels(table), cg.col(table, NINDIV)))
    v = dict(zip(cg.labels(table), cg.col(table, VARIANTS)))
    before = "Before the crash"
    low = "At the lowest point"
    after = "After fifty years of recovery in numbers"
    assert n[after] > 0.8 * n[before], "the numbers must have largely recovered"
    assert v[after] < 0.4 * v[before], "the genetic variants must NOT have recovered"
    assert v[low] < v[before], "'no variants were lost at the lowest point' must be false"
    assert v[after] <= v[before], "'more variants after recovery than before' must be false"
    return (f"individuals return from {n[low]:.0f} to {n[after]:.0f} against {n[before]:.0f} "
            f"before the crash, while variants stay at {v[after]:.0f} against "
            f"{v[before]:.0f}")


def q12(table, item):
    pairs = sorted(zip(cg.col(table, BEFORE_SPP), cg.col(table, YEARS)))
    assert all(pairs[i + 1][1] < pairs[i][1] for i in range(len(pairs) - 1)), \
        f"recovery time must fall as species number rises; got {pairs}"
    assert pairs[0][1] == max(y for _, y in pairs), \
        "the poorest ecosystem must be the slowest, so 'fewest species recovered fastest' is false"
    assert len(set(y for _, y in pairs)) == len(pairs), "'all recovered in the same time' must be false"
    return (f"sorted by species number the recovery times read {[y for _, y in pairs]} years, "
            "strictly decreasing")


def q13(table, item):
    trio = sorted(zip(cg.col(table, AREA), cg.col(table, SPECIALIST), cg.col(table, GENERALIST)),
                  reverse=True)
    spec = [s for _, s, _ in trio]
    gen = [g for _, _, g in trio]
    assert all(spec[i + 1] <= spec[i] for i in range(len(spec) - 1)), f"specialists must decline; got {spec}"
    assert all(gen[i + 1] <= gen[i] for i in range(len(gen) - 1)), f"generalists must decline; got {gen}"
    spec_drop = (spec[0] - spec[-1]) / spec[0]
    gen_drop = (gen[0] - gen[-1]) / gen[0]
    assert spec_drop > gen_drop, f"specialists must fall proportionally faster; got {spec_drop} against {gen_drop}"
    assert spec[-1] != max(spec), "'the smallest fragment holds the most specialists' must be false"
    return (f"from the largest fragment to the smallest, specialists fall {spec} and "
            f"generalists fall {gen}, a proportional loss of {spec_drop:.2f} against "
            f"{gen_drop:.2f}")


def q14(table, item):
    trio = sorted(zip(cg.col(table, AREA), cg.col(table, SPECIALIST), cg.col(table, GENERALIST)))
    smallest = trio[0]
    assert smallest[1] == 0, f"the smallest fragment must hold no specialists; got {smallest[1]}"
    assert smallest[2] > 0, f"the smallest fragment must still hold generalists; got {smallest[2]}"
    assert any(s > 0 for _, s, _ in trio[1:]), "larger fragments must still hold specialists"
    return (f"the smallest fragment holds {smallest[1]:.0f} specialists and "
            f"{smallest[2]:.0f} generalists, so one group has gone and the other has not")


def q15(table, item):
    pairs = sorted(zip(cg.col(table, TERRITORY), cg.col(table, FRAGSHARE)))
    assert all(pairs[i + 1][1] < pairs[i][1] for i in range(len(pairs) - 1)), \
        f"the share of fragments occupied must fall as territory grows; got {pairs}"
    assert pairs[-1][1] == min(s for _, s in pairs), \
        "'the species needing most territory persists in the most fragments' must be false"
    assert len(set(s for _, s in pairs)) == len(pairs), "'all persist equally' must be false"
    return (f"sorted by territory required the share of small fragments occupied reads "
            f"{[s for _, s in pairs]} percent, strictly decreasing")


def _measurements(table):
    return {r[0]: cg.normalize(r[1]) for r in table["rows"]}


def q16(table, item):
    m = _measurements(table)
    genetic = [k for k, v in m.items() if "gene variants" in v]
    assert genetic == ["Measurement 1"], f"exactly one measurement must count gene variants; got {genetic}"
    assert "different species" in m["Measurement 2"], "the second must count species"
    assert "habitat types" in m["Measurement 3"], "the third must count habitat types"
    return ("the three measurements count gene variants, species and habitat types "
            "respectively, which are the three levels the framework names")


def q17(table, item):
    m = _measurements(table)
    species = [k for k, v in m.items() if "different species" in v]
    assert species == ["Measurement 2"], f"exactly one measurement must count species; got {species}"
    assert "gene variants" not in m["Measurement 2"], "the species count must not also be a gene count"
    return ("exactly one of the three measurements counts different species, which is what "
            "species richness is defined as")


CLAIMS = [
 ("Genetic, species and habitat diversity",
  "ERT-2.A.1, near verbatim: biodiversity in an ecosystem includes genetic, species, and habitat diversity."),
 ("number of different species found in an ecosystem",
  "ERT-2.A.5, near verbatim: species richness refers to the number of different species found in an ecosystem, which is a count of kinds rather than of individuals."),
 ("respond better to environmental stressors",
  "ERT-2.A.2, near verbatim: the more genetically diverse a population is, the better it can respond to environmental stressors. The claim is about the response, not about population size."),
 ("lead to a loss of genetic diversity",
  "ERT-2.A.2 states that a population bottleneck can lead to a loss of genetic diversity, and the framework attaches no other consequence to a bottleneck."),
 ("more likely to recover from disruptions",
  "ERT-2.A.3, near verbatim: ecosystems that have a larger number of species are more likely to recover from disruptions."),
 ("Specialist species are lost first",
  "ERT-2.A.4, near verbatim: loss of habitat leads to a loss of specialist species, followed by a loss of generalist species. The order is the framework's own."),
 ("Reduced numbers of species that have large territorial requirements",
  "ERT-2.A.4 states that loss of habitat also leads to reduced numbers of species that have large territorial requirements, alongside the loss of specialists and then generalists."),
 ("largest number of different species",
  "Recomputed in q8 above: the plot with the most species is not the plot with the most individuals, so the two columns rank differently. ERT-2.A.5 defines richness as the count of different species."),
 ("Species richness counts different species",
  "Recomputed in q9 above: the plot with the most individuals holds the fewest species. ERT-2.A.5 makes species richness a count of different species rather than of individuals."),
 ("survived the drought better",
  "Recomputed in q10 above: sorting the populations by genetic variants leaves survival strictly increasing. ERT-2.A.2 states that a more genetically diverse population responds better to environmental stressors."),
 ("recovered its numbers but not its genetic diversity",
  "Recomputed in q11 above: the individual count returns close to its starting value while the variant count stays near its low point. ERT-2.A.2 states that a bottleneck can lead to a loss of genetic diversity."),
 ("returned to their pre-storm community sooner",
  "Recomputed in q12 above: sorting the ecosystems by species number leaves recovery time strictly decreasing. ERT-2.A.3 states that ecosystems with more species are more likely to recover from disruptions."),
 ("Specialist species fall away faster",
  "Recomputed in q13 above: across the fragments the specialist count falls proportionally faster than the generalist count. ERT-2.A.4 puts the loss of specialists BEFORE the loss of generalists."),
 ("Specialists have gone entirely while some generalists remain",
  "Recomputed in q14 above: in the smallest fragment the specialist column has reached zero and the generalist column has not, which is the end state ERT-2.A.4's ordering describes."),
 ("found in fewer of the small fragments",
  "Recomputed in q15 above: sorting the species by territory required leaves the share of fragments occupied strictly decreasing. ERT-2.A.4 states that habitat loss reduces the numbers of species with large territorial requirements."),
 ("counts gene variants within one species",
  "Recomputed in q16 above: exactly one of the three measurements counts gene variants. ERT-2.A.1 names genetic, species and habitat diversity as three separate levels of biodiversity."),
 ("Measurement 2",
  "Recomputed in q17 above: exactly one of the three measurements counts different species, which is what ERT-2.A.5 defines species richness to be."),
 ("with ninety species is more likely to recover",
  "ERT-2.A.3 states that ecosystems that have a larger number of species are more likely to recover from disruptions, and the two ecosystems differ in exactly that quantity."),
 ("Keeping the population's genetic diversity high",
  "ERT-2.A.2 states both that a more genetically diverse population responds better to environmental stressors and that a bottleneck can lead to a loss of genetic diversity, so both halves point the same way."),
 # Both halves, because the distractor is the SWAP: it uses each clause with
 # the other term. Either clause alone matches both choices.
 ("Species diversity concerns the different species in an ecosystem; genetic",
  "ERT-2.A.1 lists genetic, species and habitat diversity as separate levels, ERT-2.A.5 defines species richness as a count of different species, and ERT-2.A.2 treats genetic diversity as a property of a population."),
 ("disappear first, then generalist species",
  "ERT-2.A.4 carries all three parts of the keyed sequence: a loss of specialist species, followed by a loss of generalist species, and reduced numbers of species with large territorial requirements."),
 ("suffer lower mortality in the same drought",
  "ERT-2.A.2 claims a relationship between genetic diversity and the response to environmental stressors, so the evidence bearing on it compares populations differing in genetic diversity under the same stress."),
 ("Its species richness is low",
  "ERT-2.A.5 makes species richness a count of different species rather than of individuals, and ERT-2.A.3 states that ecosystems with a larger number of species are more likely to recover from disruptions."),
 ("stated to include genetic, species and habitat diversity together",
  "ERT-2.A.1 lists the three levels together in one sentence, which is what makes habitat diversity a level of its own rather than a restatement of either of the others."),
 ("may remain lower than before",
  "ERT-2.A.2 states that a population bottleneck can lead to a loss of genetic diversity, and it supplies no mechanism by which the lost variants return when the count of individuals does."),
 ("An increase in the genetic diversity of the species that remain",
  "ERT-2.A.4 names the loss of specialists, the subsequent loss of generalists and reduced numbers of species with large territorial requirements. It makes no claim that genetic diversity rises, and ERT-2.A.2 gives no such mechanism."),
 ("unlikely to hold the species",
  "ERT-2.A.4 states that loss of habitat leads to reduced numbers of species that have large territorial requirements, which is precisely the group the proposed reserve is meant to hold."),
 ("together with the range of habitat types",
  "ERT-2.A.1 states that biodiversity in an ecosystem includes genetic, species and habitat diversity, so a full account addresses all three levels rather than counting individuals or measuring mass."),
 ("Species richness refers to the number of different species",
  "The two ecosystems are matched on the number of individuals and differ in the number of different species, which is exactly the quantity ERT-2.A.5 defines as species richness."),
 ("a smaller surviving population risks losing genetic diversity",
  "ERT-2.A.4 supplies the species-level and territory-level consequences of habitat loss and ERT-2.A.2 supplies the genetic-level one, so the two statements together span more than one of the levels ERT-2.A.1 names."),
]

TABLE_CHECKS = {8: q8, 9: q9, 10: q10, 11: q11, 12: q12, 13: q13,
                14: q14, 15: q15, 16: q16, 17: q17}


def _selftest():
    """Negative control: every gate below must FAIL when its input is corrupted."""
    import copy
    import types

    def must_fail(label, mutate):
        mod = types.ModuleType("e2_1_mutant")
        mod.TOPIC = e2_1.TOPIC
        mod.QUESTIONS = copy.deepcopy(e2_1.QUESTIONS)
        claims = list(CLAIMS)
        try:
            mutate(mod, claims)
            cg.check(mod, claims, table_checks=TABLE_CHECKS)
        except AssertionError as exc:
            print(f"  control OK  {label}: {str(exc)[:90]}")
            return
        raise SystemExit(f"CONTROL FAILED: {label} did not raise")

    def move_key(mod, claims):
        mod.QUESTIONS[5]["ans"] = 1

    def break_anchor(mod, claims):
        claims[4] = ("no such phrase anywhere in the module", claims[4][1])

    def corrupt_table(mod, claims):
        # let the genetic variants recover along with the numbers
        mod.QUESTIONS[10]["table"] = dict(
            headers=e2_1._T_BOTTLENECK["headers"],
            rows=[[s, n, ("57" if s.startswith("After fifty") else v)]
                  for s, n, v in e2_1._T_BOTTLENECK["rows"]])

    def corrupt_order(mod, claims):
        # Reverse ERT-2.A.4's order by SWAPPING the two columns, so it is the
        # generalists that collapse to zero and the specialists that persist.
        #
        # An earlier version of this control just lowered Fragment 4's
        # generalist count to 1 and did not fire -- and could not have. The
        # specialists already fall to 0, a proportional loss of 1.00, which is
        # the maximum; no change to the generalist column alone can make them
        # fall faster. The control passed silently and said nothing about
        # whether q13 works. Swapping is what actually inverts the claim.
        mod.QUESTIONS[12]["table"] = dict(
            headers=e2_1._T_HABITAT["headers"],
            rows=[[f, a, g, s] for f, a, s, g in e2_1._T_HABITAT["rows"]])

    def duplicate_choice(mod, claims):
        mod.QUESTIONS[1]["choices"][3] = mod.QUESTIONS[1]["choices"][0]

    def thin_why(mod, claims):
        mod.QUESTIONS[22]["why"] = "It just is."

    def letter_reference(mod, claims):
        mod.QUESTIONS[26]["why"] = ("Choice D is wrong because the framework says so and "
                                    "the rest of the reasoning follows from that.")

    def latex_slips_in(mod, claims):
        mod.QUESTIONS[0]["choices"][2] = "Species, trophic and \\alpha diversity."
        style(mod)

    def range_slips_in(mod, claims):
        mod.QUESTIONS[4]["q"] = "Between 1990-2010 what did the framework say about species number?"
        style(mod)

    print("negative controls:")
    must_fail("a backslash macro in a choice", latex_slips_in)
    must_fail("a digit-hyphen-digit range in a stem", range_slips_in)
    must_fail("key moved off its anchor", move_key)
    must_fail("anchor no longer in the keyed choice", break_anchor)
    must_fail("table value corrupted so the keyed conclusion is false", corrupt_table)
    must_fail("the specialist-then-generalist order reversed in the data", corrupt_order)
    must_fail("a distractor made identical to the key", duplicate_choice)
    must_fail("a why reduced below the minimum", thin_why)
    must_fail("a why naming an option by letter", letter_reference)
    print("all negative controls raised as required.")


import e2_1  # noqa: E402

if __name__ == "__main__" and "--selftest" in sys.argv:
    _selftest()

style(e2_1)
cg.check(e2_1, CLAIMS, table_checks=TABLE_CHECKS)
