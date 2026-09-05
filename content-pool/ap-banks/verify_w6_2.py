"""Key audit for AP WORLD HISTORY: MODERN 6.2 State Expansion from 1750 to 1900.

One (anchor, claim) per item, in module order. ``anchor`` is a distinctive
substring that must appear in the KEYED choice and in no distractor, so an
off-by-one key or a reordered choice list fails here rather than reaching a
student. ``claim`` states what the key rests on, for a human to audit.

The structural gate is ``cg_check.check``; the notation gate and the negative
control are ``es_check``, reused unchanged, because World History is a prose
subject that ``export_units.py`` does not typeset, exactly as ENV_SCI is.

WHAT THE KEYS REST ON
---------------------
Items 1, 12, 20, 21, 23, 24, 27 rest on KC-5.2.I.A: some states with existing
colonies strengthened their control over those colonies and in some cases
assumed direct control over colonies previously held by non-state entities.
Items 2 and 3 rest on the CED's two printed illustrations of that statement,
the Congo passing from King Leopold II's private ownership to the Belgium
government and Indonesia and Southeast Asia passing from the Dutch East India
Company to Dutch government control. The DIRECTION is the whole content of both
items, so each anchor carries both clauses and the exact reversal is a
distractor.

Items 4, 5, 22 rest on KC-5.2.I.B: European states as well as the United States
and Japan acquired territories throughout Asia and the Pacific, while Spanish and
Portuguese influence declined. Item 4's anchor carries both clauses for the same
reason.

Items 6, 7, 13, 18, 28 rest on KC-5.2.I.C: many European states used both
warfare and diplomacy to expand their empires in Africa. The framework names TWO
means, which is why every single-means option is wrong rather than partial.
Item 13 rests on the CED's printed illustrations for that statement: Britain in
West Africa, Belgium in the Congo, French in West Africa.

Items 8, 9, 17, 25 rest on KC-5.2.I.D, that Europeans established settler
colonies in some parts of their empires, with New Zealand as the CED's printed
example. The framework does not define a settler colony; items 8 and 25 use the
plainest sense of the term the framework presupposes, and its own vocabulary of
settlement in KC-5.2.II.B, and nothing further.

Items 10, 11, 26 rest on KC-5.2.II.B: the United States, Russia and Japan
expanded their land holdings by conquering and settling neighboring territories.
Item 10 turns on the difference between that list and KC-5.2.I.B's, which is
Russia; both statements are printed under this topic, so the comparison is the
framework's own.

Items 29 and 30 rest on Unit 6 Learning Objective B, comparing processes by
which state power shifted, and on what the topic's five statements do and do not
assert. No item asks for a year, a battle, a treaty text, a person or a
population figure the CED does not print, and every source is unattributed.

DATA ITEMS: 14 to 19 carry tables whose values are hypothetical and labelled so
in the stem. Each keyed conclusion is recomputed below from that table alone,
and each check also falsifies the distractors.

NEGATIVE CONTROL: ``python3 verify_w6_2.py --selftest`` rotates every key off its
anchor, corrupts every table cell in turn, injects each banned notation form
(and one legal string that must pass), duplicates a choice, thins a why and
makes a why name an option by letter, and requires every one of those to raise.
"""
import sys

import cg_check as cg
import es_check as es
import w6_2

START = "Body exercising control at the start of the period"
END = "Body exercising control at the end of the period"
MEANS = "Means by which control was first obtained"
SETTLERS = ("Settlers from the imperial state resident at the end of the period "
            "(hypothetical)")


def _rows(table):
    """Rows as dicts keyed by header, so a reordered column cannot repoint a check."""
    idx = {h: j for j, h in enumerate(table["headers"])}
    return [{h: str(r[j]) for h, j in idx.items()} for r in table["rows"]]


def _nonstate(text):
    t = text.lower()
    return "company" in t or "privately owned" in t


def _state(text):
    return "government" in text.lower()


def _shifted(row):
    return _nonstate(row[START]) and _state(row[END])


def q14(table, item):
    rows = _rows(table)
    shifted = [r["Territory (hypothetical)"] for r in rows if _shifted(r)]
    assert len(rows) == 5, f"the stem says five territories; the table holds {len(rows)}"
    assert len(shifted) == 3, f"key requires three shifts; the table gives {shifted}"
    return (f"three of the five rows begin under a company or a private estate and end under a "
            f"government: {', '.join(shifted)}")


def q15(table, item):
    rows = _rows(table)
    other = [r["Territory (hypothetical)"] for r in rows
             if _shifted(r) and "different" in r[END].lower()]
    assert other == ["Territory S"], f"the different-state row is {other}"
    # "the same European state" and "that monarch's own state" both mean the
    # acquiring state is the one the previous holder belonged to. The first
    # version of this check looked for "same" alone and reported Territory U as
    # a different-state shift, which the register does not say -- the checker
    # was wrong, not the register.
    same = [r["Territory (hypothetical)"] for r in rows
            if _shifted(r) and ("same" in r[END].lower() or "own state" in r[END].lower())]
    assert set(same) == {"Territory Q", "Territory U"}, f"same-state shifts are {same}"
    return ("only Territory S ends under the government of a different European state; the other "
            "two shifts end under the government of the same state")


def q16(table, item):
    rows = _rows(table)
    unshifted = [r["Territory (hypothetical)"] for r in rows if not _shifted(r)]
    assert unshifted == ["Territory R", "Territory T"], f"unshifted rows are {unshifted}"
    return ("Territory R keeps the same company at both ends and Territory T is under a "
            "government at both ends, so neither shows a non-state to state shift")


def q17(table, item):
    rows = _rows(table)
    counts = {r["African territory (hypothetical)"]: cg.num(r[SETTLERS]) for r in rows}
    top = max(counts, key=counts.get)
    assert top == "Territory V", f"largest settler figure is {top!r}"
    assert counts[top] > sum(v for k, v in counts.items() if k != top), \
        "the keyed territory must hold more settlers than the rest combined"
    assert all(v > 0 for v in counts.values()), "settlement is recorded, so 'not recorded' is false"
    return (f"Territory V holds {counts['Territory V']:g} settlers, more than the other three "
            "combined, and every row records a settler figure")


def q18(table, item):
    means = [r[MEANS].lower() for r in _rows(table)]
    assert any("treaty" in m for m in means), "no diplomatic means in the table"
    assert any("military" in m for m in means), "no warfare in the table"
    assert not all("military" in m for m in means), "'only warfare' must be false"
    assert not all("treaty" in m for m in means), "'only diplomacy' must be false"
    assert not all("company" in m for m in means), "'every territory by company transfer' must be false"
    return ("the table records a negotiated treaty, two military campaigns and a company "
            "transfer, so both named means appear and no single means accounts for all rows")


def q19(table, item):
    rows = _rows(table)
    war = {r["African territory (hypothetical)"]: cg.num(r[SETTLERS]) for r in rows
           if "military" in r[MEANS].lower()}
    other = {r["African territory (hypothetical)"]: cg.num(r[SETTLERS]) for r in rows
             if "military" not in r[MEANS].lower()}
    assert max(war.values()) > min(other.values()), \
        "the keyed statement must be FALSE on the table: some campaign row must beat some other row"
    treaty = [cg.num(r[SETTLERS]) for r in rows if "treaty" in r[MEANS].lower()]
    allv = list(war.values()) + list(other.values())
    assert treaty and treaty[0] == max(allv), "'treaty row holds the most' must be true"
    assert min(allv) < 1000, "'one territory below a thousand' must be true"
    assert len(war) == 2, "'two territories obtained by military campaign' must be true"
    company = [cg.num(r[SETTLERS]) for r in rows if "company" in r[MEANS].lower()]
    assert company and company[0] == min(allv), "'company transfer holds the fewest' must be true"
    return ("a military-campaign row holds 95,000 against 600 in the company-transfer row, so the "
            "keyed claim is false while the four rejected statements recompute as true")


TABLE_CHECKS = {14: q14, 15: q15, 16: q16, 17: q17, 18: q18, 19: q19}

CLAIMS = [
 ("non-state entity to direct control by a state",
  "KC-5.2.I.A states that some states assumed direct control over colonies previously held by non-state entities. A chartered company is such an entity and a Crown is a state, so the statute is that process in one document; the reversal is offered as a distractor."),
 ("privately owned by King Leopold II and control then passed to the Belgian government",
  "The CED prints, as its illustration of non-state to state colonial control, the shift from the private ownership of the Congo by King Leopold II to the Belgium government. The anchor carries both clauses because the exact reversal is a distractor and is the easy wrong answer."),
 ("Dutch East India Company to control by the Dutch government",
  "The CED's second printed illustration for KC-5.2.I.A is the shift from the Dutch East India Company to Dutch government control in Indonesia and Southeast Asia. The anchor carries both halves of the direction, since the reversal is offered."),
 ("acquired territories there while Spanish and Portuguese influence declined",
  "KC-5.2.I.B, near verbatim: European states as well as the United States and Japan acquired territories throughout Asia and the Pacific, while Spanish and Portuguese influence declined. Both clauses are in the anchor because the swapped version is a distractor."),
 ("The United States and Japan",
  "KC-5.2.I.B names European states as well as the United States and Japan as acquiring territories throughout Asia and the Pacific. No other non-European state is named in that statement."),
 ("both warfare and diplomacy",
  "KC-5.2.I.C states that many European states used both warfare and diplomacy to expand their empires in Africa. The framework names two means, which is why each single-means option is wrong rather than merely incomplete."),
 ("expansion by diplomacy, one of the two means",
  "KC-5.2.I.C names warfare and diplomacy as the two means of European expansion in Africa. An agreement concluded without fighting is the second of them, and the source reports no company, no settlement and no declining empire."),
 ("permanent settlement of populations from the imperial state",
  "KC-5.2.I.D states that Europeans established settler colonies in some parts of their empires, and KC-5.2.II.B uses the same vocabulary of settling territory. Settlement is what the term picks out; the framework attaches none of the four rejected features to it."),
 ("New Zealand",
  "The CED prints New Zealand as its illustrative example of settler colonies established in empires, beside KC-5.2.I.D. The Congo and Indonesia appear in this topic as non-state to state transfers and West Africa among the African expansions, so none of them is the settler-colony example."),
 ("Russia",
  "KC-5.2.II.B names the United States, Russia and Japan as expanding their land holdings by conquering and settling neighboring territories, while KC-5.2.I.B names European states, the United States and Japan as acquiring territories throughout Asia and the Pacific. Russia is in the first list and not the second."),
 ("one into neighbouring territory and one overseas",
  "KC-5.2.I.B describes acquisition across Asia and the Pacific and KC-5.2.II.B describes conquest and settlement of neighboring territories, so the framework treats both as expansions of state holdings. Learning objective B asks for exactly this comparison, so a difference of geography is what is compared rather than a bar to comparing."),
 ("from a private body to a state that had not held it directly before",
  "KC-5.2.I.A describes states assuming DIRECT control over colonies previously held by non-state entities, which is a change in the kind of body exercising power rather than in its personnel. The reversal is a distractor, and the framework attaches no border change, no end of empire and no fiscal consequence to the transfer itself."),
 ("Britain in West Africa, Belgium in the Congo, and the French in West Africa",
  "These are the CED's printed illustrative examples of European states that expanded empires in Africa, alongside KC-5.2.I.C. The rejected options move those states to regions the framework does not attach to them."),
 ("Three of the five",
  "Recomputed in q14 above from the register alone: Territory Q, Territory S and Territory U each begin under a company or a private estate and end under a government, while Territory R and Territory T do not shift."),
 ("Territory S",
  "Recomputed in q15 above: Territory S is the only row ending under the government of a DIFFERENT European state; the other two shifts end under the government of the same state."),
 ("Territory R and Territory T",
  "Recomputed in q16 above: Territory R keeps the same chartered company at both ends and Territory T is under a government at both ends, so neither is an instance of the KC-5.2.I.A shift."),
 ("Territory V",
  "Recomputed in q17 above: Territory V holds 180,000 settlers, more than the other three rows combined, and every row records a settler figure, so KC-5.2.I.D's mark of a settler colony falls on that row and the 'not recorded' option is false."),
 ("Both warfare and diplomacy appear",
  "KC-5.2.I.C names both means for Africa, and q18 above confirms the register carries a negotiated treaty, two military campaigns and a company transfer, so both appear and no single means accounts for all four rows."),
 ("fewer settlers than any territory obtained otherwise",
  "Recomputed in q19 above: a military-campaign row holds 95,000 settlers against 600 in the company-transfer row, so the keyed statement is false on the register's own numbers while each rejected statement recomputes as true."),
 ("non-state holder came under the direct control of a European government",
  "KC-5.2.I.A states the pattern and the CED prints these two cases as its illustrations of it. The reversal, a government handing a territory to a non-state holder, is offered as a distractor and is not what either example describes."),
 ("body exercising control changed while the territory remained under imperial rule",
  "KC-5.2.I.A describes states ASSUMING direct control over colonies previously held by non-state entities, so the holder changes and the colonial relationship continues. The anchor carries both clauses because the exact reversal is a distractor."),
 ("declining while other states acquired territories",
  "KC-5.2.I.B pairs the acquisitions by European states, the United States and Japan with the decline of Spanish and Portuguese influence in one sentence, so the framework asserts the opposite of the student's claim while still affirming that acquisition occurred in the region."),
 ("strengthening its control over a colony it already held",
  "KC-5.2.I.A opens with states that strengthened their control over existing colonies, which is what more resident officials, courts extended into the interior and a new direct tax describe. The source names no company, no settlement, no independence and no second imperial state."),
 ("previously held by non-state entities",
  "KC-5.2.I.A names exactly two processes: strengthening control over existing colonies, and assuming direct control over colonies previously held by non-state entities. Purchase, division by treaty, self-government, company founding and taxation policy are not asserted in that statement."),
 ("settler colony",
  "KC-5.2.I.D states that Europeans established settler colonies in some parts of their empires, and permanent emigration to take up land is what the term picks out. The source describes no charter, no resistance movement, no commercial sphere and no conquest of adjacent land."),
 ("added neighbouring territory by conquest and settlement",
  "KC-5.2.II.B states that the United States, Russia and Japan expanded their land holdings by conquering and settling neighboring territories. Purchase, company transfer and abandonment of territory are not asserted of them there."),
 ("states the pattern in general terms and offers these cases as examples",
  "KC-5.2.I.A is a general statement and the CED prints the Congo and the Dutch East Indies beside it as illustrative examples. The framework marks such examples as illustrative and asks for no dates, so neither uniqueness nor memorisation is implied."),
 ("diplomacy between imperial states",
  "KC-5.2.I.C names warfare and diplomacy as the two means of European expansion in Africa, and a boundary fixed by negotiation between two states is diplomacy. The source reports no fighting, no company, no settlement and no anticolonial movement."),
 ("Which states acquired territories in Asia and the Pacific can be settled; whether a particular acquisition was popular at home cannot",
  "KC-5.2.I.B names the acquiring states and KC-5.2.I.C names the means used in Africa, so those questions have answers in the framework; opinion at home, colonial voting and settler numbers are asserted nowhere in this topic. The anchor carries both clauses because the exact reversal is a distractor."),
 ("the holder or the reach of state power over a territory changed",
  "Learning objective B asks students to compare processes by which state power shifted. The topic's five statements are strengthened control, control assumed from non-state entities, acquisitions in Asia and the Pacific, warfare and diplomacy in Africa, settler colonies, and conquest and settlement of neighbouring land; each changes who exercises state power or how far it reaches, across several continents."),
]

es.run(w6_2, CLAIMS, TABLE_CHECKS, sys.argv)
