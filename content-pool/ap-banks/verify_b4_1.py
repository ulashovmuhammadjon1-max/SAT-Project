"""Key audit for AP BIOLOGY 4.1 Cell Communication.

One (anchor, claim) per item, in module order. The anchor is a distinctive
substring that must appear in the keyed choice and in no distractor, so the key
survives the shuffle ``export_units.py`` applies on export.

WHAT THE KEYS REST ON
---------------------
  4.1.A.1  cells communicate through DIRECT CONTACT or FROM A DISTANCE via
           CHEMICAL SIGNALING
  4.1.B.1  short distances: LOCAL REGULATORS targeting cells IN THE VICINITY
           of the signal-emitting cell
  4.1.B.2  signals released by ONE CELL TYPE travel LONG distances to TARGET
           CELLS OF ANOTHER TYPE

Eleven items name one of the CED's own illustrative examples. Each of those
keys is a CLASSIFICATION -- which of the three statements above the CED lists
that example under -- and never a mechanism the CED does not print for it:

  under EK 4.1.A.1   immune cells interacting through cell-to-cell contact:
                     antigen-presenting cells, helper T-cells, killer T-cells
  under EK 4.1.B.1   neurotransmitters; plant immune response; quorum sensing
                     in bacteria; morphogens in embryonic development
  under EK 4.1.B.2   insulin; human growth hormone; thyroid hormones;
                     testosterone; estrogen

BOUNDARY WITH 4.2 AND 4.3. Ligands, receptors, the ligand-binding domain, G
protein-coupled receptors, phosphorylation cascades, second messengers,
amplification and ligand-gated channels belong to topic 4.2; changes in gene
expression, apoptosis, mutations in pathway components and activating or
inhibiting chemicals belong to topic 4.3. No key here rests on any of them.
This module is confined to the MODE of communication and the DISTANCE it
covers.

Items 15, 16, 17 and 18 carry tables. Every number is HYPOTHETICAL and the stem
says so; each keyed conclusion is recomputed below from the table alone, and
the distractors are shown false against the same numbers. No stem refers to a
figure.

FIVE choices per item (A-E), per SCIENCE_BRIEF.md.
"""
import cg_check as cg
import b4_1

DISTANCE = b4_1._T_DISTANCE
TARGET = b4_1._T_TARGET
CONTACT = b4_1._T_CONTACT

H_DIST = "Distance from the releasing cell (micrometers)"
H_R = "Concentration of local regulator R (hypothetical, nanomolar)"
H_H = "Concentration of circulating signal H (hypothetical, nanomolar)"
H_S = "Response to signal S (hypothetical, arbitrary units)"
H_T = "Response to signal T (hypothetical, arbitrary units)"
H_CONTACTS = "Cell-to-cell contacts counted per field"
H_RESP = "Response measured (hypothetical, arbitrary units)"

RESPONDING = 10  # arbitrary units; the table is built with a wide gap either side


def _distance(table):
    d = cg.col(table, H_DIST)
    r = cg.col(table, H_R)
    h = cg.col(table, H_H)
    assert all(b > a for a, b in zip(d, d[1:])), f"distance must increase down the table: {d}"
    return d, r, h


def q15(table, item):
    d, r, h = _distance(table)
    assert all(b < a for a, b in zip(r, r[1:])), f"the local regulator must fall with distance: {r}"
    assert r[-1] <= 0.05 * r[0], f"it must be negligible at the far end: {r[0]} to {r[-1]}"
    assert len(set(h)) == 1, f"the other column must be flat, or the contrast fails: {h}"
    assert r[0] > h[0], "'lowest concentration nearest the releasing cell' must not describe the keyed molecule"
    return (f"regulator R falls {r} across distances {d} while signal H holds at {h[0]:.0f} nanomolar "
            f"throughout, so only R is concentrated near its source")


def q16(table, item):
    d, r, h = _distance(table)
    assert len(set(h)) == 1 and h[0] > 0, f"the long-distance signal must be present at every distance: {h}"
    assert r[-1] == 0, "'falls to zero far from the releasing cell' must describe the other molecule"
    assert r[0] > h[0], "'highest concentration closest to the cell' must describe the other molecule"
    assert d[-1] >= 100 * d[0], f"the range tested must actually span long distances: {d}"
    return (f"signal H reads {h[0]:.0f} nanomolar at every distance from {d[0]:.0f} to {d[-1]:.0f} "
            f"micrometers, while R has fallen to {r[-1]:.0f} at the far end")


def q17(table, item):
    labs = cg.labels(table)
    s = dict(zip(labs, cg.col(table, H_S)))
    t = dict(zip(labs, cg.col(table, H_T)))
    resp_s = {k for k in labs if s[k] >= RESPONDING}
    resp_t = {k for k in labs if t[k] >= RESPONDING}
    for name, resp, vals in (("S", resp_s, s), ("T", resp_t, t)):
        assert resp, f"signal {name} must produce a response in at least one cell type"
        assert len(resp) < len(labs), f"signal {name} must leave at least one cell type unresponsive"
        assert all(vals[k] < RESPONDING / 2 for k in labs if k not in resp), \
            f"signal {name}'s non-responders must be clearly below the responders: {vals}"
    assert resp_s != resp_t, "'the two signals act on exactly the same cell types' must be false"
    assert not resp_s & resp_t, "the two responder sets must not overlap, or the contrast is muddied"
    return (f"signal S is answered by {sorted(resp_s)} and signal T by {sorted(resp_t)}, out of "
            f"{len(labs)} cell types exposed to both")


def q18(table, item):
    labs = cg.labels(table)
    contacts = dict(zip(labs, cg.col(table, H_CONTACTS)))
    resp = dict(zip(labs, cg.col(table, H_RESP)))
    top = max(labs, key=lambda k: contacts[k])
    assert resp[top] == max(resp.values()), \
        "the arrangement with the most contacts must give the largest response"
    others = [k for k in labs if k != top]
    for k in others:
        assert contacts[k] <= 0.2 * contacts[top], f"{k} must have far fewer contacts"
        assert resp[k] <= 0.2 * resp[top], f"{k} must give far less response"
    filt = [k for k in labs if "passes molecules" in k.lower()]
    assert len(filt) == 1, f"one arrangement must pass molecules while blocking cells; got {labs}"
    assert contacts[filt[0]] == 0, "the filter arrangement must permit no contacts at all"
    assert len(set(resp.values())) > 1, "'the response is the same in all three arrangements' must be false"
    return (f"{contacts[top]:.0f} contacts give a response of {resp[top]:.0f}, while the two "
            f"contact-free arrangements give {[resp[k] for k in others]} despite molecules still passing")


CLAIMS = [
 ("or from a distance by chemical signaling",
  "EK 4.1.A.1 states that cells communicate with one another through direct contact with other cells or from a distance via chemical signaling. Those two routes are the whole of the statement."),
 ("Local regulators, which target cells in the vicinity",
  "EK 4.1.B.1 states that cells communicate over short distances by using local regulators that target cells in the vicinity of the signal-emitting cell. Both the name and the range come from that one sentence."),
 ("long distances to target cells of another type",
  "EK 4.1.B.2 states that signals released by one cell type can travel long distances to target cells of another type, which names both the crossing of cell types and the distance."),
 ("short distance using a local regulator",
  "The CED lists neurotransmitters as an illustrative example of EK 4.1.B.1, which covers communication over short distances by local regulators targeting cells in the vicinity of the signal-emitting cell."),
 ("long distance to target cells of another type",
  "The CED lists insulin as an illustrative example of EK 4.1.B.2, which covers signals released by one cell type that travel long distances to target cells of another type."),
 ("direct contact between cells",
  "The CED lists immune cells interacting through cell-to-cell contact, naming antigen-presenting cells and helper T-cells, as an illustrative example of the direct-contact route in EK 4.1.A.1."),
 ("released molecule acts on cells in the vicinity",
  "The CED lists quorum sensing in bacteria as an illustrative example of EK 4.1.B.1, short-distance communication by local regulators targeting cells in the vicinity of the signal-emitting cell."),
 ("molecule acting on cells near its source",
  "The CED lists morphogens in embryonic development as an illustrative example of EK 4.1.B.1, communication over short distances by local regulators targeting cells in the vicinity."),
 ("molecules acting on cells near the source",
  "The CED lists the plant immune response as an illustrative example of EK 4.1.B.1, short-distance communication by local regulators that target cells in the vicinity of the signal-emitting cell."),
 ("Long-distance communication reaching target cells of another type",
  "The CED lists thyroid hormones as an illustrative example of EK 4.1.B.2, signals released by one cell type travelling long distances to target cells of another type."),
 ("Estrogen and neurotransmitters",
  "The CED lists estrogen among the illustrative examples of EK 4.1.B.2, long-distance signals reaching target cells of another type, and neurotransmitters among those of EK 4.1.B.1, local regulators acting on cells in the vicinity. Each other pair draws both members from one list."),
 ("long-distance signal reaching target cells of another type",
  "The CED lists human growth hormone among the illustrative examples of EK 4.1.B.2, signals released by one cell type that travel long distances to target cells of another type."),
 ("Direct contact with other cells",
  "The CED lists killer T-cells among the immune cells that interact through cell-to-cell contact, its illustrative example of the direct-contact route named in EK 4.1.A.1."),
 ("How far the signal travels",
  "EK 4.1.B.1 and EK 4.1.B.2 are distinguished by range alone: local regulators act on cells in the vicinity of the emitting cell, while long-distance signals reach target cells of another type elsewhere."),
 ("falls sharply with distance from the releasing cell",
  "Recomputed in q15 above. EK 4.1.B.1 defines a local regulator by its action on cells in the vicinity of the signal-emitting cell, so its concentration must be high at the source and negligible away from it."),
 ("same concentration at every distance measured",
  "Recomputed in q16 above. EK 4.1.B.2 describes signals travelling long distances to target cells of another type, which requires the signal to still be present far from where it was released."),
 ("response in some cell types and not in others",
  "Recomputed in q17 above. EK 4.1.B.2 speaks of TARGET cells of another type, which implies that some exposed cells respond and others do not; the table shows each signal acting on a different subset."),
 ("requires the cells to touch, since arrangements that prevent contact",
  "Recomputed in q18 above. EK 4.1.A.1 names direct contact as one of the two routes, and a filter that passes molecules while blocking cells separates that route from chemical signaling."),
 ("depends on direct contact does not occur",
  "EK 4.1.A.1 makes direct contact one of the two routes of cell communication, and the CED places this immune interaction in that route. Removing contact removes the route the interaction uses."),
 ("acts on cells in the vicinity and in the other it can reach cells far away",
  "EK 4.1.B.1 and EK 4.1.B.2 are statements about how far a released signal travels rather than about the identity of the molecule, so the site of release determines the range over which it can act."),
 ("released molecule can cross a space",
  "EK 4.1.A.1 separates communication through direct contact from communication FROM A DISTANCE via chemical signaling, and EK 4.1.B.2 extends the second route to target cells of another type far from the source."),
 ("detectable only within a short distance",
  "EK 4.1.B.1 defines a local regulator by its range, targeting cells in the vicinity of the signal-emitting cell. Only a measurement of range separates it from the long-distance signal of EK 4.1.B.2."),
 ("reaches one region strongly and the other weakly",
  "EK 4.1.B.1 gives short-distance communication by local regulators targeting cells in the vicinity, and the CED lists morphogens in embryonic development as its illustrative example. A signal at equal concentration everywhere could not distinguish two regions."),
 ("reaches every other cell in the organism",
  "EK 4.1.B.1 confines local regulators to the vicinity of the emitting cell and EK 4.1.B.2 speaks of TARGET cells, so nothing in the framework makes every signal universal. The other four options restate EK 4.1.A.1, EK 4.1.B.1 and EK 4.1.B.2."),
 ("must touch one another for the interaction to occur",
  "EK 4.1.A.1 separates direct contact from chemical signaling, and the CED's illustrative example of contact is immune cells interacting cell-to-cell. The other four options are illustrative examples of the chemical route under EK 4.1.B.1 or EK 4.1.B.2."),
 ("travelling a long distance to target cells of another type",
  "EK 4.1.B.2 states that signals released by one cell type can travel long distances to target cells of another type, which names both features of the scenario."),
 ("Chemical signaling remains possible while direct contact does not",
  "EK 4.1.A.1 names two routes, direct contact and chemical signaling from a distance. A barrier that passes molecules but not cells removes exactly one of the two and leaves the other intact."),
 ("produces its effect in only some of them",
  "EK 4.1.B.2 speaks of TARGET cells of another type, a phrase distinguishing the cells that respond from the cells a circulating signal merely reaches. Being reached and being a target are not the same."),
 ("separated by a barrier that passes molecules but not cells",
  "EK 4.1.A.1 names contact and chemical signaling as the two routes, so a design that removes contact while leaving molecular exchange intact isolates one of them. Separate flasks remove both at once and settle nothing."),
 ("if they do not, by how far the released signal travels",
  "EK 4.1.A.1 draws the first distinction between direct contact and chemical signaling from a distance, and EK 4.1.B.1 and EK 4.1.B.2 divide the chemical route by range into local regulators and long-distance signals."),
]

cg.check(b4_1, CLAIMS, table_checks={15: q15, 16: q16, 17: q17, 18: q18})
