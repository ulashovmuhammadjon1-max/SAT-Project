"""Key audit for AP BIOLOGY 7.2 Natural Selection.

One (anchor, claim) per item, in module order. ``cg_check.check`` is the
structural gate; it is described in ``verify_b5_3.py``.

WHAT IS RECOMPUTED. Eight items carry data. The two worth naming are the
three-habitat table, which is checked to have a DIFFERENT phenotype leading in
each column -- if one phenotype led everywhere, the item about no phenotype
being fittest everywhere would have a false key and the item about the dry
habitat would be trivial -- and the enzyme table, which is checked to have no
single form high at both temperatures, since that is what makes the population's
coverage come from carrying more than one form rather than from any individual.
The rest are trend and comparison checks that also confirm the rejected reading
is false on the same numbers.

WHAT IS NOT CLAIMED. The CED prints illustrative examples beside two of this
topic's statements. No key here names a species, a chemical or a disease, and
the scan at the foot of this file fails if one appears -- including the
illustrative examples themselves, since those are teaching suggestions rather
than assessable content. The scan also bars any claim about extinction risk,
which is EK 7.11.A.1's and belongs to a sibling's module.

NEGATIVE CONTROL: ``negcontrol_b5_7.py``.
"""
import cg_check as cg
import b7_2

T_PRESSURE = b7_2._T_PRESSURE
T_RESIST = b7_2._T_RESIST
T_FLOWER = b7_2._T_FLOWER
T_ENZYME = b7_2._T_ENZYME
T_THREEENV = b7_2._T_THREEENV
T_MOLEC = b7_2._T_MOLEC
T_OVERGEN = b7_2._T_OVERGEN

# Named species, chemicals and diseases have no place in a key here: the CED's
# illustrative examples are teaching suggestions, not assessable content.
BARRED = ("ddt", "sickle cell", "sickle-cell", "peppered moth", "biston",
          "anopheles", "malaria", "penicillin",
          # EK 7.11.A.1's territory, which belongs to b7_11
          "extinction", "extinct")


def _rows(table):
    heads = [cg.normalize(h) for h in table["headers"]]
    return [dict(zip(heads, r)) for r in table["rows"]]


def q6(table, item):
    before = "percent of the population before the pressure"
    after = "percent of the population after ten generations of the pressure"
    d = {cg.normalize(r["phenotypic variant"]): (cg.num(r[before]), cg.num(r[after]))
         for r in _rows(table)}
    for label, col in ((before, 0), (after, 1)):
        total = sum(v[col] for v in d.values())
        assert total == 100, f"the {label!r} column sums to {total}, not 100"
    risers = sorted(k for k, v in d.items() if v[1] > v[0])
    assert risers == ["variant 3"], f"the variants that rose are {risers}"
    assert d["variant 3"][0] < 20 and d["variant 3"][1] > 50, \
        f"the risen variant must go from a small minority to a majority; got {d['variant 3']}"
    commonest_before = max(d, key=lambda k: d[k][0])
    assert commonest_before != risers[0], \
        "the variant that rose must not also have been the commonest to start with"
    return (f"both columns sum to 100 percent; only {risers} rose, from {d['variant 3'][0]:.0f} to "
            f"{d['variant 3'][1]:.0f}, while the commonest starting variant was {commonest_before}")


def q7(table, item):
    s = [(cg.normalize(r["generation of exposure to the treatment"]),
          cg.num(r["percent of the population surviving the treatment"])) for r in _rows(table)]
    vals = [v for _, v in s]
    assert all(0 <= v <= 100 for v in vals), f"a survival percentage outside 0 to 100: {vals}"
    assert vals == sorted(vals) and len(set(vals)) == len(vals), \
        f"survival must rise strictly across the generations; got {vals}"
    assert vals[-1] - vals[0] > 50, "the rise must be large enough to call a trend"
    assert 0 < vals[0] < 10, \
        "a few individuals must already have survived at the start, or nothing was there to sort"
    assert vals[-1] > 80, "the rise must reach most of the population for the trend to be clear"
    # The generation labels are data too: a series read out of order says nothing.
    gens = [cg.num(lab) for lab, _ in s]
    assert gens == sorted(gens) and len(set(gens)) == len(gens), \
        f"the generations must be listed in increasing order; got {gens}"
    return (f"survival rises strictly from {vals[0]:.0f} to {vals[-1]:.0f} percent across "
            f"generations {gens}, starting from a small surviving minority")


def q8(table, item):
    spring = "mean day of the year on which spring temperatures arrived"
    flower = "mean day of the year on which the population flowered"
    s = [(cg.num(r[spring]), cg.num(r[flower])) for r in _rows(table)]
    sp = [a for a, _ in s]
    fl = [b for _, b in s]
    assert sp == sorted(sp, reverse=True), f"spring must arrive earlier by decade; got {sp}"
    assert fl == sorted(fl, reverse=True), f"flowering must move earlier by decade; got {fl}"
    assert all(b > a for a, b in s), "flowering must follow the arrival of spring in every decade"
    assert all(1 <= v <= 366 for v in sp + fl), "a day of the year outside the calendar is not data"
    return (f"spring moves from day {sp[0]:.0f} to day {sp[-1]:.0f} and flowering from day "
            f"{fl[0]:.0f} to day {fl[-1]:.0f}, both earlier, with flowering after spring throughout")


def q10(table, item):
    cold = "activity at 10 degrees celsius arbitrary units"
    warm = "activity at 35 degrees celsius arbitrary units"
    d = {cg.normalize(r["form of the enzyme carried by an individual"]):
         (cg.num(r[cold]), cg.num(r[warm])) for r in _rows(table)}
    best_cold = max(d, key=lambda k: d[k][0])
    best_warm = max(d, key=lambda k: d[k][1])
    assert best_cold != best_warm, (
        "no single form may be best at both temperatures, or the population's coverage would not "
        "depend on carrying more than one"
    )
    assert not any(v[0] > 70 and v[1] > 70 for v in d.values()), \
        "no single form may be highly active at both temperatures"
    assert d[best_cold][1] < 0.3 * d[best_cold][0], "the cold-adapted form must fall off in the warm"
    assert d[best_warm][0] < 0.3 * d[best_warm][1], "the warm-adapted form must fall off in the cold"
    return (f"{best_cold} leads in the cold at {d[best_cold][0]:.0f} and {best_warm} in the warm at "
            f"{d[best_warm][1]:.0f}, and no form exceeds 70 units at both temperatures")


def _habitats(table):
    cols = ["mean offspring in the wet habitat", "mean offspring in the dry habitat",
            "mean offspring in the shaded habitat"]
    d = {cg.normalize(r["phenotype"]): [cg.num(r[c]) for c in cols] for r in _rows(table)}
    leaders = [max(d, key=lambda k: d[k][i]) for i in range(len(cols))]
    return d, cols, leaders


def q11(table, item):
    d, cols, leaders = _habitats(table)
    dry = cols.index("mean offspring in the dry habitat")
    assert leaders[dry] == "phenotype 2", f"the dry habitat's leader is {leaders[dry]}"
    vals = sorted(v[dry] for v in d.values())
    assert vals[-1] > 2 * vals[-2], "the dry-habitat leader must lead clearly, not by a hair"
    return (f"the dry column reads {[d[k][dry] for k in d]} and its largest value belongs to "
            f"{leaders[dry]}, more than twice the next")


def q12(table, item):
    d, cols, leaders = _habitats(table)
    assert len(set(leaders)) == len(cols), (
        f"a different phenotype must lead in each habitat for the key to hold; leaders are {leaders}"
    )
    assert len(set(leaders)) == len(d), "every phenotype must lead somewhere"
    for i, k in enumerate(leaders):
        others = sorted(v[i] for kk, v in d.items() if kk != k)
        assert d[k][i] > others[-1], f"in column {i} the leader must be strictly ahead"
    return f"the leader in each of the three habitats is {leaders}, a different phenotype each time"


def q16(table, item):
    s = [cg.num(r["percent of the population carrying the favored variation"])
         for r in _rows(table)]
    assert all(0 <= v <= 100 for v in s), f"a percentage outside 0 to 100: {s}"
    assert s == sorted(s) and len(set(s)) == len(s), f"the series must rise strictly; got {s}"
    assert s[0] < 15, "the variation must start as a small minority, or nothing needs explaining"
    assert s[-1] > 70, "the rise must reach a majority for the trend to be clear"
    return f"the recorded percentages {s} rise at every step, from a small minority to a large majority"


def q17(table, item):
    forms = "number of different forms of the enzyme present in the population"
    envs = "number of the four test environments in which the population persisted"
    d = {cg.normalize(r["population"]): (cg.num(r[forms]), cg.num(r[envs])) for r in _rows(table)}
    assert len(d) == 2, "the comparison needs exactly two populations"
    (a, va), (b, vb) = d.items()
    assert (va[0] > vb[0]) == (va[1] > vb[1]), \
        f"more forms must go with more environments for the key to hold; got {d}"
    assert va[1] != vb[1], "the two populations must differ in how many environments they persisted in"
    assert max(va[1], vb[1]) <= 4, "a population cannot persist in more than the four tested"
    more = a if va[0] > vb[0] else b
    return (f"{more} carries the more forms and persisted in the more environments; the counts are "
            f"{d}, and neither exceeds the four environments tested")


CLAIMS = [
 ("Phenotypic variations in populations",
  "EK 7.2.A.1 states that natural selection acts on phenotypic variations in populations, so it acts on what is observable and on differences among individuals rather than editing alleles directly."),
 ("no phenotypic variation for selection to act on",
  "EK 7.2.A.1 makes phenotypic variation what selection acts on, so a uniform trait supplies none. New variation comes from mutation under EK 6.7.B.1.ii rather than from selection."),
 ("change and apply selective pressures to populations",
  "EK 7.2.A.2 states exactly this. Both clauses are the framework's: environments are not constant, and what they do is apply a pressure rather than supply new variation."),
 ("Increase or decrease the fitness of an organism in particular environments",
  "EK 7.2.A.3 states this, naming both directions, and the qualifier in particular environments prevents the effect from being read as a property of the variation alone."),
 ("raise fitness under one set of conditions and lower it under another",
  "EK 7.2.A.3's qualifier taken with EK 7.2.A.2's statement that environments change: the effect on fitness is relative to conditions, so one variation can act in either direction."),
 ("Variant 3",
  "EK 7.2.A.3 makes some variations increase fitness in particular environments, and a variation whose bearers leave more offspring becomes more common. The table check confirms both columns sum to one hundred, that exactly one variant rose, and that it was not the commonest to begin with."),
 ("individuals already carrying a variation that survives it left more offspring",
  "EK 7.2.A.2 has the environment apply a selective pressure and EK 7.2.A.1 has selection act on variation already present. The table check confirms survival rises strictly across the generations from a small surviving minority, which is sorting rather than creation; EK 6.7.B.1 makes mutations random."),
 ("flowering date moved earlier as the arrival of spring moved earlier",
  "EK 7.2.A.2 states that environments change and apply selective pressures to populations. The table check confirms both series move earlier by decade and that flowering follows the arrival of spring in every decade."),
 ("greater ability for populations to survive and reproduce in different environments",
  "EK 7.2.B.1 states exactly this. The claim is about a population's coverage across a range of environments, not a guarantee for any individual."),
 ("Some individuals retain high enzyme activity at the cold temperature and others at the warm one",
  "EK 7.2.B.1 states that variation in the number and types of molecules within cells can provide populations a greater ability to survive and reproduce in different environments. The table check confirms no single form is highly active at both temperatures, which is what makes the coverage depend on the population carrying more than one."),
 ("leaves the most offspring in that habitat",
  "EK 7.1.B.1 measures fitness by reproductive success and EK 7.2.A.3 makes the effect specific to particular environments, so the comparison is made within one habitat. The table check confirms the dry column's leader is ahead by more than a factor of two."),
 ("Each phenotype leaves the most offspring in a different habitat",
  "EK 7.2.A.3's qualifier in particular environments. The table check confirms a different phenotype strictly leads in each of the three habitats, which is what makes the key true and the one-phenotype-fittest-everywhere reading false."),
 ("apply selective pressures to populations, and variations that raise fitness in the new conditions",
  "EK 7.2.A.2 supplies the pressure and EK 7.2.A.3 makes the effect on fitness specific to the new conditions, with EK 7.2.A.1 confining selection to the variation already present."),
 ("causes individuals with some phenotypes to leave more offspring than others",
  "EK 7.2.A.2 has environments apply selective pressures and EK 7.2.A.3 has variations increase or decrease fitness in particular environments. A pressure falling identically on every individual would sort nothing."),
 ("alleles that the surviving individuals inherited",
  "EK 7.2.A.1 has selection act on phenotypic variations, EK 5.3.A.2.iii makes the set of alleles what is inherited, and EK 5.3.A.2.iv makes the phenotype the observable expression of those inherited traits."),
 ("became steadily more common while the pressure continued",
  "EK 7.2.A.2 and EK 7.2.A.3. The table check confirms the recorded percentages rise at every step and that the variation began as a small minority, so the first-generation reading rules out its already being universal."),
 ("more different forms of the enzyme persisted in more of the environments",
  "EK 7.2.B.1 states that variation in the number and types of molecules within cells can provide populations a greater ability to survive and reproduce in different environments. The table check confirms the two counts move together and that neither exceeds the four environments tested."),
 ("acts on phenotypic variations already present",
  "EK 7.2.A.1 presupposes that the variation is there, and EK 6.7.B.1.ii makes mutations a source of genetic variation. Selection sorts; it does not create."),
 ("increase or decrease the fitness of an organism in particular environments",
  "EK 7.2.A.3 allows the same variation to be favoured in one habitat and not in another. Mutations arise randomly under EK 6.7.B.1 rather than where they would be useful."),
 ("differences among the individuals of a population; environmental variation is differences in the conditions",
  "EK 7.2.A.1 locates the variation selection acts on among the individuals of a population and EK 7.2.A.2 makes the environment what changes and applies a pressure to them."),
 ("different molecular variants suit different conditions",
  "EK 7.2.B.1 speaks of an ability to survive and reproduce in DIFFERENT environments; the plural is the point, so the advantage is coverage across conditions rather than a guarantee within any one."),
 ("leave more offspring than individuals with another after the change",
  "EK 7.2.A.2 has environments apply selective pressures and EK 7.2.A.3 makes the pressure's effect a difference in fitness between variations. An individual altering its own phenotype is EK 5.5.A.1's plasticity instead."),
 ("leave fewer offspring, so it becomes less common in that environment",
  "EK 7.2.A.3 allows a variation to decrease fitness in particular environments and EK 7.1.B.1 measures fitness by reproductive success, but the qualifier confines the prediction to that environment."),
 ("can rise over generations even from a small starting fraction",
  "EK 7.2.A.1 has selection act on the variations present and EK 7.2.A.3 makes some of them raise fitness in particular environments; nothing restricts selection to common variations, and the change accumulates across generations under EK 7.1.A.2."),
 ("difference between phenotypes exists only among the individuals of a population",
  "EK 7.2.A.1 states that selection acts on phenotypic variations in populations, and EK 5.3.A.2.iv makes the phenotype an individual's observable expression, so a variation requires more than one individual."),
 ("Environments change and apply selective pressures to populations",
  "EK 7.2.A.2 is the statement joining a changing habitat to a change in a population; the rejected options are framework statements about other matters."),
 ("greater ability to survive and reproduce across different salt concentrations",
  "EK 7.2.B.1 states that variation in the number and types of molecules within cells can provide populations a greater ability to survive and reproduce in different environments, which concerns the population's coverage rather than an individual switching forms."),
 ("acts on phenotypic variations in populations, and that some variations increase fitness in particular environments",
  "EK 7.2.A.1 makes variation what selection acts on and EK 7.2.A.3 makes some variations raise fitness in particular environments, so a varying population can contain individuals suited to new conditions. EK 6.7.B.1 rather than selection supplies new variation."),
 ("hold in particular environments, so the same variation may lower fitness elsewhere",
  "EK 7.2.A.3 attaches the qualifier in particular environments, which is what the claim drops, and EK 7.2.A.2 adds that environments change."),
 ("population already varied; the changed environment applied a pressure",
  "Each clause is one of the framework's statements: EK 7.2.A.1, EK 7.2.A.2 and EK 7.2.A.3 in turn. Each rejected account has the environment or the individual supply the variation, which EK 6.7.B.1 assigns to random mutation."),
]

cg.check(b7_2, CLAIMS,
         table_checks={6: q6, 7: q7, 8: q8, 10: q10, 11: q11, 12: q12, 16: q16, 17: q17})

_text = " ".join(" ".join([q["q"], q["why"], *q["choices"]]) for q in b7_2.QUESTIONS)
for word in BARRED:
    assert not cg.contains_phrase(_text, word), (
        f"7.2: {word!r} appears in the module. The CED's illustrative examples are teaching "
        f"suggestions rather than assessable content, and extinction risk is EK 7.11.A.1's, "
        f"which belongs to b7_11"
    )
for word in BARRED:
    assert cg.contains_phrase(f"a stem naming {word} here", word), \
        f"the scan cannot detect {word!r} even in a string containing it"
print(f"    A different phenotype leads in each habitat and no enzyme form covers both temperatures,")
print(f"    both recomputed; {len(BARRED)} named examples and neighbouring-topic terms scanned for.")
