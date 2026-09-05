"""Key audit for AP WORLD HISTORY: MODERN 4.7 Changing Social Hierarchies from 1450 to 1750.

One (anchor, claim) per item, in module order. The anchor is a distinctive
substring that MUST appear in the keyed choice and in NO distractor; the claim
states the CED sentence the key rests on, with its Key Concept code, for a human
to audit. `wh_check` refuses any claim or `why` citing neither a KC code nor a
Learning Objective.

EVERYTHING SHARED IS SHARED. `wh_check.run` supplies the structural gate
(`cg_check.check`), the notation gate (`es_check.style`), the citation rule, the
figure-language ban, and a self-test that rotates all thirty keys, breaks all
thirty anchors, corrupts every cell of every table and asserts WHICH message came
back each time. `wh_stimulus` supplies the marked-stimulus gate.

THE CONTENT RISK HERE IS FLATTENING A TWO-SIDED SENTENCE. KC-4.3.I.B says that
many states adopted practices to accommodate the ethnic and religious diversity
of their subjects OR to utilize the economic, political, and military
contributions of different ethnic or religious groups, AND that in other cases
states suppressed diversity or limited certain groups' roles in society,
politics, or the economy. Both halves are the framework's, and it commits to
neither as the rule. It is very easy to write a bank in which every item keys
one half; q5, q25 and q30 exist to hold the two together, and q24 keys the
comparison of their frequency as precisely the claim that would need an outside
source, because the CED never says which was commoner.

THE SECOND RISK IS THE WORD "FLUCTUATED". KC-4.2.III.B does not say the power of
existing elites rose, and does not say it fell. q8 and q26 key the fluctuation
itself, and q22's table is built so that the share of petitions granted moves
down, up and down again -- a monotonic table would have made a "rose" or "fell"
distractor arguably correct.

THE THIRD RISK IS THE NEW/EXISTING ELITE SPLIT. KC-4.2.III.A's new elites are
the Qing transition and the Casta system; the illustrative examples' EXISTING
elites are Ottoman timars, Russian boyars and the European nobility. Each of
those five names reads plausibly under the other heading, so q7, q13 and q14
separate them and q14's anchor carries both clauses.

QING CHINA APPEARS TWICE AND BOTH APPEARANCES ARE REAL: as a new elite at
KC-4.2.III.A and as a state with restrictive policies against Han Chinese in the
illustrative examples for KC-4.3.I.B. q15 is built on the double rather than
around it, so a student who has noticed it is rewarded rather than tripped.

NEGATIVE CONTROL: `python3 verify_w4_7.py --selftest`.
"""
import sys

import cg_check as cg
import wh_check as wh
import wh_stimulus as ws

import w4_7

DID = "What the record says it did"
HOW = "How the survey describes it"
GRANTED = "Petitions from the existing elite that the monarch granted"
REFUSED = "Petitions from the existing elite that the monarch refused"


def q20(table, item):
    """Two practices accommodate, one limits a role, and one distinguishes no group."""
    labs = cg.labels(table)
    assert labs == ["Practice %d" % n for n in range(1, 5)], \
        f"the four practices the key counts are not the rows: {labs}"
    # A closed vocabulary, parsed rather than searched. KC-4.3.I.B's two halves
    # are the two classes; the fourth row belongs to neither and that is what
    # makes the "all four" distractors false.
    classes = {
        "guaranteed a religious minority the use of its own courts": "accommodates",
        "recruited soldiers from several ethnic groups into the army": "accommodates",
        "barred one group from holding any office of state": "limits",
        "set the same harvest tax for every household alike": "neither",
    }
    got = []
    for row in table["rows"]:
        note = cg.normalize(row[1])
        assert note in classes, f"the practice {note!r} is outside this item's vocabulary"
        got.append(classes[note])
    assert got.count("accommodates") == 2, \
        f"the key needs two accommodating practices; got {got}"
    assert got.count("limits") == 1, f"the key needs one limiting practice; got {got}"
    assert got.count("neither") == 1, f"the key needs one practice that is neither; got {got}"
    return ("two rows accommodate diversity or use the contributions of different groups, one "
            "bars a group from office, and the fourth taxes every household alike and so "
            "distinguishes no group at all")


def q21(table, item):
    """Two elite groups are newly formed and two are long established."""
    groups = cg.labels(table)
    assert len(groups) == 4 and len(set(groups)) == 4, \
        f"the survey must list four distinct groups; got {groups}"
    new, old = [], []
    for row in table["rows"]:
        note = cg.normalize(row[1])
        if note == "newly formed in this period":
            new.append(row[0])
        elif note == "long established before this period":
            old.append(row[0])
        else:
            raise AssertionError(
                f"{row[0]!r} is described as {note!r}, which is neither of the two categories "
                "KC-4.2.III.A and KC-4.2.III.B distinguish")
    assert len(new) == 2 and len(old) == 2, \
        f"the key needs two of each; got {len(new)} new and {len(old)} established"
    # KC-4.2.III.A gives two routes into a new elite, conquest and economic
    # opportunity, and the survey must show both rather than the same one twice.
    routes = {"conquest" in cg.normalize(n) for n in new}
    assert routes == {True, False}, (
        "KC-4.2.III.A names imperial conquests AND widening global economic opportunities, so "
        f"the two new elites must not arrive by the same route; got {new}")
    return (f"two rows, {new}, are newly formed in the period by the two routes KC-4.2.III.A "
            f"names, and two, {old}, were long established before it")


def q22(table, item):
    """The share of petitions granted is not monotonic -- it falls, rises, falls."""
    labs = cg.labels(table)
    assert labs == ["First period", "Second period", "Third period", "Fourth period"], (
        f"the key speaks of the share in every period shown, so the record must be four "
        f"labelled periods in order; got {labs}")
    granted, refused = cg.col(table, GRANTED), cg.col(table, REFUSED)
    totals = [g + r for g, r in zip(granted, refused)]
    assert all(t > 0 for t in totals), "a period with no petitions has no share to compute"
    shares = [g / t for g, t in zip(granted, totals)]
    rises = [shares[i + 1] > shares[i] for i in range(len(shares) - 1)]
    assert set(rises) == {True, False}, (
        f"KC-4.2.III.B's word is FLUCTUATED, so the share must move in both directions; "
        f"got shares {[round(s, 2) for s in shares]}")
    assert rises == [False, True, False], (
        f"the key says the share falls, rises, then falls; got {rises} from "
        f"{[round(s, 2) for s in shares]}")
    # and every distractor false on the same numbers
    assert not all(rises), "'the share rises in every period' must be false"
    assert any(rises), "'the share falls in every period' must be false"
    assert len(set(round(s, 6) for s in shares)) > 1, \
        "'the share is the same in every period' must be false"
    assert all(r > 0 for r in refused), \
        "'every petition was granted in every period' must be false"
    return (f"the share of petitions granted runs {[round(s, 2) for s in shares]}, falling then "
            "rising then falling, which is a fluctuation and not a direction")


CLAIMS = [
 ("accommodate the ethnic and religious diversity of their subjects",
  "KC-4.3.I.B says many states, such as the Mughal and Ottoman empires, adopted practices to accommodate the ethnic and religious diversity of their subjects. Imposed language, forced migration, abolished distinctions and transferred populations appear nowhere in that statement."),
 ("utilize the economic, political, and military contributions",
  "KC-4.3.I.B pairs accommodation with a second aim: to utilize the economic, political, and military contributions of different ethnic or religious groups. Reducing the number of groups and standardizing religion belong to the other half of the same sentence."),
 ("Mughal and Ottoman empires",
  "KC-4.3.I.B names the Mughal and Ottoman empires as its examples of states that adopted such practices. The other empires and states listed appear at KC-4.3.II.B, KC-4.3.II.C, KC-4.3.II.A.ii and KC-4.3.II.A.i, but not in this sentence."),
 ("suppressed diversity or limited certain groups' roles",
  "KC-4.3.I.B closes by saying that in other cases states suppressed diversity or limited certain groups' roles in society, politics, or the economy. That is the second half of one sentence whose first half describes accommodation, and neither half is offered as the general rule."),
 # Both clauses: two distractors keep one half of KC-4.3.I.B and drop the other,
 # so an anchor naming only accommodation or only suppression matches one of them.
 ("many states accommodated or used the contributions of different groups, and in other cases states suppressed diversity",
  "KC-4.3.I.B holds both cases in one sentence and commits to neither as the rule. Choosing one half is the flattening this item exists to catch, and KC-4.3.I.B is the only statement in the topic that speaks to how states treated the groups within them."),
 ("Imperial conquests and widening global economic opportunities",
  "KC-4.2.III.A says imperial conquests and widening global economic opportunities contributed to the formation of new political and economic elites. Each rejected option describes a contraction or withdrawal the framework nowhere records as producing new elites."),
 # Both clauses: three distractors keep one true example and pair it with an
 # EXISTING elite, so an anchor naming one example alone matches them.
 ("transition to the Qing Dynasty, and the Americas with the rise of the Casta system",
  "KC-4.2.III.A names China with the transition to the Qing Dynasty and the Americas with the rise of the Casta system as its examples of new elites. The boyars, the timars and the European nobility are printed under the separate heading of existing elites, belonging to KC-4.2.III.B."),
 ("It fluctuated",
  "KC-4.2.III.B says the power of existing political and economic elites fluctuated as the elites confronted new challenges. Fluctuation is the framework's own word, so a steady rise, a steady fall, no change and a complete transfer each assert a direction the sentence declines to give."),
 ("New challenges to their ability to affect the policies of increasingly powerful monarchs",
  "KC-4.2.III.B says the power of existing elites fluctuated as they confronted new challenges to their ability to affect the policies of the increasingly powerful monarchs and leaders. The phrase increasingly powerful is the framework's own and rules out the readings in which monarchs weaken or withdraw."),
 # Both clauses: the distractor swaps the two states, and either half of the
 # key would match the swap.
 ("expulsion of Jews from Spain and Portugal, and the acceptance of Jews in the Ottoman Empire",
  "The illustrative examples beside Unit 4: Learning Objective M print exactly this pairing under the heading of differential treatment of groups in society, politics, and the economy, which is what KC-4.3.I.B's two halves look like side by side. Reversing the two states inverts it."),
 ("Han Chinese",
  "The illustrative examples name restrictive policies against Han Chinese in Qing China under the heading of differential treatment of groups, illustrating KC-4.3.I.B's second half. The merchants named belong to KC-4.3.II.A.iii, and the boyars and timars to the heading of existing elites."),
 ("varying status of different classes of women within the Ottoman Empire",
  "The illustrative examples print this under the heading of differential treatment of groups in society, politics, and the economy, illustrating KC-4.3.I.B. Each rejected option asserts a uniformity the framework never claims for any state."),
 ("Ottoman timars, Russian boyars, and the European nobility",
  "The illustrative examples for this topic print Ottoman timars, Russian boyars and the European nobility under the heading of existing elites, which is what KC-4.2.III.B means by existing political and economic elites. The Casta system and the Qing transition are KC-4.2.III.A's new elites."),
 # Both clauses: the distractor exchanges the two examples between the two
 # categories, so an anchor naming one of them alone matches it.
 ("Casta system among the new elites, and the Russian boyars among the existing elites",
  "KC-4.2.III.A names the rise of the Casta system in the Americas among the new political and economic elites, while the illustrative examples print Russian boyars under existing elites, belonging to KC-4.2.III.B. The rejected sortings exchange them or collapse the two categories."),
 # Both clauses: the distractor exchanges the two roles the Qing plays.
 ("transition to the Qing Dynasty is given as the formation of a new elite, and restrictive policies against Han Chinese are given as differential treatment",
  "KC-4.2.III.A names China with the transition to the Qing Dynasty among the new political and economic elites, while the illustrative examples name restrictive policies against Han Chinese in Qing China under differential treatment of groups, illustrating KC-4.3.I.B. Both are printed and they are different statements about the same state."),
 ("Social categories, roles, and practices",
  "Unit 4: Learning Objective M asks how social categories, roles, and practices have been maintained or have changed over time, which is why KC-4.3.I.B, KC-4.2.III.A and KC-4.2.III.B are printed beside it. The rejected options belong to Learning Objectives A, I, D and B of the same unit."),
 ("some states adopted practices to accommodate the diversity of their subjects",
  "KC-4.3.I.B says many states adopted practices to accommodate ethnic and religious diversity or to utilize the contributions of different groups, while in other cases states suppressed diversity, so evidence of the first half MODIFIES a claim of uniform hostility rather than simply refuting it, which is what suggested skill 3.D asks a student to distinguish. Authorship, copies, figures and length are features of the document."),
 ("practice adopted to accommodate the diversity of a state's subjects",
  "KC-4.3.I.B says many states adopted practices to accommodate the ethnic and religious diversity of their subjects or to utilize their contributions, and a grant of separate courts with confirmed trades is such a practice. The rejected options are the second half of that sentence, KC-4.2.III.A, KC-4.2.III.B and KC-4.3.II.A.i."),
 ("imperial conquests contributed to the formation of new political and economic elites",
  "KC-4.2.III.A says imperial conquests and widening global economic opportunities contributed to the formation of new political and economic elites, and a province whose offices and estates have passed to families that held neither before is that formation. The rejected options are KC-4.2.III.B, both halves of KC-4.3.I.B, and KC-5.3.III.C."),
 ("Two accommodate diversity or use the contributions of different groups, one limits a group's role",
  "KC-4.3.I.B names both accommodating diversity or using the contributions of different groups and suppressing diversity or limiting certain groups' roles. Recomputed in q20 above: two rows fall on the first side, one on the second, and a tax charged alike to every household distinguishes no group at all."),
 ("Two of the groups are described as newly formed in this period and two as long established",
  "KC-4.2.III.A describes new political and economic elites formed by imperial conquests and widening global economic opportunities, while KC-4.2.III.B describes existing elites whose power fluctuated. Recomputed in q21 above: two rows are new, by both of the routes KC-4.2.III.A names, and two were long established."),
 ("falls, then rises, then falls again rather than moving in one direction",
  "KC-4.2.III.B says the power of existing political and economic elites fluctuated as they confronted new challenges to their ability to affect the policies of increasingly powerful monarchs. Recomputed in q22 above: the share granted moves down, up and down, so it is not monotonic in either direction."),
 # Both clauses: this pairs a continuity with a change and each half alone sits
 # inside a rejected pairing.
 ("Existing elites persisted while their power fluctuated, and new political and economic elites were formed",
  "KC-4.2.III.B has existing elites confronting new challenges with their power fluctuating, which presupposes their persistence, and KC-4.2.III.A has new political and economic elites formed by imperial conquests and widening global economic opportunities. Each rejected pairing deletes one of those statements."),
 ("more common in this period than suppression",
  "The four rejected statements are KC-4.3.I.B, KC-4.2.III.A and KC-4.2.III.B almost verbatim. KC-4.3.I.B records both accommodation and suppression without saying which was commoner, so a comparison of frequency would have to be defended from another source."),
 ("accommodate diversity or to use the contributions of different groups, though in other cases states did suppress it",
  "KC-4.3.I.B says many states adopted practices to accommodate ethnic and religious diversity or to utilize the contributions of different groups, and that in other cases states suppressed diversity or limited certain groups' roles. A correction has to keep both halves, and each rejected option deletes one."),
 ("overstates the framework, which says the power of existing elites fluctuated",
  "KC-4.2.III.B says the power of existing political and economic elites fluctuated as the elites confronted new challenges to their ability to affect the policies of the increasingly powerful monarchs and leaders. Fluctuation is neither a permanent loss nor a steady gain, so the supporting and the flatly contradicting readings both go beyond the sentence."),
 ("societies group their members, and the norms governing those groups",
  "The Social Interactions and Organization thematic focus printed with this topic says the process by which societies group their members and the norms that govern the interactions between those groups influence political, economic, and cultural institutions and organization, which is what KC-4.3.I.B, KC-4.2.III.A and KC-4.2.III.B describe. The rejected statements are the other four thematic focuses."),
 ("families that made their fortunes in long-distance trade entering the highest ranks",
  "KC-4.2.III.A says imperial conquests and widening global economic opportunities contributed to the formation of new political and economic elites, so evidence for the economic half has to connect commercial wealth with a rise in rank. Rainfall, building stone, wrecks and servants' names bear on none of it."),
 ("differential treatment of groups, the other collects elites that already existed",
  "The first heading, differential treatment of groups in society, politics, and the economy, illustrates KC-4.3.I.B, and the second, existing elites, illustrates KC-4.2.III.B's account of elites whose power fluctuated. Conflicts between states are KC-4.3.III.i and KC-4.3.III.ii, and labor systems and trading networks belong to other topics."),
 ("drew on the contributions of different groups while others suppressed it",
  "The keyed sentence joins both halves of KC-4.3.I.B to KC-4.2.III.A's new elites and KC-4.2.III.B's fluctuating existing elites. Each rejected version flattens KC-4.3.I.B to one half, asserts a direction where the framework says fluctuated, or denies the change Unit 4: Learning Objective M asks students to explain."),
]

TABLE_CHECKS = {20: q20, 21: q21, 22: q22}

if __name__ == "__main__" and "--selftest" in sys.argv:
    ws.controls(w4_7)

ws.marked_stimulus(w4_7)
wh.run(w4_7, CLAIMS, table_checks=TABLE_CHECKS, argv=sys.argv)
