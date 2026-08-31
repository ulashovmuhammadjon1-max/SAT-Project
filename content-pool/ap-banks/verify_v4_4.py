"""Structural gate for AP U.S. Government 4.4 Influence of Political Events on
Ideology.

gov345_check plus the four usgov_anchor helpers, plus three content gates.

  _chain        EK 4.4.A.1 states a three-link chain with a named middle:

                    events -> individual political attitudes -> ideology
                              (= political socialization)

                and the middle link is precisely what a summary deletes. "Major
                events shape ideology" is the sentence everyone writes and it
                skips the step the framework troubled to name. Keeping it has
                two consequences the module is built on: the route runs THROUGH
                A PERSON, and ideology is DOWNSTREAM and therefore slower than
                the attitudes an event moves. The gate refuses any key that
                reverses the order or routes an event to ideology directly.

  _modal        The framework's verb is CAN INFLUENCE, not determines. It names
                no event, no attitude and no resulting ideology. A key asserting
                that events produce a particular attitude, or produce the same
                attitude in everyone, would state more than the sentence does --
                and would do it in the one topic where a reader's own political
                memory supplies the missing content automatically.

  _no_fabricated_source
                This is the gate that matters most here, and it is unusual
                enough to be worth stating plainly. The suggested skill is 4.B,
                SOURCE ANALYSIS -- but the CED attaches no foundational document
                and no required case to 4.4.A. Every other source-analysis topic
                in this bank quotes the document the framework itself supplies;
                here there is nothing to quote. SOCIAL_BRIEF.md says to quote
                accurately or DESCRIBE INSTEAD and never to invent a quotation,
                so items 13 to 18 state each argument in the third person and
                attribute it to no one.

                A fabricated quotation is the single failure in this bank that
                nothing downstream could ever catch, because an invented source
                reads exactly like a real one -- there is no round trip, no
                recomputation and no CED sentence to check it against. So the
                gate is mechanical: no attributed quotation may appear anywhere
                in this module. It looks for the em-dash attribution line that
                every real quoted stem in this bank uses, and refuses it here.
"""
import re

import gov345_check as gc
import usgov_anchor as ua
import v4_4

ANCHORS = {
 1: "The development of individual political attitudes",
 2: "Political socialization",
 3: "Political ideology",
 4: "and that process of socialization in turn influences political ideology",
 5: "so an event acts on attitudes and reaches ideology only through the process",
 6: "The intermediate step, in which events influence individual attitudes",
 7: "By identifying the influence of events on attitudes as an example of the political",
 8: "that movement is a case of political socialization, and socialization in turn bears",
 9: "That such influence is possible rather than guaranteed in every case",
 10: "without saying which attitudes result",
 11: "which is EK 4.3.A.1's definition of a generational effect",
 12: "and those views shape a broader outlook over time",
 13: "It disputes the relative weight of contributors the framework lists without ranking",
 14: "since the argument turns on attitudes formed earlier persisting",
 15: "requires measurement well after the event, since ideology sits downstream",
 16: "not that they produce a uniform attitude",
 17: "since framing reaches people through what they read and hear",
 18: "which the framework itself does not define",
 19: "Which attitudes a major political event produces",
 20: "everything the framework says about how socialization works applies to events",
 21: "before the event and again well afterward",
 22: "which is a process rather than an immediate transfer",
 23: "later hold a broader political outlook different from those who did not",
 24: "without naming any event, any attitude, or any resulting ideology",
 25: "highest among those who were 18 to 25 when it occurred",
 26: "can influence the development of individual political attitudes, which is an example",
 27: "which is a smaller share than in other groups but is not none",
 28: "while the general view of how much government should do moved by 2",
 29: "with ideology reached later through political socialization rather than at once",
 30: "and the framework routes events to ideology through the development of attitudes",
}

GROUNDING = {
 1: "EK 4.4.A.1, verbatim: 'Major political events can influence the development of individual "
    "political attitudes.' The object is a person's attitudes, not an institution.",
 2: "EK 4.4.A.1's own clause, 'which is an example of political socialization', placing events "
    "inside the process EK 4.2.A.1 defines rather than in a separate category.",
 3: "EK 4.4.A.1's second sentence: 'Political socialization, in turn, influences political "
    "ideology.' The phrase IN TURN is what makes the statement a chain.",
 4: "EK 4.4.A.1's full order: events, attitudes (named as socialization), ideology. Each "
    "distractor reverses at least one link.",
 5: "EK 4.4.A.1's middle term read for what it does: the route runs through a person, and EK "
    "4.2.A.1 describes that development as a process running over time.",
 6: "EK 4.4.A.1 against the summary that skips its middle link. The summary is not false; it "
    "omits the step the framework named.",
 7: "EK 4.4.A.1's clause 'an example of political socialization', which subordinates this "
    "topic to EK 4.2.A.1 rather than competing with it.",
 8: "Both sentences of EK 4.4.A.1 restated with all three links and the modal verb intact.",
 9: "EK 4.4.A.1's modal verb CAN, which claims possibility rather than necessity.",
 10: "EK 4.4.A.1 names no attitude and no direction of change, so divergent conclusions from "
     "one event are consistent with its claim.",
 11: "EK 4.3.A.1's definition of a generational effect -- experiences shared by people of a "
     "common age -- applied to a major political event, with EK 4.4.A.1 supplying the route.",
 12: "EK 4.4.A.1's whole chain in one example: an event, a change in an individual's "
     "attitudes, and a broader outlook shaped over time.",
 13: "CED skill 4.B on a described argument. EK 4.2.A.1 names five contributors and EK 4.4.A.1 "
     "adds events as an example of the same process; neither ranks them, so an argument about "
     "relative weight goes beyond the framework rather than contradicting it.",
 14: "CED skill 4.B. EK 4.4.A.1 identifies the influence of events as political socialization "
     "and routes it to ideology, so a delay between event and effect is that process in time.",
 15: "CED skill 4.B. EK 4.4.A.1 places ideology at the end of a chain running through the "
     "development of attitudes, so a momentary movement is not yet evidence about that end.",
 16: "CED skill 4.B. The argument requires the framework to have claimed uniformity; EK "
     "4.4.A.1's verb is CAN INFLUENCE and it names no resulting attitude.",
 17: "CED skill 4.B. EK 4.2.A.1 names media among the contributors to political socialization, "
     "and EK 4.4.A.1 makes the influence of events an example of that process.",
 18: "CED skill 4.B. EK 4.4.A.1 uses MAJOR POLITICAL EVENTS without defining what makes an "
     "event major, so a criterion supplied by an argument is an addition to the framework.",
 19: "EK 4.4.A.1 read for what it omits. Every other option restates part of its two "
     "sentences.",
 20: "EK 4.4.A.1's word EXAMPLE, which places events inside a category, so EK 4.2.A.1's "
     "account of the process governs them too.",
 21: "EK 4.4.A.1's chain ending in ideology, a broader outlook, reached through a process of "
     "development -- which is what dictates measuring the same people across time.",
 22: "EK 4.4.A.1's middle term, the DEVELOPMENT of attitudes, against a reading in which every "
     "event transmits to ideology immediately.",
 23: "LO 4.4.A's object, how major political events influence political ideology, with EK "
     "4.4.A.1 routing that influence through individuals.",
 24: "EK 4.4.A.1's two sentences read as a mechanism and nothing more: no names, no "
     "magnitudes, no ranking.",
 25: "Data item, CED skill 4.B. The shape of the important column is recomputed below.",
 26: "EK 4.4.A.1's claim shown as data: respondents attributing part of their outlook to an "
     "event. The framework does not say socialization is completed at any age.",
 27: "Data item: reading the smallest share in a column as zero. Recomputed below, with EK "
     "4.4.A.1's modal verb CAN INFLUENCE rather than always influences.",
 28: "Data item, CED skill 4.B. All four movements are recomputed below.",
 29: "EK 4.4.A.1's first link located in the sharply moving rows, and its downstream end in "
     "the barely moving one.",
 30: "EK 4.4.A.1's chain against a claim that an event changed an ideology. The general row's "
     "movement is recomputed below.",
}

IMPORTANT, UNIMPORTANT = ("Called it important to their outlook (%)",
                          "Called it unimportant to their outlook (%)")
BEFORE, AFTER = "Before the event (%)", "After the event (%)"


def _rows(t):
    return [(r[0], [gc.num(c) for c in r[1:]]) for r in t["rows"]]


def _col(t, header):
    j = t["headers"].index(header)
    return [gc.num(r[j]) for r in t["rows"]]


def q25(t):
    """The important column peaks in the middle rather than running monotonically."""
    imp = _col(t, IMPORTANT)
    labels = [r[0] for r in t["rows"]]
    peak = imp.index(max(imp))
    assert labels[peak] == "Ages 18 to 25", f"the peak is on {labels[peak]!r}"
    assert imp.index(min(imp)) == 0, f"the minimum is not the first row: {imp}"
    assert imp != sorted(imp) and imp != sorted(imp, reverse=True), \
        f"the column is monotonic, so the key's second and third distractors would be true: {imp}"
    for r in t["rows"]:
        assert gc.num(r[1]) + gc.num(r[2]) == 100, f"row {r[0]!r} does not total 100"
    return (f"important column {', '.join(f'{x:.0f}' for x in imp)} -- peaks at "
            f"{labels[peak]!r}, lowest at {labels[0]!r}; every row totals 100")


def q26(t):
    """Every row reports a nonzero share, so the table shows influence rather than none."""
    imp = _col(t, IMPORTANT)
    assert all(x > 0 for x in imp), f"a row reports zero: {imp}"
    assert len(t["rows"]) == 5, f"{len(t['rows'])} age brackets, not five"
    assert len(set(r[0] for r in t["rows"])) == 5, "an age bracket is repeated"
    return f"five brackets, all reporting a nonzero share: {', '.join(f'{x:.0f}' for x in imp)}"


def q27(t):
    """The over-40 row is 29 percent: the second lowest, not zero."""
    row = [r for r in t["rows"] if r[0] == "Over 40"]
    assert len(row) == 1, "the over 40 row is missing or duplicated"
    imp = gc.num(row[0][1])
    assert imp == 29, f"the over 40 row reads {imp:.0f}, not the 29 the key states"
    col = sorted(_col(t, IMPORTANT))
    assert col.index(imp) == 1, f"29 is not the second lowest value in {col}"
    return f"over 40 row at {imp:.0f} percent -- second lowest of {len(col)}, and not zero"


def _moves(t):
    b, a = _col(t, BEFORE), _col(t, AFTER)
    return {r[0]: y - x for r, x, y in zip(t["rows"], b, a)}


def q28(t):
    """Three rows move more than 20 points; the general row moves 2."""
    moves = _moves(t)
    general = [k for k in moves if k.startswith("General view")]
    assert len(general) == 1, "the general view row is missing or duplicated"
    g = moves[general[0]]
    others = [v for k, v in moves.items() if k != general[0]]
    assert g == 2, f"the general view moved {g:.0f}, not the 2 the key states"
    assert all(v > 20 for v in others), f"an issue-specific view moved {min(others):.0f} points"
    assert all(v > 0 for v in moves.values()), "a view moved downward"
    return ("movements " + ", ".join(f"{k.split()[0]} {v:+.0f}" for k, v in moves.items())
            + f" -- general {g:+.0f} against a minimum of {min(others):+.0f} elsewhere")


def q29(t):
    """The general row is the smallest mover, which is what puts it at the chain's far end."""
    moves = _moves(t)
    smallest = min(moves, key=lambda k: moves[k])
    assert smallest.startswith("General view"), f"the smallest mover is {smallest!r}"
    return (f"smallest movement is {smallest!r} at {moves[smallest]:+.0f} points, the row "
            "closest to a broader outlook")


def q30(t):
    """The general row moved 2 points against issue-specific movements above 20."""
    moves = _moves(t)
    general = [k for k in moves if k.startswith("General view")][0]
    others = [v for k, v in moves.items() if k != general]
    assert moves[general] == 2, f"the general view moved {moves[general]:.0f}, not 2"
    assert min(others) >= 21, f"an issue-specific view moved only {min(others):.0f}"
    return (f"general view {moves[general]:+.0f} points against issue-specific movements of at "
            f"least {min(others):+.0f}")


# --- module-specific content gates -------------------------------------------

_REVERSALS = (
    "political ideology influences political socialization",
    "ideology influences major political events",
    "socialization influences major political events",
    "ideology, which in turn produces attitudes",
    "major political events influence political ideology, which in turn",
)
_DIRECT = (
    "events act directly on ideology",
    "events change ideology directly",
    "events reach ideology without",
)


def _chain(module):
    """EK 4.4.A.1's three links keep their order and their middle."""
    bad = []
    for i, item in enumerate(module.QUESTIONS, 1):
        key = item["choices"][item["ans"]].lower()
        for r in _REVERSALS:
            if r in key:
                bad.append(f"q{i} key: reverses EK 4.4.A.1's chain ({r!r}); the framework runs "
                           "events -> individual attitudes (political socialization) -> "
                           "political ideology")
        for d in _DIRECT:
            if d in key:
                bad.append(f"q{i} key: routes an event to ideology directly ({d!r}); EK "
                           "4.4.A.1 places the development of individual attitudes between "
                           "them and names it political socialization")
    q4 = module.QUESTIONS[3]
    k4 = q4["choices"][q4["ans"]].lower()
    for link in ("major political events", "individual attitudes", "socialization",
                 "political ideology"):
        if link not in k4:
            bad.append(f"q4: the key has dropped {link!r} from EK 4.4.A.1's chain")
    q2 = module.QUESTIONS[1]
    if "political socialization" not in q2["choices"][q2["ans"]].lower():
        bad.append("q2: the key no longer names the middle link, political socialization")
    if bad:
        print(f"FAIL {module.__name__} chain")
        for b in bad:
            print("  -", b)
        raise SystemExit(1)
    print(f"OK  {module.__name__} chain: no key reverses EK 4.4.A.1's order or routes an event "
          "to ideology directly, and all three links survive in the item that states them")


_DETERMINISM = (
    "occurs in every case without exception",
    "produces the same attitude in everyone",
    "determines a person's ideology immediately",
    "events always produce", "every major event changes",
    "everyone draws the same lesson",
)


def _modal(module):
    """EK 4.4.A.1's CAN INFLUENCE may not harden into a determination."""
    bad = []
    for i, item in enumerate(module.QUESTIONS, 1):
        key = item["choices"][item["ans"]].lower()
        for d in _DETERMINISM:
            if d in key:
                bad.append(f"q{i} key: states {d!r}. EK 4.4.A.1's verb is CAN INFLUENCE, and "
                           "the framework names no event, no attitude and no resulting "
                           "ideology")
    q9 = module.QUESTIONS[8]
    if "possible rather than guaranteed" not in q9["choices"][q9["ans"]].lower():
        bad.append("q9: the key no longer records EK 4.4.A.1's modal verb as a claim of "
                   "possibility rather than necessity")
    q19 = module.QUESTIONS[18]
    if "which attitudes" not in q19["choices"][q19["ans"]].lower():
        bad.append("q19: the key no longer identifies the resulting attitude as the thing EK "
                   "4.4.A.1 does not state")
    if bad:
        print(f"FAIL {module.__name__} modal")
        for b in bad:
            print("  -", b)
        raise SystemExit(1)
    print(f"OK  {module.__name__} modal: EK 4.4.A.1's CAN INFLUENCE stays a possibility claim, "
          "and no key names an attitude the framework leaves unnamed")


# Every genuinely quoted stem in this bank uses the same shape: a quotation
# followed by an em-dash attribution line. 4.4 has no document to quote, so the
# shape must not appear here at all.
_ATTRIBUTION = re.compile(r"^\s*[—-]\s*\S", re.MULTILINE)
_QUOTED = re.compile(r"[“”\"]")


def _no_fabricated_source(module):
    """No attributed quotation may appear: 4.4 has no required source to quote."""
    bad = []
    for i, item in enumerate(module.QUESTIONS, 1):
        strings = [("stem", item["q"]), ("why", item["why"])]
        strings += [(f"choice {'ABCDE'[k]}", c) for k, c in enumerate(item["choices"])]
        for label, s in strings:
            if _ATTRIBUTION.search(s) and _QUOTED.search(s):
                bad.append(f"q{i} {label}: carries a quotation with an attribution line. The "
                           "CED attaches no foundational document and no required case to "
                           "4.4.A, so there is nothing here to quote. SOCIAL_BRIEF.md's rule "
                           "is quote accurately or DESCRIBE INSTEAD -- and an invented source "
                           "is the one defect in this bank that nothing downstream could "
                           "catch, because it reads exactly like a real one")
    described = sum(1 for item in module.QUESTIONS
                    if item["q"].lower().startswith("a commentator argues"))
    if described < 4:
        bad.append(f"only {described} items state a described argument; the suggested skill "
                   "for this topic is 4.B, source analysis, and described arguments are how "
                   "this module supplies sources without a document to quote")
    if bad:
        print(f"FAIL {module.__name__} sources")
        for b in bad:
            print("  -", b)
        raise SystemExit(1)
    print(f"OK  {module.__name__} sources: no attributed quotation anywhere, and {described} "
          "items carry a described argument for skill 4.B -- the CED attaches no document to "
          "4.4.A, so nothing here is quoted")


ua.shape(v4_4)
ua.check(v4_4, ANCHORS, GROUNDING)
ua.notation(v4_4)
_chain(v4_4)
_modal(v4_4)
_no_fabricated_source(v4_4)
gc.check(v4_4, arith={25: q25, 26: q26, 27: q27, 28: q28, 29: q29, 30: q30})
