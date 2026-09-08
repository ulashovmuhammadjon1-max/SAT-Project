"""Scope and attribution guards for the AP U.S. HISTORY unit 5 and unit 6 banks.

`wh_check.run` already gates structure, anchors, notation, the CED citation,
figure language and the marked-stimulus rule, and `cg_check` recomputes every
`table=`. Two further things matter across Periods 5 and 6 and neither is
visible to those gates.

1. CITATION SCOPE
-----------------
The shared gate requires SOME Key Concept code in every `why`; it does not care
which one. That is exactly how a topic bank drifts: the cited sentence is real
and the `why` reads well, but it is the NEXT topic's sentence, and a student who
opened this topic is answering a question that belongs somewhere else. Unit 5's
topics are unusually easy to drift between -- 5.4 and 5.6 both rest on the
framework's sentence about attempts to resolve the issue of slavery in the
territories, split into KC-5.2.II.B.i and KC-5.2.II.B.ii -- so `kc_scope` pins
each module to the codes ITS OWN topic page prints.

The rule is deliberately one-directional. A cited code passes if it is the whole
of, or a dotted PREFIX of, a code the page prints: a page printing KC-5.1.I.B
licenses KC-5.1.I and KC-5.1 too, because a `why` explaining a lettered
sub-point normally has to quote the roman-numeral sentence it sits under. The
other direction is NOT licensed, because a page printing only the roman-numeral
sentence (every contextualizing topic) would otherwise license every lettered
sub-point under it -- which is the whole boundary those topics exist to hold.
A sibling never passes: KC-5.1.I.C is neither a prefix of KC-5.1.I.B nor equal
to it.

Only ONE in-scope citation is required per `why`. A `why` that also names a
neighbouring code in order to say what the answer is NOT is doing the right
thing, and a check that failed it would be the over-matching own-goal this
repository keeps paying for.

2. ATTRIBUTION
--------------
Periods 5 and 6 carry claims the framework REPORTS rather than asserts: that
American institutions were superior (KC-5.1.I.B, an argument of advocates of
annexation), that slavery was a positive social good (KC-5.2.I.C, the
defenders' argument), Social Darwinism (KC-6.3.I.A, theories social
commentators advocated), the Gospel of Wealth (KC-6.3.I.B, what some business
leaders argued), and laissez-faire (KC-6.1.II.A, what some argued). A choice
that states one of those flatly reaches a student as the framework's own view.
`attributed` requires an attribution word in the same string as the reported
claim. It proves the attribution is PRESENT, not that it is accurate -- no
checker over prose can do the second -- but the failure it catches is the
common one: a distractor or a `why` compressed until the reporting verb fell
out.

NO `\\b` ANYWHERE. A digit and a letter are both word characters, so `\\b` is
silently not a boundary exactly where it looks like one; this repository has
paid for that five separate times. Every pattern uses explicit lookarounds.

Both checks carry negative controls, run by `controls(module, ...)` from each
verifier's `--selftest`.
"""
import copy
import re
import types

# A Key Concept code as this CED prints them: KC-5.1.I.A, KC-5.2.II.B.i,
# KC-5.3.II.i, KC-6.1.I.E.ii. Explicit lookarounds, never \b -- the code sits
# against digits at both ends.
_KC = re.compile(r"(?<![A-Za-z0-9])KC-\d+(?:\.[A-Za-z0-9]+)+(?![A-Za-z0-9])")

# Words that mark a claim as REPORTED rather than asserted. Deliberately does
# NOT include "states", "says" or "view": "states" matches the noun in
# "Southern states" and "view" matches far too much, and an attribution list
# that matches by accident would let an unattributed claim through while
# looking like a check. Short of that, the list errs toward accepting, because
# the cost of a false failure here is an author rewriting good prose.
_ATTRIBUTION = re.compile(
    r"(?<![A-Za-z])(?:argue[ds]?|arguing|arguments?|advocate[sd]?|advocating|"
    r"claim(?:s|ed|ing)?|assert(?:s|ed|ing|ion|ions)?|contend(?:s|ed|ing)?|"
    r"maintain(?:s|ed)?|defend(?:s|ed|ing)?|defenders?|proponents?|supporters?|"
    r"champion(?:s|ed|ing)?|urged|insisted|portray(?:s|ed|ing)?|doctrines?|"
    r"theor(?:y|ies)|according to|held that|on the ground that|the belief that|"
    r"the view that|justif(?:y|ies|ied|ication))(?![A-Za-z])", re.IGNORECASE)


def _parts(code):
    return code.split(".")


def _in_scope(cited, allowed):
    """True if `cited` is one of `allowed` or a dotted prefix of one of them."""
    p = _parts(cited)
    return any(_parts(a)[:len(p)] == p for a in allowed)


def kc_scope(module, allowed, objective=None):
    """Every `why` must cite a Key Concept this topic's own page prints."""
    code = module.TOPIC[0]
    assert allowed, f"{code}: kc_scope needs the codes this topic page prints"
    for a in allowed:
        assert _KC.fullmatch(a), f"{code}: {a!r} is not a Key Concept code"
    for i, item in enumerate(module.QUESTIONS, 1):
        why = item["why"]
        cited = _KC.findall(why)
        ok = any(_in_scope(c, allowed) for c in cited)
        if not ok and objective and objective in why:
            ok = True
        assert ok, (
            f"{code} q{i}: the why cites {cited or 'no KC code'} and none of them is "
            f"printed on this topic's page ({', '.join(allowed)}"
            + (f", or {objective}" if objective else "") + f") -- {why[:90]!r}"
        )
    print(f"OK  {code} citation scope: every why traces to a Key Concept this topic's "
          f"own page prints, in {len(module.QUESTIONS)} questions.")


def attributed(module, reported):
    """A claim the framework REPORTS may not be stated anywhere as fact.

    `reported` is a list of (compiled regex, short description) pairs naming the
    claims this topic reports. Every stem, choice and `why` matching one of them
    must carry an attribution word.

    THE STEM COUNTS AS CONTEXT FOR ITS OWN CHOICES, and that is deliberate. A
    student reads a choice underneath its question, so "Which statement gives
    the argument advocates made?" followed by a bare statement of the argument
    is honest reporting, while "Which of the following is true?" followed by the
    same words is not. Requiring the attribution word inside the choice alone
    would fail the first as well as the second, and an author would then pad
    every option with "advocates argued that" -- a checker making the prose
    worse, which this repository has shipped once already.
    """
    code = module.TOPIC[0]
    n = 0
    for i, item in enumerate(module.QUESTIONS, 1):
        for text in [item["q"], item["why"]] + list(item["choices"]):
            for pat, what in reported:
                if not pat.search(text):
                    continue
                n += 1
                assert _ATTRIBUTION.search(item["q"] + " " + text), (
                    f"{code} q{i}: states {what} with no attribution in the stem or in the "
                    f"text itself, so the framework's report of an argument reads as the "
                    f"framework's own assertion -- {text[:90]!r}"
                )
    print(f"OK  {code} attribution: all {n} mentions of a reported claim name whose "
          f"claim it is.")


# ------------------------------------------------------------------ the controls

def _mutant(module):
    m = types.ModuleType(module.__name__ + "_scope_mutant")
    m.TOPIC = module.TOPIC
    m.QUESTIONS = copy.deepcopy(module.QUESTIONS)
    return m


def controls(module, allowed, objective=None, reported=(), out_of_scope="KC-9.9.IX.Z"):
    """Negative and positive controls for both checks above.

    `out_of_scope` must be a code this topic's page does NOT print; the default
    cannot be in scope for any real topic, and a caller passing a NEIGHBOUR's
    code gets a sharper control. A positive control follows each, so a check
    that rejected everything would fail here rather than look thorough.
    """
    assert not _in_scope(out_of_scope, allowed), (
        f"the control's code {out_of_scope!r} is IN scope for this topic, so the control "
        f"below would prove nothing")
    code = module.TOPIC[0]

    def must_raise(label, mutate, run, expect):
        mod = _mutant(module)
        mutate(mod)
        try:
            run(mod)
        except AssertionError as exc:
            assert re.search(expect, str(exc), re.I), (
                f"CONTROL FIRED FOR THE WRONG REASON: {label} -- {exc}")
            print(f"  control OK  {label}: {str(exc)[:96]}")
            return
        raise SystemExit(f"CONTROL FAILED: {label} did not raise")

    def drift(mod):
        mod.QUESTIONS[0]["why"] = (
            f"This follows directly from {out_of_scope}, which the framework prints on "
            f"another topic's page altogether and not on this one.")

    must_raise(f"a why citing only {out_of_scope}, which this page does not print",
               drift,
               lambda m: kc_scope(m, allowed, objective),
               r"none of them is printed on this topic's page")

    # POSITIVE control for the same check: a why that cites an in-scope code AND
    # a neighbour's code, in order to say what the answer is not, must pass.
    mod = _mutant(module)
    mod.QUESTIONS[0]["why"] = (
        f"{allowed[0]} states the sentence this key rests on, while {out_of_scope} "
        f"belongs to another topic and is why the rejected option is wrong.")
    try:
        kc_scope(mod, allowed, objective)
    except AssertionError as exc:
        raise SystemExit(
            f"CONTROL FAILED for {code}: kc_scope rejected a why that cites an in-scope "
            f"code alongside a neighbour's -- {exc}")
    print("  control OK  a why citing an in-scope code alongside a neighbour's is accepted")

    for pat, what in reported:
        bare = pat.pattern.replace("\\", "")
        # The STEM is replaced as well as the choice. It has to be: the stem
        # counts as context, so a control that changed only the choice would
        # silently pass whenever the stem it sat under already carried a
        # reporting verb -- a control that cannot fail, on the item it happened
        # to be attached to.
        neutral = "Which of the following is correct about this period?"

        def strip_attribution(mod, bare=bare, neutral=neutral):
            mod.QUESTIONS[1]["q"] = neutral
            mod.QUESTIONS[1]["choices"][0] = (
                f"The {bare} settled the matter for the whole of the period")

        must_raise(f"{what} stated with no attribution",
                   strip_attribution,
                   lambda m: attributed(m, reported),
                   r"with no attribution")

        mod = _mutant(module)
        mod.QUESTIONS[1]["q"] = neutral
        mod.QUESTIONS[1]["choices"][0] = (
            f"Advocates argued that the {bare} settled the matter for the period")
        try:
            attributed(mod, reported)
        except AssertionError as exc:
            raise SystemExit(
                f"CONTROL FAILED for {code}: the attribution gate rejected an attributed "
                f"statement of {what} -- {exc}")
        print(f"  control OK  {what} is accepted once it is attributed")
