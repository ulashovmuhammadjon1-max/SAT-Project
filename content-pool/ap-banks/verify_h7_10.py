"""Key audit for AP CHEMISTRY 7.10 Reaction Quotient and Le Chatelier's Principle.

One (anchor, claim) per item, in module order.

WHAT THE KEYS REST ON.

  7.10.A.1  a disturbance makes Q differ from K; the system responds by bringing
            Q back into agreement with K, establishing a NEW equilibrium state
  7.10.A.2  a concentration change moves Q only; a temperature change moves K;
            either way the concentrations redistribute until the two agree

THE TOPIC BOUNDARY, checked rather than asserted. 7.9 owns the qualitative
response to a stress and its measurable consequences, and its verifier asserts
that no item there argues from Q. This verifier asserts the mirror image:
``every_rationale_names_q_or_k`` requires each rationale HERE to name Q or K.
Two banks written to one principle would otherwise converge, and the pair of
checks is what makes the split real.

ARITHMETIC. Every reaction quotient below is recomputed from the stated
equilibrium concentrations and the stated disturbance -- in ``TABLE_CHECKS`` for
the nine items carrying a table and in ``NUMERIC`` for the four whose numbers
are in the stem -- and the numeric distractors are falsified against the same
inputs.

NEGATIVE CONTROL: ``python3 verify_h7_10.py --selftest``.
"""
import re
import sys

import cg_check as cg
import h_check as h

import h7_10

QCH = "Does Q change immediately"
KCH = "Does K change"
AA = "[A] just after the disturbance (M)"
BB = "[B] just after the disturbance (M)"
KT = "Equilibrium constant"
N2O4 = "[N2O4] (M)"
NO2 = "[NO2] (M)"

# Explicit lookarounds, never \b: a bare Q or K as a token, or the spelled-out
# names. "K" abuts a digit in "K = 4.0", which is exactly where \b fails.
_QK = re.compile(r"(?<![A-Za-z])[QK](?![A-Za-z])|reaction quotient|equilibrium constant",
                 re.I)


def every_rationale_names_q_or_k(module):
    """This topic is the Q-versus-K account; 7.9 is the one that must avoid it."""
    for i, item in enumerate(module.QUESTIONS, 1):
        assert _QK.search(item["why"]), (
            f"{module.TOPIC[0]} q{i}: the rationale names neither Q nor K, so it is "
            f"topic 7.9's question rather than this one -- {item['why'][:70]!r}"
        )
    print(f"OK  {module.TOPIC[0]} scope: all {len(module.QUESTIONS)} rationales argue "
          "from Q or K, which is what separates this topic from 7.9.")


# ------------------------------------------------------------------ table items

def q4(table, item):
    q = cg.cell(table, "2", BB) / cg.cell(table, "2", AA)
    assert abs(q - 6.0) < 1e-9, f"Q in vessel 2 is {q}"
    assert q > 4.0, "Q must exceed the stated K for the keyed reverse direction"
    h.shows(item, "Q is 6.0, which is above K, so the system proceeds in reverse")
    return f"vessel 2 gives Q equal to {q:g}, above the stated constant of 4.0"


def q5(table, item):
    q = cg.cell(table, "3", BB) / cg.cell(table, "3", AA)
    assert abs(q - 4.0) < 1e-9, f"Q in vessel 3 is {q}"
    assert cg.cell(table, "3", AA) != 0.20 and cg.cell(table, "3", BB) != 0.80, \
        "both tabulated concentrations must have moved, or the item asks nothing"
    h.shows(item, "Q equals K")
    return (f"vessel 3 gives Q equal to {q:g}, the stated constant, even though both "
            "tabulated concentrations differ from the original pair")


def q7(table, item):
    rows = {str(r[0]): r for r in table["rows"]}
    head = [str(x) for x in table["headers"]]
    ki = head.index(KCH)
    moves_k = [lab for lab, r in rows.items() if r[ki].strip().lower() == "yes"]
    assert len(moves_k) == 1 and "warmed" in moves_k[0], \
        f"rows recording a change in K: {moves_k}"
    h.shows(item, "the vessel is warmed")
    return f"exactly one tabulated disturbance records a change in K, namely {moves_k[0]!r}"


def q8(table, item):
    rows = {str(r[0]): r for r in table["rows"]}
    head = [str(x) for x in table["headers"]]
    qi, ki = head.index(QCH), head.index(KCH)
    for lab, r in rows.items():
        assert (r[qi].strip().lower() == "yes") != (r[ki].strip().lower() == "yes"), (
            f"row {lab!r} must move exactly one of Q and K, per EK 7.10.A.2"
        )
    h.shows(item, "redistributed so that Q and K are equal once more")
    return ("each tabulated row moves exactly one of Q and K, and every row ends with "
            "the two brought back into equality")


def q9(table, item):
    ks = dict(zip(cg.labels(table), cg.col(table, KT)))
    assert ks["300"] == 4.0 and ks["500"] == 10.0, f"tabulated constants are {ks}"
    assert ks["500"] > ks["300"], "the constant must be larger at the higher temperature"
    h.shows(item, "Q is 4.0 and K is 10")
    return (f"the tabulated constant rises from {ks['300']:g} at 300 K to {ks['500']:g} "
            "at 500 K while the concentrations, and so Q, have not yet moved")


def q10(table, item):
    ks = dict(zip(cg.labels(table), cg.col(table, KT)))
    assert ks["500"] > ks["300"], "Q must have to RISE for the keyed forward direction"
    h.shows(item, "Forward, because Q must rise from 4.0")
    return (f"Q must move from {ks['300']:g} to {ks['500']:g}, an increase, which is net "
            "forward reaction")


def q12(table, item):
    n, no2 = cg.cell(table, "At equilibrium", N2O4), cg.cell(table, "At equilibrium", NO2)
    k = no2 ** 2 / n
    assert abs(k - 0.40) < 1e-9, f"K recomputes to {k}"
    assert abs(no2 / n - 1.0) < 1e-9, "the 1.0 distractor must be the unsquared ratio"
    h.shows(item, "0.40")
    return f"the square of {no2:g} over {n:g} recomputes the constant as {k:g}"


def q13(table, item):
    row = "Just after the volume is halved"
    n, no2 = cg.cell(table, row, N2O4), cg.cell(table, row, NO2)
    base_n = cg.cell(table, "At equilibrium", N2O4)
    assert abs(n - 2 * base_n) < 1e-9, "the halved-volume row must double the concentration"
    q = no2 ** 2 / n
    assert abs(q - 0.80) < 1e-9, f"Q recomputes to {q}"
    h.shows(item, "0.80")
    return f"doubling both concentrations gives Q equal to {q:g}"


def q14(table, item):
    row = "Just after the volume is halved"
    q = cg.cell(table, row, NO2) ** 2 / cg.cell(table, row, N2O4)
    k = (cg.cell(table, "At equilibrium", NO2) ** 2
         / cg.cell(table, "At equilibrium", N2O4))
    assert q > k, f"Q of {q} must exceed K of {k} for the keyed reverse direction"
    h.shows(item, "In reverse, because Q rose above K")
    return f"Q of {q:g} against K of {k:g} requires Q to fall, which is reverse reaction"


def q15(table, item):
    row = "Just after the volume is doubled"
    n, no2 = cg.cell(table, row, N2O4), cg.cell(table, row, NO2)
    base_n = cg.cell(table, "At equilibrium", N2O4)
    assert abs(n - base_n / 2) < 1e-9, "the doubled-volume row must halve the concentration"
    q = no2 ** 2 / n
    k = (cg.cell(table, "At equilibrium", NO2) ** 2
         / cg.cell(table, "At equilibrium", N2O4))
    assert abs(q - 0.20) < 1e-9 and q < k, f"Q recomputes to {q} against K of {k}"
    h.shows(item, "Q is 0.20, below K, so the system proceeds forward")
    return f"halving both concentrations gives Q equal to {q:g}, below K of {k:g}"


def q29(table, item):
    q = cg.cell(table, "1", BB) / cg.cell(table, "1", AA)
    assert abs(q - 1.6) < 1e-9, f"Q in vessel 1 is {q}"
    assert abs(cg.cell(table, "1", AA) / cg.cell(table, "1", BB) - 0.625) < 1e-9, \
        "the 0.63 distractor must be the inverted ratio"
    h.shows(item, "1.6")
    return f"vessel 1 gives Q equal to {q:g}, against {1 / q:.3f} for the inverted ratio"


TABLE_CHECKS = {4: q4, 5: q5, 7: q7, 8: q8, 9: q9, 10: q10, 12: q12, 13: q13,
                14: q14, 15: q15, 29: q29}


# ---------------------------------------------------------------- stem numerics

def n2(item):
    q = 0.80 / 0.50
    assert abs(q - 1.6) < 1e-9, f"Q recomputes to {q}"
    assert q < 4.0, "the injection must leave Q below the stated constant"
    h.shows(item, "1.6")
    return f"0.80 over the raised 0.50 recomputes Q as {q:g}, below the constant of 4.0"


def n3(item):
    q = 0.80 / 0.50
    assert q < 4.0, f"Q of {q} must lie below K for the keyed forward direction"
    h.shows(item, "Forward, because Q now lies below K")
    return f"Q of {q:g} against a constant of 4.0 must rise, which is forward reaction"


def n19(item):
    h2, i2, hi = 2 * 0.50, 2 * 0.50, 2 * 1.00
    q = hi ** 2 / (h2 * i2)
    assert abs(q - 4.0) < 1e-9, f"Q after doubling recomputes to {q}"
    before = 1.00 ** 2 / (0.50 * 0.50)
    assert abs(before - q) < 1e-9, "doubling must leave the quotient unchanged here"
    h.shows(item, "4.0")
    return (f"doubling every concentration leaves Q at {q:g}, the same as the {before:g} "
            "before the compression")


def n22(item):
    q = 0.40 / 0.20
    assert abs(q - 2.0) < 1e-9, f"Q recomputes to {q}"
    assert q < 4.0, "removing product must leave Q below the constant"
    h.shows(item, "2.0")
    return f"the lowered 0.40 over the unchanged 0.20 recomputes Q as {q:g}"


NUMERIC = {2: n2, 3: n3, 19: n19, 22: n22}


CLAIMS = [
 ("made Q differ from K",
  "EK 7.10.A.1, near verbatim: a disturbance causes Q to differ from K, taking the system out of equilibrium, and the system responds by bringing Q back into agreement with K, establishing a new equilibrium state."),
 ("1.6",
  "EK 7.10.A.2: a concentration change moves Q only. Recomputed in n2 from the raised reactant concentration and the momentarily unchanged product concentration."),
 ("Forward, because Q now lies below K",
  "EK 7.10.A.1 has the system close the gap between Q and K, and EK 7.10.A.2 keeps K fixed at constant temperature. Recomputed in n3."),
 ("Q is 6.0, which is above K, so the system proceeds in reverse",
  "EK 7.10.A.1: Q above K is lowered by net reverse reaction. Q recomputed from the tabulated post-disturbance concentrations in q4."),
 ("Q equals K",
  "EK 7.10.A.1 makes being out of equilibrium a matter of Q DIFFERING from K, so a disturbance that moves both concentrations without moving the quotient produces no net change. Recomputed in q5."),
 ("concentration change moves Q only, while a temperature change moves K",
  "EK 7.10.A.2, verbatim in substance: some stresses, such as changes in concentration, cause a change in Q only, and a change in temperature causes a change in K."),
 ("the vessel is warmed",
  "EK 7.10.A.2 assigns a change in K to a change in temperature alone. The tabulated rows are read in q7, where exactly one records a change in K."),
 ("redistributed so that Q and K are equal once more",
  "EK 7.10.A.2 closes with this: in either case, the concentrations or partial pressures redistribute to bring Q and K back into equality. Checked row by row in q8."),
 ("Q is 4.0 and K is 10",
  "EK 7.10.A.2: heating moves K while the concentrations, and therefore Q, have not yet moved. The two tabulated constants are read in q9."),
 ("Forward, because Q must rise from 4.0",
  "EK 7.10.A.1 has the system bring Q to the NEW K, and the tabulated constant is larger at the higher temperature, so Q must rise. Checked in q10."),
 ("lowers Q and leaves K alone",
  "EK 7.10.A.2 assigns a concentration change to Q alone. A larger reactant term enlarges the denominator of the quotient, so Q falls, and EK 7.10.A.1 then has forward reaction restore the equality."),
 ("0.40",
  "The value of K that the later rows are compared against, recomputed in q12 from the tabulated equilibrium row with the product coefficient carried in as a square."),
 ("0.80",
  "EK 7.10.A.2: compression is a concentration change and so moves Q only. Recomputed in q13 from the tabulated post-compression row."),
 ("In reverse, because Q rose above K",
  "EK 7.10.A.1 has a Q above K lowered by net reverse reaction, and the reverse direction here converts two moles of gas into one. Both the quotient and the constant are recomputed in q14."),
 ("Q is 0.20, below K, so the system proceeds forward",
  "EK 7.10.A.1 with an expansion, which lowers Q below K. Recomputed in q15 from the tabulated post-expansion row."),
 ("fixed by the temperature",
  "EK 7.10.A.2 assigns a change in K to a change in temperature and a change in Q alone to a change in concentration, so the constant does not depend on how much material is present."),
 ("product terms fall and the reactant terms rise",
  "EK 7.10.A.1 has the system bring Q back to K and EK 7.10.A.2 says the concentrations redistribute to do it; lowering a quotient requires its numerator to shrink and its denominator to grow."),
 ("same number of moles of gas on both sides",
  "Compression multiplies every gas concentration by one factor, which cancels from the quotient exactly when numerator and denominator carry the same total power, leaving Q equal to K and, by EK 7.10.A.1, nothing to respond to."),
 ("4.0",
  "EK 7.10.A.1: an equation with equal moles of gas on the two sides has its quotient unchanged by compression. Recomputed in n19, which also recomputes the quotient before the compression."),
 ("K rises above the unchanged Q",
  "EK 7.10.A.2 makes cooling a change in K with Q momentarily unchanged, and EK 7.10.A.1 then has the system raise Q to the new constant."),
 ("no longer at equilibrium, because Q has been made to differ from K",
  "EK 7.10.A.1 identifies loss of equilibrium with Q differing from K, not with any change in K. Q is defined for any set of concentrations and K is defined by the temperature."),
 ("2.0",
  "EK 7.10.A.2: removing product lowers the numerator of the quotient only. Recomputed in n22."),
 ("More B is being formed and A is being consumed",
  "EK 7.10.A.1 has the system raise a quotient that lies below the constant, which requires the product term to grow and the reactant term to shrink."),
 ("comparison of Q with K",
  "EK 7.10.A.1 makes the DIFFERENCE between Q and K both the criterion for being out of equilibrium and the thing the response closes, so neither value alone answers the question."),
 ("proceeds in reverse until Q has fallen to K",
  "EK 7.10.A.1 makes the direction depend on the comparison of Q with K rather than on the magnitude of either, so a quotient above a large constant is still lowered by reverse reaction."),
 ("first moved Q only; the second moved K",
  "EK 7.10.A.2 assigns a concentration change to Q and a temperature change to K, so two disturbances of those two kinds act on different quantities."),
 ("generally different, but they satisfy the same value of K",
  "EK 7.10.A.1 calls the result a NEW equilibrium state, so the concentrations need not return; EK 7.10.A.2 leaves K unmoved when the temperature is unmoved, so the new set satisfies the same constant."),
 ("Neither changes, so no net reaction follows",
  "EK 7.10.A.2 attaches a change in Q to concentration and a change in K to temperature, and a catalyst alters neither at the moment it is added, so EK 7.10.A.1 leaves nothing to respond to."),
 ("1.6",
  "EK 7.10.A.2: a concentration change moves Q only. Recomputed in q29 from the tabulated post-disturbance concentrations, with the inverted ratio recomputed as the distractor."),
 ("K did not move in the first place unless the temperature changed",
  "EK 7.10.A.2 makes a concentration change a change in Q alone, so there is no displacement of K to be undone; and where temperature did move K, EK 7.10.A.1 has Q brought to the NEW value."),
]


def _extra_mutations():
    def corrupt_table(mod, cl):
        mod.QUESTIONS[3]["table"] = dict(
            headers=h7_10._T_AFTER["headers"],
            rows=[[lab, a, ("0.60" if lab == "2" else b)]
                  for lab, a, b in h7_10._T_AFTER["rows"]])

    def scope_slips(mod, cl):
        mod.QUESTIONS[5]["why"] = ("The system shifts toward the side that relieves the "
                                   "stress, which is what the principle predicts here.")
        every_rationale_names_q_or_k(mod)

    def corrupt_numeric(mod, cl):
        ch = list(mod.QUESTIONS[1]["choices"])
        ch[0] = "Q = 1.8"
        mod.QUESTIONS[1]["choices"] = ch
        cl[1] = ("1.8", cl[1][1])

    def flip_disturbance_table(mod, cl):
        mod.QUESTIONS[7]["table"] = dict(
            headers=h7_10._T_DISTURB["headers"],
            rows=[[lab, "yes", "yes"] for lab, _, _ in h7_10._T_DISTURB["rows"]])

    return [("a tabulated concentration corrupted so the keyed Q is false", corrupt_table),
            ("a rationale that argues without Q or K, which is 7.9's question", scope_slips),
            ("a recomputed quotient no longer in the keyed choice", corrupt_numeric),
            ("a disturbance table claiming one stress moves both Q and K",
             flip_disturbance_table)]


if __name__ == "__main__" and "--selftest" in sys.argv:
    h.selftest(h7_10, CLAIMS, table_checks=TABLE_CHECKS, numeric_checks=NUMERIC,
               mutations=_extra_mutations())

every_rationale_names_q_or_k(h7_10)
h.run(h7_10, CLAIMS, table_checks=TABLE_CHECKS, numeric_checks=NUMERIC)
