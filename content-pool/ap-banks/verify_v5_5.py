"""Structural gate for AP U.S. Government 5.5 Third-Party Politics.

gov345_check plus the four usgov_anchor helpers, plus two content gates.

  _comparative  EK 5.5.A.1 is a COMPARATIVE claim with a stated DIRECTION, and
                both parts are droppable:
                  * its first four words are IN COMPARISON TO PROPORTIONAL
                    SYSTEMS, so winner-take-all is a barrier relative to a named
                    alternative rather than in the abstract;
                  * its second sentence says winner-take-all voting ADVANTAGES
                    THE TWO-PARTY SYSTEM.
                Reversing the direction -- making proportional allocation the
                barrier, or winner-take-all a help to third parties -- is a
                clean falsehood, and it is the kind that reads fluently because
                both sentences contain the same nouns. The gate refuses it.

  _second_barrier
                EK 5.5.A.2 is the heart of the topic and the harder half. A
                third party whose ideas SUCCEED -- taken up by a major party --
                is thereby made LESS likely to succeed ELECTORALLY. Winning the
                argument costs it the reason voters had to support it.

                A student who has absorbed only the first barrier explains every
                third-party failure by the electoral system and has no account
                of the party that fades while its programme is being adopted.
                So the gate pins EK 5.5.A.2's mechanism, counts how many keys
                turn on it, and refuses any key that explains a third party's
                decline by its ideas being unpopular -- which is exactly the
                inference the second table is built to defeat, since the
                proposals that were incorporated there are the MOST popular
                ones in it.
"""
import gov345_check as gc
import usgov_anchor as ua
import v5_5

ANCHORS = {
 1: "Winner-take-all voting districts",
 2: "so winner-take-all is a barrier relative to a named alternative",
 3: "The two-party system in the United States",
 4: "so support that falls short everywhere yields nothing",
 5: "which winner-take-all does not guarantee",
 6: "arises from how the electoral system is built",
 7: "account of winner-take-all districts as a structural barrier",
 8: "That the United States should adopt a proportional system",
 9: "The incorporation of third-party agendas into the platforms of major political parties",
 10: "can now obtain them by voting for a major party",
 11: "It operates through the third party's ideas succeeding rather than failing",
 12: "incorporation of third-party agendas into major party platforms",
 13: "describes a consequence of what a major party puts in it",
 14: "whose distinctive proposals appear in a major party's platform and whose vote then",
 15: "Both identify a barrier to third-party and independent candidate success",
 16: "separate barriers that can operate at once",
 17: "which is a barrier operating through ideas rather than through seat allocation",
 18: "though an independent candidate has no party agenda for a major party to incorporate",
 19: "while this topic describes structural features that reduce the number of parties",
 20: "new parties will keep forming even where the system disadvantages them",
 21: "How often major parties incorporate third-party agendas",
 22: "which is a comparison of quantities",
 23: "one built into how votes become seats, and one arising when major parties adopt",
 24: "so a candidate can draw votes across many states and win no electors",
 25: "and 2 of the 100 seats under winner-take-all, against 19 seats under proportional",
 26: "structural barrier in comparison to proportional systems",
 27: "since both major parties hold a larger share of seats than of votes",
 28: "drew lower vote shares in the next election than those whose proposals were not",
 29: "incorporation of third-party agendas into major party platforms is a barrier",
 30: "removes the distinctive reason to vote for the third party",
}

GROUNDING = {
 1: "EK 5.5.A.1, verbatim: 'In comparison to proportional systems, winner-take-all voting "
    "districts serve as a structural barrier to third-party and independent candidate "
    "success.'",
 2: "EK 5.5.A.1's opening phrase IN COMPARISON TO PROPORTIONAL SYSTEMS, which makes the claim "
    "comparative and supplies the alternative in the same sentence.",
 3: "EK 5.5.A.1's second sentence: 'Winner-take-all voting advantages the two-party system in "
    "the U.S.'",
 4: "EK 5.5.A.1's mechanism: one winner per district means votes for anyone else produce no "
    "seats, which is why the framework calls it structural rather than a matter of appeal.",
 5: "EK 5.5.A.1's named alternative. Proportional allocation matches seats to vote shares; "
    "winner-take-all can leave the same share with almost nothing.",
 6: "The framework's term STRUCTURAL BARRIER, which EK 5.2.A.1 also uses for features of "
    "election administration -- a property of the arrangement rather than of a candidate.",
 7: "EK 5.5.A.1 applied to uniform support that never leads a district, the clearest case of "
    "the rule converting substantial votes into no seats.",
 8: "EK 5.5.A.1 read for what it omits: an effect described and nothing recommended.",
 9: "EK 5.5.A.2, verbatim. A second barrier, operating through the major parties rather than "
    "through the voting system.",
 10: "EK 5.5.A.2's mechanism: incorporation removes the distinctive reason to vote for the "
     "smaller party. The framework claims no legal consequence and no loss of popularity.",
 11: "EK 5.5.A.2 read for what makes it unusual: the barrier arises when the third party's "
     "ideas succeed, so its programme advances while its electoral prospects do not.",
 12: "EK 5.5.A.2 applied to the sequence it describes -- adoption followed by reduced success "
     "-- in a scenario where the electoral rule did not change.",
 13: "EK 5.3.B.1.ii names party platforms as a party function; EK 5.5.A.2 describes a "
     "consequence of what a major party puts in one.",
 14: "EK 5.5.A.2 against EK 5.5.A.1. Evidence for the second must involve incorporation; the "
     "distractors all concern how votes become seats.",
 15: "EK 5.5.A.1 and EK 5.5.A.2's shared object: third-party and independent candidate "
     "success. Neither recommends anything.",
 16: "EK 5.5.A.1 and EK 5.5.A.2 as separate mechanisms the framework does not present as "
     "exclusive.",
 17: "EK 5.5.A.2 as the second barrier a single-cause explanation misses -- the party that "
     "fades while its programme is being adopted.",
 18: "Both statements name 'third-party AND INDEPENDENT CANDIDATE success', so both barriers "
     "are stated to reach independents; EK 5.5.A.2's mechanism runs through a party agenda, "
     "which is a difference worth noticing.",
 19: "Federalist No. 10 (required document), quoted verbatim; the CED attaches it to 5.5.A. "
     "Madison treats variety among parties and interests as protective, which sits beside EK "
     "5.5.A.1's account of a rule advantaging a two-party system.",
 20: "Federalist No. 10, quoted verbatim. A standing cause of division keeps producing "
     "organizations, which is a different question from why they struggle to win office.",
 21: "EK 5.5.A.2 read for what it omits: a mechanism identified, no frequency stated.",
 22: "The CED's assignment of skill 3.D to this topic. Each barrier is visible as a "
     "discrepancy: votes against seats, and support against subsequent vote share.",
 23: "EK 5.5.A.1 and EK 5.5.A.2 together. The last distractor is contradicted by EK 5.5.A.2, "
     "under which a third party is undercut when its ideas prove popular enough to adopt.",
 24: "EK 5.8.B.1, which states that most states use a winner-take-all system to allocate "
     "electors, read against EK 5.5.A.1's identification of that rule as the barrier. The "
     "framework says MOST because states can choose how they allocate.",
 25: "Data item, CED skill 3.D. Every vote share and both seat allocations are recomputed.",
 26: "EK 5.5.A.1's comparison located in a table setting the same votes against two rules.",
 27: "EK 5.5.A.1's second sentence in numbers: both major parties over-represented and both "
     "third parties under-represented. Recomputed below.",
 28: "Data item, CED skill 3.D. Adoption and subsequent vote share are cross-tabulated below.",
 29: "EK 5.5.A.2's mechanism and its effect located as the table's third and fourth columns.",
 30: "EK 5.5.A.2 against the inference that the parties failed because their ideas were "
     "unpopular. The support column is recomputed below, and it runs the other way.",
}

VOTES, WTA, PROP = ("Share of votes cast (%)", "Seats won under winner-take-all",
                    "Seats under proportional allocation")
SUPPORT, ADOPTED, NEXT = ("Public support at the time (%)",
                          "Adopted into a major party platform",
                          "Third-party vote share next election (%)")


def _col(t, header):
    j = t["headers"].index(header)
    return [r[j] for r in t["rows"]]


def _num(t, header):
    return [gc.num(c) for c in _col(t, header)]


def _thirds(t):
    return [i for i, n in enumerate(_col(t, "Party")) if n.startswith("Third")]


def q25(t):
    """Third parties: 19 percent of votes, 2 winner-take-all seats, 19 proportional."""
    votes, wta, prop = _num(t, VOTES), _num(t, WTA), _num(t, PROP)
    assert sum(votes) == 100 and sum(wta) == 100 and sum(prop) == 100, \
        f"a column does not total 100: {sum(votes):.0f}, {sum(wta):.0f}, {sum(prop):.0f}"
    idx = _thirds(t)
    tv = sum(votes[i] for i in idx)
    tw = sum(wta[i] for i in idx)
    tp = sum(prop[i] for i in idx)
    assert (tv, tw, tp) == (19, 2, 19), \
        f"third parties hold {tv:.0f} percent, {tw:.0f} and {tp:.0f} seats, not 19, 2 and 19"
    return (f"third parties: {tv:.0f} percent of votes, {tw:.0f} winner-take-all seats, "
            f"{tp:.0f} proportional seats")


def q26(t):
    """The table sets one set of votes against two allocation rules."""
    heads = [h.lower() for h in t["headers"]]
    assert any("winner-take-all" in h for h in heads), f"no winner-take-all column: {heads}"
    assert any("proportional" in h for h in heads), f"no proportional column: {heads}"
    for h in heads:
        for other in ("platform", "adopted", "agenda"):
            assert other not in h, f"column {h!r} concerns incorporation, the other statement"
    return "one vote column against two allocation rules, and no platform column"


def q27(t):
    """Both majors over-represented under winner-take-all; both thirds under."""
    votes, wta = _num(t, VOTES), _num(t, WTA)
    names = _col(t, "Party")
    for i, n in enumerate(names):
        if n.startswith("Major"):
            assert wta[i] > votes[i], f"{n} is not over-represented: {wta[i]:.0f} vs {votes[i]:.0f}"
        else:
            assert wta[i] < votes[i], f"{n} is not under-represented: {wta[i]:.0f} vs {votes[i]:.0f}"
    return ("winner-take-all seats against vote shares: "
            + ", ".join(f"{n.split()[-1]} {w:+.0f}" for n, w, v in zip(names, wta, votes)
                        for w in [w - v]))


def _split(t):
    adopted = [a.strip().lower() == "yes" for a in _col(t, ADOPTED)]
    nxt, sup = _num(t, NEXT), _num(t, SUPPORT)
    return adopted, nxt, sup


def q28(t):
    """Adopted proposals are followed by lower third-party vote shares."""
    adopted, nxt, sup = _split(t)
    yes = [x for a, x in zip(adopted, nxt) if a]
    no = [x for a, x in zip(adopted, nxt) if not a]
    assert yes and no, "the adoption column does not take both values"
    assert max(yes) < min(no), f"adopted {yes} do not all fall below not adopted {no}"
    return (f"next-election vote shares: adopted {yes}, not adopted {no}")


def q29(t):
    """The table records incorporation and its aftermath, not seat allocation."""
    heads = [h.lower() for h in t["headers"]]
    assert any("adopted" in h and "platform" in h for h in heads), \
        f"no incorporation column: {heads}"
    assert any("next election" in h for h in heads), f"no aftermath column: {heads}"
    for h in heads:
        for other in ("seat", "district", "proportional"):
            assert other not in h, f"column {h!r} concerns seat allocation, the other statement"
    return "an incorporation column and an aftermath column, and no seat column"


def q30(t):
    """The adopted proposals are the two MOST popular, which defeats the unpopularity reading."""
    adopted, nxt, sup = _split(t)
    yes_sup = [s for a, s in zip(adopted, sup) if a]
    no_sup = [s for a, s in zip(adopted, sup) if not a]
    assert min(yes_sup) > max(no_sup), \
        f"the adopted proposals {yes_sup} are not the most popular against {no_sup}"
    assert sorted(yes_sup, reverse=True) == [61, 54], \
        f"the adopted proposals stand at {yes_sup}, not the 61 and 54 the key names"
    return (f"adopted proposals had support {sorted(yes_sup, reverse=True)}, the two highest, "
            f"against {sorted(no_sup, reverse=True)} for the others")


# --- module-specific content gates -------------------------------------------

_REVERSED = (
    "proportional allocation of seats serve",
    "proportional systems are the barrier",
    "winner-take-all advantages third parties",
    "winner-take-all voting advantages third-party",
    "winner-take-all disadvantages the two-party system",
    "the winner-take-all rule disadvantages it",
)


def _comparative(module):
    """EK 5.5.A.1 keeps its comparison and its direction."""
    bad = []
    for i, item in enumerate(module.QUESTIONS, 1):
        key = item["choices"][item["ans"]].lower()
        for r in _REVERSED:
            if r in key:
                bad.append(f"q{i} key: reverses EK 5.5.A.1 ({r!r}). The framework says "
                           "winner-take-all districts are the barrier, in comparison to "
                           "proportional systems, and that winner-take-all voting ADVANTAGES "
                           "the two-party system")
    q1 = module.QUESTIONS[0]
    if "winner-take-all" not in q1["choices"][q1["ans"]].lower():
        bad.append("q1: the key no longer names winner-take-all districts as the barrier")
    q2 = module.QUESTIONS[1]
    k2 = q2["choices"][q2["ans"]].lower()
    if "comparative" not in k2 and "relative to" not in k2:
        bad.append("q2: the key no longer records EK 5.5.A.1's opening phrase as making the "
                   "claim comparative rather than absolute")
    q3 = module.QUESTIONS[2]
    if "two-party system" not in q3["choices"][q3["ans"]].lower():
        bad.append("q3: the key no longer states what EK 5.5.A.1 says winner-take-all voting "
                   "ADVANTAGES")
    if bad:
        print(f"FAIL {module.__name__} comparative")
        for b in bad:
            print("  -", b)
        raise SystemExit(1)
    print(f"OK  {module.__name__} comparative: EK 5.5.A.1 keeps its comparison to proportional "
          "systems and its direction, and no key makes winner-take-all a help to third parties")


_UNPOPULAR = (
    "because their proposals were unpopular",
    "because their ideas were unpopular",
    "the proposals become unpopular",
    "third parties fail because their ideas are unpopular",
)


def _second_barrier(module):
    """EK 5.5.A.2's mechanism survives, and decline is not explained by unpopularity."""
    bad = []
    for i, item in enumerate(module.QUESTIONS, 1):
        key = item["choices"][item["ans"]].lower()
        stem = item["q"].lower()
        refusing = "correction" in stem or "not state" in stem or "most popular" in key
        for u in _UNPOPULAR:
            if u in key and not refusing:
                bad.append(f"q{i} key: explains a third party's decline by {u!r}. EK 5.5.A.2's "
                           "barrier operates when the party's ideas SUCCEED and a major party "
                           "adopts them, which is the opposite of unpopularity")
    q9 = module.QUESTIONS[8]
    k9 = q9["choices"][q9["ans"]].lower()
    if "incorporation" not in k9 or "platform" not in k9:
        bad.append("q9: the key no longer states EK 5.5.A.2's barrier, the incorporation of "
                   "third-party agendas into the platforms of major political parties")
    q11 = module.QUESTIONS[10]
    if "succeeding" not in q11["choices"][q11["ans"]].lower():
        bad.append("q11: the key no longer records what makes EK 5.5.A.2 unusual -- that the "
                   "barrier operates through the third party's ideas succeeding")
    turn = sum(1 for item in module.QUESTIONS
               if "incorporat" in item["choices"][item["ans"]].lower()
               or "adopt" in item["choices"][item["ans"]].lower())
    if turn < 5:
        bad.append(f"only {turn} keys turn on EK 5.5.A.2; it is the harder of the two barriers "
                   "and a module that lets it go explains every third-party failure by the "
                   "electoral system")
    if bad:
        print(f"FAIL {module.__name__} second barrier")
        for b in bad:
            print("  -", b)
        raise SystemExit(1)
    print(f"OK  {module.__name__} second barrier: EK 5.5.A.2's incorporation mechanism "
          f"survives, {turn} keys turn on it, and no key explains a third party's decline by "
          "its ideas being unpopular")


ua.shape(v5_5)
ua.check(v5_5, ANCHORS, GROUNDING)
ua.notation(v5_5)
_comparative(v5_5)
_second_barrier(v5_5)
gc.check(v5_5, arith={25: q25, 26: q26, 27: q27, 28: q28, 29: q29, 30: q30})
