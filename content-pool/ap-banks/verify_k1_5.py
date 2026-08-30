"""Key audit for AP COMPARATIVE GOVERNMENT 1.5 Sources of Power and Authority.

One (anchor, claim) per item, in module order. The anchor must appear in the
keyed choice and in no distractor; the claim states what the key rests on.

WHAT THE KEYS REST ON
---------------------
This topic has ONE essential knowledge statement, PAU-1.D.1, which does two
things: it names six sources of power and authority -- constitutions, religions,
military forces, political parties, legislatures, popular support -- and it gives
five country illustrations, .a China's Communist Party controlling the military
to maintain regime stability, .b Iran's transition from dictatorial rule to a
theocracy based on Islamic Sharia law after 1979, .c Nigeria and Mexico becoming
multiparty republics following military rule and single-party dominance
RESPECTIVELY, .d the political elite's backing of a strong president in Russia
creating a managed democracy with election rules favoring one party, .e
constitutional reforms in the United Kingdom devolving power to multiple
parliaments and allowing the regime to maintain stability.

Because a single statement cannot carry thirty items on its own, the country
items are filled out from Unit 2's institutional statements, each named in the
claim that uses it: PAU-3.C.2.a (China's president as commander in chief, chair
of the Military Commission and party General Secretary; leadership changes made
behind closed doors), PAU-3.C.2.b (the Supreme Leader's powers, including HALF
of the Guardian Council), PAU-3.C.2.f (the monarch formally appointing the leader
of the largest Commons party), PAU-3.E.1.a and PAU-3.E.1.b, PAU-3.F.1.a, plus
LEG-1.A.1 on legitimacy and LEG-1.B.4 on devolution's two-sided effects.

THE TRAP THIS MODULE IS BUILT AROUND
------------------------------------
PAU-3.E.1.a says China's CONSTITUTION recognizes the National People's Congress
as the government's most powerful institution; PAU-3.F.1.a says the Politburo
Standing Committee is the ACTUAL center of power in the state. Both are the
framework's sentences and they are not in conflict, because they are about
different things. Items 16 and 29 key that distinction explicitly; no item asks
which body is 'more powerful' without saying in which sense, because such an item
would have no defensible key. See AP_COMP_GOV_CED.md note 5.

Item 6 also keys the fact that devolution does NOT reclassify the United Kingdom:
PAU-2.A.1 still lists it among the unitary states.

DATA ITEMS
----------
Items 20-22 share a hypothetical survey table and items 23-24 a hypothetical
devolved-spending table, both labelled as hypothetical in the stems because the
framework prints no such figures. Item 22 is deliberately a check on the data
itself: a survey of who people think decides is not one of the framework's
indicators of regime type, and the key says so.

A DEFECT THE TABLE CHECK CAUGHT
-------------------------------
Item 21's keyed choice first read '55 percent, more than any other institution in
any row'. That is FALSE on the table: another row names a party leadership body
at 61. The key was still the right row, but the reason printed beside it was
wrong, which is exactly the kind of error no structural check sees. The choice now
claims only what recomputes -- an outright majority, ahead of every other
institution in that same country.

FIVE choices per item (A-E); see AP_COMP_GOV_CED.md.
"""
import cg_check as cg
import k1_5

LEG = "Named the elected legislature"
PARTY = "Named the governing party's leadership body"
ARMY = "Named the armed forces"
HOS = "Named the head of state"
S2000 = "Share of public spending decided by a devolved parliament, 2000"
S2020 = "Share of public spending decided by a devolved parliament, 2020"
_COLS = (LEG, PARTY, ARMY, HOS)


def _row_sums(table):
    return {lab: sum(cg.cell(table, lab, h) for h in _COLS) for lab in cg.labels(table)}


def q20(table, item):
    for lab, total in _row_sums(table).items():
        assert total == 100, f"{lab}'s shares sum to {total}, not 100"
    party = {lab: cg.cell(table, lab, PARTY) for lab in cg.labels(table)}
    leg = {lab: cg.cell(table, lab, LEG) for lab in cg.labels(table)}
    assert party["Country 2"] == 61 and leg["Country 2"] == 9, \
        f"the keyed figures read as {party['Country 2']} and {leg['Country 2']}"
    gaps = {lab: party[lab] - leg[lab] for lab in party}
    assert max(gaps, key=gaps.get) == "Country 2", f"the largest party-over-legislature gap is {max(gaps, key=gaps.get)}"
    assert all(gaps[lab] < 0 for lab in gaps if lab != "Country 2"), \
        "in every other row the legislature must lead the party body, so only one row fits"
    return "one row alone puts the party leadership body ahead of the legislature, 61 against 9, and every row sums to 100"


def q21(table, item):
    army = {lab: cg.cell(table, lab, ARMY) for lab in cg.labels(table)}
    assert army["Country 3"] == 55, f"the keyed 55 percent reads as {army['Country 3']}"
    assert army["Country 3"] > 50, "the key calls it an outright majority"
    own_row = [cg.cell(table, "Country 3", h) for h in _COLS]
    assert army["Country 3"] == max(own_row), \
        "the key says the armed forces lead every other institution in that same country"
    assert army["Country 3"] == max(army.values()), "no other row may name the armed forces more often"
    assert all(v <= 50 for lab, v in army.items() if lab != "Country 3"), \
        "only one row may put the armed forces at a majority"
    return "the armed forces reach 55 percent in one row, an outright majority and ahead of every other institution in that same country"


def q22(table, item):
    leg = {lab: cg.cell(table, lab, LEG) for lab in cg.labels(table)}
    assert max(leg, key=leg.get) == "Country 1" and leg["Country 1"] == 54, \
        "the student's premise requires one row to lead on the legislature with a majority"
    assert set(table["headers"][1:]) == set(_COLS), \
        "the objection turns on the table reporting only named institutions, and no indicator of regime type"
    return "the row the student points to does lead on the legislature at 54 percent, so the objection is to what the column measures rather than to the reading"


def q23(table, item):
    start = {lab: cg.cell(table, lab, S2000) for lab in cg.labels(table)}
    end = {lab: cg.cell(table, lab, S2020) for lab in cg.labels(table)}
    zeros = [lab for lab, v in start.items() if v == 0]
    assert zeros == ["Region III"], f"exactly one region may start at zero; got {zeros}"
    assert end["Region III"] == 27, f"the keyed 27 percent reads as {end['Region III']}"
    assert all(v < 50 for v in end.values()), \
        "no region reaches half, which is what makes the 'none reached half' distractor tempting"
    return "one region alone starts at 0 percent and ends at 27, so only there did a devolved parliament acquire authority it did not have"


def q24(table, item):
    deltas = [cg.cell(table, lab, S2020) - cg.cell(table, lab, S2000) for lab in cg.labels(table)]
    total = sum(deltas)
    assert sorted(deltas) == [1, 27, 29], f"the three changes recompute to {sorted(deltas)}"
    assert total == 57, f"the keyed 57 points recomputes to {total}"
    for wrong in (29, 68, 41, 77):
        assert wrong != total, f"distractor {wrong} equals the correct total"
    return f"the three regions move by 29, 1 and 27 points, summing to {total:.0f}"


CLAIMS = [
 ("religions, military forces",
  "EK PAU-1.D.1 lists constitutions, religions, military forces, political parties, legislatures and popular support as the sources of power and authority. The rejected lists are the elements of statehood in EK PAU-1.A.2, the data resources of EK MPA-1.A.8, and territorial structure."),
 ("control over the military",
  "EK PAU-1.D.1.a names the Communist Party's control over China's military as what provided power and authority to maintain regime stability. The four rejected descriptions are the framework's own words about Russia, Iran, the United Kingdom and Nigeria."),
 ("Islamic Sharia",
  "EK PAU-1.D.1 names religions among the sources of power and authority and EK PAU-1.D.1.b describes the transition of power from dictatorial rule in Iran to a theocracy based on Islamic Sharia law after the 1979 Revolution."),
 ("Nigeria following military rule",
  "EK PAU-1.D.1.c states the transition of power in Nigeria and Mexico to multiparty republics following military rule and single-party dominance respectively. The framework's 'respectively' fixes the pairing, so the reversed option contradicts the sentence."),
 ("managed democracy",
  "EK PAU-1.D.1.d states that the political elite's backing of a strong president in Russia created a managed democracy with election rules favoring one party, and EK DEM-1.C.5 supplies the matching label of a competitive authoritarian regime or illiberal democracy."),
 ("maintain stability",
  "EK PAU-1.D.1.e states that constitutional reforms in the United Kingdom devolved power to multiple parliaments, allowing the regime to maintain stability. EK PAU-2.A.1 still lists the United Kingdom as unitary, so devolution here redistributes power within a unitary state rather than reclassifying it."),
 ("Nigeria and Mexico",
  "EK PAU-1.D.1.c is the only one of the five illustrations naming two countries that reach the same destination, a multiparty republic, from different starting points. The others concern party control of the military, a theocratic transition, elite backing of a presidency, and devolution."),
 ("whereas Russia's rests on the political elite",
  "EK PAU-1.D.1.a names the Communist Party's control over China's military and EK PAU-1.D.1.d names the political elite's backing of a strong president in Russia. Both are sources operating outside ordinary electoral competition, but the framework identifies a different one in each case."),
 ("religion supplying the basis of rule",
  "EK PAU-1.D.1.b describes a transition to a theocracy based on Islamic Sharia law while EK PAU-1.D.1.e describes constitutional reforms devolving power to multiple parliaments. Religions and constitutions are separate entries on EK PAU-1.D.1's list, and each illustration is offered for one of them."),
 ("constitutions",
  "EK PAU-1.D.1 names constitutions first among the sources of power and authority. A document that creates the offices and settles disputes about their powers is that source at work, whereas the other five named sources operate through belief, force, election or lawmaking."),
 ("religions",
  "EK PAU-1.D.1 names religions among the sources of power and authority and EK PAU-1.D.1.b gives a theocracy based on Islamic Sharia law as the illustration. EK PAU-3.E.1.b adds that Iran's elected legislature acts under supervision ensuring compatibility with Islam and Sharia law, which is this source shaping an ordinary legislative process."),
 ("producing a military regime",
  "EK PAU-1.D.1 names military forces among the sources of power and authority and EK PAU-1.B.3 names military regimes among the authoritarian types. EK PAU-1.D.1.c's reference to Nigeria's transition following military rule is the framework's own instance of this source having held power."),
 ("political parties",
  "EK PAU-1.D.1 names political parties among the sources of power and authority, EK PAU-1.D.1.a gives one party's control over the military as the illustration, and EK PAU-3.F.1.a identifies a party body rather than a state organ as the actual center of power in that state."),
 ("legislatures",
  "EK PAU-1.D.1 names legislatures among the sources of power and authority, and the lawmaking, budgetary and confirmation powers described are those EK PAU-3.E.1 attributes to the legislative institutions of the course countries. Nothing in the description turns on a founding text, a faith, an army or a party."),
 ("popular support",
  "EK PAU-1.D.1 names popular support among the sources of power and authority, and a government that must leave office when support is withdrawn depends on it. EK LEG-1.A.1's legitimacy is the related but distinct idea that constituents believe the government has the right to use power as it does."),
 ("actual center of power in the state",
  "EK PAU-3.E.1.a says the constitution recognizes the National People's Congress as the government's most powerful institution, and EK PAU-3.F.1.a says the Politburo Standing Committee is the actual center of power in the Chinese state. Both are the framework's sentences, about the constitutional text and about actual power respectively."),
 ("half of the Guardian Council",
  "EK PAU-3.C.2.b assigns the Supreme Leader the setting of the political agenda, command in chief, and the appointment of top ministers, the Expediency Council, HALF of the Guardian Council and the head of the judiciary. The rejected options describe the Majles, the elected president, the House of Lords and Russia's president."),
 ("command of a majority in the elected chamber",
  "EK PAU-3.C.2.f states that the monarch serves ceremonially as head of state and FORMALLY appoints as prime minister the leader of the party or coalition holding the largest number of seats in the Commons. The seat count decides the outcome, which is why the framework calls the monarch's role ceremonial."),
 ("settled inside the party",
  "EK PAU-3.C.2.a states that changes in China's top leadership are accomplished behind closed doors, and EK PAU-1.D.1.a locates that regime's stability in the Communist Party's control. A succession decided outside public institutions is one decided by the party."),
 ("named by 61 percent",
  "EK PAU-3.F.1.a describes a party body as the actual center of power in a state whose constitution names a legislature as its most powerful institution, so the pattern to look for is the party body far ahead of the legislature. Recomputed in q20 above: only one row shows that gap, and every row sums to 100."),
 ("named by 55 percent",
  "EK PAU-1.D.1 names military forces among the sources of power and authority. Recomputed in q21 above: in one row the armed forces are named by an outright majority, and that figure is the largest anywhere in the table."),
 ("beliefs about where decisions are made",
  "EK PAU-1.B.1 supplies the indicators of the democratic-authoritarian scale and none of them is a survey of who people think decides. EK LEG-1.A.1 shows the framework does care what constituents believe, but as the source of legitimacy rather than as a test of regime type. Recomputed in q22 above, the premise itself is a correct reading of the column."),
 ("from 0 percent to 27 percent",
  "EK PAU-1.D.1.e describes constitutional reforms that devolved power to multiple parliaments, so the case of a parliament acquiring authority it did not have is a region starting from nothing. Recomputed in q23 above: exactly one region does."),
 ("57 percentage points",
  "Recomputed in q24 above from the three regions' changes of 29, 1 and 27 points. Reading only the largest single change, or adding figures from the final column, produces each of the values offered against it."),
 ("right to use power in the way it does",
  "EK PAU-1.D.1 lists what a regime's capacity to rule rests on, while EK LEG-1.A.1 defines legitimacy as whether a government's constituents believe it has the right to use power as it does. One concerns what a regime rules through and the other what its people accept."),
 ("cease to answer to the governing party",
  "EK PAU-1.D.1 names military forces and political parties among the sources of power and authority, and EK PAU-1.D.1.a treats one party's control over the military as what supplied a regime with the power to remain stable. Moving the army from party command to civilian command moves it between two of the six sources; symbols, buildings and names touch none of them."),
 ("cannot be inferred from the fact that it is stable",
  "EK PAU-1.D.1.a attributes regime stability to a party's control of the armed forces and EK PAU-1.D.1.e attributes the maintenance of stability to devolution by constitutional reform. Both are the framework's own words, so an observation of stability does not identify which source is at work."),
 ("matched to local needs",
  "EK LEG-1.B.4 lists policy innovation, matching policies to local needs, checking central power and better minority representation alongside contradictory policies, more complicated implementation, interregional inequality, competition for resources and exacerbated ethnic tensions, in one two-sided statement. Treating devolution as unambiguously good or bad contradicts it."),
 ("a different body is the actual center",
  "EK PAU-3.E.1.a and EK PAU-3.F.1.a make both claims about the same state, one about what the constitution recognizes and one about where power actually sits. The framework therefore treats the text and the practice as separable questions."),
 ("affected over time by one or more of the named sources",
  "EK PAU-1.D.1 introduces its five illustrations with the statement that over time course country regimes have been affected by such sources. Two are transitions toward multiparty republics, one a transition to a theocracy, one elite backing of a presidency and one a constitutional reform, so the shared feature is the influence of a source rather than a common direction."),
]

cg.check(k1_5, CLAIMS, table_checks={20: q20, 21: q21, 22: q22, 23: q23, 24: q24})
