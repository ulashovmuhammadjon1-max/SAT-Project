"""Key audit for AP WORLD HISTORY: MODERN 9.6 Globalized Culture After 1900.

One (anchor, claim) per item, in module order. The anchor is a distinctive
substring that MUST appear in the keyed choice and in NO distractor; the claim
states the CED sentence the key rests on, with its Key Concept code or Learning
Objective, for a human to audit. `wh_check` refuses any claim or `why` that
cites neither.

THE THREE SENTENCES ARE CLOSE IN MEANING AND THAT IS THE HAZARD. A bank that did
not separate them would be thirty ways of saying "culture became global". Every
claim below names which of the three it is using:

  * KC-6.3.IV.i carries a CAUSE and a TIMING -- political and social changes LED
    TO changes in the arts, and it is in the SECOND HALF of the century that
    popular and consumer culture became more global. q1, q2, q9, q16 and q24
    turn on the cause; q6, q10, q17 and q20 on the timing.
  * KC-6.3.IV.ii is arts, entertainment and popular culture REFLECTING the
    influence of a globalized society -- reflecting, not causing. q4, q13, q22
    and q26 hold that verb.
  * KC-6.3.IV.iii is specifically CONSUMER culture and specifically TRANSCENDING
    NATIONAL BORDERS. q5, q11, q15, q23 and q25 stay on that.

WHAT NO CLAIM BELOW ASSERTS. Whether the globalization of culture was good or
bad for the societies it reached is a live argument and the framework does not
settle it. No claim says a global culture enriched or impoverished anyone, that
any tradition was lost or saved, that any culture is more or less authentic than
another, or that any country's cultural influence was deserved or excessive. No
real work of art, film, song or programme is described or evaluated anywhere in
the module, and the two illustrative-example items ask only which list the CED
prints. The objections belong to Topic 9.7 under KC-6.3.IV.iv and are neither
imported here nor argued away.

WHERE A DISTRACTOR IS THE SWAP OF THE KEY, THE ANCHOR CARRIES BOTH CLAUSES.
Six items are built on a reversal a prepared student could believe:

  q1   politics causing art swapped for art causing politics
  q4   reflecting a globalized society swapped for creating it
  q14  the NOT-supported item, where the key is deliberately the false claim
  q16  the same reversal as q1, offered as a correction
  q23  transcending borders swapped for abolishing them
  q26  a change and a continuity exchanged

For each the anchor spans the whole relation, so an anchor that matched the
swapped distractor would fail the gate rather than pass it. That defect is on
record in `verify_e2_1.py`.

WHAT THIS CANNOT DO: it cannot tell whether the history is right. It gates
structure, key/anchor agreement, notation, the absence of figure language, the
presence of a citation, and the arithmetic of the three data questions.

NEGATIVE CONTROL: `python3 verify_w9_6.py --selftest`. It rotates all thirty
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
import w9_6

T_FILMS = w9_6._T_FILMS
T_SCHEDULE = w9_6._T_SCHEDULE
T_MARKETS = w9_6._T_MARKETS

FILMS = "Films released"
ABROAD = "Of those, shown also outside the country"
HOME_ONLY = "Of those, shown only within it"
HOURS = "Broadcast hours"
FOREIGN = "Of those, programmes made in other countries"
DOMESTIC = "Of those, programmes made at home"
COUNTRIES = "Countries in which the firm sells"
OUTSIDE = "Of those, countries outside its home region"
INSIDE = "Of those, countries within its home region"


def _parts_sum_to_whole(table, whole, parts, what):
    """Every row's parts must total its whole.

    This is what makes the negative control mean anything on these tables. The
    corruption in `es_check` only ever makes a number LARGER, so a check of the
    form "this count is above zero" is monotone and can never fail: it reads the
    table without being able to object to anything in it. Sibling module 8.5
    shipped a first draft whose table check caught 1 of 12 corrupted cells for
    exactly that reason. Each row here states a whole and the two parts it was
    divided into, and every stem says so.
    """
    labs = cg.labels(table)
    totals = cg.col(table, whole)
    cols = [cg.col(table, p) for p in parts]
    for i, lab in enumerate(labs):
        got = sum(c[i] for c in cols)
        assert got == totals[i], (
            f"{lab}: the {what} split into {[c[i] for c in cols]} totals {got}, but the "
            f"row states {totals[i]} in all -- the parts do not sum to the whole")


def q3(table, item):
    """Releases rise and the shown-abroad SHARE rises with them."""
    periods = cg.labels(table)
    assert periods == ["1930s", "1960s", "1990s"], \
        f"the key speaks of each period recorded; the rows are {periods}"
    _parts_sum_to_whole(table, FILMS, [ABROAD, HOME_ONLY], "films released")
    total = cg.col(table, FILMS)
    out = cg.col(table, ABROAD)
    home = cg.col(table, HOME_ONLY)
    assert all(b > a for a, b in zip(total, total[1:])), \
        f"the key says releases rose in each period; they run {total}"
    shares = [o / t for o, t in zip(out, total)]
    assert all(b > a for a, b in zip(shares, shares[1:])), (
        f"the key says the shown-abroad portion rose AS A SHARE; the shares run "
        f"{[round(s, 3) for s in shares]}")
    # every distractor false on the same numbers
    assert total[-1] > total[0], \
        "'releases fell in each period after the first' must be false"
    assert shares[-1] > shares[0], \
        "'the shown-abroad share fell across the record' must be false"
    assert not all(b > a for a, b in zip(home, home[1:])), \
        "'films shown only within the country rose in each period' must be false"
    assert not all(s > 0.5 for s in shares), (
        "'most films were shown abroad in every period' must be false; the shares are "
        f"{[round(s, 3) for s in shares]}")
    return (f"releases run {total} and the shown-abroad share "
            f"{[round(s, 3) for s in shares]}, both rising, against {home} shown only at "
            f"home; the parts sum to the stated wholes and all four distractors recompute "
            f"false")


def q7(table, item):
    """Hours rise, the foreign share rises, and never reaches a majority."""
    periods = cg.labels(table)
    assert periods == ["1955", "1975", "1995"], \
        f"the key speaks of each period recorded; the rows are {periods}"
    _parts_sum_to_whole(table, HOURS, [FOREIGN, DOMESTIC], "broadcast hours")
    total = cg.col(table, HOURS)
    foreign = cg.col(table, FOREIGN)
    home = cg.col(table, DOMESTIC)
    assert all(b > a for a, b in zip(total, total[1:])), \
        f"the key says total hours rose in each period; they run {total}"
    shares = [f / t for f, t in zip(foreign, total)]
    assert all(b > a for a, b in zip(shares, shares[1:])), (
        f"the key says the foreign-made share rose; the shares run "
        f"{[round(s, 3) for s in shares]}")
    assert all(s < 0.5 for s in shares), (
        f"the key says it never reached a majority; the shares run "
        f"{[round(s, 3) for s in shares]}")
    # every distractor false on the same numbers
    assert foreign[0] > 0, \
        "'no foreign-made programme was broadcast in the earliest period' must be false"
    assert shares[-1] > shares[0], \
        "'the foreign-made share fell across the record' must be false"
    assert all(b > a for a, b in zip(home, home[1:])), \
        "'the hours given to home-made programmes fell in each period' must be false"
    assert shares[-1] < 0.5, \
        "'foreign-made programmes filled more than half the last schedule' must be false"
    return (f"hours run {total} and the foreign-made share "
            f"{[round(s, 3) for s in shares]}, rising but never a majority, against {home} "
            f"made at home; the parts sum to the stated wholes and all four distractors "
            f"recompute false")


def q12(table, item):
    """Every firm sells beyond its region; a majority abroad for exactly two."""
    labs = cg.labels(table)
    total = dict(zip(labs, cg.col(table, COUNTRIES)))
    out = dict(zip(labs, cg.col(table, OUTSIDE)))
    _parts_sum_to_whole(table, COUNTRIES, [OUTSIDE, INSIDE], "countries in which the firm sells")
    for lab in labs:
        assert out[lab] > 0, (
            f"the key needs every firm to sell outside its home region; {lab} reads "
            f"{out[lab]}")
    majority = [lab for lab in labs if out[lab] > 0.5 * total[lab]]
    assert len(majority) == 2, (
        f"the key says two of the three have most of their markets outside the home "
        f"region; the firms for which that holds are {majority}")
    # every distractor false on the same numbers
    assert any(out[l] > 0 for l in labs), \
        "'no firm sells outside its home region' must be false"
    assert len(majority) > 0, \
        "'for every firm most markets lie within its home region' must be false"
    assert len(set(total.values())) > 1, \
        "'every firm sells in the same number of countries' must be false"
    assert total["Firm three"] <= total["Firm two"], \
        "'firm three sells in more countries than firm two' must be false"
    return (f"markets outside the home region {out} of totals {total}: every firm sells "
            f"beyond its region and {majority} do so for most of their markets; the parts "
            f"sum to the stated wholes and all four distractors recompute false")


TABLE_CHECKS = {3: q3, 7: q7, 12: q12}

CLAIMS = [
 ("changes in the arts that followed the political and social changes of the twentieth century",
  "KC-6.3.IV.i states that political and social changes of the twentieth century LED TO changes in the arts. The catalogue puts the upheavals before the paintings and makes the paintings depend on them, which is the framework's own order; a distractor reverses it, so the anchor carries the direction as well as the pair."),

 ("The political and social changes of the century",
  "KC-6.3.IV.i states that political and social changes of the twentieth century led to changes in the arts. Unit 9 Learning Objective F asks HOW AND WHY globalization changed culture, and this sentence is the framework's answer to the why; the distractors name developments the framework states in other topics."),

 ("share shown outside the country rose with it",
  "KC-6.3.IV.i states that in the second half of the century popular and consumer culture became more global, and films crossing borders in rising proportion are one form that takes. The record is hypothetical and is recomputed from the table alone in q3 above."),

 ("increasingly reflected the influence of a globalized society",
  "KC-6.3.IV.ii states exactly that of arts, entertainment, and popular culture. Reflected is the framework's own verb and makes the culture the register of the change rather than its author, so a distractor having them create that society goes past the sentence."),

 ("consumer culture becoming globalized and transcending national borders",
  "KC-6.3.IV.iii states that consumer culture became globalized and transcended national borders. Goods from a dozen countries asked for by name in one shop is that crossing at the point of sale, and the framework treats it as a fact about consumer culture rather than about the arts."),

 ("In the second half of the twentieth century",
  "KC-6.3.IV.i states that political and social changes of the twentieth century led to changes in the arts and IN THE SECOND HALF OF THE CENTURY popular and consumer culture became more global. The framework's own phrase places the second development in the century's later half."),

 ("share given to programmes made abroad rose without ever reaching a majority",
  "KC-6.3.IV.ii states that arts, entertainment, and popular culture increasingly reflected the influence of a globalized society, and a schedule taking in more foreign-made programmes over time is that influence in one broadcaster's week. The record is hypothetical and both halves of the key are recomputed from the table alone in q7 above."),

 ("Reggae in music, Bollywood in movies, Facebook and Twitter in social media",
  "The CED prints these beside KC-6.3.IV.i and KC-6.3.IV.ii as illustrative examples of global culture. The second option is this page's separate list of global consumerism and the rest are printed beside statements in other topics. The item asks which list the course prints and evaluates none of the works or organizations named."),

 ("consistent with the framework, which states that political and social changes led to changes in the arts",
  "KC-6.3.IV.i states that political and social changes of the twentieth century led to changes in the arts, which is the essay's premise stated as course content. The distractors deny the relation, reverse it or move it outside the period, so the anchor carries the verdict together with the sentence it rests on."),

 ("popular culture becoming more global in the second half of the twentieth century",
  "KC-6.3.IV.i states that in the second half of the century popular and consumer culture became more global, and the CED prints reggae among its illustrative examples of a global culture in music. A form moving from the imports rack to the main section is that globalization inside one shop, which skill 4.B asks a student to situate in the broader process."),

 ("It became globalized and transcended national borders",
  "KC-6.3.IV.iii states that consumer culture became globalized and TRANSCENDED NATIONAL BORDERS. That phrase is what distinguishes this sentence from the two beside it, so the anchor carries both halves of it."),

 ("Every firm surveyed sells outside its home region, and for two of the three most of their markets lie outside it",
  "KC-6.3.IV.iii states that consumer culture became globalized and transcended national borders, and firms selling beyond their home regions are one form that crossing takes. The survey is hypothetical and is recomputed from the table alone in q12 above; the key says two of three rather than all three because that is what the figures show."),

 ("arts increasingly reflecting the influence of a globalized society",
  "KC-6.3.IV.ii states that arts, entertainment, and popular culture increasingly reflected the influence of a globalized society. A staging borrowing across continents and expecting to be understood is that influence registered in the work itself, and the framework's verb is reflected rather than rejected, which is the distractor the anchor excludes."),

 ("remained wholly contained within national borders",
  "KC-6.3.IV.iii states that consumer culture became globalized and TRANSCENDED national borders, so a claim that it stayed wholly within them reverses the framework's sentence. The item asks which statement is NOT supported, so the anchor is pinned to the false one deliberately; the other four restate KC-6.3.IV.i, KC-6.3.IV.ii and KC-6.3.IV.iii."),

 ("consumer culture becoming globalized and transcending national borders",
  "KC-6.3.IV.iii states that consumer culture became globalized and transcended national borders, and the CED prints global brands among its illustrative examples of global consumerism. One campaign running in thirty countries with only the language changed is that transcendence in its plainest commercial form."),

 ("political and social changes led to changes in the arts, which is the reverse relation",
  "KC-6.3.IV.i fixes politics as prior and the arts as what followed. The student has the right pair the wrong way round, so the correction names the direction rather than denying the connection, and the anchor carries both."),

 ("popular culture becoming more global in the second half of the century",
  "KC-6.3.IV.i states that in the second half of the century popular and consumer culture became more global, and the CED prints World Cup soccer and the Olympics among its illustrative examples of a global culture in sports. An audience in countries with no team in the competition is that globalization measured by attention rather than by participation."),

 ("How globalization changed culture, and why it did so",
  "Unit 9 Learning Objective F, printed on this topic's page, is to explain HOW AND WHY globalization changed culture over time. The framework supplies the why in KC-6.3.IV.i, and it does not ask a student to rank cultures or to judge whether globalization should have occurred, which is what two distractors offer."),

 ("Alibaba and eBay in online commerce, and Toyota and Coca-Cola as global brands",
  "The CED prints these beside KC-6.3.IV.iii as illustrative examples of global consumerism. The second option is this page's separate list of global culture, and the rest are printed beside KC-6.3.II.B and KC-6.3.I.E in Topic 9.4. The item asks which list the course prints and evaluates none of the firms named."),

 ("attributes the changes in the arts to the century's political and social changes and dates the spread of popular culture to the century's second half",
  "KC-6.3.IV.i contains both: political and social changes led to changes in the arts, AND in the second half of the century popular and consumer culture became more global. The sentence attributes the first and dates the second, so the anchor carries both halves."),

 ("how much of what was watched, heard and read there came from elsewhere",
  "KC-6.3.IV.i states that in the second half of the century popular and consumer culture became more global, and KC-6.3.IV.ii that arts, entertainment and popular culture increasingly reflected the influence of a globalized society. What people watched, heard and read, and where it came from, is the direct measure of both."),

 ("arts and popular culture increasingly reflected the influence of a globalized society",
  "KC-6.3.IV.ii uses the word INCREASINGLY, and a reviewer finding such borrowing unremarkable is reporting that increase as an accomplished fact. The key describes what the work does and makes no judgement of its quality or its authenticity."),

 ("transcended those borders rather than being contained by them",
  "KC-6.3.IV.iii states that consumer culture became globalized and TRANSCENDED national borders. Transcended means the culture crossed the borders rather than being confined by them, and it is not the same as abolishing them, so the anchor carries the crossing and excludes both the containment and the overstatement."),

 ("political and social changes of the century led to changes in the arts",
  "KC-6.3.IV.i locates a cause of change in the arts outside the arts themselves. Unit 9 Learning Objective F asks for the WHY of cultural change, and the framework's answer is what the commentator's argument leaves out."),

 ("consumer culture becoming globalized across national borders",
  "KC-6.3.IV.iii states that consumer culture became globalized and transcended national borders. Goods arriving from four times as many origins over forty years is that crossing recorded by the authority that counts what crosses, and skill 4.B asks a student to situate the specific record in the broader process."),

 ("sources on which arts and popular culture drew widened, while societies went on producing arts and popular culture",
  "KC-6.3.IV.ii states that arts, entertainment, and popular culture increasingly reflected the influence of a globalized society, which is a widening of what they drew on within an activity that continued. The reasoning process the CED prints beside this topic is continuity and change, and a distractor exchanges the two, so the anchor holds one of each."),

 ("globalization of popular and consumer culture in the second half of the century",
  "KC-6.3.IV.i states that in the second half of the century popular and consumer culture became more global, and KC-6.3.IV.iii that consumer culture transcended national borders. A ministry asking whether its audiences now resemble foreign audiences more than earlier generations of their own is asking about that process, and the framework supplies no answer about whether it is to be welcomed."),

 ("arts changed under the century's political and social pressures, popular culture became more global, and consumer culture crossed national borders",
  "KC-6.3.IV.i supplies the first two and KC-6.3.IV.iii the third. The key is the conjunction of the three sentences, and the framework nowhere states that culture became identical everywhere, which is what a distractor supplies instead."),

 ("names consumer culture alongside popular culture as something that became global and crossed borders",
  "KC-6.3.IV.i names popular AND CONSUMER culture together as what became more global in the second half of the century, and KC-6.3.IV.iii gives consumer culture its own sentence about transcending national borders. The framework therefore places it inside the cultural statements of this unit rather than only inside the economic ones of Topic 9.4."),

 ("popular and consumer culture became more global in the century's second half, and what people watched, heard and bought increasingly reflected a world that crossed its own borders",
  "KC-6.3.IV.i supplies the political and social changes leading to changes in the arts and the globalization of popular and consumer culture in the second half of the century, KC-6.3.IV.ii the arts and popular culture increasingly reflecting a globalized society, and KC-6.3.IV.iii consumer culture transcending national borders. The key is the conjunction of the three and none of the five options passes judgement on whether the change was good."),
]

wh.run(w9_6, CLAIMS, table_checks=TABLE_CHECKS, argv=sys.argv)
