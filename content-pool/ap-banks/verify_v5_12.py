"""Structural gate for AP U.S. Government 5.12 The Media.

gov345_check plus the four usgov_anchor helpers, plus two content gates and a
negative control for each.

  _modal  EK 5.12.A.2's verb is CAN AFFECT. The framework says the media's use
          of polling results CAN AFFECT elections by turning them into horse
          races; it does not say that it does, that it decides an outcome, or
          that it is harmless. This is the single most likely place for an
          author to drift, because public commentary on horse race coverage is
          confident in both directions and the framework is confident in
          neither.

          So the gate refuses any key that upgrades the modal to a certainty --
          determines, decides, guarantees, causes, always, never -- and it
          requires items 11 and 30, whose whole point is the modal, to keep the
          possibility language. It also requires the key that states what horse
          race coverage displaces to keep BOTH of the framework's nouns,
          qualifications AND platforms, since dropping one leaves a different
          claim that reads just as well.

  _agenda The course defines agenda setting twice and the definitions differ.
          EK 2.7.A.1.ii makes it a president's influence over WHICH POLICIES the
          public sees as most important; EK 5.12.A.1 makes it media influence
          over HOW CITIZENS ROUTINELY ACQUIRE POLITICAL INFORMATION. An author
          reaching for the familiar definition answers topic 2.7's question
          under this topic's code, and nothing structural would notice.

          So the gate requires every key that defines agenda setting to name the
          acquisition of information, and it refuses any key defining it as
          telling citizens what to think or which policies matter most.

THE ARITHMETIC
--------------
Items 25 to 27 share a hypothetical survey of how respondents encounter each of
EK 5.12.A.1's four kinds of political information; items 28 to 30 share a
hypothetical study of one broadcaster's election coverage over four periods.

Both tables are HYPOTHETICAL and labelled so in the stems. Neither asserts
anything about a real survey, outlet or election.

Item 27 is the rebuttal brake and item 28 the direction brake. Item 27's key is
true only because traditional news media leads in exactly three rows and in the
two rows with the widest weekly reach; item 28's key is true only because the
poll column rises at every step while both other columns fall and the poll
column leads in exactly one period. Move one figure and each item still READS
correctly and is no longer true, so both are recomputed from the table.

The route columns are also required to sum to the weekly column in every row,
because the survey's own design says they should: the two routes partition the
respondents who encounter the category at all. A table whose parts do not sum to
its whole is incoherent in a way no reader would catch.

NEGATIVE CONTROLS
-----------------
Every gate below is run against a deliberately corrupted copy and must fail. A
checker that cannot fail is worse than none. The controls corrupt: a key
upgrading the modal to a certainty, a key that drops one of the framework's two
displaced nouns, a key defining agenda setting as telling citizens what to
think, a survey figure that makes item 27's rebuttal false, and a coverage
figure that breaks item 28's direction claim.
"""
import contextlib
import io
import types

import gov345_check as gc
import usgov_anchor as ua
import v5_12

ANCHORS = {
 1: "How citizens routinely acquire political information",
 2: "Traditional news media, new communication technologies, and advances in social media",
 3: "News events, investigative journalism, election coverage, and political commentary",
 4: "the ordinary repeated ways information is acquired",
 5: "not about what conclusions they reach from it",
 6: "here the media are the actor and the object is how citizens acquire information",
 7: "so the media's role runs toward citizens as well as toward policymakers",
 8: "Popular levels of trust and confidence in government",
 9: "Horse races",
 10: "Popularity and factors other than the qualifications and platforms of candidates",
 11: "which states a possibility rather than a settled outcome",
 12: "Their qualifications and their platforms",
 13: "on the media's use of polling results turning elections into horse races",
 14: "Investigative journalism",
 15: "Political commentary",
 16: "Respond to opposing or alternate perspectives with rebuttal or refutation",
 17: "takes up the evidence against it and explains why the claim is still the better one",
 18: "the framework's concern is the displacement of qualifications and platforms",
 19: "acquiring is something a citizen does rather than something done to a citizen",
 20: "explains why the claim remains the better position",
 21: "The choice of what to publish stays with the outlets",
 22: "singles out one development within it rather than leaving that development implicit",
 23: "Whether any particular outlet's coverage is fair or unfair",
 24: "so a student must be able to take the contrary case into account",
 25: "commentary is the only category reached mainly through social media",
 26: "list of what political information includes",
 27: "the more common route for three of the four categories",
 28: "poll standings take the largest share only in the final week",
 29: "since coverage shifts toward who is ahead",
 30: "the table supports the described shift in coverage without establishing an effect",
}

GROUNDING = {
 1: "EK 5.12.A.1's own words: agenda setting takes place when the named media influence HOW "
    "CITIZENS ROUTINELY ACQUIRE POLITICAL INFORMATION. The object is the route.",
 2: "EK 5.12.A.1's three named kinds of media: traditional news media, new communication "
    "technologies, and advances in social media.",
 3: "EK 5.12.A.1's four named kinds of political information, in the order the framework gives "
    "them.",
 4: "EK 5.12.A.1's adverb ROUTINELY, which makes the claim about a habit of acquisition rather "
    "than about any one occasion.",
 5: "The limit of EK 5.12.A.1. Its object is how information is acquired, and it makes no claim "
    "about the conclusions citizens draw from what they acquire.",
 6: "EK 2.7.A.1.ii against EK 5.12.A.1. The earlier statement makes the State of the Union and "
    "the bully pulpit tools a president uses to influence which policies the public sees as most "
    "important; this one makes the media the influence and the route the object.",
 7: "EK 5.3.A.1, which lists media among linkage institutions carrying preferences to "
    "policymakers, held together with EK 5.12.A.1 and LO 5.12.A's phrase MEDIA'S ROLE AS A "
    "LINKAGE INSTITUTION.",
 8: "EK 5.12.A.2, which names popular levels of trust and confidence in government as what the "
    "media use polling results to convey.",
 9: "EK 5.12.A.2's own term for what elections can be turned into, HORSE RACES.",
 10: "EK 5.12.A.2's phrase: based more on POPULARITY and factors other than the QUALIFICATIONS "
     "AND PLATFORMS of candidates.",
 11: "EK 5.12.A.2's verb, CAN AFFECT. The framework states a possible effect on elections, not "
     "an established determination of any result.",
 12: "EK 5.12.A.2's two named nouns, qualifications and platforms, which are what the framework "
     "says horse race coverage moves away from.",
 13: "EK 5.12.A.2 applied to a scenario of repeated poll standing coverage, which is the "
     "coverage the framework describes.",
 14: "EK 5.12.A.1's category of investigative journalism, listed separately from news events "
     "because the material had to be uncovered rather than observed.",
 15: "EK 5.12.A.1's category of political commentary, which is opinion offered about politics "
     "rather than a report of what occurred.",
 16: "CED skill 5.D as stated (p. 14 and p. 116) and assigned to this topic.",
 17: "CED skill 5.D's prompts (p. 164): what evidence goes against your claim, and taking the "
     "rebuttal evidence into account why is your claim still the best. Skill 5.B assembles the "
     "supporting evidence instead.",
 18: "EK 5.12.A.2 read for what it actually objects to, a proportion of coverage rather than the "
     "publication of poll results, worked through CED skill 5.D.",
 19: "EK 5.12.A.1's verb ACQUIRE, which assigns an activity to the citizen even while the "
     "influence the statement describes is real.",
 20: "CED skill 5.D's third prompt: taking the rebuttal evidence into account, why is your claim "
     "still the best. A response that does not engage the objection has not answered it.",
 21: "New York Times Co. v. United States (1971), required case, cross-referenced by the CED to "
     "LO 5.12.A (p. 33). CED holding (p. 30): a heavy presumption against prior restraint even "
     "in cases involving national security, read for what it leaves with the publisher.",
 22: "EK 5.12.A.1's list structure, which names new communication technologies and then advances "
     "in social media, a particular case of the general category.",
 23: "The limit of EK 5.12.A.1 and EK 5.12.A.2 together. They describe a process and a possible "
     "effect and reach no verdict about any outlet's coverage.",
 24: "CED skill 5.D assigned to a topic whose central claim is stated with the modal CAN AFFECT, "
     "which is a claim reasonable people dispute.",
 25: "Recomputed from the table: weekly reach runs 84 percent down to 29 percent, and exactly "
     "one row shows a larger social share than traditional share.",
 26: "EK 5.12.A.1's four kinds of political information matched to the table's four row labels.",
 27: "Recomputed from the table: traditional news media leads in three of four rows, including "
     "the two rows with the widest weekly reach.",
 28: "Recomputed from the table: the poll standings column rises at every step, the other two "
     "fall at every step, and poll standings hold the largest share in exactly one period.",
 29: "EK 5.12.A.2's contrast between coverage of standing in a contest and coverage of "
     "qualifications and platforms, matched to the columns that grow and shrink.",
 30: "EK 5.12.A.2's modal CAN AFFECT worked through CED skill 5.D: the evidence reaches the "
     "shift in coverage and does not reach an effect on any result.",
}


# --- content gate 1: the framework's modal, and its two nouns -----------------
_CERTAIN = ("determines", "determine", "decides", "decide", "guarantees", "guarantee",
            "always", "never", "makes certain", "ensures", "causes voters")


def _modal(module):
    """No key may upgrade EK 5.12.A.2's CAN AFFECT into a certainty."""
    bad = []
    for i, item in enumerate(module.QUESTIONS, 1):
        key = item["choices"][item["ans"]]
        norm = gc.normalize(key)
        if "horse race" in norm or "poll standing" in norm or "polling result" in norm:
            for word in _CERTAIN:
                # Padded so containment is measured on whole words: "decide"
                # must not match inside "decided", and "never" must not match a
                # word that merely contains it.
                if f" {gc.normalize(word)} " in f" {norm} ":
                    bad.append(f"q{i}: the key says {word!r} about poll coverage. EK 5.12.A.2's "
                               "verb is CAN AFFECT, which states a possibility")
    # The items whose whole point is the modal must keep the possibility.
    for i in (11, 30):
        norm = gc.normalize(module.QUESTIONS[i - 1]["choices"][module.QUESTIONS[i - 1]["ans"]])
        if "can affect" not in norm and "possibility" not in norm:
            bad.append(f"q{i}: the key no longer carries the framework's possibility language, "
                       "which is the whole content of the item")
    # The displacement item must keep BOTH nouns.
    norm10 = gc.normalize(module.QUESTIONS[9]["choices"][module.QUESTIONS[9]["ans"]])
    for noun in ("qualifications", "platforms"):
        if noun not in norm10:
            bad.append(f"q10: the key drops {noun!r}. EK 5.12.A.2 names qualifications AND "
                       "platforms, and half the pair is a different claim")
    if bad:
        print(f"FAIL {module.__name__} modal")
        for b in bad:
            print("  -", b)
        raise SystemExit(1)
    print(f"OK  {module.__name__} modal: no key upgrades EK 5.12.A.2's CAN AFFECT into a "
          "certainty, and the framework's two displaced nouns both survive")


# --- content gate 2: this topic's definition of agenda setting ----------------
_WRONG_AGENDA = ("what to think", "what opinions to hold", "which policies the public sees",
                 "which policies are most important", "what conclusions to reach")


def _agenda(module):
    """A key defining agenda setting must use EK 5.12.A.1's definition, not 2.7's."""
    bad = []
    defining = []
    for i, item in enumerate(module.QUESTIONS, 1):
        stem = gc.normalize(item["q"])
        key = item["choices"][item["ans"]]
        norm = gc.normalize(key)
        for wrong in _WRONG_AGENDA:
            if gc.normalize(wrong) in norm:
                bad.append(f"q{i}: the key defines agenda setting as {wrong!r}, which is EK "
                           "2.7.A.1.ii's statement about a president, not EK 5.12.A.1's about "
                           "the media")
        # An item whose STEM asks what agenda setting is must answer with the
        # acquisition of information.
        asks = "agenda setting takes place" in stem or "agenda setting" in stem and "means" in stem
        if asks:
            defining.append(i)
            if "acquire" not in norm and "acquisition" not in norm and "information" not in norm:
                bad.append(f"q{i}: the stem asks what agenda setting is and the key does not "
                           "name the acquisition of political information, which is the whole "
                           "of EK 5.12.A.1's definition")
    if not defining:
        bad.append("no item asks what agenda setting is, which is EK 5.12.A.1's own subject")
    if bad:
        print(f"FAIL {module.__name__} agenda")
        for b in bad:
            print("  -", b)
        raise SystemExit(1)
    print(f"OK  {module.__name__} agenda: {len(defining)} defining item(s) answer with EK "
          "5.12.A.1's acquisition of information, and no key imports topic 2.7's definition")


# --- the arithmetic -----------------------------------------------------------
WEEK = "Encountering it in a typical week (%)"
TRAD = "Mainly through traditional news media (%)"
SOCIAL = "Mainly through social media or new technologies (%)"
POLLS = "Coverage of poll standings (%)"
QUALS = "Coverage of candidate qualifications (%)"
PLATS = "Coverage of candidate platforms (%)"


def _col(table, header):
    """Column by header NAME, keyed by row label. Never by index -- inserting a
    column must not silently repoint a check at different numbers."""
    j = table["headers"].index(header)
    return {r[0]: gc.num(r[j]) for r in table["rows"]}


def _routes(table):
    week, trad, social = _col(table, WEEK), _col(table, TRAD), _col(table, SOCIAL)
    for name in week:
        assert abs(trad[name] + social[name] - week[name]) < 1e-9, (
            f"{name}: routes {trad[name]} plus {social[name]} do not sum to the weekly share "
            f"{week[name]}, so the table's parts do not make its whole")
    return week, trad, social


def q25(table):
    week, trad, social = _routes(table)
    top = max(week, key=week.get)
    bottom = min(week, key=week.get)
    social_led = [k for k in week if social[k] > trad[k]]
    assert top == "News events", top
    assert bottom == "Investigative journalism", bottom
    assert social_led == ["Political commentary"], social_led
    return (f"weekly reach runs {week[top]:.0f}% for {top} down to {week[bottom]:.0f}% for "
            f"{bottom}, and exactly one row is social media led: {social_led[0]} "
            f"({social['Political commentary']:.0f}% against {trad['Political commentary']:.0f}%)")


def q26(table):
    week, _, _ = _routes(table)
    expected = {"News events", "Investigative journalism", "Election coverage",
                "Political commentary"}
    assert set(week) == expected, sorted(week)
    return ("the four row labels are exactly EK 5.12.A.1's four kinds of political information, "
            "and every row's two routes sum to its weekly share")


def q27(table):
    week, trad, social = _routes(table)
    trad_led = [k for k in week if trad[k] > social[k]]
    assert len(trad_led) == 3, trad_led
    widest = sorted(week, key=week.get, reverse=True)[:2]
    assert all(k in trad_led for k in widest), (widest, trad_led)
    return (f"traditional news media leads in {len(trad_led)} of 4 rows, including the two with "
            f"the widest weekly reach ({widest[0]} at {week[widest[0]]:.0f}% and {widest[1]} at "
            f"{week[widest[1]]:.0f}%)")


def _shares(table):
    order = [r[0] for r in table["rows"]]
    polls = [_col(table, POLLS)[k] for k in order]
    quals = [_col(table, QUALS)[k] for k in order]
    plats = [_col(table, PLATS)[k] for k in order]
    for k, p, q, pl in zip(order, polls, quals, plats):
        assert abs(p + q + pl - 100) < 1e-9, f"{k}: shares sum to {p + q + pl}, not the whole"
    return order, polls, quals, plats


def q28(table):
    order, polls, quals, plats = _shares(table)
    assert all(b > a for a, b in zip(polls, polls[1:])), f"poll column does not rise: {polls}"
    assert all(b < a for a, b in zip(quals, quals[1:])), f"qualifications column does not fall: {quals}"
    assert all(b < a for a, b in zip(plats, plats[1:])), f"platforms column does not fall: {plats}"
    leads = [i for i in range(len(order)) if polls[i] > quals[i] and polls[i] > plats[i]]
    assert leads == [len(order) - 1], (
        f"poll standings lead in periods {leads}, not in the final period alone")
    return (f"every row sums to the whole; poll standings rise {polls[0]:.0f}% to "
            f"{polls[-1]:.0f}% while qualifications fall {quals[0]:.0f}% to {quals[-1]:.0f}% and "
            f"platforms fall {plats[0]:.0f}% to {plats[-1]:.0f}%, and poll standings lead only "
            f"in the {order[-1].lower()}")


def q29(table):
    order, polls, quals, plats = _shares(table)
    assert polls[-1] > polls[0], polls
    assert quals[-1] + plats[-1] < quals[0] + plats[0], (quals, plats)
    return ("the standing column grows while the qualifications and platforms columns shrink "
            "together, which is EK 5.12.A.2's contrast expressed as data")


def q30(table):
    order, polls, quals, plats = _shares(table)
    # The item's key concedes that a shift in coverage is all the table reaches.
    # That concession is honest only if the table really does show the shift.
    assert polls[-1] > polls[0] and plats[-1] < plats[0], (polls, plats)
    assert len(order) == len({r for r in order}), order
    return (f"the table reaches a shift in one broadcaster's coverage across {len(order)} "
            "periods and reports nothing about any election result, which is exactly what the "
            "key concedes")


# --- negative controls --------------------------------------------------------
def _copy(module):
    """A shallow module stand-in whose questions may be corrupted freely."""
    qs = []
    for item in module.QUESTIONS:
        c = dict(item)
        c["choices"] = list(item["choices"])
        if item.get("table") is not None:
            t = item["table"]
            c["table"] = dict(headers=list(t["headers"]), rows=[list(r) for r in t["rows"]])
        qs.append(c)
    return types.SimpleNamespace(__name__=module.__name__ + " (corrupted)",
                                 TOPIC=module.TOPIC, QUESTIONS=qs)


def _must_fail(label, fn):
    """Run a gate against corrupted content and require that it complains."""
    try:
        with contextlib.redirect_stdout(io.StringIO()):
            fn()
    except (SystemExit, AssertionError):
        print(f"OK  negative control fires: {label}")
        return
    print(f"FAIL negative control stayed SILENT: {label}")
    raise SystemExit(1)


def _controls():
    # 1. The modal upgraded to a certainty.
    m = _copy(v5_12)
    m.QUESTIONS[10]["choices"][0] = "The framework says horse race coverage determines who wins"
    _must_fail("a key upgrading CAN AFFECT into a certainty", lambda: _modal(m))

    # 2. One of the framework's two displaced nouns dropped.
    m = _copy(v5_12)
    m.QUESTIONS[9]["choices"][0] = "Popularity and factors other than the platforms of candidates"
    _must_fail("a key dropping one of the framework's two displaced nouns", lambda: _modal(m))

    # 3. Topic 2.7's definition of agenda setting imported into this topic.
    m = _copy(v5_12)
    m.QUESTIONS[0]["choices"][0] = "Which policies the public sees as most important"
    _must_fail("a key importing topic 2.7's definition of agenda setting", lambda: _agenda(m))

    # 4. A survey figure that makes item 27's rebuttal false.
    m = _copy(v5_12)
    for item in m.QUESTIONS[24:27]:
        rows = item["table"]["rows"]
        rows[0][2], rows[0][3] = "38", "46"   # news events flips to social media led
    _must_fail("a route figure that makes item 27's rebuttal false",
               lambda: q27(m.QUESTIONS[26]["table"]))

    # 5. A coverage figure that breaks item 28's direction claim.
    m = _copy(v5_12)
    for item in m.QUESTIONS[27:30]:
        rows = item["table"]["rows"]
        rows[1][1], rows[1][3] = "20", "53"   # poll standings no longer rise at every step
    _must_fail("a coverage figure that breaks item 28's rising poll column",
               lambda: q28(m.QUESTIONS[27]["table"]))


ua.shape(v5_12)
ua.check(v5_12, ANCHORS, GROUNDING)
ua.notation(v5_12)
_modal(v5_12)
_agenda(v5_12)
gc.check(v5_12, arith={25: q25, 26: q26, 27: q27, 28: q28, 29: q29, 30: q30})
_controls()
