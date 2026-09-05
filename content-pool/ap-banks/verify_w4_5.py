"""Key audit for AP WORLD HISTORY: MODERN 4.5 Maritime Empires Maintained and Developed.

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

THE CONTENT RISK IS A SENTENCE THAT RUNS IN FOUR DIRECTIONS AT ONCE. KC-4.1.IV
says the global flow of silver came especially from Spanish colonies in the
Americas, was used to purchase ASIAN goods for the ATLANTIC markets, and
satisfied CHINESE demand for silver. Every one of those three legs can be
reversed and still read as a sentence about silver and trade -- "Asian silver
satisfying European demand and buying Atlantic goods for Asian markets" is the
same words in a different order and is false. q8 and q16 are built on that, and
their anchors carry the whole relation rather than the word "silver".

The second risk is the pair of policies. KC-4.1.IV.C gives MERCANTILIST policies
to EUROPEAN rulers; KC-4.3.II.A.i, studied one topic earlier, gives RESTRICTIVE
OR ISOLATIONIST policies to some ASIAN states. Exchanging them is a single-word
error that reads fluently, and q17 exists to catch it.

WHAT NO ITEM ASSERTS, and both were live temptations:

  * KC-4.1.VI opens "IN SOME CASES", and that qualifier is kept in every item
    that touches it. The framework does not say interactions always expanded a
    religion's reach or that syncretism happened everywhere, and q15's key keeps
    the qualifier while one distractor drops it for "in every case".
  * KC-4.1.IV asserts BOTH that Afro-Eurasian regional markets continued to
    flourish using ESTABLISHED commercial practices AND that European merchants
    developed NEW shipping services. Neither half displaces the other, and q9,
    q24 and q29 are built to hold them together rather than to key one as
    replacing the other.

NOTE ON AN OVERLAP WITH TOPIC 3.1. The Songhai Empire's conflict with Morocco is
printed twice in this CED: beside 3.1 under "State rivalries" for KC-4.3.III.i,
and beside this topic under "Competition over trade routes" for KC-4.3.III.ii.
`w3_1.py` keys the first; q5 here keys the second and says so, so the two modules
do not contradict each other.

NEGATIVE CONTROL: `python3 verify_w4_5.py --selftest`.
"""
import sys

import cg_check as cg
import wh_check as wh
import wh_stimulus as ws

import w4_5

MINED = "Where the silver was mined"
BOUGHT = "What the ledger records it buying"
EARLY = "Output in an early year"
LATER = "Output in a later year"
MOVING = "What the entry records moving"


def q20(table, item):
    """Three consignments are American silver spent in Asia; the fourth is neither."""
    labs = cg.labels(table)
    assert labs == ["Consignment %d" % n for n in range(1, 5)], \
        f"the four consignments the key counts are not the rows: {labs}"
    # Each cell is PARSED against the two categories this item distinguishes,
    # rather than searched for a substring, so a corrupted cell falls into
    # neither and the check fails instead of quietly passing.
    american, asian = [], []
    for row in table["rows"]:
        mine, spend = cg.normalize(row[1]), cg.normalize(row[2])
        assert mine in ("a spanish colony in the americas", "a mine within europe"), \
            f"the origin {mine!r} is neither of the two this item distinguishes"
        assert spend in ("asian goods for the atlantic markets",
                         "goods in china where demand for silver was high",
                         "grain within europe"), \
            f"the destination {spend!r} is none of the three this item distinguishes"
        american.append(mine == "a spanish colony in the americas")
        asian.append(spend != "grain within europe")
    both = [a and b for a, b in zip(american, asian)]
    assert sum(both) == 3, \
        f"the key needs three American consignments spent in Asia or China; got {sum(both)}"
    # and every distractor false on the same rows
    assert any(american), "'every consignment was mined within Europe' must be false"
    assert not all(a for a in american), \
        "the European-mined row must exist, or the even-split distractor is not clearly false"
    assert any(asian), "'no consignment was spent on Asian goods' must be false"
    assert sum(american) != len(labs) - sum(american), \
        "'divided evenly between American and European mines' must be false"
    return (f"three of the four rows are silver mined in a Spanish colony in the Americas and "
            f"spent on Asian goods or in China, and the fourth is European silver spent on "
            "European grain")


def q21(table, item):
    """Output rises in every district between the two years."""
    districts = cg.labels(table)
    early, later = cg.col(table, EARLY), cg.col(table, LATER)
    assert len(districts) == 4, f"the survey must cover four districts; got {districts}"
    assert all(l > e for e, l in zip(early, later)), \
        f"output must rise in every district; got {early} then {later}"
    # and every distractor false on the same numbers
    assert not any(l < e for e, l in zip(early, later)), \
        "'output fell in every district' must be false"
    assert len(set(later)) == len(later), \
        "'output was the same in every district in the later year' must be false"
    assert all(l != e for e, l in zip(early, later)), \
        "'output did not change in any district' must be false"
    return (f"the four districts move from {early} to {later}, every one of them upward, so no "
            "district falls and no two end level with each other")


def q22(table, item):
    """Three manifest entries are goods, wealth or labor; the fourth is none of them."""
    labs = cg.labels(table)
    assert labs == ["Entry %d" % n for n in range(1, 5)], \
        f"the four entries the key counts are not the rows: {labs}"
    # KC-4.1.IV.D.i names exactly three things: goods, wealth, and labor
    # (including enslaved persons). A row counts only if it opens with one of
    # them, so a corrupted cell no longer counts and the check fails.
    named = ("goods", "wealth", "labor")
    inside = []
    for row in table["rows"]:
        what = cg.normalize(row[1])
        hits = [n for n in named if what.startswith(n)]
        assert len(hits) <= 1, f"the entry {what!r} matches more than one named category"
        inside.append(bool(hits))
    assert sum(inside) == 3, \
        f"the key needs three entries inside the framework's list; got {sum(inside)}"
    assert not all(inside), "'all four entries' must be false"
    assert any(inside), "'none of the entries' must be false"
    assert sum(inside) != 1 and sum(inside) != 2, \
        "the one-entry and two-entry readings must both be false"
    return ("three of the four entries record goods, wealth or labor, the three things "
            "KC-4.1.IV.D.i names, and the fourth is a private letter that is none of them")


CLAIMS = [
 ("expand and control their economies and claim overseas territories",
  "KC-4.1.IV.C states that mercantilist policies and practices were used by European rulers to expand and control their economies and claim overseas territories. Abolition of duties, transfer of claims, withdrawal from trade and a single world price each contradict one part of that sentence."),
 # Both clauses: a distractor keeps 'to finance exploration' and reverses the
 # second half, so an anchor naming only the financing matches it too.
 ("finance exploration, and by rulers to compete against one another",
  "KC-4.1.IV.C says joint-stock companies were used by rulers and merchants to finance exploration and were used by rulers to compete against one another in global trade. Ending competition reverses the second half; tribute is KC-4.3.I.D and the colonial labor systems are KC-4.2.II.D."),
 ("Mercantilist principles",
  "KC-4.1.IV.C describes joint-stock companies as influenced by mercantilist principles, the same principles behind the policies European rulers used to expand and control their economies. Isolationist policy is KC-4.3.II.A.i and belongs to some Asian states; tribute collection is KC-4.3.I.D."),
 ("Rivalries and conflict between states",
  "KC-4.3.III.ii states that economic disputes led to rivalries and conflict between states, sitting beside KC-4.3.III.i on political and religious disputes as a second cause of the same outcome. Settlement, abandonment, merger and an end to competition each reverse it."),
 ("Muslim and European rivalry in the Indian Ocean, and the Moroccan conflict with the Songhai Empire",
  "The illustrative examples beside Unit 4: Learning Objective H print these two under the heading of competition over trade routes, illustrating KC-4.3.III.ii. The same Moroccan conflict is printed again beside topic 3.1 under state rivalries, where it illustrates KC-4.3.III.i, which is why this item names the trade-route heading explicitly."),
 ("Chartered European monopoly companies and the global flow of silver",
  "KC-4.1.IV says the new global circulation of goods was facilitated by chartered European monopoly companies and the global flow of silver. Restrictive policies are KC-4.3.II.A.i, revenue methods KC-4.3.I.D, and the labor systems KC-4.2.II.D."),
 ("Spanish colonies in the Americas",
  "KC-4.1.IV says the global flow of silver came especially from Spanish colonies in the Americas. The framework names no other source of silver anywhere in this unit."),
 # Both clauses: the distractor reverses BOTH legs at once, so an anchor naming
 # only the Asian goods or only the Chinese demand matches it.
 ("purchase Asian goods for the Atlantic markets and to satisfy Chinese demand",
  "KC-4.1.IV says the silver was used to purchase Asian goods for the Atlantic markets and satisfy Chinese demand for silver. The reversal, Atlantic goods for Asian markets satisfying European demand, is the same words in a different order and is not what the sentence says."),
 # Both clauses: the sentence asserts the established practices and the new
 # services together, and each distractor drops one of them.
 ("established commercial practices and new shipping services developed by European merchants",
  "KC-4.1.IV says regional markets continued to flourish in Afro-Eurasia by using established commercial practices and new transoceanic and regional shipping services developed by European merchants. A reading that keeps one half and drops the other misreports one sentence."),
 ("Goods, wealth, and labor, including enslaved persons",
  "KC-4.1.IV.D.i states that the Atlantic trading system involved the movement of goods, wealth, and labor, including enslaved persons. Each rejected option removes one or more of the three things that sentence names."),
 ("African, American, and European, with all parties contributing",
  "KC-4.1.IV.D.ii says the Atlantic trading system involved the movement of labor, including enslaved persons, and the mixing of African, American, and European cultures and peoples, with all parties contributing to this cultural synthesis. The phrase all parties is the framework's own and each rejected option removes a contributor it names."),
 ("continued and intensified in many regions",
  "KC-4.2.II.A states that peasant and artisan labor continued and intensified in many regions as the demand for food and consumer goods increased. Continuity together with intensification is what the sentence asserts, so disappearance, decline and replacement each contradict it."),
 # Both clauses: three distractors rotate the same three products between the
 # same three regions, so an anchor naming one pair alone would not separate them.
 ("Western Europe with wool and linen, India with cotton, and China with silk",
  "The illustrative examples beside Unit 4: Learning Objective I print Western Europe with wool and linen, India with cotton, and China with silk under the heading of increased peasant and artisan labor, which is KC-4.2.II.A's intensification. The rejected options rotate those products between those regions."),
 ("demographic changes in Africa resulting from the trade of enslaved persons",
  "KC-4.2.III.C says some notable gender and family restructuring occurred, including demographic changes in Africa that resulted from the trade of enslaved persons. The word some is the framework's own and the African demographic change is the example it gives."),
 # Both clauses: the qualifier 'in some cases' is half the content, and a
 # distractor keeps the expansion while dropping the qualifier and the conflict.
 ("In some cases the reach of existing religions expanded, and religious conflicts and syncretic belief systems also developed",
  "KC-4.1.VI says that in some cases the increase and intensification of interactions between newly connected hemispheres expanded the reach and furthered development of existing religions, and contributed to religious conflicts and the development of syncretic belief systems and practices. Both the qualifier and the joint mention of conflict and syncretism are the framework's own."),
 # Both clauses: the true statements are themselves distractors, so the anchor
 # must carry the reversed source AND the reversed destination.
 ("from Asian mines to satisfy European demand and to buy Atlantic goods for Asian markets",
  "KC-4.1.IV has silver coming especially from Spanish colonies in the Americas, buying Asian goods for the Atlantic markets and satisfying Chinese demand, so reversing both the source and the destination is the error. The other four options are that one sentence in pieces."),
 # Both clauses: the item is an exchange of two policies between two sets of
 # states, so an anchor naming one policy alone matches a distractor.
 ("Mercantilist policies were used by European rulers, and restrictive or isolationist policies were adopted by some Asian states",
  "KC-4.1.IV.C says mercantilist policies and practices were used by European rulers, while KC-4.3.II.A.i says some Asian states adopted restrictive or isolationist trade policies to limit the effects of European-dominated long-distance trade. The student has exchanged the two."),
 ("mercantilist policy used to expand and control an economy",
  "KC-4.1.IV.C says mercantilist policies and practices were used by European rulers to expand and control their economies and claim overseas territories, and an order reserving colonial carriage to the ruler's own subjects is such a policy. The rejected options are KC-4.3.II.A.i, the second half of KC-4.1.IV.C, KC-4.3.I.D and KC-4.2.II.D."),
 ("joint-stock companies were used by rulers and merchants to finance exploration",
  "KC-4.1.IV.C says joint-stock companies, influenced by mercantilist principles, were used by rulers and merchants to finance exploration and by rulers to compete against one another in global trade, which is the arrangement a chartered monopoly funded by shareholders records. The rejected options are KC-4.1.IV, KC-4.2.II.A, KC-4.3.III.ii and KC-4.1.IV.D.i."),
 ("mined in a Spanish colony in the Americas and spent on Asian goods or in China",
  "KC-4.1.IV says the global flow of silver came especially from Spanish colonies in the Americas and was used to purchase Asian goods for the Atlantic markets and satisfy Chinese demand for silver. Recomputed in q20 above: three of the four rows are exactly that pattern and the fourth is European silver spent on European grain."),
 ("rose in every district",
  "KC-4.2.II.A says peasant and artisan labor continued and intensified in many regions as demand for food and consumer goods increased, and the illustrative examples name wool and linen, cotton and silk. Recomputed in q21 above: all four districts rise between the two years and no two end level."),
 ("Three of the four entries, since the framework names goods, wealth, and labor",
  "KC-4.1.IV.D.i says the Atlantic trading system involved the movement of goods, wealth, and labor, including enslaved persons. Recomputed in q22 above: three entries fall inside that list of three and the private letter falls outside it."),
 ("power is served by controlling the economy and its overseas trade",
  "Under suggested skill 3.A the claim is what the source argues for, and KC-4.1.IV.C supplies the position argued: mercantilist policies and practices were used by European rulers to expand and control their economies and claim overseas territories. A date, an addressee, a length and a use of figures are features of the document rather than its argument."),
 # Both clauses: this is a continuity paired with a change, and each half alone
 # appears inside a rejected pairing.
 ("established commercial practices, while European merchants developed new transoceanic and regional shipping services",
  "KC-4.1.IV holds both in one sentence: regional markets continued to flourish in Afro-Eurasia by using established commercial practices AND new transoceanic and regional shipping services developed by European merchants. Each rejected pairing contradicts that sentence or one of KC-4.2.II.A and KC-4.1.IV.C."),
 ("Mercantilist policies, and the use of joint-stock companies to compete in global trade",
  "KC-4.1.IV.C names both strategies Unit 4: Learning Objective H asks about: mercantilist policies and practices used by European rulers to expand and control their economies, and joint-stock companies used by rulers to compete against one another in global trade. Tribute and bureaucratic elites are KC-4.3.I.D and KC-4.3.I.C, restrictive policies KC-4.3.II.A.i, and the African export trade KC-4.2.II.B."),
 ("changed balance of ages and sexes in the populations of affected African regions",
  "KC-4.2.III.C says some notable gender and family restructuring occurred, including demographic changes in Africa that resulted from the trade of enslaved persons, so evidence for it has to be about the composition of those populations. Silver, weaving, company shares and shipbuilding bear on KC-4.1.IV, KC-4.2.II.A and KC-4.1.IV.C."),
 ("more successful than another's",
  "The four rejected statements are KC-4.1.IV.C, KC-4.1.IV and KC-4.1.IV.D.i almost verbatim. The framework compares no two rulers' policies for success, so a ranking of that kind would need a source outside it."),
 ("contributed to religious conflicts and to syncretic belief systems as well as expanding the reach",
  "KC-4.1.VI says that in some cases the increase and intensification of interactions expanded the reach and furthered development of existing religions, and contributed to religious conflicts and the development of syncretic belief systems and practices, so growth is only one of the outcomes named. The rejected statements are KC-4.2.II.A, KC-4.1.IV, KC-4.1.IV.C and KC-4.2.II.D."),
 ("continued to flourish using established practices, alongside the new shipping services",
  "KC-4.1.IV says regional markets continued to flourish in Afro-Eurasia by using established commercial practices and new transoceanic and regional shipping services developed by European merchants, and KC-4.3.II.A.iii says the same of the Indian Ocean networks. The correction has to keep both the continuation and the new services."),
 ("American silver bought Asian goods and met Chinese demand while Afro-Eurasian regional markets kept flourishing",
  "The keyed sentence joins KC-4.1.IV.C, KC-4.1.IV, KC-4.1.IV.D.i, KC-4.1.IV.D.ii and KC-4.3.III.ii in turn. Each rejected version denies the policies and companies, reverses the direction of the silver, denies the movement of labor and the cultural synthesis, or contradicts KC-4.3.III.ii and KC-4.2.II.A."),
]

TABLE_CHECKS = {20: q20, 21: q21, 22: q22}

if __name__ == "__main__" and "--selftest" in sys.argv:
    ws.controls(w4_5)

ws.marked_stimulus(w4_5)
wh.run(w4_5, CLAIMS, table_checks=TABLE_CHECKS, argv=sys.argv)
