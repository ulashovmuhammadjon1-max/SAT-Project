"""Key audit for AP CHEMISTRY 4.8 Introduction to Acid-Base Reactions.

One ``(anchor, claim)`` per item, in module order; the anchor must appear in the
KEYED choice and in no distractor. Five table items are recomputed from their own
stimulus.

WHAT THE KEYS REST ON
---------------------
EK 4.8.A.1  By definition, a Bronsted-Lowry acid is a proton donor and a
            Bronsted-Lowry base is a proton acceptor.
            (items 1, 2, 3, 4, 9, 12, 15, 16, 17, 19, 20, 24, 28, 29)
EK 4.8.A.2  Water plays an important role in many acid-base reactions, as its
            molecular structure allows it to accept protons from and donate
            protons to dissolved species.  (items 7, 12, 20, 27, 30)
EK 4.8.A.3  When an acid or base ionizes in water, the conjugate acid-base pairs
            can be identified and their relative strengths compared.
            (items 5, 6, 8, 10, 11, 13, 14, 18, 21, 22, 23, 25, 26)

Items 5, 6, 10, 11, 18, 23, 25 and 29 all turn on one fact that EK 4.8.A.1 and
4.8.A.3 make between them: a conjugate pair is two species separated by ONE
transferred proton, so the hydrogen count and the charge each differ by one.
They ask it in seven different directions -- name the conjugate base, name the
conjugate acid, pick a valid pair, reject an invalid one, count the pairs in a
polyprotic series, reason from the charges alone, and state the relationship --
which is what LO 4.8.A asks a student to be able to do.

RELATIVE STRENGTH, items 13, 14, 21 and 26: every comparison is made from data
given in the item, either a tabulated percent ionization or a stated extent of
reaction. None rests on a Ka value, a pH or any constant a student would have to
recall; those belong to Unit 8.

THE EXCLUSION STATEMENT, CHECKED MECHANICALLY: "Lewis acid-base concepts will
not be assessed on the AP Exam." ``excluded_terms`` fails the module if the
phrase reappears in any stem, choice, rationale or claim, and the selftest
reintroduces it on purpose to prove the check fires.

NEGATIVE CONTROL: ``python3 verify_h4_8.py --selftest``.
"""
import re
import sys

import h_chem_notation as hn
import h4_8 as M

PCT = "Percent of the acid ionized in 0.10 M aqueous solution"
LOSES = "Species that loses a proton"
GAINS = "Species that gains a proton"
GIVE = "Number of protons the species can donate"
TAKE = "Can the species accept a proton?"
MINUS = "Formula obtained by removing one proton"
PLUS = "Formula obtained by adding one proton"

_BANNED_TERMS = [re.compile(r"(?<![a-z])lewis\s+(acid|base)", re.I)]


def excluded_terms(module, claims):
    """The CED excludes Lewis acid-base concepts from assessment."""
    texts = []
    for item in module.QUESTIONS:
        texts += hn.texts(item)
    texts += [c for pair in claims for c in pair]
    for text in texts:
        for pat in _BANNED_TERMS:
            hit = pat.search(text)
            assert not hit, (
                f"{module.TOPIC[0]}: {hit.group(0)!r} appears in {text[:70]!r}, but the "
                "CED's exclusion statement says Lewis acid-base concepts are not assessed"
            )
    print(f"OK  {module.TOPIC[0]} exclusions: no Lewis acid-base language in "
          f"{len(texts)} strings.")


# ------------------------------------------------------------ table questions

def q12(t, item):
    labs = hn.cg.labels(t)
    loses = {r[0]: r[1] for r in t["rows"]}
    gains = {r[0]: r[2] for r in t["rows"]}
    donor_water = [l for l in labs if loses[l] == "H2O"]
    assert len(donor_water) == 1, f"rows in which water donates: {donor_water}"
    assert "NH3" in donor_water[0], f"the water-as-donor row is {donor_water[0]}"
    acceptor_water = [l for l in labs if gains[l] == "H2O"]
    assert acceptor_water and acceptor_water != donor_water, \
        "water must also appear as an acceptor somewhere, so 'always an acid' is false"
    hn.keyed(item, "water is the species that loses a proton")
    return (f"of {len(labs)} tabulated reactions exactly one lists water as the species "
            "losing a proton, and a different one lists it as the species gaining one")


def q13(t, item):
    pct = dict(zip(hn.cg.labels(t), hn.cg.col(t, PCT)))
    top = max(pct, key=pct.get)
    assert top == "HA", f"the largest ionized fraction belongs to {top}"
    assert len(set(pct.values())) == len(pct), \
        "'all four equally' must be false, so no two percentages may match"
    hn.keyed(item, "HA, because the largest fraction")
    return (f"the tabulated percentages are {sorted(pct.values())} and the largest, "
            f"{pct[top]}, belongs to {top}")


def q14(t, item):
    pct = dict(zip(hn.cg.labels(t), hn.cg.col(t, PCT)))
    bottom = min(pct, key=pct.get)
    assert bottom == "HE", f"the smallest ionized fraction belongs to {bottom}"
    assert pct[bottom] < 0.05 * max(pct.values()), \
        "the least ionized acid should be far below the most ionized one"
    hn.keyed(item, "conjugate base of HE")
    return (f"{bottom} ionizes {pct[bottom]} percent against {max(pct.values())} for the "
            "most ionized acid, so it is the one that parts with its proton least readily")


def q17(t, item):
    labs = hn.cg.labels(t)
    give = dict(zip(labs, hn.cg.col(t, GIVE)))
    take = {r[0]: r[2].strip().lower() for r in t["rows"]}
    only_base = [l for l in labs if give[l] == 0 and take[l] == "yes"]
    assert only_base == ["Cl-"], f"species that can only accept: {only_base}"
    assert give["NH4+"] > 0 and take["NH4+"] == "no", \
        "the ammonium distractor must be an acid-only species, not a base-only one"
    assert max(give, key=give.get) == "H2PO4-", \
        "the 'donates the most' distractor must point at the dihydrogen phosphate row"
    hn.keyed(item, "no proton to donate while it can still accept one")
    return ("exactly one row records zero protons available to donate together with the "
            "ability to accept one, and the other three can each donate at least one")


def q20(t, item):
    labs = hn.cg.labels(t)
    minus = {r[0]: r[1] for r in t["rows"]}
    plus = {r[0]: r[2] for r in t["rows"]}
    both = [l for l in labs if minus[l].strip() and plus[l].strip()
            and minus[l] != l and plus[l] != l]
    assert both == labs, f"rows carrying both a conjugate base and a conjugate acid: {both}"
    assert len(labs) == 4, f"the key says all four, but the table has {len(labs)} rows"
    charged = [l for l in labs if "+" in l or "-" in l]
    assert charged and len(charged) < len(labs), \
        "'only the ions' and 'only the neutral one' must both be false, so the table must mix them"
    hn.keyed(item, "All four")
    return (f"every one of the {len(labs)} rows supplies a formula both for removing a "
            "proton and for adding one, and the rows are a mix of neutral species and ions")


TABLE_CHECKS = {12: q12, 13: q13, 14: q14, 17: q17, 20: q20}

CLAIMS = [
 ("A proton donor",
  "EK 4.8.A.1, verbatim: by definition, a Bronsted-Lowry acid is a proton donor. Conductivity and the presence of any particular element appear nowhere in that definition."),
 ("A proton acceptor",
  "EK 4.8.A.1, verbatim: a Bronsted-Lowry base is a proton acceptor. Containing hydroxide is one way to accept a proton but is not required, as ammonia shows."),
 ("gives up a proton to the water molecule",
  "EK 4.8.A.1 makes a Bronsted-Lowry acid a proton donor, and comparing the two sides of the equation shows HF losing a hydrogen while the water gains one."),
 ("accepts a proton from the water molecule",
  "EK 4.8.A.1 makes a Bronsted-Lowry base a proton acceptor. Ammonia gains a hydrogen to become the ammonium ion, so here the water is the donor and the ammonia the acceptor."),
 ("NO2-",
  "A conjugate base is what a Bronsted-Lowry acid becomes after donating the proton EK 4.8.A.1 defines it by, so under EK 4.8.A.3 the pair differs by exactly one hydrogen and one unit of charge."),
 ("H2PO4-",
  "A conjugate acid is what a Bronsted-Lowry base becomes after accepting a proton, so it carries one more hydrogen and a charge one unit more positive than the base it came from."),
 ("accept protons from and donate protons to dissolved species",
  "EK 4.8.A.2, near verbatim: water's molecular structure allows it to accept protons from and donate protons to dissolved species. The structure does not change between the two reactions."),
 ("HCN and CN-",
  "EK 4.8.A.3 has the conjugate acid-base pairs identified when an acid ionizes in water. A pair is one species before and after a single proton has moved, so the two members differ by exactly one hydrogen."),
 ("proton acceptor in one reaction and a proton donor in the other",
  "EK 4.8.A.1 defines an acid as a proton donor and a base as a proton acceptor. Gaining a hydrogen to become carbonic acid is acceptance and losing one to become the carbonate ion is donation."),
 ("H2SO4 and HSO4-",
  "EK 4.8.A.3's conjugate pairs are related by a single transferred proton, which changes the hydrogen count by one and the charge by one unit; only one of the listed pairs meets both conditions."),
 ("differ by two protons rather than one",
  "EK 4.8.A.3 identifies conjugate pairs from a single proton transfer. Turning the hydronium ion into hydroxide would require two hydrogens to be removed, so neither species is the conjugate of the other."),
 ("water is the species that loses a proton",
  "Recomputed in q12 above from the table's own donor and acceptor columns. EK 4.8.A.1 makes the donor the acid, and exactly one tabulated reaction lists water in that column."),
 ("HA, because the largest fraction",
  "Recomputed in q13 above. EK 4.8.A.1 makes an acid a proton donor and EK 4.8.A.3 allows relative strengths to be compared on ionization in water, so at equal concentration the largest ionized fraction has donated most readily."),
 ("conjugate base of HE",
  "Recomputed in q14 above. EK 4.8.A.3 allows the relative strengths of conjugate pairs to be compared; the acid that parted with its proton least readily is the one whose conjugate base is most inclined to keep a proton."),
 ("each is the species that can donate a proton",
  "EK 4.8.A.1 makes an acid a proton donor. Read forward the hydrogen sulfate ion is the donor; read in reverse the hydronium ion can hand a proton to the sulfate ion, so each direction has its own."),
 ("contains no hydrogen atom to donate",
  "EK 4.8.A.1 defines a Bronsted-Lowry acid as a proton donor, and a species holding no hydrogen atom has no proton to donate. Carrying a charge, of either sign, prevents nothing."),
 ("no proton to donate while it can still accept one",
  "Recomputed in q17 above. EK 4.8.A.1 makes donation the mark of an acid and acceptance the mark of a base, and exactly one tabulated row records zero available protons together with acceptance."),
 ("each adjacent species differs from the next by one proton",
  "EK 4.8.A.3 identifies conjugate pairs from an ionization, and a pair is related by a single proton transfer. The first and third species of a two-step series differ by two protons and so are not a pair."),
 ("accepts the proton released by the ammonium ion",
  "EK 4.8.A.1 makes a base a proton acceptor. The hydroxide ion gains a hydrogen to become water, while ammonia appears here among the products rather than the reactants."),
 ("All four",
  "Recomputed in q20 above. EK 4.8.A.1 makes donation the mark of an acid and acceptance the mark of a base, and every tabulated row supplies a formula for both operations."),
 ("far more X- than HX",
  "EK 4.8.A.3 has the conjugate pair identified when an acid ionizes in water. If nearly every molecule has donated its proton, nearly all of the acid is present as its conjugate base."),
 ("Two pairs",
  "EK 4.8.A.3 has conjugate pairs identified when an acid ionizes in water. One proton moves, but it leaves a donor behind and arrives at an acceptor, so each of those two species pairs with what it became."),
 ("more negative species the base of the two",
  "EK 4.8.A.3 relates the members of a conjugate pair by one transferred proton, which carries one positive charge. The more negative member is the one that has already given the proton up and so is the acceptor of the two."),
 ("acetic acid donates a proton and the ammonia accepts",
  "EK 4.8.A.1 defines the two roles by donation and acceptance. Comparing the two sides shows the acid losing a hydrogen to become the acetate ion and the ammonia gaining one to become the ammonium ion."),
 ("differ by exactly one proton",
  "EK 4.8.A.3 identifies conjugate pairs by proton transfer, and a proton is a hydrogen nucleus carrying one positive charge, so both the hydrogen count and the charge shift by exactly one unit."),
 ("D- accepts a proton more readily",
  "EK 4.8.A.3 allows the relative strengths of conjugate pairs to be compared. The acid that mostly keeps its proton has a conjugate base that takes a proton back readily, which is what the stated extents of reaction describe."),
 ("with HBr the donor and water the acceptor",
  "EK 4.8.A.1 makes the donor the acid and the acceptor the base, and EK 4.8.A.2 has water accept protons from dissolved species. The rejected equations also fail to conserve atoms or charge."),
 ("one more hydrogen atom after the reaction",
  "EK 4.8.A.1 makes a base a proton acceptor. A proton is a hydrogen nucleus, so acceptance shows up as one more hydrogen atom on the species than it carried before."),
 ("HPO4 2- as the acid product",
  "EK 4.8.A.1 makes acceptance the mark of a base and donation the mark of an acid. Accepting adds one hydrogen and one unit of positive charge; donating removes one of each."),
 ("accepting a proton in one reaction and donating a proton in another",
  "EK 4.8.A.2 states that water plays an important role in many acid-base reactions because its molecular structure allows it to accept protons from and donate protons to dissolved species; both roles are named in the statement."),
]


def _wreck_ionization(mod, cl):
    """Module-specific control: make a different acid the most ionized."""
    t = mod.QUESTIONS[12]["table"]
    mod.QUESTIONS[12]["table"] = dict(
        headers=t["headers"],
        rows=[[r[0], "99"] if r[0] == "HD" else list(r) for r in t["rows"]])


def _wreck_roles(mod, cl):
    """Module-specific control: put water on the wrong side of a proton transfer."""
    t = mod.QUESTIONS[11]["table"]
    mod.QUESTIONS[11]["table"] = dict(
        headers=t["headers"],
        rows=[[r[0], "NH3", "H2O"] if r[0].startswith("NH3") else list(r)
              for r in t["rows"]])


def _wreck_candidates(mod, cl):
    """Module-specific control: give the base-only species a proton to donate."""
    t = mod.QUESTIONS[16]["table"]
    mod.QUESTIONS[16]["table"] = dict(
        headers=t["headers"],
        rows=[[r[0], "1", r[2]] if r[0] == "Cl-" else list(r) for r in t["rows"]])


def _reintroduce_excluded_term(mod, cl):
    mod.QUESTIONS[0]["why"] += " A Lewis acid accepts an electron pair instead."


def _selftest():
    hn.selftest(M, CLAIMS, TABLE_CHECKS,
                extra=[("a percent-ionization cell corrupted", _wreck_ionization),
                       ("a proton-transfer role cell corrupted", _wreck_roles),
                       ("a donatable-proton cell corrupted", _wreck_candidates)])
    mod = hn._mutant(M)
    _reintroduce_excluded_term(mod, CLAIMS)
    try:
        excluded_terms(mod, CLAIMS)
    except AssertionError as exc:
        print(f"  control OK  an excluded concept reintroduced: {str(exc)[:88]}")
    else:
        raise SystemExit("CONTROL FAILED: Lewis acid-base language was not caught")


if __name__ == "__main__" and "--selftest" in sys.argv:
    _selftest()

excluded_terms(M, CLAIMS)
hn.audit(M, CLAIMS, TABLE_CHECKS)
