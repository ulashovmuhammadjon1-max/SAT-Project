"""Key audit for AP CHEMISTRY 9.8 Galvanic (Voltaic) and Electrolytic Cells.

One (anchor, claim) per item, in module order.

WHAT THE KEYS REST ON.

  9.8.A.1  the components and their roles, and the operational characteristics
           that can be described at both the macroscopic and particulate levels
                   1, 7, 9, 10, 11, 12, 13, 14, 16, 17, 18, 19, 28, 29
  9.8.A.2  galvanic cells run a thermodynamically favored reaction and
           electrolytic cells an unfavored one; visual representations are tools
           of analysis            4, 5, 6, 20, 21, 22, 23, 24, 30
  9.8.A.3  for ALL electrochemical cells, oxidation occurs at the anode and
           reduction at the cathode          2, 3, 8, 13, 14, 15, 18, 19, 25,
                                             26, 27
  4.7.A.3  electrons are transferred from the species oxidized to the species
           reduced, which is what fixes the direction of flow  8, 15, 16, 17, 19

THE FIGURE PROBLEM. EK 9.8.A.2 makes a visual representation the characteristic
tool of this topic and this bank cannot show one, so every cell is described in
words or carried as a table of observations. ``h9_check.no_figure_language``
asserts that nothing points at a picture -- the defect SCIENCE_BRIEF.md names
and the project has shipped once.

THE SWAP GUARD, which is the reason this verifier is longer than the topic
warrants. EK 9.8.A.3 is one sentence and it is the easiest in the unit to write
backwards. Two things are asserted:

  * no KEY anywhere in the module contains a reversed pairing -- oxidation at
    the cathode, or reduction at the anode. Distractors may and do; keys may
    not.
  * every anchor belonging to a pairing item names BOTH an electrode and a
    process. An anchor reading only "the anode" would match a key that had the
    process the wrong way round, which is exactly the defect the guard exists
    to make impossible.

SCOPE. 9.9 owns the cell potential and 9.11 owns Faraday's law, so no item
states a potential in volts or a charge in coulombs. The exclusion statement
attached to EK 9.8.A.3 bars labelling an electrode positive or negative, and
EK 4.7.A.3's own exclusion bars "reducing agent" and "oxidizing agent"; both are
asserted. The ban is written to catch the ASSERTION ("the anode is the negative
electrode"), not the mention -- one item states the exclusion itself and must
be able to say what it excludes.

NEGATIVE CONTROL: ``python3 verify_h9_8.py --selftest``.
"""
import re
import sys

import cg_check as cg
import h_check as h
import h9_check as h9

import h9_8

OBS = "Observation after one hour"
HOW = "How it operates"

# Explicit lookarounds, never \b. "voltage" is allowed -- EK 9.8.A.1 names the
# voltage measuring device -- so the unit is matched with a lookahead that
# refuses a following letter.
_OUT_OF_SCOPE = re.compile(
    r"(?<![A-Za-z])(cell potential|standard reduction potential|volts?|faraday|nernst|"
    r"coulombs?|amperes?|reducing agent|oxidizing agent)(?![A-Za-z])", re.I)

# The EXCLUSION statement attached to EK 9.8.A.3. Written to catch an assertion
# about a particular electrode, not the mention of the exclusion itself, since
# one item states what the framework excludes and has to name it.
_SIGNED_ELECTRODE = [
    re.compile(r"(?<![A-Za-z])(?:positive|negative)\s+(?:electrode|terminal)", re.I),
    re.compile(r"(?<![A-Za-z])(?:anode|cathode|electrode)\s+is\s+(?:the\s+)?"
               r"(?:positive|negative)", re.I),
]

# A reversed pairing of EK 9.8.A.3. Legitimate in a distractor, never in a key.
_REVERSED = [
    re.compile(r"(?<![A-Za-z])oxidation\s+(?:occurs\s+)?at\s+the\s+cathode", re.I),
    re.compile(r"(?<![A-Za-z])reduction\s+(?:occurs\s+)?at\s+the\s+anode", re.I),
    re.compile(r"(?<![A-Za-z])anode,?\s+where\s+reduction", re.I),
    re.compile(r"(?<![A-Za-z])cathode,?\s+where\s+oxidation", re.I),
]

# The framework's own pairing, in the phrasings the module uses.
_CORRECT = [
    re.compile(r"(?<![A-Za-z])oxidation\s+(?:occurs\s+)?at\s+the\s+anode", re.I),
    re.compile(r"(?<![A-Za-z])reduction\s+(?:occurs\s+)?at\s+the\s+cathode", re.I),
    re.compile(r"(?<![A-Za-z])anode,?\s+where\s+oxidation", re.I),
    re.compile(r"(?<![A-Za-z])cathode,?\s+where\s+reduction", re.I),
]

_ELECTRODE = re.compile(r"(?<![A-Za-z])(anode|cathode)(?![A-Za-z])", re.I)
_PROCESS = re.compile(r"(?<![A-Za-z])(oxidation|reduction|oxidized|reduced)(?![A-Za-z])",
                      re.I)
# Every word that carries part of EK 9.8.A.3's pairing, including the half-cell
# labels the tabulated items answer with.
_TOKENS = re.compile(
    r"(?<![A-Za-z])(anode|cathode|oxidation|reduction|oxidized|reduced|half-cell \d)"
    r"(?![A-Za-z])", re.I)

# Items whose key states EK 9.8.A.3's pairing. Listed explicitly so the guard
# cannot quietly stop covering an item that was edited.
PAIRING_ITEMS = (2, 3, 8, 13, 14, 19, 25, 26, 27)


def _tokens(text):
    return {m.group(1).lower() for m in _TOKENS.finditer(text)}


def _single_pairing(item):
    """The one electrode and the one process the item names, or None.

    Read from the stem AND the key together, because some items name the
    electrode in the stem ("where does oxidation occur?") and the process in
    the key, and others do the reverse. Returns None where more than one of
    either appears, which is the case the phrase patterns handle instead.
    """
    text = item["q"] + " " + h.keyed(item)
    electrodes = {m.group(1).lower() for m in _ELECTRODE.finditer(text)}
    processes = {("oxidation" if m.group(1).lower().startswith("oxid") else "reduction")
                 for m in _PROCESS.finditer(text)}
    if len(electrodes) == 1 and len(processes) == 1:
        return electrodes.pop(), processes.pop()
    return None


def no_out_of_scope(module):
    for i, item in enumerate(module.QUESTIONS, 1):
        for text in h9.facing(item):
            hit = _OUT_OF_SCOPE.search(text)
            assert not hit, (
                f"{module.TOPIC[0]} q{i}: mentions {hit.group(0)!r}, which belongs to 9.9 "
                f"or 9.11, or is excluded by EK 4.7.A.3 -- {text[:70]!r}"
            )
    print(f"OK  {module.TOPIC[0]} scope: no cell potential, no charge, and neither term "
          "EK 4.7.A.3's exclusion statement bars.")


def no_signed_electrode(module):
    """The exclusion statement attached to EK 9.8.A.3."""
    for i, item in enumerate(module.QUESTIONS, 1):
        for text in h9.facing(item):
            for pat in _SIGNED_ELECTRODE:
                hit = pat.search(text)
                assert not hit, (
                    f"{module.TOPIC[0]} q{i}: labels an electrode {hit.group(0)!r}, which "
                    f"the exclusion statement attached to EK 9.8.A.3 places outside the "
                    f"exam -- {text[:70]!r}"
                )
    print(f"OK  {module.TOPIC[0]} exclusion: no item labels an electrode as positive or "
          "negative, which EK 9.8.A.3's exclusion statement bars.")


def pairing_guard(module, claims):
    """EK 9.8.A.3 in one direction only, in every key and every pairing anchor.

    Three separate assertions, each named for what it forbids:

    1. No KEY anywhere contains a reversed pairing phrase. Distractors may and
       do; a key may not.
    2. Every pairing item's key is internally consistent -- either it states the
       framework's pairing in one of the phrasings the module uses, or it names
       exactly one electrode and one process (counting the stem as well as the
       key) and those two pair correctly. Named booleans, never two parallel
       tuples compared by index.
    3. Every pairing anchor carries EVERY pairing word its key carries. An
       anchor that dropped one -- "Half-cell 1" where the key says "Half-cell 1,
       where oxidation occurs" -- would still match a key with the process
       swapped, which is the defect this guard exists to make impossible.
    """
    for i, item in enumerate(module.QUESTIONS, 1):
        key = h.keyed(item)
        for pat in _REVERSED:
            hit = pat.search(key)
            assert not hit, (
                f"{module.TOPIC[0]} q{i}: the key says {hit.group(0)!r}, which is EK "
                f"9.8.A.3 backwards -- {key!r}"
            )
    for i in PAIRING_ITEMS:
        item = module.QUESTIONS[i - 1]
        key = h.keyed(item)
        anchor = claims[i - 1][0]

        states_the_pairing = any(p.search(key) for p in _CORRECT)
        if not states_the_pairing:
            pair = _single_pairing(item)
            assert pair, (
                f"{module.TOPIC[0]} q{i}: the key states no pairing and the item does not "
                f"name exactly one electrode and one process: {key!r}"
            )
            electrode, process = pair
            names_the_anode = electrode == "anode"
            names_oxidation = process == "oxidation"
            assert names_the_anode == names_oxidation, (
                f"{module.TOPIC[0]} q{i}: pairs the {electrode} with {process}, which is EK "
                f"9.8.A.3 backwards -- {key!r}"
            )

        missing = sorted(_tokens(key) - _tokens(anchor))
        assert not missing, (
            f"{module.TOPIC[0]} q{i}: the anchor {anchor!r} drops {missing} from the key, so "
            f"a key with the pairing swapped would still match it"
        )
    print(f"OK  {module.TOPIC[0]} swap guard: no key reverses EK 9.8.A.3, each of the "
          f"{len(PAIRING_ITEMS)} pairing keys is internally consistent, and each anchor "
          "carries every pairing word its key carries.")


# ------------------------------------------------------------------ table items

def _observation(table, label):
    return str(dict(zip(cg.labels(table), table["rows"]))[label][3]).strip().lower()


def _losing_and_gaining(table):
    losing = [lab for lab in cg.labels(table) if "loses mass" in _observation(table, lab)]
    gaining = [lab for lab in cg.labels(table) if "gains mass" in _observation(table, lab)]
    assert len(losing) == 1 and len(gaining) == 1, (
        f"the table must have exactly one electrode losing mass and one gaining it: "
        f"losing {losing}, gaining {gaining}"
    )
    return losing[0], gaining[0]


def q13(table, item):
    losing, gaining = _losing_and_gaining(table)
    assert losing == "Half-cell 1", f"the tabulated electrode losing mass is in {losing}"
    h.shows(item, "Half-cell 1, where oxidation occurs and the electrode loses mass")
    return (f"the tabulated observations put the mass loss in {losing} and the mass gain in "
            f"{gaining}, and a metal oxidized to ions leaves the electrode it came from")


def q14(table, item):
    losing, gaining = _losing_and_gaining(table)
    assert gaining == "Half-cell 2", f"the tabulated electrode gaining mass is in {gaining}"
    h.shows(item, "Half-cell 2, where reduction occurs and the electrode gains mass")
    return (f"the tabulated observations put the mass gain in {gaining}, where ions reduced "
            f"onto the electrode add to it")


def q15(table, item):
    losing, gaining = _losing_and_gaining(table)
    assert losing == "Half-cell 1" and gaining == "Half-cell 2", (
        f"the tabulated mass changes are losing {losing}, gaining {gaining}"
    )
    h.shows(item, "From the electrode in half-cell 1 to the electrode in half-cell 2")
    return (f"EK 4.7.A.3 sends electrons from the oxidized species, which the tabulated "
            f"mass loss locates in {losing}, to the reduced species in {gaining}")


def q16(table, item):
    losing, gaining = _losing_and_gaining(table)
    assert losing != gaining, "the two changes must be at different electrodes"
    h.shows(item, "Metal atoms leave the electrode being oxidized")
    return (f"the table records opposite mass changes at {losing} and {gaining}, which is "
            f"what atoms leaving one electrode and ions arriving at the other produces")


def _cell_kind(table, label):
    """Electrolytic if the tabulated description names an external power supply."""
    how = str(dict(zip(cg.labels(table), table["rows"]))[label][1]).lower()
    driven = "power supply" in how
    unaided = "nothing else connected" in how
    assert driven != unaided, (
        f"the tabulated description of {label} says neither clearly that it is driven nor "
        f"clearly that it runs unaided: {how!r}"
    )
    return "electrolytic" if driven else "galvanic"


def q22(table, item):
    kinds = {lab: _cell_kind(table, lab) for lab in cg.labels(table)}
    galvanic = sorted(lab for lab, k in kinds.items() if k == "galvanic")
    assert galvanic == ["Cell 1", "Cell 4"], f"the tabulated galvanic cells are {galvanic}"
    h.shows(item, "Cells 1 and 4")
    return (f"reading each tabulated description for an external power supply classifies "
            f"the cells as {kinds}")


def q23(table, item):
    kinds = {lab: _cell_kind(table, lab) for lab in cg.labels(table)}
    electrolytic = sorted(lab for lab, k in kinds.items() if k == "electrolytic")
    assert electrolytic == ["Cell 2", "Cell 3"], (
        f"the tabulated electrolytic cells are {electrolytic}"
    )
    h.shows(item, "Cells 2 and 3")
    return (f"the tabulated descriptions naming an external power supply are {electrolytic}, "
            f"which EK 9.8.A.2 makes the electrolytic ones")


def q24(table, item):
    kinds = {lab: _cell_kind(table, lab) for lab in cg.labels(table)}
    unfavored = sorted(lab for lab, k in kinds.items() if k == "electrolytic")
    assert unfavored == ["Cell 2", "Cell 3"], (
        f"the tabulated cells running an unfavored reaction are {unfavored}"
    )
    h.shows(item, "Cells 2 and 3, which are the electrolytic cells")
    return (f"EK 9.8.A.2 ties the electrolytic cells {unfavored} to a thermodynamically "
            f"unfavored reaction, and those are the tabulated rows needing a supply")


TABLE_CHECKS = {13: q13, 14: q14, 15: q15, 16: q16, 22: q22, 23: q23, 24: q24}

NUMERIC = {}


CLAIMS = [
 ("electrodes, the solutions in the half-cells, the salt bridge, and the voltage",
  "EK 9.8.A.1 lists exactly these components as each playing a specific role in the overall functioning of the cell."),
 ("Oxidation occurs at the anode and reduction occurs at the cathode",
  "EK 9.8.A.3, verbatim: for ALL electrochemical cells, so the pairing does not depend on whether the cell is galvanic or electrolytic."),
 ("The cathode, where reduction occurs, while oxidation occurs at the anode",
  "EK 9.8.A.3 assigns reduction to the cathode and oxidation to the anode, so naming one electrode by its process fixes the other."),
 ("A thermodynamically favored reaction",
  "EK 9.8.A.2: galvanic, sometimes called voltaic, cells involve a thermodynamically favored reaction."),
 ("A thermodynamically unfavored reaction",
  "EK 9.8.A.2's other half, which is why EK 9.7.A.1 lists electrical energy driving an electrolytic cell as an external source of energy."),
 ("A voltaic cell",
  "EK 9.8.A.2 opens with the phrase galvanic, sometimes called voltaic, cells."),
 ("Labelling an electrode as positive or as negative",
  "The exclusion statement attached to EK 9.8.A.3 names exactly this, while EK 9.8.A.1 keeps electron flow, electrode mass and the half-cell reactions in scope."),
 ("From the anode, where oxidation occurs, to the cathode, where reduction occurs",
  "EK 4.7.A.3 sends electrons from the species oxidized to the species reduced, and EK 9.8.A.3 places those at the anode and the cathode respectively."),
 ("allows ions to move between the half-cells so charge does not build up",
  "EK 9.8.A.1 lists the salt bridge as a component with a specific role and names ion flow through it among the operational characteristics; electrons travel through the wire."),
 ("reports the electrical behaviour of the cell while it operates",
  "EK 9.8.A.1 lists the voltage or current measuring device among the components with a specific role; driving an electrolytic cell is the external supply's job under EK 9.7.A.1."),
 ("surfaces at which the two half-reactions take place",
  "EK 9.8.A.1 lists the electrodes among the components with a role, and EK 9.8.A.3 places one half-reaction at each."),
 ("supply the species that are oxidized or reduced",
  "EK 9.8.A.1 lists the solutions in the half-cells among the components with a role and names the reactions occurring in each half-cell as an observable characteristic."),
 ("Half-cell 1, where oxidation occurs and the electrode loses mass",
  "EK 9.8.A.3 puts oxidation at the anode and EK 4.7.A.3 makes it the loss of electrons, so an oxidized metal electrode passes into solution. q13 reads the tabulated mass changes."),
 ("Half-cell 2, where reduction occurs and the electrode gains mass",
  "EK 9.8.A.3 puts reduction at the cathode, where ions reduced onto the electrode add to its mass. q14 reads the tabulated mass changes."),
 ("From the electrode in half-cell 1 to the electrode in half-cell 2",
  "EK 4.7.A.3 sends electrons from the oxidized species to the reduced one, and q15 locates each from the tabulated mass changes rather than from the electrode names."),
 ("Metal atoms leave the electrode being oxidized",
  "EK 9.8.A.3 and EK 4.7.A.3 together: atoms leave one electrode as ions and ions arrive at the other as atoms. q16 checks the table really records opposite changes."),
 ("falls, because atoms leave the electrode as ions when they are oxidized",
  "EK 4.7.A.3 makes oxidation the transfer of electrons away from the species oxidized, and EK 9.8.A.1 names change in electrode mass as an observable characteristic."),
 ("rises, because reduced ions are deposited on the electrode as metal atoms",
  "EK 9.8.A.3 puts reduction at the cathode, where ions gaining electrons build up as metal on the surface."),
 ("Reduction, so that electrode is the cathode",
  "Hydrogen ions gaining electrons is a gain of electrons, which EK 4.7.A.3 identifies as reduction, and EK 9.8.A.3 places reduction at the cathode. EK 9.8.A.1 names gas evolution as an observable."),
 ("An electrolytic cell, involving a thermodynamically unfavored reaction",
  "EK 9.8.A.2 pairs the electrolytic cell with an unfavored reaction, and EK 9.7.A.1 names electrical energy driving one as an external source of energy."),
 ("A galvanic cell, involving a thermodynamically favored reaction",
  "EK 9.8.A.2 pairs the galvanic cell with a favored reaction, which proceeds without being driven."),
 ("Cells 1 and 4",
  "EK 9.8.A.2's distinction applied to four tabulated descriptions. q22 classifies each row by whether it names an external power supply."),
 ("Cells 2 and 3",
  "EK 9.8.A.2's other half, applied the same way. q23 classifies each tabulated row."),
 ("Cells 2 and 3, which are the electrolytic cells",
  "EK 9.8.A.2 ties the electrolytic cell to a thermodynamically unfavored reaction. q24 recomputes the classification from the tabulated descriptions."),
 ("At the anode, as in every electrochemical cell",
  "EK 9.8.A.3 covers ALL electrochemical cells, so being driven from outside changes the favorability under EK 9.8.A.2 and not the naming of the electrodes."),
 ("At the cathode, as in every electrochemical cell",
  "EK 9.8.A.3 again covers all cells without exception, putting reduction at the cathode whether the reaction is favored or unfavored."),
 ("Oxidation occurs at the anode, and reduction occurs at the cathode",
  "EK 9.8.A.3 assigns the processes the other way round from the student's statement, and does so for both types of cell alike."),
 ("charge would build up in each solution and the reaction would stop",
  "EK 9.8.A.1 lists the salt bridge as a component with a specific role and names ion flow through it as an observable characteristic; the electrons themselves travel through the wire."),
 ("At both the macroscopic and the particulate levels",
  "EK 9.8.A.1 says the operational characteristics of the cell can be described at both the macroscopic and particulate levels."),
 ("tools of analysis for identifying where the half-reactions occur",
  "EK 9.8.A.2 says visual representations of galvanic and electrolytic cells are tools of analysis to identify where half-reactions occur and in what direction current flows."),
]


def _extra_mutations():
    def figure_language(mod, cl):
        mod.QUESTIONS[0]["q"] = "In the cell shown, which components have a role?"
        h9.no_figure_language(mod)

    def cell_potential_creeps_in(mod, cl):
        mod.QUESTIONS[0]["why"] = mod.QUESTIONS[0]["why"] + " It reads 1.10 volts."
        no_out_of_scope(mod)

    def electrode_given_a_sign(mod, cl):
        ch = list(mod.QUESTIONS[1]["choices"])
        ch[4] = "The anode is the negative electrode in every cell"
        mod.QUESTIONS[1]["choices"] = ch
        no_signed_electrode(mod)

    def key_reverses_the_pairing(mod, cl):
        # The number of clauses and the shape of the sentence are untouched;
        # only the pairing is turned round. Confirmed to violate the reversed
        # patterns rather than any structural check.
        ch = list(mod.QUESTIONS[1]["choices"])
        ch[0] = "Reduction occurs at the anode and oxidation occurs at the cathode"
        mod.QUESTIONS[1]["choices"] = ch
        cl[1] = ("Reduction occurs at the anode and oxidation occurs at the cathode",
                 cl[1][1])
        pairing_guard(mod, cl)

    def anchor_drops_the_process(mod, cl):
        # The key says "Half-cell 1, where oxidation occurs"; an anchor of just
        # the label would match a key that said "where reduction occurs" too.
        cl[12] = ("Half-cell 1", cl[12][1])
        pairing_guard(mod, cl)

    def anchor_drops_the_second_clause(mod, cl):
        cl[26] = ("Oxidation occurs at the anode", cl[26][1])
        pairing_guard(mod, cl)

    def key_pairs_the_wrong_process(mod, cl):
        # The stem asks where OXIDATION occurs in an electrolytic cell and the
        # key answers "the cathode". No reversed phrase appears, so only the
        # single-pairing rule can catch it.
        ch = list(mod.QUESTIONS[24]["choices"])
        ch[0] = "At the cathode, as in every electrochemical cell"
        mod.QUESTIONS[24]["choices"] = ch
        cl[24] = ("At the cathode, as in every electrochemical cell", cl[24][1])
        pairing_guard(mod, cl)

    def mass_changes_exchanged(mod, cl):
        mod.QUESTIONS[12]["table"] = dict(
            headers=h9_8._T_ZNCU["headers"],
            rows=[["Half-cell 1", "zinc", "1.0 M zinc nitrate", "the electrode gains mass"],
                  ["Half-cell 2", "copper", "1.0 M copper(II) nitrate",
                   "the electrode loses mass"]])

    def both_electrodes_lose_mass(mod, cl):
        mod.QUESTIONS[14]["table"] = dict(
            headers=h9_8._T_ZNCU["headers"],
            rows=[["Half-cell 1", "zinc", "1.0 M zinc nitrate", "the electrode loses mass"],
                  ["Half-cell 2", "copper", "1.0 M copper(II) nitrate",
                   "the electrode loses mass"]])

    def cell_descriptions_reclassified(mod, cl):
        mod.QUESTIONS[21]["table"] = dict(
            headers=h9_8._T_TYPES["headers"],
            rows=[["Cell 1", "it requires an external power supply before any change occurs"],
                  ["Cell 2", "it requires an external power supply before any change occurs"],
                  ["Cell 3", "it uses an external power supply to reverse a battery reaction"],
                  ["Cell 4", "it turns a small motor with nothing else connected"]])

    def ambiguous_cell_description(mod, cl):
        mod.QUESTIONS[21]["table"] = dict(
            headers=h9_8._T_TYPES["headers"],
            rows=[["Cell 1", "it operates in a way the description does not settle"],
                  ["Cell 2", "it requires an external power supply before any change occurs"],
                  ["Cell 3", "it uses an external power supply to reverse a battery reaction"],
                  ["Cell 4", "it turns a small motor with nothing else connected"]])

    return [
        ("a stem pointing at a cell the bank cannot show", figure_language),
        ("a why stating a potential in volts, which is 9.9's material",
         cell_potential_creeps_in),
        ("a choice labelling an electrode negative, which EK 9.8.A.3's exclusion bars",
         electrode_given_a_sign),
        ("a key pairing oxidation with the cathode, which is EK 9.8.A.3 backwards",
         key_reverses_the_pairing),
        ("a pairing anchor cut down to the half-cell label alone", anchor_drops_the_process),
        ("a pairing anchor that drops the key's second clause",
         anchor_drops_the_second_clause),
        ("a key naming the cathode where the stem asks about oxidation",
         key_pairs_the_wrong_process),
        ("the two tabulated electrode mass changes exchanged", mass_changes_exchanged),
        ("both tabulated electrodes made to lose mass", both_electrodes_lose_mass),
        ("a tabulated cell description changed so the keyed pair is wrong",
         cell_descriptions_reclassified),
        ("a tabulated description that settles neither classification",
         ambiguous_cell_description),
    ]


if __name__ == "__main__" and "--selftest" in sys.argv:
    h.selftest(h9_8, CLAIMS, table_checks=TABLE_CHECKS, numeric_checks=NUMERIC,
               mutations=_extra_mutations())

h9.no_figure_language(h9_8)
no_out_of_scope(h9_8)
no_signed_electrode(h9_8)
pairing_guard(h9_8, CLAIMS)
h.run(h9_8, CLAIMS, table_checks=TABLE_CHECKS, numeric_checks=NUMERIC)
