"""Key audit for AP WORLD HISTORY: MODERN 5.7 Economic Developments and Innovations.

One (anchor, claim) per item, in module order. The anchor must appear in the
keyed choice and in no distractor; the claim cites the Key Concept or Learning
Objective the key traces to.

WHAT THE KEYS REST ON
---------------------
Three statements, and every key traces to one of them or to Unit 5 Learning
Objective H:

  KC-5.1.III.A  Western European countries BEGAN abandoning mercantilism and
                adopting free trade policies, PARTLY in response to the GROWING
                acceptance of Adam Smith's theories of laissez-faire capitalism
                and free markets.
  KC-5.1.III.B  The global nature of trade and production CONTRIBUTED TO the
                proliferation of large-scale transnational businesses that RELIED
                ON new practices in banking and finance.
  KC-5.1        The development of industrial capitalism led to increased
                standards of living FOR SOME, and to continued improvement in
                manufacturing methods that increased the availability,
                affordability, and variety of consumer goods.

The CED prints four illustrative examples on this page: HSBC and Unilever under
"Transnational businesses", stock markets and limited-liability corporations
under "Financial instruments". Items 10, 11, 12 and 20 key those and nothing
further, because the framework says nothing further about them.

"FOR SOME" IS THE WHOLE TOPIC
-----------------------------
The single easiest wrong key in this unit is a general claim that industrial
capitalism raised living standards. KC-5.1 says FOR SOME. Items 13, 14, 22, 23,
26 and 30 each hold that qualification, and item 23's table is built so that two
of four groups gain and two do not -- the qualification recomputed rather than
asserted. The framework also never says WHO the some were, so item 14 rejects a
distractor that names them.

NO DATE IS KEYED
----------------
The framework prints no date for the repeal of any duty and no date for any firm.
"Began abandoning" is a process, and the CED separately states that its
developments may begin before or continue after the years given, so item 24's
table deliberately leaves protective duties still in place in the final decade.

SWAP ANCHORS
------------
All three statements are causal and all three read plausibly backwards, so items
1, 5, 9, 11 and 16 carry the reversal as a distractor -- free trade and
mercantilism exchanged, the policy change and the acceptance of the theories
exchanged, the businesses and the global trade that produced them exchanged, a
firm's base and its field of operation exchanged, and the manufacturing methods
and the consumer goods exchanged. Each of those anchors carries BOTH clauses,
which is the defect found in verify_e2_1.py.

WHY THE TABLE CONTROL DOES NOT CATCH EVERY CELL
-----------------------------------------------
The selftest prints a per-table catch rate rather than requiring one hundred
percent. Raising a figure that is already the largest in an already-ordered
column can leave the keyed conclusion TRUE of the corrupted table, and a check
that fired on that would be reporting a defect that is not there. What the
control requires is that no table sits undefended: q23, q24 and q25 must each
catch at least one corrupted cell, and the printed count is what makes a check
that has stopped reading its table show up as a zero.

FIVE choices per item (A-E); see HISTORY_BRIEF.md.
"""
import sys

import cg_check as cg
import wh_check as wh
import w5_7

EARLIER = "Index of real income, earlier decade"
LATER = "Index of real income, later decade"
PROTECTED = "Share of imports carrying protective duties (percent)"
TREATIES = "Treaties in force that reduce duties"
COUNTRIES = "Countries in which the firm operates"
PRACTICES = "Uses the new banking and finance practices"


def _column(table, header):
    """A column read as raw strings, for a column that holds words not numbers."""
    heads = [cg.normalize(h) for h in table["headers"]]
    j = heads.index(cg.normalize(header))
    return [str(row[j]) for row in table["rows"]]


def q23(table, item):
    """Exactly two of four groups gain; the other two do not. That is 'for some'."""
    labels = cg.labels(table)
    assert labels == ["Group 1", "Group 2", "Group 3", "Group 4"], \
        f"the four rows must be the four groups in order; got {labels}"
    earlier = cg.col(table, EARLIER)
    later = cg.col(table, LATER)
    risen = [lab for lab, a, b in zip(labels, earlier, later) if b > a]
    flat_or_down = [lab for lab, a, b in zip(labels, earlier, later) if b <= a]
    assert len(risen) == 2, (
        f"exactly two groups must rise, or the keyed 'two of the four' is false; got {risen}"
    )
    assert len(flat_or_down) == 2, (
        f"exactly two groups must fail to rise, or 'the other two' is false; got {flat_or_down}"
    )
    assert len(risen) < len(labels), "'rises for all four groups' must be false"
    assert risen, "'falls for all four groups' must be false"
    assert any(a != b for a, b in zip(earlier, later)), "'unchanged for every group' must be false"
    return (f"recomputed from the table: real income rises for {risen} and does not rise for "
            f"{flat_or_down}, which is two of the four either way")


def q24(table, item):
    """Protection falls at every step, treaties rise at every step, protection survives."""
    labels = cg.labels(table)
    assert labels == ["First decade", "Second decade", "Third decade", "Fourth decade"], \
        f"the four rows must be the four decades in order; got {labels}"
    protected = cg.col(table, PROTECTED)
    treaties = cg.col(table, TREATIES)
    assert all(b < a for a, b in zip(protected, protected[1:])), \
        f"the protected share must fall at every step; got {protected}"
    assert all(b > a for a, b in zip(treaties, treaties[1:])), \
        f"the treaty count must rise at every step; got {treaties}"
    assert protected[-1] > 0, (
        f"protective duties must still be in place in the last decade, because KC-5.1.III.A says "
        f"the countries BEGAN abandoning mercantilism and never says they finished; "
        f"got {protected[-1]}"
    )
    return (f"recomputed from the table: the protected share {protected} falls at every step, the "
            f"treaty count {treaties} rises at every step, and protection is still above zero in "
            f"the final decade")


def q25(table, item):
    """Every multi-country firm uses the new practices; the single-country firm does not."""
    labels = cg.labels(table)
    assert labels == ["Firm 1", "Firm 2", "Firm 3", "Firm 4"], \
        f"the four rows must be the four firms in order; got {labels}"
    countries = cg.col(table, COUNTRIES)
    uses = _column(table, PRACTICES)
    assert set(uses) <= {"Yes", "No"}, f"the practices column must hold only Yes or No; got {uses}"
    many = [lab for lab, n in zip(labels, countries) if n > 1]
    one = [lab for lab, n in zip(labels, countries) if n <= 1]
    flag = dict(zip(labels, uses))
    assert len(one) == 1, (
        f"exactly one firm must be confined to a single country, or 'the one firm' is false; "
        f"got {one}"
    )
    assert all(flag[lab] == "Yes" for lab in many), (
        f"every firm operating in more than one country must use the new practices; "
        f"got {[(lab, flag[lab]) for lab in many]}"
    )
    assert flag[one[0]] == "No", (
        f"the single-country firm must NOT use the new practices, or the second half of the key "
        f"is false; got {one[0]} = {flag[one[0]]}"
    )
    assert max(countries) == max(countries[i] for i, lab in enumerate(labels)
                                 if flag[lab] == "Yes"), \
        "the firm operating in the most countries must be one that uses the new practices"
    return (f"recomputed from the table: {many} each operate in more than one country and use the "
            f"new practices, while {one} operates in one country and does not")


CLAIMS = [
 ("Abandon mercantilism and adopt free trade policies",
  "KC-5.1.III.A states the direction: western European countries began abandoning mercantilism and adopting free trade policies. A distractor exchanges the two policies, so the anchor carries both halves of the sentence rather than either alone."),
 ("Adam Smith's theories of laissez-faire capitalism and free markets",
  "KC-5.1.III.A names them as the theories whose growing acceptance was part of the reason for the shift. Marx belongs to KC-5.3.IV.A.ii and the social contract to KC-5.3.I.A, both on other topic pages."),
 ("one part of the reason and does not present them as the whole of it",
  "KC-5.1.III.A says PARTLY in response to the growing acceptance of those theories. The adverb limits the claim, so a key making the theories the sole cause asserts more than the framework does."),
 ("the shift was under way, not that it was complete",
  "KC-5.1.III.A says these countries BEGAN abandoning mercantilism, which describes a process in motion. The framework never says the process finished, and the CED separately states that its developments may continue after the period given."),
 ("growing acceptance of those theories is part of what moved those countries away from mercantilism",
  "KC-5.1.III.A makes the policy change the thing explained and the growing acceptance of the theories part of the explanation. The anchor carries both clauses because a distractor exchanges them."),
 ("Western European countries",
  "KC-5.1.III.A names western European countries and no others. The framework's other regional statements in this unit, KC-5.1.I.D and KC-5.1.II.B, sit on topic 5.4 and make different claims."),
 ("global nature of trade and production",
  "KC-5.1.III.B says the global nature of trade and production CONTRIBUTED TO the proliferation of large-scale transnational businesses. The framework's verb is contributed to, not caused."),
 ("New practices in banking and finance",
  "KC-5.1.III.B closes with it: transnational businesses that relied on new practices in banking and finance. The CED prints stock markets and limited-liability corporations beside that statement."),
 ("global nature of trade and production contributed to the proliferation of those businesses",
  "KC-5.1.III.B puts the global nature of trade first and the businesses second. The anchor carries both clauses because the distractor exchanges them, and the direction of the sentence is the whole of the answer."),
 ("Hong Kong and Shanghai Banking Corporation",
  "The CED prints two transnational businesses beside KC-5.1.III.B and this is one of them. The rejected options are illustrative examples printed beside KC-5.1.II.A, KC-5.1.V.C and KC-5.2.I.E on other topics' pages."),
 ("Based in England and the Netherlands, operating in British West Africa and the Belgian Congo",
  "The illustrative example printed beside KC-5.1.III.B gives the base and the field of operation in that order. Three distractors exchange them, so the anchor carries both clauses rather than the base alone."),
 ("Stock markets and limited-liability corporations",
  "The CED prints exactly that pair under the heading financial instruments beside KC-5.1.III.B, the statement about businesses relying on new practices in banking and finance. Nothing else on the page is offered as an instrument."),
 ("Increased standards of living for some, and continued improvement in manufacturing methods",
  "KC-5.1 names both consequences in one sentence and qualifies the first: increased standards of living FOR SOME, and continued improvement in manufacturing methods. Dropping the qualification is the easiest wrong key in this topic."),
 ("a rise for part of the population and not for all of it",
  "KC-5.1 says FOR SOME, which limits the claim without naming who benefited. A key identifying a group would supply what the CED does not print, and a key generalizing the rise would contradict it."),
 ("availability, affordability, and variety of consumer goods",
  "KC-5.1 names all three together: continued improvement in manufacturing methods that increased the availability, affordability, and variety of consumer goods. The framework's list has three items and the key carries all of them."),
 ("improvement in manufacturing methods increased the availability of consumer goods",
  "KC-5.1 puts the improvement in methods first and the availability of goods second. The anchor carries both clauses because a distractor exchanges them, and this topic's reasoning process asks students to trace exactly such a relationship."),
 ("how they contributed to change in the period",
  "Unit 5 Learning Objective H asks for the development of economic systems, ideologies, and institutions and how they contributed to change from 1750 to 1900. The rejected questions belong to the objectives behind KC-5.1.I.A, KC-5.1.I.B, KC-5.1.VI.A and KC-5.3."),
 ("global nature of trade and production, and the spread of large-scale transnational businesses",
  "KC-5.1.III.B joins those two developments in a single sentence, saying the first contributed to the second. The rejected pairings join this page to KC-5.1.V.A, KC-5.1.VI.C, KC-5.1.VI.A or KC-5.1.IV, connections the framework nowhere makes."),
 ("began abandoning mercantilism and adopting free trade policies",
  "KC-5.1.III.A describes the shift away from mercantilism toward free trade, partly in response to the growing acceptance of free market theories. An argument for repealing a duty on that ground is that shift stated as a claim."),
 ("large-scale transnational business and a limited-liability corporation",
  "KC-5.1.III.B describes large-scale transnational businesses relying on new practices in banking and finance, and the CED prints stock markets and limited-liability corporations beside it. Shares sold to subscribers whose loss is capped are those two things at once."),
 ("availability, affordability and variety of consumer goods",
  "KC-5.1 ties improved manufacturing methods to the availability, affordability, and variety of consumer goods, and a catalogue offering more patterns at lower prices shows all three. The rejected options are KC-5.1.III.A, KC-5.1.III.B, KC-5.1.V.A and KC-5.1.V.C."),
 ("framework, which says standards of living increased for some",
  "KC-5.1 says the development of industrial capitalism led to increased standards of living FOR SOME. A district in which some households gained and others did not is exactly what that qualification allows for."),
 ("rises for two of the four groups and does not rise for the other two",
  "KC-5.1 says standards of living increased for some, and q23 above recomputes the sample: two of four groups rise and two do not. Both halves come from comparing the earlier and later columns row by row, with nothing recalled."),
 ("falls in every decade while the number of treaties reducing duties rises, and protection has not disappeared",
  "KC-5.1.III.A says these countries BEGAN abandoning mercantilism, a shift under way rather than a completed one, and q24 above recomputes the table the same way: the protected share falls at every step, the treaties rise at every step, and the share is still above zero in the final row."),
 ("operating in more than one country uses the new banking and finance practices, and the one firm confined to a single country does not",
  "KC-5.1.III.B describes large-scale transnational businesses that relied on new practices in banking and finance, and q25 above sorts the sample by both columns. The anchor carries both halves because two distractors reverse one of them."),
 ("adopted by every state in the world by the end of the period",
  "KC-5.1.III.A, KC-5.1.III.B and KC-5.1 state the other four claims. None extends free trade beyond western European countries or says the shift was completed, so worldwide adoption supplies what the CED does not print."),
 ("trade policies of western European states, the other the spread of businesses operating across borders",
  "KC-5.1.III.A is about the trade policies of western European countries and KC-5.1.III.B about transnational businesses and the finance they relied on. Workers' organizations belong to KC-5.1.V.A and urban growth to KC-5.1.VI.C, neither printed on this page."),
 ("how businesses were financed at the start and at the end of the period",
  "Unit 5 Learning Objective H asks how economic institutions developed and contributed to change, and KC-5.1.III.B names banking and finance practices as the institutions in question. A comparison across the period is what a claim of change requires; a single year cannot show change at all."),
 ("How much profit any of them made",
  "KC-5.1.III.B supplies the scale, the cross-border operation, the reliance on new banking and finance practices and the connection to global trade. It prints no figure of any kind, so a profit claim would fill a silence in the CED."),
 ("raised living standards for some while making consumer goods more available",
  "The summary joins KC-5.1.III.A, KC-5.1.III.B and KC-5.1 and keeps every hedge those sentences carry: a shift that began, businesses whose spread was contributed to rather than caused, and living standards that rose for some. Each rejected option contradicts one of the three."),
]

TABLE_CHECKS = {23: q23, 24: q24, 25: q25}

wh.run(w5_7, CLAIMS, TABLE_CHECKS, sys.argv)
