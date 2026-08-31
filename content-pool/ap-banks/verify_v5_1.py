"""Structural gate for AP U.S. Government 5.1 Voting Rights and Models of Voting
Behavior.

gov345_check plus the four usgov_anchor helpers, plus two content gates.

  _amendments  EK 5.1.A.1 lists six amendments and gives each a distinct effect,
               and two of the six are described in ways a summary flattens:

                 14th  granted CITIZENSHIP -- not the vote. Five of the six
                       items extend or protect a vote and this one does not. It
                       belongs to a list about expanding participation because
                       citizenship is the status the later protections attach
                       to, but reporting it as having granted the vote misstates
                       the framework's own sentence.
                 24th  eliminated POLL TAXES, which EK 5.1.A.1.v calls a
                       STRUCTURAL BARRIER -- the same term EK 5.2.A.1 uses. It
                       is described by what it REMOVED, not by whom it added,
                       which is why the smallest row of the first table is not
                       the least important one and why item 27 says so.
                 17th  moved the election of SENATORS from state legislatures to
                       the people. It adds no voters at all, which is why it
                       appears in no row of the expansion table.

               The gate pins each of the six effects to its own amendment and
               refuses the citizenship-for-vote conflation anywhere in a key.

  _models      EK 5.1.B.1's four models, and the pair that swaps is
               RETROSPECTIVE against PROSPECTIVE. They swap because both concern
               performance; the framework separates them by TIME ALONE --
               recent past and whether those in power should be REELECTED,
               against a PREDICTION of FUTURE performance. Both statements refer
               to "a party or candidate", so the subject is not the difference,
               and a checker that looked for one would be looking at the wrong
               thing.

               A definition is attributed to the model named NEAREST BEFORE IT,
               so items 13 and 30, whose keys correctly contrast the two in a
               single sentence, are not reported. That is the same rule this
               build has now needed in five verifiers.

               The gate also keeps straight ticket voting defined by the BALLOT
               rather than by reasoning: EK 5.1.B.1.iv is the one model of the
               four that describes what was marked, not why, which is what makes
               item 20's answer -- that a voter can satisfy two models at once
               -- correct rather than a trick.
"""
import gov345_check as gc
import usgov_anchor as ua
import v5_1

ANCHORS = {
 1: "In the legal protections of the Amendments to the Constitution",
 2: "Citizenship to all persons born or naturalized in the United States",
 3: "Because citizenship is the status the later voting protections attach to",
 4: "The right to vote to African American men",
 5: "from a vote by state legislatures to a direct vote by the people",
 6: "The right to vote to women",
 7: "Poll taxes, which it calls a structural barrier to voting",
 8: "Lowered the voting age to 18",
 9: "which moved the election of senators from state legislatures to the people",
 10: "base their decisions on what is perceived to be in their best interest",
 11: "decide whether the party or candidate in power should be reelected based on the recent",
 12: "vote based on predictions of how a party or candidate will perform in the future",
 13: "while prospective voting rests on a prediction about future performance",
 14: "vote for all of the candidates from one political party on a ballot",
 15: "It describes the pattern of choices marked on a ballot",
 16: "since the decision turns on the recent past record of the party or candidate in power",
 17: "since the decision rests on a prediction of future performance",
 18: "since the decision rests on what the voter perceives to be in their best interest",
 19: "since the voter chose all of one party's candidates on the ballot",
 20: "nothing in the framework makes them exclusive",
 21: "Which of the four models describes the largest share of voters",
 22: "which eliminated poll taxes, a structural barrier to voting",
 23: "and the second about why voters choose as they do",
 24: "rather than predicting what any particular voter will do",
 25: "more than four times the next largest",
 26: "The 19th Amendment",
 27: "so counting newly eligible adults measures something different",
 28: "and the one illustrating straight ticket voting least often",
 29: "which is the recent past rather than a prediction",
 30: "one judges a record already established and the other predicts performance not yet",
}

GROUNDING = {
 1: "EK 5.1.A.1's opening sentence: expansions of opportunities for political participation "
    "'are found in the legal protections of the Amendments to the Constitution.'",
 2: "EK 5.1.A.1.i, verbatim: the 14th Amendment 'granted citizenship to all persons born or "
    "naturalized in the U.S., including formerly enslaved people.' Citizenship, not the vote.",
 3: "EK 5.1.A.1's list read as a whole: the 15th, 19th, 24th and 26th all extend or protect "
    "voting by persons whose citizenship the 14th established.",
 4: "EK 5.1.A.1.ii, verbatim. The framework's phrase is African American MEN, which is why the "
    "19th Amendment appears separately in the same list.",
 5: "EK 5.1.A.1.iii, verbatim: the 17th Amendment 'changed the practice for electing Senators "
    "from a vote by state legislatures to a direct vote by the people.'",
 6: "EK 5.1.A.1.iv, verbatim: the 19th Amendment 'granted women the right to vote.'",
 7: "EK 5.1.A.1.v, verbatim: the 24th Amendment 'eliminated poll taxes, a structural barrier "
    "to voting.' The same term EK 5.2.A.1 uses for influences on turnout.",
 8: "EK 5.1.A.1.vi, verbatim: the 26th Amendment 'lowered the voting age to 18.'",
 9: "EK 5.1.A.1.iii read against the rest of the list: it changes who chooses an officeholder "
    "rather than adding voters or removing an obstacle facing them.",
 10: "EK 5.1.B.1.i, verbatim. The framework's word PERCEIVED makes the model turn on the "
     "voter's own judgment rather than on an objective interest.",
 11: "EK 5.1.B.1.ii, verbatim, with both of its elements: the party or candidate IN POWER, and "
     "the RECENT PAST.",
 12: "EK 5.1.B.1.iii, verbatim: a PREDICTION of how a party or candidate WILL PERFORM IN THE "
     "FUTURE.",
 13: "EK 5.1.B.1.ii against EK 5.1.B.1.iii. Both models concern performance and the framework "
     "separates them by time direction alone; both refer to a party or candidate, so the "
     "subject is not the difference.",
 14: "EK 5.1.B.1.iv, verbatim: 'individuals who vote for all of the candidates from one "
     "political party on a ballot.'",
 15: "EK 5.1.B.1.iv against the other three items, which are each defined by what the voter "
     "reasons from. A straight ticket voter could arrive there by any of those routes.",
 16: "EK 5.1.B.1.ii applied, CED skill 1.D. Every vote concerns a future term, so that feature "
     "cannot be what makes a vote prospective.",
 17: "EK 5.1.B.1.iii applied: judging plans not yet enacted is a prediction of future "
     "performance, and nothing in the scenario refers to an established record.",
 18: "EK 5.1.B.1.i applied. A prediction is involved, but the framework's distinguishing "
     "feature for this model is whose interest is served rather than the tense.",
 19: "EK 5.1.B.1.iv applied. The model describes the pattern marked, regardless of how much "
     "thought went into it.",
 20: "EK 5.1.B.1's own sentence, that various models EXPLAIN DIFFERENCES in voting behavior. "
     "The framework assigns no voter to exactly one model, and a voter predicting future "
     "performance to serve a perceived interest satisfies items i and iii at once.",
 21: "EK 5.1.B.1 read for what it omits: four models defined, none ranked by prevalence.",
 22: "EK 5.1.A.1.v as the item that removes an obstacle facing the otherwise eligible, rather "
     "than extending eligibility to a group that lacked it.",
 23: "LO 5.1.A against LO 5.1.B: legal protections for voting, and models of voting behavior.",
 24: "EK 5.1.B.1's word MODELS and its verb EXPLAIN DIFFERENCES, which account for variation "
     "across voters rather than dictating any one voter's choice.",
 25: "Data item, CED skill 1.D. Every count and the ratio between the two largest are "
     "recomputed below.",
 26: "EK 5.1.A.1.iv located as the table's largest row. The 17th Amendment appears in no row "
     "because it added no voters.",
 27: "EK 5.1.A.1.v's STRUCTURAL BARRIER against a count of newly eligible adults, which is the "
     "wrong measure for a change that cleared an obstacle. Recomputed below.",
 28: "Data item, CED skill 1.D. Every share and the ordering are recomputed below.",
 29: "EK 5.1.B.1.ii located in the table's first row: a record of what has already been done "
     "is the recent past, not a prediction.",
 30: "EK 5.1.B.1.ii against EK 5.1.B.1.iii, located in the table's first two rows, which also "
     "report different shares.",
}

NEWLY, SHARE = "Adults newly eligible (thousands)", "Share of the adult population (%)"
CHANGE = "Change in the law"
VOTERS, MODEL = "Share of voters (%)", "Model illustrated"
CONSIDERATION = "Consideration named as most important"


def _col(t, header):
    j = t["headers"].index(header)
    return [r[j] for r in t["rows"]]


def _num(t, header):
    return [gc.num(c) for c in _col(t, header)]


def q25(t):
    """The women's row is more than four times the next largest, and above a tenth."""
    counts = dict(zip(_col(t, CHANGE), _num(t, NEWLY)))
    top = max(counts, key=lambda k: counts[k])
    rest = sorted((v for k, v in counts.items() if k != top), reverse=True)
    assert "women" in top, f"the largest row is {top!r}"
    assert counts[top] > 4 * rest[0], \
        f"the largest row {counts[top]:.0f} is not four times the next {rest[0]:.0f}"
    shares = dict(zip(_col(t, CHANGE), _num(t, SHARE)))
    assert shares[top] > 10, f"the largest row is {shares[top]:.0f} percent, not above a tenth"
    return (f"counts {', '.join(f'{v:.0f}' for v in counts.values())}; largest "
            f"{counts[top]:.0f} against next {rest[0]:.0f}, a ratio of "
            f"{counts[top] / rest[0]:.2f}; {shares[top]:.0f} percent of adults")


def q26(t):
    """The largest row is the women's row, and no row corresponds to the 17th Amendment."""
    counts = dict(zip(_col(t, CHANGE), _num(t, NEWLY)))
    top = max(counts, key=lambda k: counts[k])
    assert "women" in top, f"the largest row is {top!r}, not the women's row"
    for label in counts:
        assert "senator" not in label.lower(), \
            "a row concerns the election of senators, which added no voters"
    assert len(counts) == 4, f"{len(counts)} rows, not four"
    return f"largest row {top!r} at {counts[top]:.0f} thousand; no row concerns senators"


def q27(t):
    """The poll tax row is the smallest count and is a barrier removal, not an enfranchisement."""
    counts = dict(zip(_col(t, CHANGE), _num(t, NEWLY)))
    poll = [k for k in counts if "poll tax" in k.lower()]
    assert len(poll) == 1, "the poll tax row is missing or duplicated"
    assert counts[poll[0]] == min(counts.values()), \
        f"the poll tax row {counts[poll[0]]:.0f} is not the smallest"
    assert counts[poll[0]] > 0, "the poll tax row is zero, so the qualification has no figure"
    others = [k for k in counts if k != poll[0]]
    assert all("extend" in k.lower() or "lower" in k.lower() for k in others), \
        f"a non-poll-tax row is not an extension or a threshold change: {others}"
    return (f"poll tax row {counts[poll[0]]:.0f} thousand, the smallest, and the only row "
            "describing a removal rather than an extension")


def q28(t):
    """Retrospective leads, straight ticket trails, and no row reaches half."""
    shares = dict(zip(_col(t, MODEL), _num(t, VOTERS)))
    assert sum(shares.values()) == 100, f"the shares total {sum(shares.values()):.0f}, not 100"
    top = max(shares, key=lambda k: shares[k])
    low = min(shares, key=lambda k: shares[k])
    assert top == "Retrospective", f"the leading row is {top!r}"
    assert low == "Straight ticket", f"the trailing row is {low!r}"
    assert max(shares.values()) < 50, "a row reaches a majority, which the key's distractor needs"
    assert shares["Rational choice"] != min(shares.values()), \
        "rational choice is the smallest, which the key's last distractor denies"
    return ("shares " + ", ".join(f"{k} {v:.0f}" for k, v in shares.items())
            + f"; total {sum(shares.values()):.0f}")


def q29(t):
    """The retrospective row names an established record, not a prediction."""
    rows = {r[t["headers"].index(MODEL)]: r[0] for r in t["rows"]}
    retro = rows["Retrospective"].lower()
    assert "has done" in retro or "past" in retro, \
        f"the retrospective row does not name an established record: {retro!r}"
    pro = rows["Prospective"].lower()
    assert "promises" in pro or "will" in pro or "if elected" in pro, \
        f"the prospective row does not name a prediction: {pro!r}"
    return f"retrospective row {retro!r}; prospective row {pro!r}"


def q30(t):
    """The two performance rows are distinct in the table as well as in the framework."""
    shares = dict(zip(_col(t, MODEL), _num(t, VOTERS)))
    assert shares["Retrospective"] != shares["Prospective"], \
        "the two performance rows report identical shares, so the table treats them as one"
    labels = _col(t, MODEL)
    assert len(set(labels)) == 4, f"a model is listed twice: {labels}"
    return (f"retrospective {shares['Retrospective']:.0f} against prospective "
            f"{shares['Prospective']:.0f} -- four distinct models, four distinct shares")


# --- module-specific content gates -------------------------------------------

_EFFECTS = {
 2: ("citizenship", "the 14th Amendment"),
 4: ("african american men", "the 15th Amendment"),
 5: ("state legislatures to a direct vote", "the 17th Amendment"),
 6: ("the right to vote to women", "the 19th Amendment"),
 7: ("poll taxes", "the 24th Amendment"),
 8: ("voting age to 18", "the 26th Amendment"),
}


def _amendments(module):
    """Each of EK 5.1.A.1's six effects stays with its own amendment."""
    bad = []
    for n, (clause, which) in _EFFECTS.items():
        key = module.QUESTIONS[n - 1]["choices"][module.QUESTIONS[n - 1]["ans"]].lower()
        if clause not in key:
            bad.append(f"q{n}: the key for {which} no longer carries EK 5.1.A.1's own effect, "
                       f"{clause!r}")
    # The 14th granted citizenship, not the vote.
    for i, item in enumerate(module.QUESTIONS, 1):
        key = item["choices"][item["ans"]].lower()
        at = key.find("14th amendment")
        if at >= 0:
            seg = key[at:at + 120]
            for wrong in ("right to vote", "granted the vote", "extended the vote"):
                if wrong in seg:
                    bad.append(f"q{i} key: says the 14th Amendment granted the vote; EK "
                               "5.1.A.1.i says it granted CITIZENSHIP, and five of the six "
                               "items in that list extend a vote while this one does not")
    q7 = module.QUESTIONS[6]
    if "structural barrier" not in q7["choices"][q7["ans"]].lower():
        bad.append("q7: the key no longer carries EK 5.1.A.1.v's own characterization of the "
                   "poll tax as a STRUCTURAL BARRIER, which is what makes the 24th Amendment "
                   "a removal rather than an enfranchisement")
    if bad:
        print(f"FAIL {module.__name__} amendments")
        for b in bad:
            print("  -", b)
        raise SystemExit(1)
    print(f"OK  {module.__name__} amendments: all six of EK 5.1.A.1's effects stay with their "
          "own amendment, the 14th keeps CITIZENSHIP rather than the vote, and the 24th keeps "
          "the framework's STRUCTURAL BARRIER")


_MODEL_NAMES = ("rational choice", "retrospective", "prospective", "straight ticket")
_MODEL_DEFS = {
    "rational choice": "perceived to be in their best interest",
    "retrospective": "recent past",
    "prospective": "predictions of how",
    "straight ticket": "all of the candidates from one political party",
}


def _nearest_model(text, at):
    best, best_at = None, -1
    for name in _MODEL_NAMES:
        pos = text.rfind(name, 0, at)
        if pos > best_at:
            best, best_at = name, pos
    return best


def _models(module):
    """No model may be given another's definition."""
    bad = []
    for i, item in enumerate(module.QUESTIONS, 1):
        key = item["choices"][item["ans"]].lower()
        if not any(m in key for m in _MODEL_NAMES):
            continue
        for owner, defn in _MODEL_DEFS.items():
            at = key.find(defn)
            while at >= 0:
                near = _nearest_model(key, at)
                if near is not None and near != owner:
                    bad.append(f"q{i} key: attaches {defn!r} to {near!r}; EK 5.1.B.1 gives that "
                               f"definition to {owner!r} voting")
                    break
                at = key.find(defn, at + 1)
    pins = {10: "rational choice", 11: "retrospective", 12: "prospective", 14: "straight ticket"}
    for n, model in pins.items():
        key = module.QUESTIONS[n - 1]["choices"][module.QUESTIONS[n - 1]["ans"]].lower()
        if _MODEL_DEFS[model] not in key:
            bad.append(f"q{n}: the key for {model} voting no longer carries EK 5.1.B.1's own "
                       f"phrase {_MODEL_DEFS[model]!r}")
    q13 = module.QUESTIONS[12]
    k13 = q13["choices"][q13["ans"]].lower()
    if "recent past" not in k13 or "future" not in k13:
        bad.append("q13: the key no longer separates retrospective from prospective by TIME, "
                   "which is the only thing EK 5.1.B.1 separates them by")
    q15 = module.QUESTIONS[14]
    if "ballot" not in q15["choices"][q15["ans"]].lower():
        bad.append("q15: the key no longer defines straight ticket voting by the BALLOT; EK "
                   "5.1.B.1.iv is the one model of the four that describes what was marked "
                   "rather than the reasoning behind it")
    if bad:
        print(f"FAIL {module.__name__} models")
        for b in bad:
            print("  -", b)
        raise SystemExit(1)
    print(f"OK  {module.__name__} models: no key gives one of EK 5.1.B.1's four models "
          "another's definition, retrospective and prospective stay separated by time, and "
          "straight ticket stays defined by the ballot")


ua.shape(v5_1)
ua.check(v5_1, ANCHORS, GROUNDING)
ua.notation(v5_1)
_amendments(v5_1)
_models(v5_1)
gc.check(v5_1, arith={25: q25, 26: q26, 27: q27, 28: q28, 29: q29, 30: q30})
