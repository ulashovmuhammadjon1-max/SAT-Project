"""Key audit for AP WORLD HISTORY: MODERN 4.3 Columbian Exchange.

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

THIS TOPIC'S CONTENT RISK IS THE DIRECTION OF TRAVEL, and it is why six anchors
below carry two clauses. The framework states four movements and every one of
them reads just as well backwards:

  KC-4.1.V.A  diseases endemic in the EASTERN Hemisphere spread with European
              colonization of the Americas, and substantially reduced the
              INDIGENOUS populations
  KC-4.1.V.B  AMERICAN foods became staples in Europe, Asia, and Africa; cash
              crops went out to Europe and the Middle East
  KC-4.1.V.C  AFRO-EURASIAN fruit trees, grains, sugar and animals were brought
              to the Americas, and other foods by African enslaved persons
  KC-4.1.V.D  populations in AFRO-EURASIA gained nutritionally

q13 exchanges the crops with the animals, q14 exchanges the hemispheres of the
diseases, q29 exchanges the loss with the gain, and q30 does several at once. In
each the anchor spans the whole relation rather than one noun of it, because an
anchor naming only "American foods" or only "the Eastern Hemisphere" matches the
reversal too. That defect is on record in `verify_e2_1.py`.

WHAT NO ITEM ASSERTS, and each of these was a live temptation while writing:

  * No American crop is named. The framework names none -- not maize, not the
    potato -- so the module says "American food crops", which is its own phrase.
    The illustrative examples name okra and rice, but under the heading of foods
    brought by African ENSLAVED PERSONS, and q16 keys them only there.
  * No figure or proportion for the population loss. KC-4.1.V.A says some of
    these diseases substantially reduced the indigenous populations with
    catastrophic effects in many areas, and that is all; q25 is built out of
    exactly that silence, keying the comparison of two diseases' mortality as
    the claim that would need outside evidence.
  * NO DISEASE TRAVELS WEST TO EAST HERE. The framework states one direction and
    is silent on the other. A question keying the reverse would be teaching a
    silence as a fact, so q5 and q14 ask what the framework says and key the
    Eastern Hemisphere, rather than asserting that nothing went the other way.

NEGATIVE CONTROL: `python3 verify_w4_3.py --selftest`.
"""
import sys

import cg_check as cg
import wh_check as wh
import wh_stimulus as ws

import w4_3

DIRECTION = "Direction recorded for it"
INDEX = "Recorded population of one region (index, first period equals 100)"
STAPLES = "American food crops grown there as staples"


def q19(table, item):
    """Three cargoes go to the Americas and one comes away from them."""
    cargoes = cg.labels(table)
    assert len(cargoes) == 4 and len(set(cargoes)) == 4, \
        f"the list must hold four distinct cargoes; got {cargoes}"
    # Each direction cell is PARSED into an origin and a destination rather than
    # searched for a substring. The first draft used `"to the americas" in d`,
    # which survived every corruption the self-test could inject -- 0 of 8 cells
    # caught -- because appending text to a cell leaves every substring in place.
    # A cell must now END with its destination, so a corrupted cell no longer
    # parses at all. The control is why this is here.
    dirs = [cg.normalize(r[1]) for r in table["rows"]]
    origins = ("carried from afro-eurasia", "carried by african enslaved persons",
               "carried from the americas")
    to_americas, from_americas = [], []
    for d in dirs:
        origin = [o for o in origins if d.startswith(o)]
        assert len(origin) == 1, f"the direction {d!r} names no origin this item recognises"
        rest = d[len(origin[0]):].strip()
        assert rest in ("to the americas", "to afro-eurasia"), \
            f"the direction {d!r} does not end at one of the two hemispheres"
        to_americas.append(rest == "to the americas")
        from_americas.append(rest == "to afro-eurasia")
    for d, t, f in zip(dirs, to_americas, from_americas):
        assert t != f, f"the direction {d!r} is neither clearly toward nor clearly away"
    assert sum(to_americas) == 3, \
        f"the key needs three cargoes carried to the Americas; got {sum(to_americas)}"
    assert sum(from_americas) == 1, \
        f"the key needs one cargo carried away from the Americas; got {sum(from_americas)}"
    # and every distractor false on the same rows
    assert not all(to_americas), "'all four were carried to the Americas' must be false"
    assert not all(from_americas), "'all four were carried away' must be false"
    assert sum(to_americas) != sum(from_americas), \
        "'the cargoes were divided evenly' must be false"
    return (f"three of the four rows record a cargo carried to the Americas and one records a "
            f"cargo carried away from them, so the list runs both ways and not evenly")


def q20(table, item):
    """The count falls at every step and ends below half the first period."""
    labs = cg.labels(table)
    assert labs == ["First period", "Second period", "Third period", "Fourth period"], \
        f"the four periods the key speaks of are not the rows: {labs}"
    idx = cg.col(table, INDEX)
    assert idx[0] == 100, f"the index must open at 100 by its own header; got {idx[0]}"
    assert all(idx[i + 1] < idx[i] for i in range(len(idx) - 1)), \
        f"the count must fall at every step; got {idx}"
    assert idx[-1] < 50, f"the key needs the final level below half the first; got {idx[-1]}"
    # and every distractor false on the same numbers
    assert not all(idx[i + 1] > idx[i] for i in range(len(idx) - 1)), \
        "'the population rises in every period' must be false"
    assert idx[-1] != idx[0], "'it returns to its first-period level' must be false"
    assert len(set(idx)) > 1, "'unchanged across the four periods' must be false"
    assert idx[-1] <= 75, "'it ends above three quarters of its first level' must be false"
    return (f"the recorded index reads {idx}, falling at every step and ending at "
            f"{idx[-1]:.0f} against a first period of {idx[0]:.0f}, below half of it")


def q21(table, item):
    """Every surveyed region outside the Americas grows some American staple."""
    labs = cg.labels(table)
    counts = dict(zip(labs, cg.col(table, STAPLES)))
    outside = [l for l in labs if "Americas" not in l]
    assert len(outside) == 3, \
        f"the survey must cover three regions outside the Americas; got {outside}"
    for name, region in (("Europe", "A region of Europe"), ("Asia", "A region of Asia"),
                         ("Africa", "A region of Africa")):
        assert region in counts, f"KC-4.1.V.B names {name}, and the survey has no row for it"
        assert counts[region] > 0, (
            f"the key needs the surveyed region of {name} to grow at least one American staple; "
            f"got {counts[region]}")
    # and every distractor false on the same counts
    assert sum(1 for r in outside if counts[r] > 0) == 3, \
        "'only Europe' and 'only Asia' must both be false"
    assert any(counts[r] > 0 for r in labs if "Americas" in r), \
        "the American row must also be non-zero, or 'only in the Americas' becomes arguable"
    assert not all(counts[r] == 0 for r in labs), \
        "'no region grows any American food crop as a staple' must be false"
    return (f"the three surveyed regions outside the Americas return "
            f"{[counts[r] for r in outside]} American staples, none of them zero, so the crops "
            "are grown in Europe, Asia and Africa alike")


CLAIMS = [
 ("exchange of new plants, animals, and diseases",
  "KC-4.1.V states that the new connections between the Eastern and Western Hemispheres resulted in the exchange of new plants, animals, and diseases, known as the Columbian Exchange. Coinage, legal codes, ambassadors and prisoners appear in no part of that sentence."),
 ("new connections between the Eastern and Western Hemispheres",
  "KC-4.1.V makes the new connections between the hemispheres the cause and the exchange of plants, animals, and diseases the result, which is what Unit 4: Learning Objective D asks students to explain. The framework offers no climatic, agricultural or diplomatic cause in its place."),
 ("Mosquitoes and rats",
  "KC-4.1.V.A names mosquitoes and rats as the disease vectors unintentionally transferred by European colonization of the Americas. Horses and cattle are illustrative examples of the domesticated animals brought deliberately under KC-4.1.V.C, which is a different transfer."),
 ("Smallpox, measles, and malaria",
  "KC-4.1.V.A names smallpox, measles, and malaria among the diseases endemic in the Eastern Hemisphere that spread with European colonization. The framework names no other disease anywhere in this topic."),
 ("The Eastern Hemisphere",
  "KC-4.1.V.A describes the spread of diseases that were endemic in the Eastern Hemisphere. The framework states that one direction and is silent about any traffic the other way, so both the reversal and the denial that it locates the diseases at all misreport it."),
 ("substantially reduced the indigenous populations",
  "KC-4.1.V.A says some of these diseases substantially reduced the indigenous populations, with catastrophic effects in many areas. Each rejected option denies either the reduction or the population that suffered it."),
 ("Europe, Asia, and Africa",
  "KC-4.1.V.B says American foods became staple crops in various parts of Europe, Asia, and Africa. Confining them to the Americas or moving them to regions the sentence does not name is a claim the framework never makes."),
 ("Primarily on plantations with coerced labor",
  "KC-4.1.V.B states that cash crops were grown primarily on plantations with coerced labor, and KC-4.2.II.C independently ties the growth of the plantation economy to rising demand for enslaved labor in the Americas. Owner-farmed holdings, monastic gardens, seasonal wage labor and herding appear nowhere in either sentence."),
 ("To Europe and the Middle East",
  "KC-4.1.V.B says cash crops were exported mostly to Europe and the Middle East. The other destinations appear in no part of that statement, and consumption where the crop was grown is the opposite of what exported asserts."),
 ("Fruit trees, grains, sugar, and domesticated animals",
  "KC-4.1.V.C says Afro-Eurasian fruit trees, grains, sugar, and domesticated animals were brought by Europeans to the Americas. The rejected lists are KC-4.1.II.A, KC-4.3.II, KC-4.3.I.D and KC-4.1.IV.C, which concern technology, expansion, revenue and commercial policy."),
 # Both clauses: one distractor keeps 'African enslaved persons' and swaps what
 # they brought, so an anchor naming only the group would match it too.
 ("African enslaved persons, who brought other foods",
  "KC-4.1.V.C says Afro-Eurasian fruit trees, grains, sugar, and domesticated animals were brought by Europeans to the Americas, while other foods were brought by African enslaved persons, and the illustrative examples print okra and rice under that second heading. The domesticated animals belong to the European half of the same sentence."),
 ("Populations in Afro-Eurasia",
  "KC-4.1.V.D states that populations in Afro-Eurasia benefitted nutritionally from the increased diversity of American food crops. The framework records the nutritional benefit on that side of the exchange and on no other."),
 # Both clauses: the distractor exchanges the crops with the animals, and either
 # half of the key matches one of the reversals.
 ("American foods became staples in Europe, Asia, and Africa, while Afro-Eurasian animals were brought to the Americas",
  "KC-4.1.V.B has American foods becoming staple crops in various parts of Europe, Asia, and Africa, and KC-4.1.V.C has Afro-Eurasian fruit trees, grains, sugar, and domesticated animals brought by Europeans to the Americas. The rejected pairings reverse one or both directions."),
 # Both clauses: the true statement is itself a distractor, so an anchor naming
 # only the hemispheres would match both.
 ("endemic in the Western Hemisphere and were carried to the Eastern",
  "KC-4.1.V.A locates the diseases as endemic in the Eastern Hemisphere and describes their spread with European colonization of the Americas, so reversing the hemispheres is the error. The other four options are that sentence almost verbatim."),
 ("Horses, pigs, and cattle",
  "The illustrative examples beside Unit 4: Learning Objective D print horses, pigs and cattle under the heading of domesticated animals, which KC-4.1.V.C says Europeans brought to the Americas. The framework names no other animal in this topic."),
 ("Okra and rice",
  "The illustrative examples for this topic print okra and rice under the heading of foods brought by African enslaved persons, which is the second half of KC-4.1.V.C. Sugar and grains sit in the first half of that sentence, where Europeans bring them."),
 ("substantially reduced the indigenous populations",
  "KC-4.1.V.A says some of these diseases substantially reduced the indigenous populations, with catastrophic effects in many areas, and a district emptied by sickness rather than war is that effect. The rejected options are KC-4.1.V.B, KC-4.1.V.D and KC-4.1.V.C, none of which concerns mortality."),
 ("Afro-Eurasian animals and fruit trees brought to the Americas",
  "KC-4.1.V.C says Afro-Eurasian fruit trees, grains, sugar, and domesticated animals were brought by Europeans to the Americas, and livestock and orchards new to a district are that half of the exchange. The rejected options name KC-4.1.V.B's other direction, KC-4.1.V.A's vectors and KC-4.1.V.D's benefit."),
 # Both clauses: two distractors say all four went one way, and either half of
 # the key matches one of them.
 ("Three of the four cargoes were carried to the Americas and one was carried away",
  "KC-4.1.V.C brings fruit trees, grains, sugar, animals and the foods of African enslaved persons to the Americas, while KC-4.1.V.B carries American foods out to Europe, Asia, and Africa. Recomputed in q19 above: three rows run one way and one the other, so neither the one-way readings nor the even split holds."),
 ("falls in every period and ends below half its first-period level",
  "KC-4.1.V.A says some of the diseases that spread substantially reduced the indigenous populations, with catastrophic effects in many areas. Recomputed in q20 above: the index falls at every step and closes at thirty against a first period of one hundred."),
 ("Europe, Asia, and Africa alike",
  "KC-4.1.V.B says American foods became staple crops in various parts of Europe, Asia, and Africa. Recomputed in q21 above: each of the three surveyed regions outside the Americas returns a count above zero, so the crops are not confined to one of them or to the Americas."),
 ("American food crops appearing among the staples of Afro-Eurasian households",
  "KC-4.1.V.B says American foods became staple crops in various parts of Europe, Asia, and Africa and KC-4.1.V.D that Afro-Eurasian populations benefitted nutritionally from them, so under suggested skill 3.B the evidence doing the work is what people there ate. Silver, shipbuilding, titles and building stone bear on other claims."),
 ("by-product of colonization while the animals and trees were brought deliberately",
  "KC-4.1.V.A calls the transfer of disease vectors unintentional and ties it to European colonization, while KC-4.1.V.C says the fruit trees, grains, sugar, and domesticated animals were brought by Europeans. The contrast is the framework's own wording rather than an inference from it."),
 ("killed a larger share of a population than another did",
  "The four rejected statements are KC-4.1.V.A, KC-4.1.V.B and KC-4.1.V.D almost verbatim. KC-4.1.V.A gives no figure and no comparison between diseases, saying only that some of them substantially reduced the indigenous populations, so a ranking would need a source outside the framework."),
 ("environment shapes human societies and that populations in turn shape their environments",
  "The Humans and the Environment thematic focus printed with this topic says the environment shapes human societies and that as populations grow and change these populations in turn shape their environments, which is what KC-4.1.V describes. The rejected statements are the other four thematic focuses of the course."),
 ("moved in both directions, and the framework describes an effect of each direction",
  "KC-4.1.V.C brings Afro-Eurasian trees, grains, sugar and animals to the Americas, KC-4.1.V.B makes American foods staples in Europe, Asia, and Africa, and KC-4.1.V.D records a nutritional benefit in Afro-Eurasia, so effects are stated on both sides. Each rejected correction deletes one of those statements."),
 ("Afro-Eurasian grains and livestock appearing on farms in the Americas",
  "KC-4.1.V.C says Afro-Eurasian fruit trees, grains, sugar, and domesticated animals were brought by Europeans to the Americas, so evidence of change in American agriculture has to show them arriving. Treasury clerks, harbour depths, caravan taxes and shipwrights' wages bear on none of it."),
 ("grown primarily on plantations with coerced labor",
  "KC-4.1.V.B states that cash crops were grown primarily on plantations with coerced labor and exported mostly to Europe and the Middle East, which is where this topic meets KC-4.2.II.C on the plantation economy and its demand for enslaved labor. Each rejected option contradicts one of those two sentences."),
 # Both clauses: the distractor exchanges the loss and the gain between the
 # hemispheres, and either half alone matches it.
 ("loss of indigenous population in the Americas, and a nutritional gain for populations in Afro-Eurasia",
  "KC-4.1.V.A gives the substantial reduction of indigenous populations with catastrophic effects in many areas, and KC-4.1.V.D gives the nutritional benefit to populations in Afro-Eurasia. The reversal reads perfectly well and is the misreading this item exists to catch."),
 ("Afro-Eurasian crops and animals reached the Americas, American foods became staples in Europe, Asia, and Africa",
  "The keyed sentence joins KC-4.1.V on the exchange of plants, animals, and diseases to KC-4.1.V.C, KC-4.1.V.B, KC-4.1.V.D and KC-4.1.V.A in turn. Each rejected version denies the exchange, reverses the direction of the crops and animals, reverses the hemisphere the diseases came from, or denies every effect recorded."),
]

TABLE_CHECKS = {19: q19, 20: q20, 21: q21}

if __name__ == "__main__" and "--selftest" in sys.argv:
    ws.controls(w4_3)

ws.marked_stimulus(w4_3)
wh.run(w4_3, CLAIMS, table_checks=TABLE_CHECKS, argv=sys.argv)
