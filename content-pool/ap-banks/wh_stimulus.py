"""MARKED STIMULUS gate for the AP World History: Modern topic banks.

`wh_check` gates structure, anchors, notation, citations and figure language.
This adds the one rule `HISTORY_BRIEF.md` states that nothing else enforces:

> Never invent a quotation and attribute it to a real person or document. Either
> quote what the CED itself contains, or write an explicitly *unattributed,
> illustrative* source.

Section I of the real exam is stimulus-based and the bank cannot show images, so
almost every stimulus in these modules is an invented textual source. The gate
requires a stem that INTRODUCES a source document to say, in the stem, that the
source is hypothetical, unattributed or illustrative.

WHAT IT PROVES AND WHAT IT DOES NOT, stated plainly so a pass is not mistaken
for a warrant: it proves the LABEL is present, not that the label is honest. A
stem reading "a hypothetical letter of Zheng He" would pass it, and no checker
over prose can catch that. What the gate does catch is the far commoner drift --
a source introduced with no marker at all, which a student reads as a real
document -- and it makes the marker a property of the file rather than an
instruction an author can forget on the twenty-eighth question.

THE INDEFINITE ARTICLE IS LOAD-BEARING. The first draft of this pattern, in
`verify_w4_1.py`, had no article requirement and fired on 4.1 q16's phrase "the
direction of technological diffusion in the framework's ACCOUNT of this period"
-- a reference to the CED itself, not an invented document. That is the
over-matching own-goal this repository keeps paying for, and the rule that fixes
it is grammatical rather than lexical: a stimulus is INTRODUCED ("A hypothetical
shipwright's notebook describes..."), never referred back to with "the". The
false finding is kept as a positive control in `controls` below so that nobody
widens the pattern again without meeting it.

NO `\\b` ANYWHERE, per the rest of this directory: a digit and a letter are both
word characters. Explicit lookarounds, so "recording" is not "record" and
"instructions" is "instruction".
"""
import copy
import re
import types

# The article, up to three intervening words, then the noun.
SOURCE_NOUN = re.compile(
    r"(?<![A-Za-z])[Aa]n? (?:[A-Za-z']+ ){0,3}"
    r"(?:account|notebook|letter|book|treatise|inventory|instruction|chronicle|record|"
    r"manual|logbook|memoir|report|petition|decree|dispatch|ledger|testimony|charter|"
    r"proclamation|register|survey|complaint|ruling|contract)s?(?![A-Za-z])")

MARKED = re.compile(r"(?<![A-Za-z])(?:hypothetical|unattributed|illustrative)(?![A-Za-z])",
                    re.IGNORECASE)


def marked_stimulus(module):
    """A stem that introduces a source must say in the stem that it is invented."""
    n = 0
    for i, item in enumerate(module.QUESTIONS, 1):
        hit = SOURCE_NOUN.search(item["q"])
        if not hit:
            continue
        n += 1
        assert MARKED.search(item["q"]), (
            f"{module.TOPIC[0]} q{i}: the stem introduces a {hit.group(0)!r} without "
            f"marking it hypothetical, unattributed or illustrative -- {item['q'][:90]!r}"
        )
    print(f"OK  {module.TOPIC[0]} stimuli: all {n} source-bearing stems are marked invented.")


def controls(module, unmarked_index=None):
    """Negative and positive controls for the gate above.

    `unmarked_index` is the 0-based index of a question whose stem really does
    introduce a marked source; its marker is stripped and the gate must fire. If
    it is not given, the first such question is found by reading the module, so
    a control cannot silently be attached to a stem that has no source in it and
    then pass for the wrong reason.
    """
    def mutant():
        m = types.ModuleType(module.__name__ + "_stimulus_mutant")
        m.TOPIC = module.TOPIC
        m.QUESTIONS = copy.deepcopy(module.QUESTIONS)
        return m

    def must_raise(label, mutate):
        mod = mutant()
        mutate(mod)
        try:
            marked_stimulus(mod)
        except AssertionError as exc:
            assert "without marking it" in str(exc), (
                f"CONTROL FIRED FOR THE WRONG REASON: {label} -- {exc}")
            print(f"  control OK  {label}: {str(exc)[:88]}")
            return
        raise SystemExit(f"CONTROL FAILED: {label} did not raise")

    def must_pass(label, mutate):
        mod = mutant()
        mutate(mod)
        try:
            marked_stimulus(mod)
        except AssertionError as exc:
            raise SystemExit(f"CONTROL FAILED: {label} was rejected -- {exc}")
        print(f"  control OK  {label}: accepted, as legal text must be")

    if unmarked_index is None:
        hits = [i for i, q in enumerate(module.QUESTIONS)
                if SOURCE_NOUN.search(q["q"]) and MARKED.search(q["q"])]
        assert hits, (
            f"{module.TOPIC[0]}: no stem introduces a marked source, so the negative "
            "control below would prove nothing about this module")
        unmarked_index = hits[0]

    def unmark(mod):
        q = mod.QUESTIONS[unmarked_index]
        # Collapse ALL runs of whitespace, not just the two that follow an
        # article. Removing "hypothetical" from "A single hypothetical record"
        # leaves a double space in the middle of the phrase, and SOURCE_NOUN
        # requires single spaces -- so the first version of this control stopped
        # matching the noun and the guard below fired instead of the gate. That
        # guard is why the bug was visible at all; without it the control would
        # have raised for the wrong reason and looked like a pass.
        q["q"] = re.sub(r"[ \t]+", " ", MARKED.sub("", q["q"]))
        assert SOURCE_NOUN.search(q["q"]), (
            "the control removed the source noun as well as the marker, so it would "
            "fire for the wrong reason")

    def no_source(mod):
        mod.QUESTIONS[0]["q"] = ("Which statement does the framework make about this period, "
                                 "according to the sentence printed beside the topic?")

    def framework_account(mod):
        # THE REAL FALSE FINDING this gate was narrowed to clear. "The
        # framework's account" and "the report of the unit overview" introduce
        # no document at all and must stay legal.
        mod.QUESTIONS[0]["q"] = ("Which statement best describes the framework's account, and "
                                 "the report of the unit overview, of this period?")

    print("stimulus-gate controls:")
    must_raise(f"q{unmarked_index + 1}'s source-bearing stem stripped of its marker", unmark)
    must_pass("a stem that introduces no source at all", no_source)
    must_pass("a stem naming the framework's own account and report", framework_account)
