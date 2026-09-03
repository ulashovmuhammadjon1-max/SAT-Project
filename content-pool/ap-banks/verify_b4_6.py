"""Key audit for AP BIOLOGY 4.6 Regulation of Cell Cycle.

One (anchor, claim) per item, in module order. The anchor is a distinctive
substring that must appear in the keyed choice and in no distractor, so the key
survives the shuffle ``export_units.py`` applies on export.

WHAT THE KEYS REST ON
---------------------
The topic has three essential knowledge statements and every key here is one of
them:

  4.6.A.1  A NUMBER OF INTERNAL CONTROLS OR CHECKPOINTS regulate PROGRESSION
           THROUGH the cell cycle
  4.6.A.2  INTERACTIONS BETWEEN CYCLINS AND CYCLIN-DEPENDENT KINASES control
           the cell cycle
  4.6.B.1  DISRUPTIONS to the cell cycle MAY result in CANCER OR APOPTOSIS

TWO SILENCES IN THE CED ARE RESPECTED, AND THEY SHAPE THE MODULE.

First, the exclusion statement: knowledge of SPECIFIC CYCLIN-CdK PAIRS OR
GROWTH FACTORS is beyond the scope of the AP Exam, so no item names one.

Second, and less obvious: the CED does NOT name the individual checkpoints. It
says only that A NUMBER of internal controls or checkpoints regulate
progression. So no key here asserts that a checkpoint sits at G1, at G2, at the
spindle or at any other named point, even though that is standard teaching --
it is not in this framework, and SCIENCE_BRIEF.md's rule is that an uncertain
key is cut rather than guessed. Every checkpoint item asks what a checkpoint
DOES.

The disjunction in EK 4.6.B.1 is load-bearing and items 21, 25, 26 and 29 turn
on it: cancer OR apoptosis, so neither outcome is necessary and a claim that
one always follows is unsupported.

BOUNDARY WITH 4.5 AND 4.3. The stages of the cycle are topic 4.5 and carry no
key here; items 16, 17 and 28 chain to EK 4.5.B.1, EK 4.5.A.1.vi and EK
4.5.A.1.i and cite them. Apoptosis is also named in EK 4.3.A.1 as an outcome of
signal transduction; here it enters only as EK 4.6.B.1's outcome of a
disruption to the cycle.

Items 12 to 15 carry tables. Every number is HYPOTHETICAL and the stem says so;
each keyed conclusion is recomputed below from the table alone, and the
distractors are shown false against the same numbers. No stem refers to a
figure.

FIVE choices per item (A-E), per SCIENCE_BRIEF.md.
"""
import cg_check as cg
import b4_6

CYCLIN = b4_6._T_CYCLIN
CHECKPOINT = b4_6._T_CHECKPOINT
OUTCOME = b4_6._T_OUTCOME
MITOTIC = b4_6._T_MITOTIC

H_HOURS = "Hours since the start of the cycle"
H_CYC = "Cyclin concentration (hypothetical, arbitrary units)"
H_KIN = "Cyclin-dependent kinase activity (hypothetical, arbitrary units)"
H_HALT = "Cells with damaged DNA that halt before dividing (percent)"
H_DIVIDE = "Cells with damaged DNA that divide anyway (percent)"
H_NORMAL = "Cells dividing under normal control (percent)"
H_UNCON = "Cells dividing without control (percent)"
H_APOP = "Cells undergoing programmed cell death (percent)"
H_BEFORE = "Cells in mitosis out of 500 counted, before treatment"
H_AFTER = "Cells in mitosis out of 500 counted, after treatment"


def _sign(x):
    return (x > 0) - (x < 0)


def q12(table, item):
    hours = cg.col(table, H_HOURS)
    cyc = cg.col(table, H_CYC)
    kin = cg.col(table, H_KIN)
    assert all(b > a for a, b in zip(hours, hours[1:])), f"time must increase down the table: {hours}"
    steps = list(zip(cyc, cyc[1:], kin, kin[1:]))
    for c0, c1, k0, k1 in steps:
        assert _sign(c1 - c0) == _sign(k1 - k0), \
            f"the two columns must move in the same direction at every step: {cyc} against {kin}"
    assert len(set(cyc)) > 1 and len(set(kin)) > 1, \
        "'one quantity is constant while the other changes' must be false for both columns"
    assert any(c1 > c0 for c0, c1, _, _ in steps) and any(c1 < c0 for c0, c1, _, _ in steps), \
        "cyclin must both rise and fall across the cycle"
    ratios = [k / c for c, k in zip(cyc, kin)]
    assert max(ratios) - min(ratios) < 0.15, f"the two must track closely: {ratios}"
    return (f"cyclin runs {cyc} and kinase activity {kin} over {hours}: the two rise and fall "
            f"together at every step, at a near-constant ratio of about {sum(ratios) / len(ratios):.2f}")


def q13(table, item):
    labs = cg.labels(table)
    halt = dict(zip(labs, cg.col(table, H_HALT)))
    divide = dict(zip(labs, cg.col(table, H_DIVIDE)))
    for k in labs:
        assert halt[k] + divide[k] == 100, f"{k}: the two percentages must account for the damaged cells"
    normal = [k for k in labs if "normal" in k.lower()]
    lacking = [k for k in labs if "lacking" in k.lower()]
    assert len(normal) == 1 and len(lacking) == 1, f"one normal and one checkpoint-free line; got {labs}"
    n, m = normal[0], lacking[0]
    assert halt[n] > divide[n], "normal cells must mostly halt"
    assert divide[m] > halt[m], "checkpoint-free cells must mostly divide"
    assert halt[n] >= 5 * halt[m], f"the difference must be large: {halt[n]} against {halt[m]}"
    assert halt[n] != halt[m], "'both lines halt at the same rate' must be false"
    return (f"{halt[n]:.0f} percent of normal damaged cells halt against {halt[m]:.0f} percent of the "
            f"checkpoint-free line, whose damaged cells divide anyway {divide[m]:.0f} percent of the time")


def q14(table, item):
    labs = cg.labels(table)
    normal = dict(zip(labs, cg.col(table, H_NORMAL)))
    uncon = dict(zip(labs, cg.col(table, H_UNCON)))
    apop = dict(zip(labs, cg.col(table, H_APOP)))
    for k in labs:
        assert normal[k] + uncon[k] + apop[k] == 100, f"{k}: the three percentages must total the culture"
    intact = [k for k in labs if "intact" in k.lower()]
    assert len(intact) == 1, f"exactly one intact control row; got {labs}"
    i = intact[0]
    disrupted = [k for k in labs if k != i]
    assert disrupted, "there must be disrupted rows to compare"
    for k in disrupted:
        assert uncon[k] > uncon[i], f"{k}: uncontrolled division must exceed the intact culture"
        assert apop[k] > apop[i], f"{k}: programmed cell death must exceed the intact culture"
        assert normal[k] < normal[i], f"{k}: normally controlled division must fall"
    return (f"against the intact culture's {uncon[i]:.0f} percent uncontrolled and {apop[i]:.0f} percent "
            f"cell death, the disrupted cultures reach {[uncon[k] for k in disrupted]} and "
            f"{[apop[k] for k in disrupted]}, so both outcomes rise together")


def q15(table, item):
    labs = cg.labels(table)
    before = dict(zip(labs, cg.col(table, H_BEFORE)))
    after = dict(zip(labs, cg.col(table, H_AFTER)))
    control = [k for k in labs if "untreated" in k.lower()]
    treated = [k for k in labs if "treated" in k.lower() and "untreated" not in k.lower()]
    assert len(control) == 1 and len(treated) == 1, f"one control and one treated culture; got {labs}"
    c, t = control[0], treated[0]
    assert abs(after[c] - before[c]) <= 0.1 * before[c], \
        f"the control must be effectively unchanged: {before[c]} to {after[c]}"
    assert after[t] <= 0.2 * before[t], f"the treated culture must fall sharply: {before[t]} to {after[t]}"
    assert after[t] < after[c], "'both cultures stopped' and 'neither changed' must both be false"
    assert after[t] < before[t], "'the treated cells entered mitosis more often' must be false"
    for k in labs:
        assert before[k] <= 500 and after[k] <= 500, f"{k}: a count may not exceed the 500 cells counted"
    return (f"the untreated count moves {before[c]:.0f} to {after[c]:.0f} while the treated count falls "
            f"{before[t]:.0f} to {after[t]:.0f}, so only the treated culture stops entering mitosis")


CLAIMS = [
 ("regulate progression through the cell cycle",
  "EK 4.6.A.1 states that a number of internal controls or checkpoints regulate progression through the cell cycle. Regulating progression is what the statement assigns to them."),
 ("regulating machinery is part of the cell itself",
  "EK 4.6.A.1 calls them a number of INTERNAL controls or checkpoints regulating progression through the cell cycle, which places the controls within the cell."),
 ("Interactions between cyclins and cyclin-dependent kinases",
  "EK 4.6.A.2 states that interactions between cyclins and cyclin-dependent kinases control the cell cycle. No specific pair is named, per the CED's exclusion statement."),
 ("Cancer, or programmed cell death",
  "EK 4.6.B.1 states that disruptions to the cell cycle may result in cancer or apoptosis, which the framework glosses as programmed cell death. Both outcomes are named and neither is necessary."),
 ("Internal checkpoints regulate progression, and cyclin and kinase interactions control the cycle",
  "EK 4.6.A.1 gives the internal controls on progression and EK 4.6.A.2 gives the cyclin and cyclin-dependent kinase interactions. Those two are the whole of the framework's account of the control."),
 ("without the checks that would normally regulate it",
  "EK 4.6.A.1 makes checkpoints the internal controls that regulate progression, so losing them removes the regulation and not the progression. Skill 6.E asks for this prediction."),
 ("does not occur, so the cycle does not progress normally",
  "EK 4.6.A.2 states that interactions BETWEEN cyclins and cyclin-dependent kinases control the cell cycle, so removing one partner removes the interaction that provides the control at that point."),
 ("depends on the two acting together is lost",
  "EK 4.6.A.2 makes the INTERACTION between cyclins and cyclin-dependent kinases the control, so a kinase acting independently of that interaction is no longer subject to the control it provides."),
 ("regulated rather than proceeding as though nothing had happened",
  "EK 4.6.A.1 states that internal controls or checkpoints regulate progression through the cell cycle, which is what a control does when a cell is not in a fit state to proceed."),
 ("Apoptosis",
  "EK 4.6.B.1 states that disruptions to the cell cycle may result in cancer or apoptosis, giving programmed cell death as the gloss on that term."),
 ("Cancer",
  "EK 4.6.B.1 states that disruptions to the cell cycle may result in cancer or apoptosis; cancer is the first of the two outcomes the statement names."),
 ("rises and falls together with cyclin concentration",
  "Recomputed in q12 above. EK 4.6.A.2 states that interactions between cyclins and cyclin-dependent kinases control the cell cycle, and the two columns move together at every sampled time."),
 ("what halts damaged cells before they divide",
  "Recomputed in q13 above. EK 4.6.A.1 makes checkpoints the internal controls that regulate progression, and the line lacking a working checkpoint is the one whose damaged cells proceed."),
 ("raises both uncontrolled division and programmed cell death",
  "Recomputed in q14 above. EK 4.6.B.1 states that disruptions to the cell cycle may result in cancer OR apoptosis, so both outcomes are available from one disruption."),
 ("treated cells stopped entering mitosis while the untreated cells continued",
  "Recomputed in q15 above. EK 4.6.A.1 makes checkpoints the internal controls on progression through the cycle, so activating one holds cells short of the next stage."),
 ("unchecked progression puts that outcome at risk",
  "EK 4.5.B.1 makes mitosis the transfer of a complete genome to two genetically identical daughter cells, and EK 4.6.A.1 makes checkpoints the internal controls on progression. Regulation protects what mitosis is supposed to deliver."),
 ("held at a particular stage, and internal checkpoints regulate progression",
  "EK 4.5.A.1.vi states that nondividing cells may exit the cell cycle or be held at a particular stage in it, and EK 4.6.A.1 makes internal controls or checkpoints what regulates progression."),
 ("impaired, because the controlling interaction cannot occur",
  "EK 4.6.A.2 states that interactions between cyclins and cyclin-dependent kinases control the cell cycle, so blocking the kinase removes one partner in the interaction that supplies the control."),
 ("under conditions in which normal cells halt",
  "EK 4.6.A.1 defines a checkpoint by its regulation of progression, so a defect shows as progression where regulation should have prevented it. Every other listed observation is true of normal cells too."),
 ("regulation of progression by internal controls is working in one line",
  "EK 4.6.A.1 states that a number of internal controls or checkpoints regulate progression through the cell cycle, which is the difference between a line that halts appropriately and one that does not."),
 ("MAY result in cancer OR apoptosis, so both are available outcomes",
  "EK 4.6.B.1 states that disruptions to the cell cycle may result in cancer or apoptosis, a disjunction that permits either outcome rather than requiring one of them."),
 ("More than one control acts on progression",
  "EK 4.6.A.1 states that A NUMBER OF internal controls or checkpoints regulate progression through the cell cycle, which asserts more than one without committing to a count."),
 ("regulation has been disrupted, an outcome of which may be cancer",
  "EK 4.6.A.1 makes checkpoints the internal controls on progression, and EK 4.6.B.1 states that disruptions to the cell cycle may result in cancer or apoptosis. Progression where regulation should have prevented it is such a disruption."),
 ("proportion of cells in mitosis before and after treatment",
  "EK 4.6.A.1 makes a checkpoint a control on PROGRESSION, so the measurement must be of progression, and skills 4.B and 5.A make the proportion of cells at a stage how it is measured. The untreated culture shows the change was the treatment's."),
 ("names programmed cell death as an alternative outcome",
  "EK 4.6.B.1 states that disruptions to the cell cycle may result in cancer OR apoptosis, so cancer is one of two named outcomes rather than a necessary consequence of every disruption."),
 ("since the other named outcome has been removed",
  "EK 4.6.B.1 names cancer and apoptosis as the two outcomes a disruption may produce, so removing a cell's capacity for one leaves the other as the available outcome."),
 ("changing amount of cyclin gives control that varies through the cycle",
  "EK 4.6.A.2 states that interactions between cyclins and cyclin-dependent kinases control the cell cycle, so an interaction whose extent varies with the amount of cyclin supplies control that varies with position in the cycle."),
 ("act on progression from one stage of the cycle to the next",
  "EK 4.6.A.1 states that internal controls or checkpoints regulate PROGRESSION THROUGH the cell cycle, and EK 4.5.A.1.i makes the cycle a sequence of stages, so progression is movement between them."),
 ("always results in cancer and never in programmed cell death",
  "EK 4.6.B.1 names cancer OR apoptosis as possible results of a disruption, which rules out the always-and-never reading. The other four options restate EK 4.6.A.1, EK 4.6.A.2 and EK 4.6.B.1."),
 ("disrupting that control may produce cancer or programmed cell death",
  "EK 4.6.A.1 gives the internal controls on progression, EK 4.6.A.2 gives the cyclin and cyclin-dependent kinase interactions, and EK 4.6.B.1 gives cancer or apoptosis as the possible results of a disruption."),
]

cg.check(b4_6, CLAIMS, table_checks={12: q12, 13: q13, 14: q14, 15: q15})
