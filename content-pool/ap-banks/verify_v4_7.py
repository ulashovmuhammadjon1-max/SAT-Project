"""Structural gate for AP U.S. Government 4.7 Ideologies of Political Parties.

gov345_check plus the four usgov_anchor helpers, plus three content gates.

This is the shortest statement in Unit 4 and the one where a careless paraphrase
does the most damage, because what it turns into is a stereotype a student will
then apply to people.

  _hedges     EK 4.7.A.1 is built out of three hedges and all three are
              droppable, each removal making the sentence stronger and less
              accurate:
                PLATFORMS    the subject is a document a party adopts, not its
                             voters and not its officeholders. "Democrats are
                             liberal" is a claim about people the framework does
                             not make.
                GENERALLY    not every plank. The first table shows alignment
                             between 59 and 88 percent, never 100.
                MORE CLOSELY a comparison, not an identity. A comparison
                             presupposes two distinct things, and the framework
                             carefully declines to say a party IS an ideology.
              The gate pins all three and refuses the identity claim in any key.

  _ideologies EK 4.7.A.1 names two ideologies without describing either. The
              descriptions live in EK 4.9.A.1 and EK 4.10.A.1 to 3, and this
              module cites those rather than inventing content -- which also
              means the two commonest confusions are checkable. Conservative is
              FEWER regulations while libertarian is LITTLE OR NO regulation
              beyond protecting property rights and voluntary trade; and the
              libertarian social position restrains STATE governments too, so it
              is not the conservative position taken further. The gate refuses
              swapping either pair.

  _no_partisanship
              This is the topic in the whole bank where an author's own politics
              would be least visible to them and most visible to a student. LO
              4.7.A asks how party ideologies SHAPE POLICY DEBATES -- a question
              about structure, about why debates recur along a predictable axis
              -- and not a question about who is right. So the gate refuses any
              evaluative verdict on a party or an ideology in any key, and
              refuses naming a politician, an administration or a piece of
              modern legislation anywhere in the module. Item 23 makes the
              framework's own silence on which position is better the question.

Federalist No. 10 is the document the CED attaches to 4.7.A and is quoted
verbatim in items 15 to 19. Item 19 exists to refuse the overreach that
attaching it invites: the essay dates from 1787, its subject is faction in
general, and it cannot endorse a modern party.
"""
import re

import gov345_check as gc
import usgov_anchor as ua
import v4_7

ANCHORS = {
 1: "Liberal ideological positions",
 2: "Conservative ideological positions",
 3: "The parties' platforms",
 4: "neither confirms nor refutes a claim about what party platforms contain",
 5: "as a tendency rather than in every plank",
 6: "leaving the platform and the ideology as distinct things",
 7: "which is a claim about documents and a tendency rather than about people",
 8: "planks that do not align with the ideology the framework associates",
 9: "More governmental regulation of the marketplace",
 10: "Fewer regulations of the marketplace",
 11: "while libertarian ideologies favor little or no regulation beyond protecting",
 12: "a tendency across platforms rather than a rule about any one of them",
 13: "it is only an expectation because the framework says platforms generally align",
 14: "pairs with neither major party",
 15: "That differences of opinion on fundamental questions divide people into parties",
 16: "It identifies economic difference as a durable basis of political division",
 17: "so a system must be designed to operate with them present",
 18: "which is what makes recurring ideological debate a permanent feature",
 19: "and it names neither modern party nor any modern ideological position",
 20: "because each party's platform commits it in advance to a general direction",
 21: "since that is the axis EK 4.9.A.1 places the ideologies along",
 22: "which is the axis EK 4.10.A.1 and EK 4.10.A.2 describe",
 23: "Which of the two parties' positions is better for the country",
 24: "would assert something about individuals and about every plank",
 25: "but in no area does either reach every plank",
 26: "since alignment is high in every area but complete in none",
 27: "so at least some planks in every area do not align",
 28: "and in each case a substantial minority does not",
 29: "and this table measures what individuals believe",
 30: "so figures about individual identifiers neither confirm nor refute it",
}

GROUNDING = {
 1: "EK 4.7.A.1, verbatim: 'The Democratic Party (D or DEM) platforms generally align more "
    "closely to liberal ideological positions.'",
 2: "EK 4.7.A.1, verbatim: 'the Republican Party (R or GOP) platforms generally align more "
    "closely to conservative ideological positions.' Same construction, same hedges.",
 3: "EK 4.7.A.1's grammatical subject in both halves: the parties' PLATFORMS, which are "
    "documents a party adopts rather than the beliefs of any person.",
 4: "EK 4.7.A.1's subject read for what it excludes. A survey of individuals measures "
    "something other than what a platform contains, so the two can vary independently.",
 5: "EK 4.7.A.1's hedge GENERALLY, chosen in a sentence that could have been written without "
    "one. It leaves room for a plank that does not align.",
 6: "EK 4.7.A.1's phrase ALIGN MORE CLOSELY TO, a comparative. A comparison presupposes two "
    "distinct things, so the framework declines to say a party IS an ideology.",
 7: "EK 4.7.A.1's three hedges against the version that drops all of them. Each removal makes "
    "the sentence stronger and less accurate, and together they convert a description of "
    "documents into a claim about persons.",
 8: "EK 4.7.A.1's GENERALLY, which makes a nonaligning plank consistent with the statement "
    "rather than a counterexample to it.",
 9: "EK 4.7.A.1 and EK 4.9.A.1 chained: the first aligns Democratic platforms with liberal "
    "positions, the second assigns liberal ideologies more governmental regulation of the "
    "marketplace. Neither reaches the platform on its own, which is LO 4.7.A's whole point.",
 10: "EK 4.7.A.1 and EK 4.9.A.1 chained for the other party. FEWER is a comparative, which "
     "is what separates the conservative position from the libertarian one in the same "
     "sentence and keeps the third choice wrong.",
 11: "EK 4.9.A.1's three positions in one sentence, and the difference between FEWER and "
     "LITTLE OR NO regulation 'beyond the protection of property rights and voluntary trade'.",
 12: "EK 4.7.A.1 and EK 4.10.A.1 together, plus the limit of the pair. EK 4.10.A.1 names "
     "public health among its examples but names no party; EK 4.7.A.1 names the party but no "
     "position, and its GENERALLY ALIGN MORE CLOSELY TO is a comparison, so the chain "
     "supports an expectation about platforms and not a claim about every one of them.",
 13: "EK 4.7.A.1 read against EK 4.10.A.1 and EK 4.10.A.2, whose structures mirror each "
     "other with the same two variables moved in opposite directions. The second half of the "
     "key is EK 4.7.A.1's hedges, which make a departing platform consistent with the "
     "framework rather than a counterexample to it.",
 14: "EK 4.10.A.3 set against EK 4.7.A.1's two-party frame: the framework describes a third "
     "ideology it pairs with no party. The Republican pairing is the tempting error and fails "
     "on the framework's own terms, because the libertarian position restrains STATE "
     "involvement too while EK 4.10.A.2's conservative position moves responsibility toward "
     "the states.",
 15: "Federalist No. 10 (required document), quoted verbatim; the CED attaches it to 4.7.A. "
     "Madison lists zeal for different opinions among the causes that have divided people "
     "into parties.",
 16: "Federalist No. 10, quoted verbatim: 'The most common and durable source of factions has "
     "been the various and unequal distribution of property.' EK 4.9.A.1 arranges the "
     "ideologies along the economic axis this names.",
 17: "Federalist No. 10, quoted verbatim: 'The latent causes of faction are thus sown in the "
     "nature of man.' It is why the essay turns to controlling the effects of faction rather "
     "than removing its causes.",
 18: "LO 4.7.A's object, how party ideologies shape policy debates, against Federalist No. "
     "10's account of why division is durable. The essay predicts recurring disagreement "
     "without predicting its content.",
 19: "Federalist No. 10's date, 1787, and its subject, faction in general. It names no modern "
     "party, and reading a founding document as an endorsement of a present-day position is "
     "the overreach that attaching it to this topic invites.",
 20: "LO 4.7.A's verb SHAPE, read through EK 4.7.A.1 and the ideological descriptions in EK "
     "4.9.A.1 and EK 4.10.A.1 to 3: a prior general commitment is what makes one axis "
     "reappear across different issues.",
 21: "EK 4.9.A.1's axis applied to a proposed regulation, CED skill 1.E.",
 22: "EK 4.10.A.1 and EK 4.10.A.2 applied to a public health question, which is one of the "
     "framework's own named examples. CED skill 1.E.",
 23: "EK 4.7.A.1 read for what it omits. It reports where each party's platforms sit relative "
     "to two sets of positions and makes no evaluation of either.",
 24: "EK 4.7.A.1's three hedges, each ruling out a specific overstatement: about people, about "
     "every plank, and about identity.",
 25: "Data item, CED skill 1.E. Every alignment rate is recomputed below.",
 26: "EK 4.7.A.1's word GENERALLY shown as data: alignment high in every area and complete in "
     "none.",
 27: "Data item: reading a high rate as a universal one. The column's maximum is recomputed.",
 28: "Data item, CED skill 1.E. Every row's majority and minority are recomputed below.",
 29: "EK 4.7.A.1's subject against what this table measures. Platforms are documents and "
     "identifiers are persons, and the two can vary independently.",
 30: "EK 4.7.A.1's subject again, from the other side: refuting a statement about documents "
     "requires evidence about documents, which the first table supplies and this one does "
     "not.",
}

DEM_COL = "Democratic platform planks aligning with liberal positions (%)"
REP_COL = "Republican platform planks aligning with conservative positions (%)"
AREA = "Policy area"
LIB_POS, CON_POS, NEITHER = ("Held the liberal position (%)", "Held the conservative position (%)",
                             "Held neither position (%)")


def _col(t, header):
    j = t["headers"].index(header)
    return [gc.num(r[j]) for r in t["rows"]]


def q25(t):
    """Every figure is a majority and none is complete; the peaks fall in different areas."""
    dem, rep = _col(t, DEM_COL), _col(t, REP_COL)
    areas = [r[0] for r in t["rows"]]
    every = dem + rep
    assert min(every) > 50, f"a figure is not a majority: {min(every):.0f}"
    assert max(every) < 100, f"a figure reaches complete alignment: {max(every):.0f}"
    assert areas[dem.index(max(dem))] != areas[rep.index(max(rep))], \
        "both columns peak in the same policy area, which the key's last distractor denies"
    assert dem != rep, "the two columns are identical"
    return (f"all {len(every)} figures between {min(every):.0f} and {max(every):.0f}; "
            f"Democratic peak in {areas[dem.index(max(dem))]!r}, Republican peak in "
            f"{areas[rep.index(max(rep))]!r}")


def q26(t):
    """A tendency, not a rule and not an absence."""
    every = _col(t, DEM_COL) + _col(t, REP_COL)
    assert all(50 < x < 100 for x in every), f"a figure falls outside a tendency: {every}"
    assert len(set(every)) > 1, "every figure is identical, so no tendency is visible"
    return (f"alignment between {min(every):.0f} and {max(every):.0f} percent -- above half "
            "everywhere, complete nowhere")


def q27(t):
    """The Democratic column's maximum is 88, so no area is fully aligned."""
    dem = _col(t, DEM_COL)
    assert max(dem) == 88, f"the column's maximum is {max(dem):.0f}, not the 88 the key states"
    assert max(dem) < 100, "the column reaches complete alignment"
    assert min(dem) > 50, f"a figure in the column is not a majority: {min(dem):.0f}"
    assert len(dem) == 4, f"{len(dem)} policy areas, not four"
    return (f"Democratic column {', '.join(f'{x:.0f}' for x in dem)} -- maximum "
            f"{max(dem):.0f}, so a remainder in every area")


def q28(t):
    """Each party's identifiers show a majority and a substantial minority."""
    labels = [r[0] for r in t["rows"]]
    lib, con, nei = _col(t, LIB_POS), _col(t, CON_POS), _col(t, NEITHER)
    for row in t["rows"]:
        assert sum(gc.num(c) for c in row[1:]) == 100, f"row {row[0]!r} does not total 100"
    d, r = labels.index("Democratic identifiers"), labels.index("Republican identifiers")
    assert lib[d] > 50 and con[r] > 50, "a party's identifiers lack a majority on its position"
    assert 100 - lib[d] >= 30 and 100 - con[r] >= 30, \
        "the minority holding something else is not substantial in both parties"
    ind = labels.index("Independents")
    assert lib[ind] < lib[d], "independents hold the liberal position more often than Democrats"
    return (f"Democratic identifiers {lib[d]:.0f} percent with a {100 - lib[d]:.0f} percent "
            f"remainder; Republican identifiers {con[r]:.0f} percent with "
            f"{100 - con[r]:.0f} percent; rows total 100")


def q29(t):
    """The table measures persons, which is a different subject from platforms."""
    heads = [h.lower() for h in t["headers"]]
    assert any("held" in h for h in heads), f"no column measures what respondents held: {heads}"
    for h in heads:
        assert "platform" not in h and "plank" not in h, \
            f"column {h!r} measures a platform, which is the other table's subject"
    labels = [r[0] for r in t["rows"]]
    assert all("identifiers" in l or l == "Independents" for l in labels), \
        f"a row is not a group of persons: {labels}"
    return "rows are groups of persons and no column measures a platform"


def q30(t):
    """The student's 21 percent figure is real; the inference is what fails."""
    labels = [r[0] for r in t["rows"]]
    d = labels.index("Democratic identifiers")
    con = _col(t, CON_POS)[d]
    assert con == 21, f"the figure is {con:.0f}, not the 21 the item names"
    assert con > 0, "no Democratic identifier holds the conservative position"
    assert con < 50, "the figure is a majority, which the key's last distractor denies"
    return (f"{con:.0f} percent of Democratic identifiers hold the conservative position -- "
            "a real figure about persons, and no evidence about platforms")


# --- module-specific content gates -------------------------------------------

_IDENTITY = (
    "democrats are liberals", "republicans are conservatives",
    "the democratic party is liberal", "the republican party is conservative",
    "every democrat", "every republican",
    "all democrats", "all republicans",
)


def _hedges(module):
    """PLATFORMS, GENERALLY and MORE CLOSELY all survive.

    KNOWN BLIND SPOT: the _IDENTITY scan is a bare substring match, so it fires
    on a NEGATED use as readily as on an assertion -- a key reading "not every
    Democratic platform takes that position" is refused even though it says
    exactly what the gate wants said. That is a false positive in the safe
    direction and it has been left alone deliberately: widening it to parse
    negation is how a gate stops gating, and this bank has paid for
    over-matching checkers repeatedly. Phrase the hedge positively ("a tendency
    across platforms rather than a rule about any one of them") instead.
    """
    bad = []
    for i, item in enumerate(module.QUESTIONS, 1):
        key = item["choices"][item["ans"]].lower()
        for phrase in _IDENTITY:
            if phrase in key:
                bad.append(f"q{i} key: states {phrase!r}. EK 4.7.A.1 says the parties' "
                           "PLATFORMS GENERALLY ALIGN MORE CLOSELY TO those positions -- a "
                           "claim about documents, about a tendency, and about closeness "
                           "rather than identity")
    q3 = module.QUESTIONS[2]
    if "platform" not in q3["choices"][q3["ans"]].lower():
        bad.append("q3: the key no longer identifies PLATFORMS as EK 4.7.A.1's subject")
    q5 = module.QUESTIONS[4]
    k5 = q5["choices"][q5["ans"]].lower()
    if "tendency" not in k5 or "every plank" not in k5:
        bad.append("q5: the key no longer records GENERALLY as a tendency short of every plank")
    q6 = module.QUESTIONS[5]
    k6 = q6["choices"][q6["ans"]].lower()
    if "comparison" not in k6 or "distinct" not in k6:
        bad.append("q6: the key no longer records ALIGN MORE CLOSELY TO as a comparison "
                   "between two distinct things rather than an identity")
    q7 = module.QUESTIONS[6]
    k7 = q7["choices"][q7["ans"]].lower()
    for word in ("platforms", "generally", "more closely"):
        if word not in k7:
            bad.append(f"q7: the correcting key has itself dropped EK 4.7.A.1's word "
                       f"{word!r}, which is the whole point of that item")
    if bad:
        print(f"FAIL {module.__name__} hedges")
        for b in bad:
            print("  -", b)
        raise SystemExit(1)
    print(f"OK  {module.__name__} hedges: PLATFORMS, GENERALLY and MORE CLOSELY all survive, "
          "and no key equates a party with an ideology or attributes a position to every "
          "member of one")


def _ideologies(module):
    """The framework's own descriptions of the ideologies are not swapped."""
    bad = []
    swaps = (
        (9, "more governmental regulation", "EK 4.9.A.1 gives MORE regulation to liberal "
                                            "ideologies"),
        (10, "fewer regulations", "EK 4.9.A.1 gives FEWER regulations to conservative "
                                 "ideologies"),
        (12, "assigns liberal ideologies more national involvement", "EK 4.10.A.1 gives MORE "
                                                                    "national involvement to "
                                                                    "liberal ideologies"),
        (13, "state responsibility is the expected republican one", "EK 4.10.A.2 gives LESS "
                                                                   "national involvement to "
                                                                   "conservative ideologies, "
                                                                   "which EK 4.7.A.1 pairs "
                                                                   "with Republican platforms"),
        (14, "little national or state involvement", "EK 4.10.A.3's libertarian position "
                                                    "restrains STATE government too"),
    )
    for n, clause, note in swaps:
        key = module.QUESTIONS[n - 1]["choices"][module.QUESTIONS[n - 1]["ans"]].lower()
        if clause not in key:
            bad.append(f"q{n}: the key no longer carries {clause!r}; {note}")
    # Conservative is FEWER, not LITTLE OR NO: that is the libertarian position.
    # The clause is attributed to the ideology named NEAREST BEFORE IT, not to
    # any ideology within a fixed window. A window reported item 11, whose key
    # correctly reads "Conservative ideologies favor fewer regulations, WHILE
    # libertarian ideologies favor little or no regulation..." -- the two are
    # contrasted in one sentence, which is what the item is for. Third time this
    # project has paid for a proximity check that could not tell attribution
    # from adjacency.
    for i, item in enumerate(module.QUESTIONS, 1):
        key = item["choices"][item["ans"]].lower()
        at = key.find("little or no regulation")
        if at < 0:
            continue
        cons, libt = key.rfind("conservative", 0, at), key.rfind("libertarian", 0, at)
        if cons > libt:
            bad.append(f"q{i} key: gives conservative ideologies the LITTLE OR NO "
                       "regulation position; EK 4.9.A.1 assigns that to libertarian "
                       "ideologies and gives conservative ideologies FEWER regulations")
    if bad:
        print(f"FAIL {module.__name__} ideologies")
        for b in bad:
            print("  -", b)
        raise SystemExit(1)
    print(f"OK  {module.__name__} ideologies: EK 4.9.A.1's and EK 4.10.A.1 to 3's own "
          "descriptions are not swapped, conservative stays FEWER rather than little or no, "
          "and the libertarian social position still restrains state government")


_VERDICTS = (
    "is better for the country", "is the correct position", "is the right position",
    "has the better argument", "is more reasonable", "is mistaken about",
    "is the more sensible", "is wrong to favor",
)
_MODERN = ("obama", "trump", "biden", "reagan", "clinton", "bush", "pelosi", "mcconnell",
           "obamacare", "affordable care act", "new deal", "great society")


def _no_partisanship(module):
    """No verdict on a party or an ideology, and no modern political figure or statute."""
    bad = []
    for i, item in enumerate(module.QUESTIONS, 1):
        key = item["choices"][item["ans"]].lower()
        stem = item["q"].lower()
        # An item asking what the framework does NOT state has a key that NAMES
        # the omitted claim. Item 23 is exactly that, and a flat scan reported
        # its correct key as a verdict -- the fourth over-match this build has
        # paid for. Naming a verdict as the thing the framework withholds is the
        # opposite of passing it.
        withholds = "not state" in stem or "does not state" in stem
        for v in _VERDICTS:
            if v in key and not withholds:
                bad.append(f"q{i} key: passes the verdict {v!r}. EK 4.7.A.1 is descriptive "
                           "throughout, and LO 4.7.A asks how party ideologies SHAPE POLICY "
                           "DEBATES -- a question about structure, not about who is right")
        strings = [item["q"], item["why"]] + list(item["choices"])
        t = item.get("table")
        if t:
            strings += t["headers"] + [c for r in t["rows"] for c in r]
        for s in strings:
            low = s.lower()
            for name in _MODERN:
                if re.search(rf"(?<![a-z]){re.escape(name)}(?![a-z])", low):
                    bad.append(f"q{i}: names {name!r}. This module names no politician, "
                               "administration or modern statute; the framework's statement is "
                               "about platforms and ideologies, and a named example here would "
                               "invite a verdict the CED does not offer")
    q23 = module.QUESTIONS[22]
    if "better for the country" not in q23["choices"][q23["ans"]].lower():
        bad.append("q23: the key no longer identifies the evaluative question as the thing EK "
                   "4.7.A.1 does not state")
    if bad:
        print(f"FAIL {module.__name__} partisanship")
        for b in bad:
            print("  -", b)
        raise SystemExit(1)
    print(f"OK  {module.__name__} partisanship: no key evaluates a party or an ideology, no "
          "politician or modern statute is named anywhere, and the item on the framework's "
          "own silence still records it")


ua.shape(v4_7)
ua.check(v4_7, ANCHORS, GROUNDING)
ua.notation(v4_7)
_hedges(v4_7)
_ideologies(v4_7)
_no_partisanship(v4_7)
gc.check(v4_7, arith={25: q25, 26: q26, 27: q27, 28: q28, 29: q29, 30: q30})
