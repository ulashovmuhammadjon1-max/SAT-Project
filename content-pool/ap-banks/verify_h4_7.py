"""Key audit for AP CHEMISTRY 4.7 Types of Chemical Reactions.

One ``(anchor, claim)`` per item, in module order; the anchor must appear in the
KEYED choice and in no distractor. Five table items and two oxidation-number
items are recomputed from their own stimulus.

WHAT THE KEYS REST ON
---------------------
EK 4.7.A.1  Acid-base reactions involve transfer of one or more protons (H+
            ions) between chemical species.  (items 1, 6, 13, 14, 18, 24, 29, 30)
EK 4.7.A.2  Redox reactions involve transfer of one or more electrons, as
            indicated by changes in oxidation numbers; combustion is a subclass
            in which a species reacts with oxygen gas, and for hydrocarbons
            carbon dioxide and water are the products of complete combustion.
            (items 2, 4, 10, 11, 12, 14, 21, 27, 28, 29)
EK 4.7.A.3  Electrons are transferred from the species that is oxidized to the
            species that is reduced.  (items 5, 8, 16, 21, 25)
EK 4.7.A.4  Oxidation numbers may be assigned to each atom; this is often an
            effective way to identify the oxidized and reduced species.
            (items 7, 8, 15, 16, 17, 23, 28)
EK 4.7.A.5  Precipitation frequently involves mixing ions in aqueous solution to
            produce an insoluble or sparingly soluble ionic compound. All
            sodium, potassium, ammonium, and nitrate salts are soluble in water.
            (items 3, 9, 19, 20, 22, 26)

THE TWO EXCLUSION STATEMENTS, CHECKED MECHANICALLY BELOW
--------------------------------------------------------
"The meaning of the terms 'reducing agent' and 'oxidizing agent' will not be
assessed on the AP Exam."  ``excluded_terms`` fails the module if either phrase
appears in any stem, choice, rationale or claim. It is not enough to have
avoided them while writing; an edit could reintroduce one.

"Rote memorization of 'solubility rules' other than those implied in 4.7.A.5
will not be assessed."  The only solubility fact any key rests on is that all
sodium, potassium, ammonium and nitrate salts are soluble. Where an item needs
a compound to be INSOLUBLE, its stem states that a solid was observed. q9's
check below enumerates the pairings and confirms the key follows from the
framework's own four soluble families alone.

NEGATIVE CONTROL: ``python3 verify_h4_7.py --selftest`` corrupts a key, an
anchor, the notation, a table cell, a stem-recomputed value and the exclusion
gate on purpose and requires each corruption to be caught.
"""
import re
import sys

import h_chem_notation as hn
import h4_7 as M

RE_ON = "Oxidation number in the reactants"
PR_ON = "Oxidation number in the products"
MNON = "Oxidation number of the manganese atom"

# The framework's own four soluble families, and nothing else.
SOLUBLE = {"na+", "k+", "nh4+", "no3-"}

_BANNED_TERMS = [
    re.compile(r"(?<![a-z])reducing\s+agent", re.I),
    re.compile(r"(?<![a-z])oxidi[sz]ing\s+agent", re.I),
]


def excluded_terms(module, claims):
    """The CED excludes 'reducing agent' and 'oxidizing agent' from assessment."""
    texts = []
    for item in module.QUESTIONS:
        texts += hn.texts(item)
    texts += [c for pair in claims for c in pair]
    for text in texts:
        for pat in _BANNED_TERMS:
            hit = pat.search(text)
            assert not hit, (
                f"{module.TOPIC[0]}: {hit.group(0)!r} appears in {text[:70]!r}, but the "
                "CED's exclusion statement says that term will not be assessed"
            )
    print(f"OK  {module.TOPIC[0]} exclusions: neither excluded term appears in "
          f"{len(texts)} strings.")


# ------------------------------------------------------------ table questions

def q8(t, item):
    labs = hn.cg.labels(t)
    before = dict(zip(labs, hn.cg.col(t, RE_ON)))
    after = dict(zip(labs, hn.cg.col(t, PR_ON)))
    rose = [l for l in labs if after[l] > before[l]]
    fell = [l for l in labs if after[l] < before[l]]
    assert rose == ["Zn"], f"elements whose oxidation number rises: {rose}"
    assert fell == ["Cu"], f"elements whose oxidation number falls: {fell}"
    assert abs(after["Cu"] - before["Cu"]) == 2, \
        "the 'changes by two units' distractor must be true of copper and still not oxidation"
    assert max(before, key=before.get) == "S", \
        "the 'largest oxidation number' distractor must point at sulfur"
    hn.keyed(item, "Zinc")
    return (f"exactly one element rises, {rose[0]} from {before['Zn']} to {after['Zn']}, "
            f"while {fell[0]} falls and two are unchanged")


def q9(t, item):
    def ions(cell):
        return [x.strip().lower() for x in str(cell).split(",")]

    verdict = {}
    for row in t["rows"]:
        parts = ions(row[1])
        cations = [i for i in parts if i.endswith("+") or i[-2:-1] == "+"]
        anions = [i for i in parts if i not in cations]
        pairs = [(c, a) for c in cations for a in anions]
        verdict[row[0]] = all(c in SOLUBLE or a in SOLUBLE for c, a in pairs)
    safe = [k for k, v in verdict.items() if v]
    assert safe == ["Sodium chloride with potassium nitrate"], \
        f"mixtures every pairing of which is a framework-soluble salt: {safe}"
    hn.keyed(item, "every possible pairing is a sodium, potassium or nitrate salt")
    return ("in one mixture every cation-anion pairing is a sodium, potassium or "
            "nitrate salt, and in the other the lead and iodide pairing is not")


def q12(t, item):
    products = {r[0]: r[1] for r in t["rows"]}
    assert len(set(products.values())) == 1, f"the rows do not agree: {products}"
    only = next(iter(set(products.values())))
    assert "co2" in only.lower() and "h2o" in only.lower(), \
        f"the reported products are {only}, not carbon dioxide and water"
    assert len(products) >= 3, "the generalization needs more than two fuels behind it"
    hn.keyed(item, "carbon dioxide and water")
    return (f"all {len(products)} fuels report the same products, {only}, across molecules "
            "of very different size")


def q17(t, item):
    v = dict(zip(hn.cg.labels(t), hn.cg.col(t, MNON)))
    drop = v["MnO4-"] - v["Mn metal"]
    assert drop == 7, f"the fall from permanganate to the metal is {drop}, not seven"
    others = [v["MnO4-"] - v["Mn2+"], v["MnO2"] - v["Mn2+"],
              v["Mn2+"] - v["Mn metal"], v["MnO4-"] - v["MnO2"]]
    assert drop > max(others), f"a larger fall than {drop} exists among {others}"
    hn.keyed(item, "a fall of seven units")
    return (f"permanganate at {v['MnO4-']} down to the metal at {v['Mn metal']} is a fall of "
            f"{drop:.0f}, larger than every other tabulated pair")


def q22(t, item):
    obs = {r[0]: r[1].lower() for r in t["rows"]}
    solids = [k for k, o in obs.items() if "solid" in o]
    metals = [k for k, o in obs.items() if "metal" in o]
    assert solids == ["II", "III"], f"rows reporting a solid: {solids}"
    assert metals == ["III"], f"rows reporting a metal depositing: {metals}"
    precip = [k for k in solids if k not in metals]
    assert precip == ["II"], f"rows reporting a solid that is not a deposited metal: {precip}"
    assert "no oxidation number changes" in obs["I"], \
        "the gas row must state that no oxidation number changes"
    hn.keyed(item, "Reaction II")
    return ("two rows report a solid, one of them a metal depositing, which leaves a "
            "single row reporting an insoluble compound separating from solution")


TABLE_CHECKS = {8: q8, 9: q9, 12: q12, 17: q17, 22: q22}


# --------------------------------------------------------- stem-data questions

_WORDS = {0: "zero", 1: "one", 2: "two", 3: "three", 4: "four", 5: "five",
          6: "six", 7: "seven"}


def a7(item):
    # Three oxygens at the stated -2, in a neutral molecule.
    s = -3 * (-2)
    hn.keyed(item, f"+{s}")
    return f"three oxygens at negative two total negative six, so the sulfur is plus {s}"


def a23(item):
    # Carbon: zero as the element, and in CO2 it balances two oxygens at -2.
    start = 0
    end = -2 * (-2)
    assert end > start, "the carbon must rise for it to be the oxidized species"
    hn.keyed(item, f"rises from zero to positive {_WORDS[end]}")
    return (f"elemental carbon is {start} and carbon in CO2 balances two oxygens at "
            f"negative two, giving plus {end}, a rise")


ARITH = {7: a7, 23: a23}

CLAIMS = [
 ("proton is transferred from the acid",
  "EK 4.7.A.1: acid-base reactions involve transfer of one or more protons between chemical species. No element changes oxidation number here, and EK 4.7.A.5 makes all sodium salts soluble, so neither the redox nor the precipitation class applies."),
 ("electrons are transferred from the zinc",
  "EK 4.7.A.2 defines redox by the transfer of one or more electrons and EK 4.7.A.3 sends them from the oxidized species to the reduced one. Zinc metal becomes zinc ions and copper(II) ions become copper metal."),
 ("because sodium and nitrate salts are soluble",
  "EK 4.7.A.5 states that all sodium, potassium, ammonium and nitrate salts are soluble in water, so the sodium and nitrate pairing stays dissolved and only the other pairing of the four ions present can be the solid observed."),
 ("subclass of oxidation-reduction called combustion, giving carbon dioxide and water",
  "EK 4.7.A.2 names combustion an important subclass of oxidation-reduction in which a species reacts with oxygen gas, and states that carbon dioxide and water are the products of complete combustion of a hydrocarbon."),
 ("from the species that is oxidized to the species that is reduced",
  "EK 4.7.A.3, verbatim: in a redox reaction, electrons are transferred from the species that is oxidized to the species that is reduced."),
 ("protons are transferred between chemical species",
  "EK 4.7.A.1, near verbatim. Electron transfer defines the redox class under EK 4.7.A.2 and an insoluble ionic product defines precipitation under EK 4.7.A.5, so neither is the defining feature asked for."),
 ("+6",
  "Recomputed in a7 from the convention stated in the stem. EK 4.7.A.4 states that oxidation numbers may be assigned to each of the atoms in the reactants and products."),
 ("Zinc",
  "Recomputed in q8 above. EK 4.7.A.4 makes oxidation numbers the way to identify the oxidized species and EK 4.7.A.3 has electrons leave it, so the element whose number rises is the one oxidized."),
 ("every possible pairing is a sodium, potassium or nitrate salt",
  "Recomputed in q9 above against EK 4.7.A.5's four soluble families. Every cation-anion pairing available in that mixture is a sodium, potassium or nitrate salt, so no available compound can leave solution."),
 ("magnesium atoms lose electrons and hydrogen ions gain them",
  "EK 4.7.A.2 defines redox by electron transfer indicated by changes in oxidation numbers: magnesium goes from zero to positive two and hydrogen from positive one to zero in H2."),
 ("subclass of oxidation-reduction in which a species reacts with oxygen gas",
  "EK 4.7.A.2, near verbatim: combustion is an important subclass of oxidation-reduction reactions, in which a species reacts with oxygen gas."),
 ("carbon dioxide and water",
  "Recomputed in q12 above. EK 4.7.A.2 states that in the case of hydrocarbons, carbon dioxide and water are the products of complete combustion, and every tabulated fuel reports that pair."),
 ("proton passes from the hydrogen chloride to the ammonia",
  "EK 4.7.A.1 defines the acid-base class by proton transfer, which is what forms the ammonium ion. EK 4.7.A.5's precipitation class requires ions mixed in aqueous solution, and these are two gases."),
 ("potassium nitrate and water",
  "EK 4.7.A.2 makes a change in oxidation number the indicator of electron transfer. In this neutralization every element keeps its oxidation number, so only protons move, which EK 4.7.A.1 makes an acid-base reaction."),
 ("element in its standard form is assigned zero",
  "EK 4.7.A.4 states that oxidation numbers may be assigned to each of the atoms. The two assignments described are the least ambiguous cases: an uncombined element, and a monatomic ion whose whole charge is its oxidation number."),
 ("chlorine atom goes from an oxidation number of zero to negative one",
  "EK 4.7.A.4 makes changes in oxidation number the way to identify the reduced species and EK 4.7.A.3 has electrons arrive at it. Gaining electrons lowers the assigned number."),
 ("a fall of seven units",
  "Recomputed in q17 above from the tabulated oxidation numbers. EK 4.7.A.4 makes those numbers the way to identify oxidation and reduction, and reduction is the decrease."),
 ("Protons from the acid are transferred to the carbonate ion",
  "EK 4.7.A.1 defines acid-base reactions as the transfer of one or more protons. Calcium keeps its charge and carbon keeps its oxidation number, so no electron transfer occurs and EK 4.7.A.2 does not apply."),
 ("solid appears after two clear aqueous solutions",
  "EK 4.7.A.5 states that precipitation reactions frequently involve mixing ions in aqueous solution to produce an insoluble or sparingly soluble ionic compound; the appearance of that solid is the observation the class is named for."),
 ("Potassium ions and nitrate ions",
  "EK 4.7.A.5 states that all potassium and all nitrate salts are soluble in water, so that pairing cannot leave solution and the observed solid must be the other pairing available."),
 ("rise in oxidation number accompanies the loss of electrons",
  "EK 4.7.A.2 makes changes in oxidation number the indicator of electron transfer and EK 4.7.A.3 sends electrons from the oxidized species to the reduced one, so losing negative charge is what raises the assigned number."),
 ("Reaction II",
  "Recomputed in q22 above. EK 4.7.A.5 makes an insoluble ionic compound forming from ions in solution the mark of precipitation, while the deposited metal in another row accompanies an oxidation number change and so falls under EK 4.7.A.2."),
 ("rises from zero to positive four",
  "Recomputed in a23 from the convention stated in the stem. EK 4.7.A.4 makes oxidation numbers the way to identify the oxidized species, and the carbon rises while the iron falls."),
 ("whether a proton is transferred",
  "EK 4.7.A.1 defines the class by the transfer of one or more protons between chemical species. The definition is about the proton, so it applies wherever that transfer occurs regardless of what a reagent is called."),
 ("totals on each side match",
  "EK 4.7.A.3 has electrons pass from the species oxidized to the species reduced. Copper rises by two while each silver falls by one, and the two silver ions account for the two electrons a copper atom releases."),
 ("No precipitate of an ammonium or sodium compound",
  "EK 4.7.A.5 states that all sodium, potassium, ammonium and nitrate salts are soluble in water, and both new pairings available in this mixture are an ammonium salt or a sodium salt."),
 ("hydrogen rises from zero to positive one and oxygen falls",
  "EK 4.7.A.2 makes combustion a subclass of oxidation-reduction and makes changes in oxidation number the indicator of electron transfer; both elements begin uncombined at zero and end with opposite signs in water."),
 ("different oxidation number in the products",
  "EK 4.7.A.2 states that redox reactions involve transfer of electrons as indicated by changes in oxidation numbers, and EK 4.7.A.4 makes assigning those numbers an effective way to identify what was oxidized and reduced."),
 ("proton transfer can release a gas",
  "EK 4.7.A.2 makes a change in oxidation number the indicator of electron transfer, so its absence rules out the redox class, and EK 4.7.A.5 requires an insoluble solid for precipitation. EK 4.7.A.1's proton transfer is what remains."),
 ("copper stays at positive two throughout",
  "EK 4.7.A.1 defines acid-base by proton transfer and EK 4.7.A.2 requires a change in oxidation number for redox. The copper is positive two on both sides while the oxide ion accepts protons to become water."),
]


def _wreck_table(mod, cl):
    """Module-specific control: make a second element's oxidation number rise."""
    t = mod.QUESTIONS[7]["table"]
    mod.QUESTIONS[7]["table"] = dict(
        headers=t["headers"],
        rows=[[r[0], r[1], "+4"] if r[0] == "S" else list(r) for r in t["rows"]])


def _wreck_solubility(mod, cl):
    """Module-specific control: put a non-soluble-family pairing in the safe row."""
    t = mod.QUESTIONS[8]["table"]
    mod.QUESTIONS[8]["table"] = dict(
        headers=t["headers"],
        rows=[[r[0], "Na+, Cl-, Ba2+, SO4-"]
              if r[0].startswith("Sodium chloride") else list(r) for r in t["rows"]])


def _wreck_stem_number(mod, cl):
    """Module-specific control: change the stated oxygen convention."""
    mod.QUESTIONS[6]["choices"][0] = "+5"


def _reintroduce_excluded_term(mod, cl):
    mod.QUESTIONS[1]["why"] += " The zinc acts as the reducing agent throughout."


def _selftest():
    hn.selftest(M, CLAIMS, TABLE_CHECKS, arith=ARITH,
                extra=[("an oxidation-number cell corrupted", _wreck_table),
                       ("a solubility cell corrupted", _wreck_solubility),
                       ("a key edited away from its recomputed value", _wreck_stem_number)])
    # The exclusion gate is not part of hn.audit, so it gets its own control.
    mod = hn._mutant(M)
    _reintroduce_excluded_term(mod, CLAIMS)
    try:
        excluded_terms(mod, CLAIMS)
    except AssertionError as exc:
        print(f"  control OK  an excluded term reintroduced: {str(exc)[:88]}")
    else:
        raise SystemExit("CONTROL FAILED: an excluded term was not caught")


if __name__ == "__main__" and "--selftest" in sys.argv:
    _selftest()

excluded_terms(M, CLAIMS)
hn.audit(M, CLAIMS, TABLE_CHECKS, arith=ARITH)
