"""Key audit for AP WORLD HISTORY: MODERN 8.1 Setting the Stage for the Cold War
and Decolonization.

One (anchor, claim) per item, in module order. The anchor is a distinctive
substring that MUST appear in the keyed choice and in NO distractor; the claim
states the CED sentence the key rests on, with its Key Concept code, for a human
to audit. `wh_check` refuses any claim or `why` that cites neither a KC code nor
a Learning Objective, because a key traceable only to an author's knowledge of
the twentieth century cannot be checked by anyone reading this bank later.

WHERE A DISTRACTOR IS THE SWAP OF THE KEY, THE ANCHOR CARRIES BOTH CLAUSES.
Six items here are built on a reversal a prepared student could believe:

  q4   the two superpowers with their regime types exchanged
  q5   the post-1918 and post-1945 outcomes exchanged
  q11  the three stages of KC-6.2.II put in the wrong order
  q12  cause and effect reversed, sentiment produced by dissolution
  q16  sentiment falling rather than rising
  q20  most colonial servicemen swapped for fewest

For each of those the anchor spans the whole relation and not just one noun, so
an anchor that matched the swapped distractor would fail the gate rather than
pass it. That defect is on record in `verify_e2_1.py` and it is what this
comment exists to prevent recurring.

WHAT THIS CANNOT DO: it cannot tell whether the history is right. It gates
structure, key/anchor agreement, notation, the absence of figure language, the
presence of a citation, and the arithmetic of the three data questions. The
history is gated by the claims below and by the rule in HISTORY_BRIEF.md that a
key must trace to a sentence in the CED.

NEGATIVE CONTROL: `python3 verify_w8_1.py --selftest`. It rotates all thirty
keys, breaks all thirty anchors, corrupts every cell of every table, injects
each banned notation form, injects figure language into a stem and a choice,
strips the citation from a why and from a claim, duplicates a choice, thins a
why and makes a why name an option by letter -- and asserts not merely that
something raised but WHICH message came back. It also runs positive controls,
so a gate that rejected everything would fail here rather than look thorough.
"""
import sys

import cg_check as cg
import wh_check as wh
import w8_1

T_OUTPUT = w8_1._T_OUTPUT
T_MEMBERS = w8_1._T_MEMBERS
T_TROOPS = w8_1._T_TROOPS

Y38 = "Share of world manufacturing output, 1938 (percent)"
Y48 = "Share of world manufacturing output, 1948 (percent)"
MEMBERS = "Sovereign states holding membership"
YEAR = "Year (hypothetical record)"
SERVICEMEN = "Colonial subjects serving in its armed forces, 1939 to 1945 (thousands)"
COLONIES = "Colonies still administered by it in 1960"


def q6(table, item):
    labs = cg.labels(table)
    pair = {lab: (cg.cell(table, lab, Y38), cg.cell(table, lab, Y48)) for lab in labs}
    risers = [lab for lab in labs if pair[lab][1] > pair[lab][0]]
    fallers = [lab for lab in labs if pair[lab][1] < pair[lab][0]]
    assert len(labs) == 4, f"the key says four states; the table holds {len(labs)}"
    assert len(risers) == 2 and len(fallers) == 2, \
        f"the key needs two risers and two fallers; got {risers} and {fallers}"
    for lab in fallers:
        lost = (pair[lab][0] - pair[lab][1]) / pair[lab][0]
        assert lost > 0.5, f"{lab} lost {lost:.2f} of its share, not more than half"
    # and every distractor false on the same numbers
    assert len(risers) != len(labs), "'every state increased its share' must be false"
    top38 = cg.ranked(table, Y38)[0]
    low48 = cg.ranked(table, Y48)[-1]
    assert top38 != low48, \
        "'the largest in 1938 was the smallest in 1948' must be false"
    assert sum(pair[lab][1] for lab in fallers) < max(pair[lab][1] for lab in labs), \
        "'the two losers together exceeded the largest state' must be false"
    assert sum(pair[lab][0] for lab in labs) != sum(pair[lab][1] for lab in labs), \
        "'the four together were unchanged' must be false"
    return (f"risers {risers} rose; fallers {fallers} each lost more than half of "
            f"their 1938 share; all four distractors recompute false")


def q13(table, item):
    years = cg.col(table, YEAR)
    vals = cg.col(table, MEMBERS)
    assert years[-1] - years[0] == 30, \
        f"the stem says thirty years; the table spans {years[-1] - years[0]}"
    ratio = vals[-1] / vals[0]
    assert 2.5 <= ratio < 3.0, f"'nearly tripled' recomputes to a factor of {ratio:.2f}"
    steps = [b - a for a, b in zip(vals, vals[1:])]
    assert all(s > 0 for s in steps), \
        "'the count fell in at least one decade' must be false, so every step must rise"
    assert steps[-1] < max(steps), \
        "'the largest increase came in the last decade recorded' must be false"
    assert vals[0] / vals[-1] < 0.5, \
        "'more than half of the 1975 members had joined by 1945' must be false"
    return (f"membership runs {vals}, a factor of {ratio:.2f} over {years[-1] - years[0]} "
            f"years, rising at every step, with steps {steps}")


def q20(table, item):
    by_men = cg.ranked(table, SERVICEMEN)
    by_col = cg.ranked(table, COLONIES)
    assert by_men[0] == by_col[-1], (
        f"the key needs the power drawing the most servicemen ({by_men[0]}) to hold the "
        f"fewest colonies ({by_col[-1]})")
    assert by_men[-1] != by_col[-1], \
        "'the power drawing the fewest servicemen held the fewest colonies' must be false"
    assert min(cg.col(table, COLONIES)) <= 10, \
        "'every power retained more than ten colonies' must be false"
    assert sum(cg.col(table, SERVICEMEN)) >= 2000, \
        "'together fewer than two million servicemen' must be false, the column is thousands"
    assert by_men != by_col, \
        "'colonies retained rise as servicemen drawn rise' must be false"
    # The relation is not merely different at the ends, it is inverted the whole
    # way down. Asserting the full reversal rather than only the two extremes is
    # what makes the middle row's cells defended: with only the endpoint checks,
    # corrupting Power Q's figures changed nothing any assertion could see.
    assert by_men == by_col[::-1], (
        f"ordering by servicemen {by_men} is not the exact reverse of ordering by "
        f"colonies retained {by_col}, so the stated relation does not hold throughout")
    return (f"ordering by servicemen gives {by_men} and by colonies retained {by_col}, "
            f"which is the reverse relation the key asserts")


TABLE_CHECKS = {6: q6, 13: q13, 20: q20}

CLAIMS = [
 ("self-government were largely unfulfilled",
  "KC-6.2.II states that hopes for greater self-government were largely unfulfilled following World War I. The 1919 petition and the 1946 statement of non-fulfilment are the two ends of exactly that sentence, and no distractor survives it."),
 ("anti-imperialist sentiment that followed World War II",
  "KC-6.2.II states that in the years following World War II increasing anti-imperialist sentiment contributed to the dissolution of empires and the restructuring of states. The pamphlet's date and its argument from the war's cost place it in that clause and not in the World War I clause of the same sentence."),
 ("technological and economic gains made during World War II by the victorious nations",
  "KC-6.2.IV.C.i states that technological and economic gains experienced during World War II by the victorious nations shifted the global balance of power. The survey reports those gains on one side and their absence on the other, which is the shift itself."),
 ("a democracy, the United States, and an authoritarian communist state, the Soviet Union",
  "KC-6.2.IV.C.ii states that the democracy of the United States and the authoritarian communist Soviet Union emerged as superpowers. The exchanged pairing is a distractor, so the anchor carries each state together with its own regime type rather than the pair alone."),
 ("After World War I those hopes were largely unfulfilled, while after World War II anti-imperialist sentiment contributed to the dissolution of empires",
  "KC-6.2.II sets both outcomes in one sentence and in that order. The reversal of the two halves is a distractor here, so the anchor spans the whole comparison rather than either half of it."),
 ("increased their share, while the other two lost more than half",
  "KC-6.2.IV.C.i makes a redistribution of economic capacity the mechanism by which the global balance of power shifted. The figures are hypothetical and the keyed conclusion, together with the falsity of all four distractors, is recomputed from the table alone in q6 above."),
 ("dissolution of empires and the restructuring of states",
  "KC-6.2.II names the outcome of rising anti-imperialist sentiment as the dissolution of empires and the restructuring of states. The memorandum predicts both halves, sovereign states replacing imperial provinces and the metropole's own government remade."),
 ("power struggle between capitalism and communism",
  "KC-6.2.IV.C.ii states that the emergence of the two superpowers led to ideological conflict and a power struggle between capitalism and communism across the globe. Local quarrels being read everywhere as episodes of one argument is that struggle observed from a third country."),
 ("rising anti-imperialist sentiment after World War II and to the shifting global balance of power",
  "Contextualization, the suggested skill for this topic, connects a specific development to the broader processes of its period; KC-6.2.II and KC-6.2.IV.C.i supply those processes for a 1948 nationalist speech. Summary, word counts and style judgements describe the source without situating it."),
 ("nationalist organizations within those colonies",
  "KC-6.2.II locates increasing anti-imperialist sentiment inside the colonies, so a claim about colonial contentment is a claim about colonial opinion and must be tested against sources colonial subjects produced. The other options report on the imperial state instead."),
 ("then rising anti-imperialist sentiment after World War II, then the dissolution of empires",
  "KC-6.2.II states the three stages in this order: hopes largely unfulfilled after World War I, then increasing anti-imperialist sentiment after World War II, then the dissolution of empires. Every distractor moves at least one stage out of that order, so the anchor carries the ordering and not the stages alone."),
 ("Rising anti-imperialist sentiment contributed to the dissolution of empires",
  "KC-6.2.II makes the sentiment a contributing cause and the dissolution its outcome. The reversed reading is a distractor, so the anchor carries the direction of the relation as well as its two terms."),
 ("nearly tripled over the thirty years",
  "KC-6.2.II describes the dissolution of empires and the restructuring of states, of which a rising count of sovereign states is one visible form. The record is hypothetical and the arithmetic, along with the falsity of the four distractors, is recomputed in q13 above."),
 ("anti-imperialist sentiment that increased in the colonies after World War II",
  "KC-6.2.II dates the increase in anti-imperialist sentiment to the years following World War II, which is where a 1946 veterans' petition belongs. The petition's own premise refutes the exclusion reading, and KC-6.2.IV.C.i places the war's gains with the victors rather than the defeated."),
 ("unfulfilled expectations left by the first war shaped the political language",
  "KC-6.2.II states that hopes for greater self-government were largely unfulfilled after World War I and that anti-imperialist sentiment increased after World War II. The 1947 text reads as a reply to the disappointment the 1919 text set up; nothing in a pair of texts can establish common authorship."),
 ("Anti-imperialist sentiment was increasing, and it contributed to the eventual dissolution",
  "KC-6.2.II describes sentiment increasing and contributing to dissolution, not a single-year collapse and not a decline in sentiment. The reversal of the direction is a distractor, so the anchor carries both the direction and the consequence."),
 ("weakened position from which imperial powers faced rising demands for independence",
  "KC-6.2.IV.C.i marks the war as a redistribution of economic and technological capacity, and KC-6.2.II places rising anti-imperialist demands in the same years. A cabinet report on depleted means is evidence about where those two meet."),
 ("cannot by itself measure how widely that position was held",
  "KC-6.2.II makes a claim about sentiment across colonial societies, which is a claim about breadth. One party's pamphlet is inside the period and on the subject, so the limitation is representativeness rather than date or relevance."),
 ("shifted the global balance of power, and that shifted balance evolved into the Cold War",
  "KC-6.2.IV.C.i gives the first step and KC-6.2.IV.C.ii gives the second, stating that the shifted balance of economic and political power rapidly evolved into the Cold War. The anchor carries both steps because the connection, not either step alone, is what the item asks for."),
 ("drew the most colonial servicemen retained the fewest colonies",
  "KC-6.2.II makes rising anti-imperialist sentiment a contributing cause of the dissolution of empires, and wartime service is one experience such sentiment drew on. The figures are hypothetical and the ordering is recomputed in q20 above; the swapped distractor is why the anchor names both ends of the relation."),
 ("economic and military capacities that no other state could approach",
  "KC-6.2.IV.C.i speaks of a shift in the global balance of power and KC-6.2.IV.C.ii identifies its result as two superpowers. A balance shifts when capacity is redistributed, so concentrated capacity is the direct evidence; treaties and population totals are not measures of relative power."),
 ("could nonetheless lose standing relative to the war's victors",
  "KC-6.2.IV.C.i attributes the shift in the global balance of power to technological and economic gains rather than to territorial extent, which is why a state holding a large empire could still lose standing. KC-6.2.II places the dissolution of those empires in the same years."),
 ("Unfulfilled hopes for self-government after the first war, and independence won amid rising anti-imperialist sentiment",
  "KC-6.2.II supplies both halves in this order, a promise deferred after World War I and empires dissolving amid rising sentiment after World War II. The anchor spans both halves because a distractor exchanges them."),
 ("larger postwar developments make a petition of this kind appear in this year",
  "Contextualization asks what broader process a specific development sits inside, and KC-6.2.II names that process for a 1946 colonial petition. Counting words, examining paper stock and judging tone describe the artefact without situating it."),
 ("two superpowers whose rivalry was ideological as well as territorial",
  "KC-6.2.IV.C.ii states that the two superpowers' emergence led to ideological conflict and a power struggle between capitalism and communism across the globe. A dispute about how societies should be organized is that ideological conflict described from outside."),
 ("emerged economically weaker than the states they had defeated",
  "KC-6.2.IV.C.i places the technological and economic gains of the war with the victorious nations, so the keyed statement reverses the framework's own sentence and is the one not supported. The other four restate KC-6.2.IV.C.i, KC-6.2.II and KC-6.2.IV.C.ii."),
 ("pressed beyond reform toward the end of imperial rule",
  "KC-6.2.II describes anti-imperialist sentiment increasing after World War II and contributing to the dissolution of empires, which is a demand that goes past reform of colonial institutions. The same sentence records the earlier, more modest hopes as unfulfilled rather than granted."),
 ("greater strength of postwar anti-imperialist sentiment together with the war's redistribution",
  "KC-6.2.II supplies the first consideration and KC-6.2.IV.C.i the second, the wartime shift of technological and economic capacity. The distractor pairs belong to developments the framework places later in the century."),
 ("altered economic position of the imperial state after a war that shifted the balance",
  "KC-6.2.IV.C.i states that wartime gains by the victorious nations shifted the global balance of power, which changed what an empire was worth to the state holding it. KC-6.2.II records nationalist movements increasing rather than disappearing over the same years."),
 ("left two states preeminent while anti-imperialist sentiment rose",
  "KC-6.2.IV.C.i gives the redistribution of capacity, KC-6.2.IV.C.ii the two preeminent states and the ideological struggle, and KC-6.2.II the rising anti-imperialist sentiment. The key is the conjunction of the three, and each distractor contradicts at least one."),
]

wh.run(w8_1, CLAIMS, table_checks=TABLE_CHECKS, argv=sys.argv)
