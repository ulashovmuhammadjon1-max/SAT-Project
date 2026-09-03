"""Key audit for AP BIOLOGY 7.12 Origins of Life on Earth.

One (anchor, claim) per item, in module order. The anchor must appear in the
keyed choice and in no distractor, so an off-by-one key stops matching; the
claim states what the key rests on, for a human to audit.

WHAT THE KEYS REST ON
---------------------
Every item is keyed to EK 7.12.A.1 (the origin of life is supported by
scientific evidence; geological evidence reinforces the models; Earth formed
approximately 4.6 billion years ago, the environment was too hostile until
about 3.9, the earliest fossil evidence dates to 3.5, and together these give a
plausible range) or to EK 7.12.A.2 (the RNA world hypothesis PROPOSES that RNA
could have been the earliest genetic material, on three ASSUMPTIONS: genetic
continuity assured by the replication of RNA, base-pairing necessary for
replication, and genetically encoded proteins not involved as catalysts), or to
the topic's suggested skill 3.B, state the null hypothesis or predict the
results of an experiment.

ONE ITEM ASKS WHY, AND SAYS SO. Item 16 asks why the third assumption belongs
in a hypothesis about the EARLIEST genetic material. The CED prints the
assumption and does not print the reason, so its claim below states plainly
that the reasoning follows from EK 7.12.A.2's own two halves rather than from a
further sentence. Nothing else in the module keys an unstated reason.

Items 17 to 23 carry a table. The three dates are the only figures the CED
prints for this topic and every interval a key states is RECOMPUTED below from
the table, so no item depends on a remembered number. The assumptions table is
checked against the framework's own three statements, not merely counted.

NEGATIVE CONTROL. Moving any key, or changing any table cell the keys depend
on, makes this file raise; confirmed by running exactly that.
"""
import re

import cg_check as cg
import b7_12

QS = b7_12.QUESTIONS
T_DATES = b7_12._T_DATES
T_ASSUMPTIONS = b7_12._T_ASSUMPTIONS

WHEN = "Time before the present, in billions of years"
IS_ASSUMPTION = "Listed by the framework as an assumption of the RNA world hypothesis"

EARTH = "Formation of Earth"
HOSTILE = "End of the period too hostile for life"
FOSSIL = "Earliest fossil evidence for life"

# The three assumptions EK 7.12.A.2 prints, each reduced to a phrase that
# appears in it and in nothing else. Explicit lookarounds inside
# cg.contains_phrase, never \b.
ASSUMPTION_MARKS = ["replication of RNA", "base-pairing is necessary for replication",
                    "not involved as catalysts"]


def keyed(item):
    return item["choices"][item["ans"]]


def raw(table, row_label, header):
    j = [cg.normalize(h) for h in table["headers"]].index(cg.normalize(header))
    i = [cg.normalize(lab) for lab in cg.labels(table)].index(cg.normalize(row_label))
    return str(table["rows"][i][j])


def _dates_present(table):
    for lab in (EARTH, HOSTILE, FOSSIL):
        assert cg.normalize(lab) in [cg.normalize(x) for x in cg.labels(table)], \
            f"the table has no row {lab!r}; it holds {cg.labels(table)}"
    e, h, f = (cg.cell(table, lab, WHEN) for lab in (EARTH, HOSTILE, FOSSIL))
    assert e > h > f, (
        f"times before the present must fall in this order: formation {e}, "
        f"end of hostile period {h}, earliest fossils {f}"
    )
    return e, h, f


def _gap(a, b):
    return round(a - b, 6)


def _billions(x):
    s = f"{x:.1f}"
    return f"{s} billion years"


def q17(table, item):
    e, h, _ = _dates_present(table)
    assert keyed(item) == _billions(_gap(e, h)), \
        f"q17 key {keyed(item)!r} but {e} minus {h} is {_gap(e, h)}"
    return f"formation at {e} and the end of the hostile period at {h} are {_gap(e, h)} apart"


def q18(table, item):
    _, h, f = _dates_present(table)
    assert keyed(item) == _billions(_gap(h, f)), \
        f"q18 key {keyed(item)!r} but {h} minus {f} is {_gap(h, f)}"
    return f"the plausible range runs from {h} to {f}, a width of {_gap(h, f)}"


def q19(table, item):
    e, _, f = _dates_present(table)
    assert keyed(item) == _billions(_gap(e, f)), \
        f"q19 key {keyed(item)!r} but {e} minus {f} is {_gap(e, f)}"
    return f"formation at {e} and the earliest fossils at {f} are {_gap(e, f)} apart"


def q20(table, item):
    e, h, f = _dates_present(table)
    plausible, early = _gap(h, f), _gap(e, h)
    assert plausible < early, (
        f"the key says the plausible range {plausible} is shorter than the early interval {early}"
    )
    assert plausible < _gap(e, f), "the plausible range cannot exceed the whole span since formation"
    return f"the plausible range {plausible} is shorter than the {early} between formation and habitability"


def _marks(table):
    out = {}
    for lab in cg.labels(table):
        v = cg.normalize(raw(table, lab, IS_ASSUMPTION))
        assert v in ("yes", "no"), f"{lab}: the assumption column reads {v!r}, not yes or no"
        out[lab] = v == "yes"
    return out


def _assumptions_are_the_frameworks(table):
    marks = _marks(table)
    yes = [lab for lab, v in marks.items() if v]
    assert len(yes) == len(ASSUMPTION_MARKS), \
        f"the framework lists {len(ASSUMPTION_MARKS)} assumptions; the table marks {len(yes)}"
    for mark in ASSUMPTION_MARKS:
        hits = [lab for lab in yes if cg.contains_phrase(lab, mark)]
        assert len(hits) == 1, f"exactly one marked row must state {mark!r}; {hits} do"
    for lab, v in marks.items():
        if not v:
            for mark in ASSUMPTION_MARKS:
                assert not cg.contains_phrase(lab, mark), \
                    f"{lab!r} is marked as not an assumption yet states {mark!r}"
            # A row marked as NOT part of the hypothesis must also not assert the
            # hypothesis's own proposal, that RNA was the earliest genetic
            # material -- EK 7.12.A.2. Checking only the three assumptions left
            # that hole, and it was found by running the mutation.
            assert not cg.contains_phrase(lab, "RNA was the earliest genetic material"), \
                f"{lab!r} is marked as not part of the hypothesis yet states its own proposal"
    return marks, yes


def q21(table, item):
    _, yes = _assumptions_are_the_frameworks(table)
    words = ["Zero", "One", "Two", "Three", "Four", "Five"]
    assert keyed(item) == words[len(yes)], \
        f"q21 key {keyed(item)!r} but the table marks {len(yes)} rows as assumptions"
    return f"{len(yes)} of the {len(cg.labels(table))} listed statements are marked as assumptions"


def q22(table, item):
    marks, _ = _assumptions_are_the_frameworks(table)
    no_rows = [lab for lab, v in marks.items() if not v]
    assert no_rows, "at least one row must be marked as not an assumption"
    hit = [lab for lab in no_rows if _quotes(keyed(item), lab)]
    assert len(hit) == 1, \
        f"q22 key {keyed(item)!r} must quote exactly one row marked as not an assumption; it quotes {hit}"
    for lab, v in marks.items():
        if v:
            assert not _quotes(keyed(item), lab), \
                f"q22 key {keyed(item)!r} also quotes {lab!r}, which IS one of the assumptions"
    return f"the key quotes {hit[0]!r}, one of the {len(no_rows)} rows marked as not an assumption"


def _quotes(text, phrase, n=4):
    """``text`` contains at least ``n`` consecutive words of ``phrase``.

    A shorter overlap would let an incidental word satisfy the check; an
    under-matching checker is worse than none.
    """
    words = cg.normalize(phrase).split()
    if len(words) < n:
        return cg.contains_phrase(text, phrase)
    return any(cg.contains_phrase(text, " ".join(words[k:k + n]))
               for k in range(len(words) - n + 1))


def q23(table, item):
    _, yes = _assumptions_are_the_frameworks(table)
    assert len(yes) == 3, f"the key speaks of three assumptions; the table marks {len(yes)}"
    return f"the three marked rows are the framework's own three assumptions: {yes}"


TABLE_CHECKS = {17: q17, 18: q18, 19: q19, 20: q20, 21: q21, 22: q22, 23: q23}


CLAIMS = [
 ("scientific evidence",
  "EK 7.12.A.1 states that the origin of life on Earth is supported by scientific evidence, and its two sub-statements name geological evidence and a set of dates. The topic rests on more than one kind of evidence, not on a single experiment or on fossils alone."),
 ("reinforces models of the origin of life on Earth",
  "EK 7.12.A.1 states that geological evidence reinforces models of the origin of life on Earth. Reinforcing a model is supporting it, which is neither replacing it nor fixing an exact date."),
 ("4.6 billion years",
  "EK 7.12.A.1 states that Earth formed approximately 4.6 billion years ago. The distractors are the framework's other two dates and the intervals between them, none of which is the age of the planet."),
 ("3.9 billion years",
  "EK 7.12.A.1 states that the environment was too hostile for life until about 3.9 billion years ago. That date is the earlier boundary of the interval in which the origin of life is placed."),
 ("3.5 billion years",
  "EK 7.12.A.1 states that the earliest fossil evidence for life dates to 3.5 billion years ago. That date is the later boundary of the same interval."),
 ("plausible range of dates",
  "EK 7.12.A.1 states that, taken together, this evidence provides a plausible range of dates for the origin of life. A range is not a single date, and the statement says nothing about how life spread or when eukaryotes appeared."),
 ("end of the period too hostile for life and the earliest fossil evidence",
  "EK 7.12.A.1 gives one date before which the environment was too hostile and one by which life had left fossils. Life cannot have begun before conditions allowed it and must already have existed to leave the earliest fossils, so the interval between them is the plausible range the statement names."),
 ("too hostile for life until about 3.9 billion years ago",
  "EK 7.12.A.1 states exactly that, which is a claim about conditions rather than about the availability of rocks. Earth had already formed long before that date, at approximately 4.6 billion years ago."),
 ("must already have existed in order to leave the fossils",
  "EK 7.12.A.1 uses the earliest fossil evidence as one bound of a plausible RANGE rather than as the origin itself. A fossil records an organism that was already alive, so it shows life existed by that date and not that it began then."),
 ("RNA could have been the earliest genetic material",
  "EK 7.12.A.2 states that the RNA world hypothesis proposes that RNA could have been the earliest genetic material. The word proposes marks a hypothesis rather than an established finding."),
 ("genetic continuity was assured by the replication of RNA",
  "EK 7.12.A.2's first assumption, near verbatim. Substituting DNA or protein for RNA reverses the very proposal the assumption belongs to."),
 ("Base-pairing is necessary for replication",
  "EK 7.12.A.2's second assumption, verbatim. It states a requirement for copying a sequence and says nothing about rates or about when cells appeared."),
 ("were not involved as catalysts",
  "EK 7.12.A.2's third assumption, that genetically encoded proteins were not involved as catalysts. It excludes one kind of catalyst rather than denying that catalysis occurred."),
 ("Three",
  "EK 7.12.A.2 states that there are three assumptions and then lists them: RNA replication assuring genetic continuity, base-pairing as a requirement for replication, and the absence of genetically encoded proteins as catalysts."),
 ("contained within a cell membrane",
  "EK 7.12.A.2 names the proposal and exactly three assumptions, and a membrane is not among them. Adding a condition the framework does not print would change the hypothesis being described."),
 ("presupposes a genetic system already in place",
  "EK 7.12.A.2 proposes RNA as the EARLIEST genetic material and lists the exclusion of genetically encoded proteins among its assumptions. The connection between the two halves is the reasoning this key states; the CED prints the assumption and not the reason, and this claim says so rather than presenting the reason as a further framework sentence."),
 ("0.7 billion years",
  "Skill 5.A includes differences. The table check above locates the two rows the stem names and recomputes the interval between the times they report before the present."),
 ("0.4 billion years",
  "EK 7.12.A.1 bounds the origin below by the end of the hostile period and above by the earliest fossil evidence and calls the result a plausible range. The table check above recomputes the width of that range from the two dates."),
 ("1.1 billion years",
  "Skill 5.A includes differences. The table check above recomputes the interval between the formation of Earth and the earliest fossil evidence from the times the table reports."),
 ("shorter than the interval",
  "Skill 4.B asks for relationships among data points. The table check above recomputes both intervals and confirms the ordering the key asserts; approximate dates can still be subtracted and compared."),
 ("Three",
  "EK 7.12.A.2 states that there are three assumptions. The table check above counts the rows the table marks as assumptions AND confirms that those rows are the framework's own three, matched by a distinctive phrase from each."),
 ("because the hypothesis proposes RNA in that role",
  "EK 7.12.A.2 proposes that RNA could have been the earliest genetic material, so a statement putting DNA in that role contradicts the proposal rather than assuming it. The table check confirms the key quotes a row marked as not an assumption and quotes none of the three that are."),
 ("condition the hypothesis takes for granted",
  "EK 7.12.A.2 introduces the three as ASSUMPTIONS of a hypothesis that PROPOSES an account. An assumption is what an account takes as given, and none of the three is presented as a demonstrated result or as a date."),
 ("makes no difference to the amount of RNA copied",
  "Skill 3.B asks for the null hypothesis, which states that the manipulated variable has no effect. Every other option predicts a particular outcome, and a prediction of an effect is the alternative hypothesis rather than the null."),
 ("sequences correspond to the sequence of the starting molecule",
  "EK 7.12.A.2's first assumption is that genetic continuity was assured by the replication of RNA. Continuity means information is carried forward, so copies must correspond in sequence to the molecule copied."),
 ("No faithful copy of the template will be produced",
  "EK 7.12.A.2's second assumption is that base-pairing is necessary for replication. Removing the ability to pair removes the stated requirement, so the predicted result is a failure to copy the sequence."),
 ("No fossil evidence of life",
  "EK 7.12.A.1 states that the environment was too hostile for life until about 3.9 billion years ago and that geological evidence reinforces the models. Skill 3.B asks for the prediction an account makes, and no life means no fossils of life."),
 ("range of dates for the origin of life would have to be revised",
  "EK 7.12.A.1 calls the interval a PLAUSIBLE RANGE supported by evidence, and a range supported by evidence is one that further evidence can move. The end of the hostile period is one of the two dates that set it."),
 ("proposal resting on stated assumptions",
  "EK 7.12.A.2 says the hypothesis PROPOSES that RNA could have been the earliest genetic material and sets out three ASSUMPTIONS. Both words mark a proposed account rather than an established fact or a definition."),
 ("bound the origin of life within a plausible range of dates",
  "EK 7.12.A.1 supplies evidence and a plausible range, and EK 7.12.A.2 supplies a proposed account of the earliest genetic material with three assumptions. Neither claims an exact date or a settled mechanism, and neither displaces the other."),
]


# SCIENCE_BRIEF.md: Biology is exported untypeset, so a backslash macro or a
# dollar span would reach a student as literal characters, and a
# digit-hyphen-digit run reads as a subtraction. Explicit lookarounds, never \b.
_BANNED = [
    (re.compile(r"\\"), "a backslash: this bank carries no LaTeX"),
    (re.compile(r"\$"), "a dollar-delimited math span"),
    (re.compile(r"(?<![A-Za-z])\d+\s*-\s*\d+(?![A-Za-z])"), "a digit-hyphen-digit range"),
    (re.compile(r"\d\s*/\s*\d"), "a digit-slash-digit fraction"),
]

_FIGURE_TALK = re.compile(
    r"(?<![A-Za-z])(the (?:graph|figure|diagram|chart|timeline) (?:shown|above|below)|"
    r"in the (?:graph|figure|diagram|chart|timeline) (?:shown|above|below)|"
    r"shown in the (?:graph|figure|diagram|chart|timeline))(?![A-Za-z])",
    re.IGNORECASE)


def style():
    hits = 0
    for i, item in enumerate(QS, 1):
        texts = [("stem", item["q"]), ("why", item["why"])]
        texts += [(f"choice {k}", c) for k, c in enumerate(item["choices"])]
        if item.get("table"):
            texts.append(("table", " | ".join(item["table"]["headers"])))
            texts += [("table", " | ".join(str(c) for c in r)) for r in item["table"]["rows"]]
        for where, text in texts:
            for pat, why_bad in _BANNED:
                m = pat.search(text)
                assert not m, f"q{i} {where} contains {m.group(0)!r}, {why_bad}"
                hits += 1
            m = _FIGURE_TALK.search(text)
            assert not m, (
                f"q{i} {where} says {m.group(0)!r}, promising a figure the bank cannot show"
            )
            hits += 1
    return hits


def main():
    n_style = style()
    cg.check(b7_12, CLAIMS, table_checks=TABLE_CHECKS)
    print(f"    {n_style} notation and figure-reference checks clean.")


main()
