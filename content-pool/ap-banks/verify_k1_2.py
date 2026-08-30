"""Key audit for AP COMPARATIVE GOVERNMENT 1.2 Defining Political Organizations.

One (anchor, claim) per item, in module order. The anchor must appear in the
keyed choice and in no distractor; the claim states what the key rests on.

WHAT THE KEYS REST ON
---------------------
Almost every item here is keyed to one of the five essential knowledge
statements under PAU-1.A, which are the only place the framework defines these
four words:

  PAU-1.A.1  a political system is the laws, ideas and procedures addressing who
             should have authority to rule and what government's influence on
             people and economy should be
  PAU-1.A.2  a state combines a permanent population with governing institutions
             exercising control over a defined territory with international
             recognition; a regime is the fundamental rules controlling access to
             and exercise of political power, and regimes typically endure from
             government to government
  PAU-1.A.3  a regime is characterized as democratic or authoritarian based on
             how it sets rules or makes decisions about exercising power
  PAU-1.A.4  a government is the set of institutions or individuals legally
             empowered to make binding decisions for a state; the right and power
             to govern itself without outside interference is a crucial aspect of
             sovereignty
  PAU-1.A.5  a nation is a group of people with commonalities including race,
             language, religion, ethnicity, political identity and aspirations

The four terms are ordinary-English near-synonyms and the whole topic is that
they are not synonyms here, so each scenario is constructed so that exactly one
of the four has anything to act on. That is what makes a single key defensible
without a computation to fall back on.

Country illustrations are held to what the CED itself states: the United
Kingdom's Scottish, English, Welsh and Irish nations (LEG-2.A.1f), Nigeria's
more than 250 ethnic groups (LEG-2.A.1d), ethnic Russians at more than 80
percent of Russia's population (LEG-2.A.1e). Legitimacy, where it is contrasted
with sovereignty, is LEG-1.A.1. No item turns on a figure the framework does not
print.

Items 16 and 17 carry a table whose numbers are HYPOTHETICAL and labelled so in
the stem. Each keyed conclusion is recomputed from the table alone below, and
the distractors are checked false against the same numbers, so a student can
reach the key from the data plus one framework sentence.

A DEFECT FOUND AND FIXED WHILE WRITING THIS FILE
------------------------------------------------
Item 17 asks which row matches Russia's "more than 80 percent" largest group.
The table originally gave Country W 82 percent and Country Z 91 percent, so
BOTH rows satisfied "more than 80 percent" and the item had two defensible
answers; the rationale tried to save it by asking for the closest value above
the line, which the stem never said. Country Z is now 71 percent, the only row
above 80 percent is Country W, and item 16's Country Z distractor was reworded
so that it no longer asserts Z holds the largest share.

FIVE choices per item (A-E); see AP_COMP_GOV_CED.md.
"""
import cg_check as cg
import k1_2

SHARE = "Largest ethnic or national group as share of population (hypothetical)"
COUNT = "Number of recognized minority groups (hypothetical)"


def q16(table, item):
    shares = dict(zip(cg.labels(table), cg.col(table, SHARE)))
    counts = dict(zip(cg.labels(table), cg.col(table, COUNT)))
    assert shares["Country Y"] == min(shares.values()), "Country Y must hold the smallest largest-group share"
    assert shares["Country Y"] < 30, "the key calls Country Y's largest group sub-thirty-percent"
    assert counts["Country Y"] == max(counts.values()), "Country Y must recognize the most groups"
    assert counts["Country Y"] >= 100, "the key calls the group count a figure in the hundreds"
    for lab in ("Country W", "Country X", "Country Z"):
        assert shares[lab] > 50, f"{lab} must have a leading group above half, so it cannot match Nigeria"
    assert shares["Country Z"] < shares["Country W"], \
        "the reworded Country Z distractor must not be the largest share"
    assert shares["Country Z"] > 50, "the Country Z distractor asserts more than half in one group"
    return "Country Y is alone in pairing the smallest largest-group share (29%) with the largest group count (250)"


def q17(table, item):
    shares = dict(zip(cg.labels(table), cg.col(table, SHARE)))
    above = [lab for lab, v in shares.items() if v > 80]
    assert above == ["Country W"], f"exactly one row may exceed 80 percent; got {above}"
    assert shares["Country W"] == 82, f"the keyed choice says 82 percent, table says {shares['Country W']}"
    for lab, v in shares.items():
        if lab != "Country W":
            assert v < 80, f"{lab} at {v} would give the item a second defensible answer"
    return "Country W's 82 percent is the only value in the table above the framework's 80 percent line"


CLAIMS = [
 ("state",
  "EK PAU-1.A.2 defines a state as a political organization combining a permanent population with governing institutions to exercise control over a defined territory with international recognition. The stem supplies all three elements and no other listed term is territorial."),
 ("government but not the regime",
  "EK PAU-1.A.2 says regimes are the fundamental rules controlling access to and exercise of power and typically endure from government to government. Replacing officeholders under unchanged constitutional rules is by that definition a change of government alone."),
 ("abolishes competitive elections",
  "EK PAU-1.A.2. Replacing the constitution and abolishing competitive elections alters the fundamental rules of access to power themselves, whereas a succession, a reshuffle, a budget fight and a state visit are all events occurring inside rules that stay put."),
 ("nation but not a state",
  "EK PAU-1.A.5 defines a nation by shared race, language, religion, ethnicity, political identity and aspirations, none of which requires territory; EK PAU-1.A.2 makes defined territory and international recognition necessary to a state, and the group in the stem has neither."),
 ("government",
  "EK PAU-1.A.4, near verbatim: a government is the set of institutions or individuals legally empowered to make binding decisions for a state. The regime is the rules those institutions work under and civil society is by definition autonomous from the state."),
 ("without outside interference",
  "EK PAU-1.A.4 states that the right and power to govern itself without outside interference is a crucial aspect of a state's sovereignty, and that a sovereign state has independent legal authority over a population in a particular territory."),
 ("sets rules and makes decisions",
  "EK PAU-1.A.3, near verbatim: a regime can be characterized as democratic or authoritarian based on how it sets rules or makes decisions about how to exercise power. Territory, language, cabinet size and growth are outside that criterion."),
 ("political system",
  "EK PAU-1.A.1 defines a political system as the laws, ideas and procedures that address who should have authority to rule and what the government's influence on its people and economy should be, which is precisely the stem's two-part description."),
 ("state and regime persist",
  "EK PAU-1.A.2 separates the three levels, so unchanged borders and recognition leave the state intact, an unchanged constitution leaves the fundamental rules of access intact, and a new party in office is a change of officeholders only."),
 ("United Kingdom and Nigeria",
  "EK LEG-2.A.1f identifies Scottish, English, Welsh and Irish national differences within the United Kingdom and EK LEG-2.A.1d identifies more than 250 ethnic groups within Nigeria. The rejected pairings rest on unitary or federal structure, election type or geography, none of which bears on how many nations a state contains."),
 ("officeholders came and went",
  "EK PAU-1.A.2's statement that regimes typically endure from government to government. A run of prime ministers is a run of governments, so a regime outliving four of them is the framework's expected relationship rather than an anomaly."),
 ("foreign power exercises legal authority",
  "EK PAU-1.A.4 locates sovereignty in independent legal authority over a population in a particular territory, free of outside interference. Only foreign legal authority over the territory touches that; election results, resignations, legislative defeats and judicial review are ordinary internal politics."),
 ("international recognition",
  "EK PAU-1.A.2 lists a permanent population, governing institutions, control over a defined territory and international recognition. The stem grants the first three and denies the fourth, so recognition is the element in doubt."),
 ("regime sets the rules",
  "EK PAU-1.A.2 makes the regime the fundamental rules controlling access to and exercise of power and says regimes endure from government to government, so the rules frame the succession of governments and not the reverse. Both democratic and authoritarian systems have regimes."),
 ("rules of access to power have been replaced",
  "EK PAU-1.A.2. Suspending a constitution and cancelling elections replaces the fundamental rules controlling access to and the exercise of political power, which is exactly what separates a change of regime from a change of government."),
 ("no group approaches a majority",
  "EK LEG-2.A.1d describes Nigeria as containing more than 250 ethnic groups with no single dominant group. Recomputed in q16 above: one row alone pairs the smallest largest-group share with a group count in the hundreds."),
 ("at 82 percent",
  "EK LEG-2.A.1e states that ethnic Russians are more than 80 percent of the population. Recomputed in q17 above: exactly one row in the table exceeds 80 percent, so the item has one defensible answer."),
 ("nation divided across two states",
  "EK PAU-1.A.5 defines a nation by shared language, identity and aspirations rather than by borders, so a nation may lie across a state boundary; EK PAU-1.A.2's state is defined by one defined territory and cannot."),
 ("persists as a legal and territorial entity",
  "EK PAU-1.A.2 and EK PAU-1.A.4 together: the state is the territorial organization with a permanent population and recognition, the government is the current set of institutions legally empowered to bind it, and the first outlasts the second."),
 ("does not exercise effective control",
  "EK PAU-1.A.2 makes control over a defined territory with international recognition necessary to statehood. Leadership turnover, ethnic diversity, an unamended constitution and treaty membership are all compatible with being a state, so none of them supports the argument."),
 ("legally obliged to pay",
  "EK PAU-1.A.4 turns on the word BINDING: a government is legally empowered to make binding decisions for a state. An editorial, professional guidance, religious advice and an investment decision may all be influential while leaving their audience legally free to disregard them."),
 ("actually operate in practice",
  "EK PAU-1.A.3 makes the classification depend on how a regime sets rules and makes decisions about exercising power. Whether an election is held is one such rule and whether opponents may contest it is another, so both belong to the same assessment."),
 ("how far the government may direct the economy",
  "EK PAU-1.A.1 defines a political system by two things at once, who should have authority to rule and what government's influence on people and economy should be. Only the keyed option alters either, and it alters both."),
 ("independent legal authority",
  "EK PAU-1.A.4 locates sovereignty in a state's independent legal authority over a population and territory, while EK LEG-1.A.1 locates legitimacy in whether a government's constituents believe it has the right to use power as it does. One is a legal standing, the other a belief."),
 ("nation and a state need not coincide",
  "EK PAU-1.A.5's nation is a people with shared commonalities and aspirations and EK PAU-1.A.2's state is a territorial organization with recognition. A secession demand asks that the two be made to coincide, which presupposes that they presently do not."),
 ("constitutional rule fixing",
  "EK PAU-1.A.2 assigns the fundamental rules controlling access to power to the regime. A rule fixing how a head of government is selected survives every change of officeholder, whereas a current policy, a party name, a minister's identity and a reshuffle date describe who is in office now."),
 ("contain many nations",
  "EK PAU-1.A.2 defines the state territorially and EK PAU-1.A.5 defines the nation by shared commonalities, so neither constrains the count of the other. EK LEG-2.A.1f's Scottish, English, Welsh and Irish nations inside one state is the framework's own illustration."),
 ("attributes of a state",
  "EK PAU-1.A.2's list is satisfied in the stem: permanent population, governing institutions, accepted territory, international recognition. Recognition by other countries is not EK LEG-1.A.1's legitimacy, which concerns the beliefs of a government's own constituents."),
 ("constraints on how they use power",
  "EK PAU-1.A.3 makes the democratic-authoritarian classification depend on how a regime sets rules and makes decisions about exercising power, whose two halves are exactly access to office and constraint in office. Population, provinces, exports and capital cities bear on neither half."),
 ("changed far less often",
  "EK PAU-1.A.2's phrase describes the ordinary rhythm of politics: elections and successions replace officeholders frequently while the constitutional rules structuring those events are amended rarely. EK PAU-1.D.3 allows regimes to change, so the endurance is a tendency and not a bar."),
]

cg.check(k1_2, CLAIMS, table_checks={16: q16, 17: q17})
