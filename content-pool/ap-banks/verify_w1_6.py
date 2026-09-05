"""Key audit for AP WORLD HISTORY: MODERN 1.6 (Unit 1, Europe c. 1200 to c. 1450).

One (anchor, claim) per question, in module order. The anchor is a distinctive
substring of that question's OWN keyed choice and of no distractor; the claim
states the CED sentence the key rests on, with its Key Concept or Learning
Objective code, so a later reader can check the history rather than take it on
trust.

WHAT THE KEYS REST ON
---------------------
This topic page carries three historical developments and three thematic focus
blocks, and NOTHING ELSE -- it prints no illustrative examples at all, which
was checked in the framework text rather than assumed. Every key below traces
to one of these:

  KC-3.1.III.D.v   Christianity, Judaism, Islam, and the core beliefs and
                   practices of these religions continued to shape societies in
                   Europe                                       (LO 1.K, CDI)
  KC-3.2.I.B.ii    Europe was politically fragmented and characterized by
                   decentralized monarchies, feudalism, and the manorial
                   system                                       (LO 1.L, GOV)
  KC-3.3.III.C     Europe was largely an agricultural society dependent on free
                   and coerced labor, including serfdom          (LO 1.M, SIO)
  the CDI, GOV and SIO thematic focus paragraphs
  KC-3.2.I.A       cited once, in q26, only to state the CONTRAST the framework
                   itself draws between Europe and the Song Dynasty

Everything else anyone knows about medieval Europe is deliberately absent. The
temptation in this topic is enormous -- the century is famous and the framework
says three sentences about it -- and a key resting on the famous material would
rest on the author's memory, which is exactly the failure `HISTORY_BRIEF.md`
forbids and the one no reader of this bank could later check.

WHERE THE ANCHOR CARRIES TWO CLAUSES, AND WHY
---------------------------------------------
Four distractors here are the SWAP of the key rather than an unrelated claim,
so an anchor naming one clause would match the swap as well:

  q7   the service share FALLING against RISING across the three estates
  q8   lord-collected outnumbering direct, and the widest gap in the THIRD
       region against the FIRST
  q16  free labor and coerced labor, their definitions exchanged
  q26  Europe fragmented / the Song governed by bureaucracy, exchanged

Those anchors carry both clauses in order. This is the defect `verify_e2_1.py`
shipped, where an anchor matched the swapped distractor too.

DATA QUESTIONS
--------------
Items 7, 8 and 9 carry tables of HYPOTHETICAL figures and each stem says so,
because the CED prints no European figures and a plausible-looking invented
record would be read by a student as a real one. Each keyed conclusion is
recomputed below from the table alone AND every distractor is shown false on
the same numbers, so the key is reachable from the data without prior
knowledge. q9 additionally checks that the two share columns total one hundred,
which is a check on the table's own coherence rather than on the key -- said
plainly here so nobody mistakes it for evidence about the history.

The control prints a per-question catch rate for the corrupted cells and none
of the three reaches nine of nine. That is the honest number, not a weak check:
the label column cannot be corrupted into a contradiction at all, and tripling
one figure often leaves the keyed conclusion true -- q7's key is that a share
FALLS across three estates, and enlarging the first estate's service column
makes it fall harder. A checker that complained there would be testing the
numbers rather than the claim. A ZERO would mean the check had stopped reading
its table; anything above zero means only that some corruptions leave the key
sound.

NEGATIVE CONTROL: `python3 verify_w1_6.py --selftest`.
"""
import sys

import cg_check as cg
import w1_6
import wh_check

SERVICE = "Households owing labor service on the lord's own fields"
RENT = "Households holding their land for a money rent"
DIRECT = "Districts where the monarch's officers collected dues directly"
LORD = "Districts where a lord collected the dues and forwarded a share"
CULT = "Households whose main work is cultivation (percent)"
CRAFT = "Households whose main work is a craft (percent)"


def q7(table, item):
    """Both arrangements on every estate, and the service SHARE falling."""
    service, rent = cg.col(table, SERVICE), cg.col(table, RENT)
    assert all(s > 0 for s in service) and all(r > 0 for r in rent), \
        f"every estate must record both kinds: service {service}, rent {rent}"
    shares = [s / (s + r) for s, r in zip(service, rent)]
    assert all(b < a for a, b in zip(shares, shares[1:])), \
        f"the service share must FALL at every step: {shares}"
    # every distractor false on the same numbers
    assert not all(b > a for a, b in zip(shares, shares[1:])), "'the share rises' must be false"
    assert not all(r > s for s, r in zip(service, rent)), \
        "'rent households outnumber service households everywhere' must be false"
    most_service = service.index(max(service))
    most_rent = rent.index(max(rent))
    assert most_service != most_rent, \
        "'the estate with the most service households also has the most rent households' must be false"
    return (f"service {service} against rent {rent}: both present everywhere and the "
            f"service share {[round(x, 2) for x in shares]} falls at every step")


def q8(table, item):
    """Lord-collected outnumbers direct everywhere, and the gap is widest LAST."""
    direct, lord = cg.col(table, DIRECT), cg.col(table, LORD)
    assert all(l > d for d, l in zip(direct, lord)), \
        f"lord-collected must exceed direct in every region: {direct} vs {lord}"
    gaps = [l - d for d, l in zip(direct, lord)]
    assert gaps.index(max(gaps)) == len(gaps) - 1, \
        f"the widest gap must be in the LAST region listed: {gaps}"
    # every distractor false on the same numbers
    assert not all(d > l for d, l in zip(direct, lord)), \
        "'direct outnumbers lord-collected everywhere' must be false"
    assert not any(d == l for d, l in zip(direct, lord)), \
        "'the two are equal in one region' must be false"
    assert gaps.index(max(gaps)) != 0, "'the widest gap is in the first region' must be false"
    assert direct.index(max(direct)) != lord.index(max(lord)), \
        "'the region with the most direct districts also has the most lord-collected' must be false"
    return (f"direct {direct} against lord-collected {lord}: lord-collected leads "
            f"everywhere and the gaps {gaps} peak in the last region")


def q9(table, item):
    """More than three quarters cultivating in every village listed."""
    cult, craft = cg.col(table, CULT), cg.col(table, CRAFT)
    # table coherence first: these are shares of the same households
    assert all(c + k == 100 for c, k in zip(cult, craft)), \
        f"the two share columns must total one hundred: {cult} and {craft}"
    assert all(c > 75 for c in cult), f"every village must exceed three quarters: {cult}"
    # every distractor false on the same numbers
    assert not any(c < 50 for c in cult), "'fewer than half in one village' must be false"
    top_craft = craft.index(max(craft))
    assert not craft[top_craft] > cult[top_craft], \
        "'craft outnumbers cultivation in the most craft-heavy village' must be false"
    assert len(set(cult)) > 1, "'the three villages have the same share' must be false"
    assert cult.index(max(cult)) != top_craft, \
        "'the largest craft share goes with the largest cultivating share' must be false"
    return (f"cultivating shares {cult} against craft shares {craft}: each pair totals "
            f"one hundred and every cultivating share exceeds seventy five")


TABLE_CHECKS = {7: q7, 8: q8, 9: q9}

CLAIMS = [
 ("estate as the unit of cultivation",
  "KC-3.2.I.B.ii states that Europe was politically fragmented and characterized by decentralized monarchies, feudalism, and the manorial system. The survey shows a king above a count, land held for service, and an estate worked by its tenants, which is those three characteristics at once. Each rejected option denies one of the sentence's own terms."),

 ("divided among many holders",
  "KC-3.2.I.B.ii calls Europe politically fragmented and characterizes it by decentralized monarchies, and Learning Objective L asks for the causes and consequences of political DECENTRALIZATION in Europe. Division of authority is what fragmentation and decentralization share; the absence of authority altogether is a claim the framework does not make."),

 ("continued to shape societies in Europe",
  "KC-3.1.III.D.v states that Christianity, Judaism, Islam, and the core beliefs and practices of these religions continued to shape societies in Europe. All three traditions are in that sentence, so an option naming only one is short of it, and the word continued rules out a first arrival inside the period."),

 ("free and on coerced labor together",
  "KC-3.3.III.C states that Europe was largely an agricultural society dependent on free and coerced labor, including serfdom. Both conditions appear on the single estate in the stimulus, which is the pairing the sentence makes; the two strongest distractors each delete one half of it."),

 ("seek it from the lord of his district",
  "Learning Objective L distinguishes the CAUSES of political decentralization in Europe from its CONSEQUENCES, and KC-3.2.I.B.ii states that Europe was politically fragmented and characterized by decentralized monarchies and feudalism. Where a subject must go for judgment follows from a division of authority; the four rejected options are conditions that produce the division."),

 ("how far authority is dispersed within a monarchy",
  "KC-3.2.I.B.ii uses the phrase DECENTRALIZED MONARCHIES, which would be self-contradictory if decentralization meant the end of monarchy, and the Governance thematic focus treats how power is exercised as a separate question from whether a government exists at all."),

 ("records households of both kinds, and the share owing labor service falls",
  "Recomputed in q7 above from the table alone, distractors included. KC-3.3.III.C states that Europe was largely an agricultural society dependent on free AND coerced labor, and two arrangements present together in differing proportions is what such a dependence looks like in figures. The anchor carries both clauses because the strongest distractor reverses the direction of the trend."),

 ("collected through a lord outnumber those collected directly, and the gap between the two is widest in the third region",
  "Recomputed in q8 above from the two columns. KC-3.2.I.B.ii characterizes Europe by decentralized monarchies, and revenue reaching a monarch mostly through intermediaries rather than through his own officers is what decentralization looks like in an administrative record. The anchor carries both clauses because two distractors invert one clause each."),

 ("more than three quarters of households in every village",
  "Recomputed in q9 above, which also checks that the two share columns total one hundred. KC-3.3.III.C states that Europe was LARGELY an agricultural society, and a large majority of households in cultivation beside a smaller craft population is what the word largely describes."),

 ("equal in the number of their adherents",
  "KC-3.1.III.D.v states that Christianity, Judaism, Islam, and the core beliefs and practices of these religions continued to shape societies in Europe. It names three traditions and their practices and says nothing whatever about their relative numbers, so the only option the sentence does not support is the one about numbers."),

 ("could belong to a lord rather than to the monarch",
  "The Governance thematic focus states that governments maintain order through a variety of administrative institutions, policies, and procedures, and KC-3.2.I.B.ii characterizes Europe by decentralized monarchies and feudalism. A lord's court is one of that variety, and the framework nowhere describes such a court as acting against the crown."),

 ("shaped how the society grouped its members",
  "Learning Objective M asks for the effects of agriculture on social organization in Europe, KC-3.3.III.C states that Europe was largely an agricultural society dependent on free and coerced labor including serfdom, and the Social Interactions thematic focus states that the process by which societies group their members influences their institutions and organization."),

 ("authority over the road was divided among several holders",
  "KC-3.2.I.B.ii states that Europe was politically fragmented and characterized by decentralized monarchies. Several holders each exercising authority over a stretch of one road, each on his own terms, is that fragmentation at the scale of a journey."),

 ("fragmentation describes how authority was distributed",
  "KC-3.2.I.B.ii asserts fragmentation and decentralized MONARCHIES in the same clause, and the Governance thematic focus states that governments maintain order through a variety of administrative institutions, policies, and procedures. Fragmentation is a description of distribution, not a denial that government existed."),

 ("held on condition of service owed to the grantor",
  "KC-3.2.I.B.ii names feudalism among the characteristics of a politically fragmented Europe. A grant of land held OF a grantor in return for armed service is the conditional tenure that term denotes, and an outright sale is precisely the case that carries no such condition."),

 ("able to withhold his labor or depart, and the other binds him to render it",
  "KC-3.3.III.C states that Europe was largely an agricultural society dependent on free AND coerced labor, including serfdom. The sentence pairs the two inside one agricultural society, so neither a separation by place, nor a separation in time, nor an identity between them follows. The anchor carries both halves because a distractor exchanges the two definitions."),

 ("ordered ordinary conduct and not only formal worship",
  "KC-3.1.III.D.v names the core beliefs AND PRACTICES of Christianity, Judaism and Islam as continuing to shape societies in Europe, and the Cultural Developments thematic focus states that beliefs illustrate how groups in society view themselves and often carry social implications. Days of rest, fasts and almsgiving are practices ordering conduct."),

 ("owed days of work as well as a money rent",
  "KC-3.3.III.C asserts matters of fact about the arrangements under which land was worked in Europe, and Learning Objective M asks for the effects of agriculture on social organization. What a household owed can be checked against a record, while justice, superiority, desert and doctrinal truth cannot be settled by observation."),

 ("removing any one leaves the pattern unexplained",
  "The Governance thematic focus states that a VARIETY of internal and external factors contribute to state formation, expansion, and decline, and Learning Objective L asks for the causes of political decentralization in Europe. A multi-cause account is strengthened by evidence about the causes themselves, not by a fact about a single case."),

 ("fixed by the custom of the estate on which it lay",
  "KC-3.2.I.B.ii names the manorial system among the characteristics of Europe in this period and KC-3.3.III.C describes an agricultural society dependent on free and coerced labor. The estate is the unit in which those two sentences meet, and the framework nowhere describes European cultivation as centrally directed."),

 ("intermediaries who brought their own followings",
  "KC-3.2.I.B.ii characterizes Europe by decentralized monarchies and feudalism, and the Governance thematic focus states that governments obtain, retain, and exercise power in different ways and for different purposes. Acting through men who bring their own followings is one of those ways and is what decentralization means for a monarch's reach."),

 ("before this period and went on doing so within it",
  "KC-3.1.III.D.v says that Christianity, Judaism, Islam and their core beliefs and practices CONTINUED to shape societies in Europe, and the CED states that developments are not constrained by the given dates and may begin before, or continue after, the period. Continuing is not the same as never changing, which is what one distractor substitutes."),

 ("an estate may hold households of both conditions at once",
  "KC-3.3.III.C states that Europe was largely an agricultural society dependent on free and coerced labor, including serfdom. The sentence joins the two conditions within one society, which is what lets two accurate descriptions of the same estate appear to conflict without doing so."),

 ("without the claim that no other work was done",
  "KC-3.3.III.C uses the word LARGELY, which asserts predominance rather than exclusivity, and Learning Objective M asks for the effects of agriculture on social organization rather than for a ranking of regions by output. Each rejected option adds a claim the sentence does not make."),

 ("rest on established custom",
  "KC-3.2.I.B.ii names the manorial system as a characteristic of Europe in this period, and the Governance thematic focus names policies and procedures among the means by which governments maintain order. An appeal to how a thing was done in a predecessor's time is an appeal to custom as the ground of the obligation."),

 ("Europe is described as politically fragmented, while the Song are described as maintaining rule",
  "KC-3.2.I.B.ii states that Europe was politically fragmented and characterized by decentralized monarchies, feudalism, and the manorial system, while KC-3.2.I.A states that the Song Dynasty utilized traditional methods of Confucianism and an imperial bureaucracy to maintain and justify its rule. The anchor carries both halves in order because the strongest distractor is the same pair exchanged."),

 ("the same kind of authority a lay lord exercised",
  "The Cultural Developments thematic focus states that the interactions of societies and their beliefs often have political, social, and cultural implications, KC-3.1.III.D.v names the religions that continued to shape European societies, and KC-3.2.I.B.ii makes lordship over land the political question of the period. Land and jurisdiction are therefore where a religious effect shows as a political one."),

 ("a single estate may be unrepresentative",
  "KC-3.3.III.C and KC-3.2.I.B.ii both make general statements about Europe, and the Social Interactions thematic focus concerns how a society groups its members. A general claim is supported by particular evidence without being established by one instance, which is a matter of scale rather than of the record's reliability."),

 ("stand under more than one authority at once",
  "KC-3.1.III.D.v states that Christianity, Judaism, Islam and their core beliefs and practices continued to shape societies in Europe, and KC-3.2.I.B.ii describes a politically fragmented Europe. Overlapping authority is what those two sentences together describe, and the framework nowhere presents them as alternatives."),

 ("free in some cases and coerced in others",
  "The three historical developments of this topic are KC-3.2.I.B.ii on political fragmentation, decentralized monarchies, feudalism and the manorial system, KC-3.3.III.C on an agricultural society dependent on free and coerced labor including serfdom, and KC-3.1.III.D.v on Christianity, Judaism and Islam continuing to shape societies in Europe. The key states all three and every rejected option contradicts at least one."),
]

wh_check.run(w1_6, CLAIMS, TABLE_CHECKS, sys.argv)
