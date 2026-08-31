"""Structural gate for AP U.S. Government 5.4 How and Why Political Parties
Change and Adapt.

gov345_check plus the four usgov_anchor helpers, plus three content gates.

  _two_claims   EK 5.4.A.1 makes TWO claims and the second is the one that
                vanishes. The first is about where public attention sits -- on
                the candidate's characteristics AND NOT ON THE PARTY. The second
                is a separate fact about institutional power: the role of parties
                in NOMINATING candidates HAS BEEN WEAKENED.

                A summary keeping only the first has described a change in
                VOTERS and missed a change in the INSTITUTION, which is what LO
                5.4.A is asking about. The two also take different evidence,
                which is why the first table measures public focus and item 27
                says outright that it cannot bear on the nominating claim.

                The direction of the second claim is fixed -- WEAKENED -- and it
                is one of the few places in this topic where the framework
                commits to a direction rather than listing influences. Reversing
                it is a clean falsehood that reads as a reasonable thing to say
                about parties, so the gate refuses a strengthened or unchanged
                nominating role in any key.

  _critical     EK 5.4.A.3.i's parenthesis defines a critical election as one in
                which there is a REALIGNMENT OF POLITICAL PARTY SUPPORT AMONG
                VOTERS. Not an important election, not a close one, not a
                high-turnout one. The everyday sense of "critical" is exactly
                the wrong one, which makes this the definition in Unit 5 most
                likely to be quietly replaced by a synonym. Item 15 supplies a
                close, high-turnout election with no realignment and asks; the
                gate pins the definition and refuses the substitutes.

  _no_named_campaign
                The CED's illustrative examples here are two named campaign
                technology operations from a single election year, marked NOT
                REQUIRED. Beyond the usual reason for refusing those, naming
                them would turn a topic about how parties operate into
                commentary on particular campaigns. The gate refuses any
                four-digit year from 1900 on and any real candidate surname.
"""
import re

import gov345_check as gc
import usgov_anchor as ua
import v5_4

ANCHORS = {
 1: "A public focus on the characteristics of the candidate and not on the party",
 2: "That the role of parties in nominating candidates has been weakened",
 3: "and evidence about one is not evidence about the other",
 4: "It has been weakened",
 5: "It illustrates the weakened role of parties in nominating candidates",
 6: "in which the public focus is on the candidate rather than the party",
 7: "including a weakening of the candidate recruitment and nomination role",
 8: "who in practice determines which candidates appear on a general election ballot",
 9: "Their policies and messaging",
 10: "rather than something the framework says always happens",
 11: "may adapt their policies and messaging to appeal to various demographic coalitions",
 12: "A combination of demographic groups whose support a party seeks to assemble",
 13: "Critical elections, campaign finance law, and changes in communication and data",
 14: "An election in which there is a realignment of political party support among voters",
 15: "because no realignment of political party support among voters occurred",
 16: "shape how a party organizes itself to do so",
 17: "Disseminate, control, and clarify political messages",
 18: "Disseminating, controlling, and clarifying them",
 19: "and EK 5.4.A.4 describes what parties use that technology for",
 20: "use of voter data management to control and clarify messages",
 21: "Which of the three influences has changed party structure most",
 22: "which is why parties persist while adapting rather than dissolving",
 23: "different degrees and forms of political division as circumstances change",
 24: "the framework locates the weakening specifically in the role of parties in nominating",
 25: "and the two crossed between the first and second cycles",
 26: "in which the public focus is on the characteristics of the candidate and not on the",
 27: "and none measures who controls nominations",
 28: "is also the group with the most planks addressing it in the later platform",
 29: "may adapt their policies and messaging to appeal to various demographic coalitions",
 30: "so it cannot show whether the platform followed the coalition or helped produce it",
}

GROUNDING = {
 1: "EK 5.4.A.1's first sentence: parties have adapted to candidate-centered campaigns 'where "
    "the public focus is on the characteristics of the candidate and not on the party.'",
 2: "EK 5.4.A.1's second sentence: 'The role of parties in nominating candidates has also been "
    "weakened.' A claim about institutional power, not about public attention.",
 3: "EK 5.4.A.1's two claims read apart. A survey of voter attention bears on the first and "
    "says nothing about who controls nominations.",
 4: "EK 5.4.A.1's own word WEAKENED, one of the few directions the framework commits to in "
    "this topic.",
 5: "EK 5.4.A.1's second claim applied to a nomination decided against the organization's "
    "preference. EK 5.8.A.1.ii names open and closed primaries among the processes involved.",
 6: "EK 5.4.A.1's first claim applied. Running under a label does not make a campaign "
    "party-centered; the framework's test is where the public focus sits.",
 7: "EK 5.3.B.1's list of party functions against EK 5.4.A.1. The functions remain; the "
    "conditions under which parties perform them have changed.",
 8: "EK 5.4.A.1's second claim and what would count as evidence for it, against four measures "
    "of public attention or attachment that bear on the first.",
 9: "EK 5.4.A.2, verbatim: parties 'may adapt their policies and messaging'. Both are things "
    "the party controls, unlike the election rules EK 5.2.A.2 assigns to states.",
 10: "EK 5.4.A.2's modal MAY, which states a possibility rather than a regularity.",
 11: "EK 5.4.A.2 applied to a scenario changing both policies and messaging for a demographic "
     "group.",
 12: "EK 5.4.A.2's term read in context: the combination of groups a party seeks to hold "
     "together, which is what its policies and messaging are aimed at.",
 13: "EK 5.4.A.3's three influences on the STRUCTURE of parties, as distinct from EK 5.3.B.1's "
     "functions.",
 14: "EK 5.4.A.3.i's parenthesis, verbatim: 'elections in which there is a realignment of "
     "political party support among voters.'",
 15: "EK 5.4.A.3.i's definition applied to an election with no realignment. Margin and turnout "
     "are not part of the framework's definition.",
 16: "EK 5.4.A.3.ii read against the statement's subject, party STRUCTURE: the law governing "
     "fundraising is a constraint an organization builds itself around. Topic 5.11 takes up "
     "campaign finance in its own right.",
 17: "EK 5.4.A.4, verbatim: parties use these tools 'to disseminate, control, and clarify "
     "political messages and enhance outreach and mobilization efforts.'",
 18: "EK 5.4.A.4's three verbs for messages. CONTROL is the one most easily lost, and it is "
     "what distinguishes managing a message from merely sending it.",
 19: "EK 5.4.A.3.iii against EK 5.4.A.4: one gives technology as a cause of structural change, "
     "the other gives the uses parties put it to.",
 20: "EK 5.4.A.4's voter data management and EK 5.4.A.2's adaptation of messaging, describing "
     "one investment from two angles.",
 21: "EK 5.4.A.3 read for what it omits: three influences listed, none ranked.",
 22: "Federalist No. 10 (required document), quoted verbatim; the CED attaches it to 5.4.A. "
     "Madison locates division into parties in a zeal for different opinions, a standing "
     "condition rather than a passing one.",
 23: "Federalist No. 10, quoted verbatim. The clause ties the ACTIVITY of the causes to "
     "changing circumstances while the causes stay constant, which answers LO 5.4.A's WHY.",
 24: "CED skill 4.B: how a source's argument relates to the framework. This one overlaps with "
     "EK 5.4.A.1's first sentence and infers what the framework states separately in its "
     "second.",
 25: "Data item, CED skill 4.B. Both columns and the crossing point are recomputed below.",
 26: "EK 5.4.A.1's first claim located in a table whose columns all measure voter attention.",
 27: "EK 5.4.A.1's two claims against a table that measures only the first. Recomputed below.",
 28: "Data item, CED skill 4.B. Every coalition share and plank count is recomputed below.",
 29: "EK 5.4.A.2 located in a table pairing a changing coalition with platform content. Planks "
     "are policies and messaging in the framework's sense.",
 30: "CED skill 4.B: the evidence is compatible with the claim running either way, which is "
     "recomputed below as the absence of any ordering column.",
}

CAND, PARTY, BOTH = ("Candidate characteristics mattered more (%)", "Party label mattered more (%)",
                     "Both mattered equally (%)")
EARLY, LATE, PLANKS = ("Share of the party's voters, earlier cycle (%)",
                       "Share of the party's voters, later cycle (%)",
                       "Planks addressing the group in the later platform")
GROUP = "Demographic group"


def _col(t, header):
    j = t["headers"].index(header)
    return [r[j] for r in t["rows"]]


def _num(t, header):
    return [gc.num(c) for c in _col(t, header)]


def q25(t):
    """Candidate column rises, party column falls, crossing after the first cycle."""
    cand, party, both = _num(t, CAND), _num(t, PARTY), _num(t, BOTH)
    for row in t["rows"]:
        assert sum(gc.num(c) for c in row[1:]) == 100, f"row {row[0]!r} does not total 100"
    assert cand == sorted(cand) and len(set(cand)) == len(cand), f"candidate column {cand}"
    assert party == sorted(party, reverse=True), f"party column {party}"
    crossings = [i for i in range(len(cand) - 1)
                 if cand[i] < party[i] and cand[i + 1] > party[i + 1]]
    assert crossings == [0], f"the columns cross after row index {crossings}, not the first"
    assert max(both) - min(both) <= 2, f"the both-equally column moves: {both}"
    return (f"candidate {', '.join(f'{x:.0f}' for x in cand)}; party "
            f"{', '.join(f'{x:.0f}' for x in party)}; crossing after cycle 1; both-equally "
            f"steady between {min(both):.0f} and {max(both):.0f}")


def q26(t):
    """Every column measures voter attention."""
    heads = [h.lower() for h in t["headers"]]
    assert all("mattered" in h for h in heads[1:]), \
        f"a column does not measure what mattered to voters: {heads}"
    for h in heads:
        for nom in ("nomination", "nominating", "primary", "ballot access"):
            assert nom not in h, f"column {h!r} measures nominations, not public focus"
    return "all three data columns measure what voters said mattered to their choice"


def q27(t):
    """No column bears on who controls nominations."""
    heads = [h.lower() for h in t["headers"]]
    for h in heads:
        for nom in ("nomination", "nominating", "who controls", "party organization"):
            assert nom not in h, \
                f"column {h!r} bears on nominations, so the stated limitation would fail"
    assert len(t["rows"]) == 4, f"{len(t['rows'])} cycles, not four"
    return f"columns are {', '.join(heads)} -- voter attention only, across {len(t['rows'])} cycles"


def _changes(t):
    early, late = _num(t, EARLY), _num(t, LATE)
    return dict(zip(_col(t, GROUP), (b - a for a, b in zip(early, late))))


def q28(t):
    """The biggest gainer carries the most planks; the biggest loser the fewest."""
    changes = _changes(t)
    planks = dict(zip(_col(t, GROUP), _num(t, PLANKS)))
    gainer = max(changes, key=lambda k: changes[k])
    loser = min(changes, key=lambda k: changes[k])
    assert planks[gainer] == max(planks.values()), \
        f"the biggest gainer {gainer!r} does not carry the most planks"
    assert planks[loser] == min(planks.values()), \
        f"the biggest loser {loser!r} does not carry the fewest planks"
    assert sum(_num(t, EARLY)) == 100 and sum(_num(t, LATE)) == 100, "a coalition column is not 100"
    assert any(v > 0 for v in changes.values()) and any(v < 0 for v in changes.values()), \
        "the coalition moves in only one direction, which the key's third distractor denies"
    assert len(set(planks.values())) == len(planks), "two groups carry equal plank counts"
    return ("changes " + ", ".join(f"{k.split()[1]} {v:+.0f}" for k, v in changes.items())
            + f"; planks {', '.join(f'{v:.0f}' for v in planks.values())}")


def q29(t):
    """The table pairs coalition composition with platform content."""
    heads = [h.lower() for h in t["headers"]]
    assert any("plank" in h for h in heads), f"no platform column: {heads}"
    assert sum(1 for h in heads if "share of the party's voters" in h) == 2, \
        f"the two coalition columns are not both present: {heads}"
    return "two coalition columns beside a platform plank count"


def q30(t):
    """Nothing in the table orders the shift against the platform."""
    heads = [h.lower() for h in t["headers"]]
    for h in heads:
        for order in ("date", "adopted", "before", "after", "first", "month"):
            assert order not in h, \
                f"column {h!r} would order the two, weakening the stated limitation"
    assert sum(1 for h in heads if "plank" in h) == 1, \
        "there is more than one platform column, which could establish an ordering"
    return "no column dates or orders the coalition shift against the platform"


# --- module-specific content gates -------------------------------------------

_NOMINATION_REVERSED = (
    "nominating candidates has been strengthened",
    "nominating candidates has been unchanged",
    "strengthened party role in nominations",
    "parties control all nominations",
    "parties now determine every nomination",
)


def _two_claims(module):
    """EK 5.4.A.1's two claims stay two, and the nominating role stays WEAKENED."""
    bad = []
    for i, item in enumerate(module.QUESTIONS, 1):
        key = item["choices"][item["ans"]].lower()
        stem = item["q"].lower()
        refusing = "not state" in stem or "contradicts" in key or "correction" in stem
        for r in _NOMINATION_REVERSED:
            if r in key and not refusing:
                bad.append(f"q{i} key: reverses EK 5.4.A.1's second claim ({r!r}); the "
                           "framework says the role of parties in nominating candidates has "
                           "been WEAKENED")
    q1 = module.QUESTIONS[0]
    k1 = q1["choices"][q1["ans"]].lower()
    if "not on the party" not in k1:
        bad.append("q1: the key no longer carries both halves of EK 5.4.A.1's first claim -- "
                   "focus ON the candidate's characteristics AND NOT ON the party")
    for n in (2, 4):
        key = module.QUESTIONS[n - 1]["choices"][module.QUESTIONS[n - 1]["ans"]].lower()
        if "weakened" not in key:
            bad.append(f"q{n}: the key no longer carries EK 5.4.A.1's word WEAKENED")
    nominating = sum(1 for item in module.QUESTIONS
                     if "nominat" in item["choices"][item["ans"]].lower())
    if nominating < 4:
        bad.append(f"only {nominating} keys turn on the nominating claim; it is half of EK "
                   "5.4.A.1 and the half a summary drops, so a module that lets it go has "
                   "described a change in voters and missed the change in the institution")
    if bad:
        print(f"FAIL {module.__name__} two claims")
        for b in bad:
            print("  -", b)
        raise SystemExit(1)
    print(f"OK  {module.__name__} two claims: EK 5.4.A.1's candidate-centered claim keeps both "
          f"halves, the nominating role stays WEAKENED, and {nominating} keys turn on the "
          "second claim")


_NOT_CRITICAL = (
    "an election decided by a very small margin",
    "an election in which turnout is unusually high",
    "an especially important election",
    "an election that determines control",
)


def _critical(module):
    """A critical election is defined by realignment, not by importance or closeness."""
    bad = []
    for i, item in enumerate(module.QUESTIONS, 1):
        key = item["choices"][item["ans"]].lower()
        stem = item["q"].lower()
        if "critical election" not in key and "critical election" not in stem:
            continue
        refusing = "no realignment" in key or "not" in key
        for n in _NOT_CRITICAL:
            if n in key and not refusing:
                bad.append(f"q{i} key: defines a critical election as {n!r}; EK 5.4.A.3.i says "
                           "an election in which there is a REALIGNMENT of political party "
                           "support among voters")
    q14 = module.QUESTIONS[13]
    if "realignment" not in q14["choices"][q14["ans"]].lower():
        bad.append("q14: the key no longer carries EK 5.4.A.3.i's parenthetical definition, a "
                   "realignment of political party support among voters")
    q15 = module.QUESTIONS[14]
    if "realignment" not in q15["choices"][q15["ans"]].lower():
        bad.append("q15: the key no longer turns on the absence of a realignment, which is the "
                   "only thing that decides the question the item asks")
    if bad:
        print(f"FAIL {module.__name__} critical elections")
        for b in bad:
            print("  -", b)
        raise SystemExit(1)
    print(f"OK  {module.__name__} critical elections: EK 5.4.A.3.i's realignment definition "
          "survives, and no key substitutes closeness, turnout or importance for it")


_YEAR = re.compile(r"(?<![0-9])(19[0-9]{2}|20[0-9]{2})(?![0-9])")
_SURNAMES = ("romney", "obama", "trump", "clinton", "biden", "bush", "reagan", "carter",
             "mccain", "kerry", "gore")
_ALLOWED_YEARS = {"1787"}


def _no_named_campaign(module):
    """No modern campaign, candidate or year: the CED's examples here are NOT REQUIRED."""
    bad = []
    for i, item in enumerate(module.QUESTIONS, 1):
        strings = [("stem", item["q"]), ("why", item["why"])]
        strings += [(f"choice {'ABCDE'[k]}", c) for k, c in enumerate(item["choices"])]
        t = item.get("table")
        if t:
            strings += [("table header", h) for h in t["headers"]]
            strings += [("table cell", c) for r in t["rows"] for c in r]
        for label, s in strings:
            for m in _YEAR.finditer(s):
                if m.group(0) not in _ALLOWED_YEARS:
                    bad.append(f"q{i} {label}: names the year {m.group(0)}. The CED's "
                               "illustrative examples for 5.4 are two campaign operations from "
                               "one election year, marked NOT REQUIRED")
            low = s.lower()
            for name in _SURNAMES:
                if re.search(rf"(?<![a-z]){name}(?![a-z])", low):
                    bad.append(f"q{i} {label}: names {name!r}. Naming a campaign here would "
                               "turn a topic about how parties operate into commentary on "
                               "particular campaigns")
    if bad:
        print(f"FAIL {module.__name__} named campaign")
        for b in bad:
            print("  -", b)
        raise SystemExit(1)
    print(f"OK  {module.__name__} named campaign: no modern candidate, campaign or year is "
          "named anywhere in the module (1787 excepted, for the Federalist quotations)")


ua.shape(v5_4)
ua.check(v5_4, ANCHORS, GROUNDING)
ua.notation(v5_4)
_two_claims(v5_4)
_critical(v5_4)
_no_named_campaign(v5_4)
gc.check(v5_4, arith={25: q25, 26: q26, 27: q27, 28: q28, 29: q29, 30: q30})
