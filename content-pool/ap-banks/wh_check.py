"""Gate shared by the AP World History: Modern topic banks (`w<unit>_<topic>.py`).

WHAT IS REUSED, AND WHY NOTHING HERE IS REINVENTED
--------------------------------------------------
`cg_check.check` is the structural gate every prose bank in this repository
already uses: thirty questions, five distinct choices, a key pinned to an
anchor that appears in the keyed choice and in NO distractor, a `why` that does
not name an option by letter, no choice contained inside another, no two stems
opening alike, and every `table=` question recomputed from its own table by a
callable the verifier must supply.

`es_check.style` is the notation gate written for the other untypeset prose
subject (Environmental Science). WORLD_HISTORY is not run through `mathfmt`
either, so the same rules apply unchanged: no backslash macro, no bare caret,
no digit-slash-digit fraction, no dollar sign, no non-ASCII, and no
digit-hyphen-digit range. That last one is exactly what `HISTORY_BRIEF.md`
demands ("write a span as 1945 to 1991, never 1945-1991"), so it is inherited
rather than rewritten.

WHAT HISTORY ADDS
-----------------
1. **A citation in every `why` and every `claim`.** The one rule that makes
   this bank auditable is that a key traces to a sentence in the CED, not to an
   author's knowledge of the twentieth century. `HISTORY_BRIEF.md` requires the
   Key Concept or Learning Objective code in every `why`; nothing enforced it,
   so it is enforced here. A `why` with no `KC-...` code and no named Learning
   Objective fails.

2. **No figure language.** The bank cannot display an image. A stem saying "the
   map shows" reaches a student as a question about something that is not
   there, and this project has shipped that defect once already. The patterns
   below are deliberately narrow: they require a display noun ADJACENT to a
   display verb or position word. `HISTORY_BRIEF.md` records a figure-language
   check elsewhere that fired on the phrase "the fullest picture of" and on a
   distractor naming an age-structure *diagram* as a concept -- both false --
   so "picture", "image" and "figure" only trip when they carry "above",
   "below", "shown", "shows", "depicts" or "depicted" beside them. The word
   "table" is deliberately NOT in the noun list, because a `table=` question
   legitimately says "the table below".

NO `\\b` ANYWHERE. A digit and a letter are both word characters, so `\\b` is
silently not a boundary exactly where it looks like one; this repository has
paid for that four separate times. Every pattern uses explicit lookarounds.

THE NEGATIVE CONTROL
--------------------
`python3 verify_w8_1.py --selftest` corrupts the module on purpose and requires
the gate to notice. It is not enough that *something* raised: each targeted
control also asserts WHICH message came back, because a control that fires for
the wrong reason proves nothing about the guard it names. The run also carries
POSITIVE controls -- legal prose, a legal citation, a legal use of "the table
below" -- so a gate that rejected everything would fail here rather than look
like a very thorough gate.
"""
import contextlib
import copy
import io
import re
import types

import cg_check as cg
import es_check as es

# A Key Concept code as this CED prints them: KC-6.2.IV.C.ii, KC-6.3.I.A.ii,
# KC-6.1.I.A. Explicit lookarounds, never \b -- 'KC-6.1' sits against digits.
_KC = re.compile(r"(?<![A-Za-z0-9])KC-\d+(?:\.[A-Za-z0-9]+)+(?![A-Za-z0-9])")
# The CED's other citable unit: "Unit 8: Learning Objective K".
_LO = re.compile(r"(?<![A-Za-z])Learning Objective\s+[A-Z](?![A-Za-z])")

# Display noun beside a display verb or position word. Both halves are
# required, in either order, so "the fullest picture of the period" and "an
# age structure diagram" cannot match.
_NOUN = r"(?:map|image|photograph|photo|picture|cartoon|graph|chart|figure|illustration|painting|poster|diagram)"
_SHOW = r"(?:above|below|shown|shows|showing|depicts|depicted|pictured|reproduced)"
FIGURE_LANGUAGE = [
    re.compile(rf"(?<![a-z]){_NOUN}s?\s+{_SHOW}(?![a-z])", re.I),
    re.compile(rf"(?<![a-z]){_SHOW}\s+(?:in|on)\s+the\s+{_NOUN}(?![a-z])", re.I),
    re.compile(rf"(?<![a-z])in\s+the\s+{_NOUN}\s+(?:above|below)(?![a-z])", re.I),
]


def cited(text):
    """True if the text names a Key Concept code or a Learning Objective."""
    return bool(_KC.search(text) or _LO.search(text))


def history_style(module, claims):
    """The notation gate, plus the two rules history adds."""
    es.style(module)
    code = module.TOPIC[0]
    for i, item in enumerate(module.QUESTIONS, 1):
        assert cited(item["why"]), (
            f"{code} q{i}: the why cites no KC code and no Learning Objective, so the "
            f"key cannot be traced to the CED -- {item['why'][:90]!r}"
        )
        for text in es.texts(item):
            for pat in FIGURE_LANGUAGE:
                hit = pat.search(text)
                assert not hit, (
                    f"{code} q{i}: figure language {hit.group(0)!r} -- the bank cannot "
                    f"display an image; put the data in a table= instead"
                )
    for i, (_anchor, claim) in enumerate(claims, 1):
        assert cited(claim), (
            f"{code} q{i}: the claim cites no KC code and no Learning Objective: "
            f"{claim[:90]!r}"
        )
    print(f"OK  {code} history gate: every why and claim cites the CED; no figure "
          f"language; no typeset markup, in {len(module.QUESTIONS)} questions.")


# ------------------------------------------------------------------ the control

def _mutant(module):
    m = types.ModuleType(module.__name__ + "_mutant")
    m.TOPIC = module.TOPIC
    m.QUESTIONS = copy.deepcopy(module.QUESTIONS)
    return m


def _run(mod, claims, table_checks):
    """Run every gate on `mod`, silently. Returns the exception, or None."""
    buf = io.StringIO()
    try:
        with contextlib.redirect_stdout(buf):
            history_style(mod, claims)
            cg.check(mod, claims, table_checks=table_checks)
    except AssertionError as exc:
        return exc
    except Exception as exc:  # a KeyError from a corrupted cell counts as caught
        return exc
    return None


def selftest(module, claims, table_checks=None):
    """Break the module on purpose. Every gate below must raise, for its own reason."""
    table_checks = table_checks or {}
    code = module.TOPIC[0]
    clean = _run(module, claims, table_checks)
    assert clean is None, f"{code}: the module does not pass before corruption: {clean}"
    print(f"  positive control OK  {code} passes every gate before corruption")

    failures = []

    def must_fail(label, mutate, expect):
        """`mutate` must make the gate raise, and the message must match `expect`."""
        mod = _mutant(module)
        local = copy.deepcopy(claims)
        mutate(mod, local)
        exc = _run(mod, local, table_checks)
        if exc is None:
            failures.append(f"{label}: nothing raised")
        elif not re.search(expect, str(exc), re.I):
            # A control that fires for the wrong reason proves nothing about the
            # guard it names, so the message is checked, not just the fact of it.
            failures.append(f"{label}: raised for the WRONG reason -- {exc}")

    # 1. every key rotated one place. All thirty must fail, which is what proves
    #    the anchors are distinctive rather than generic English.
    for i in range(len(module.QUESTIONS)):
        def rotate(mod, cl, i=i):
            q = mod.QUESTIONS[i]
            q["ans"] = (q["ans"] + 1) % len(q["choices"])
        must_fail(f"q{i + 1} key rotated", rotate, r"anchor .* not in keyed choice")
    print(f"  control OK  all {len(module.QUESTIONS)} keys fail when rotated off their anchor")

    # 2. every anchor broken in turn -- catches an anchor so generic that the
    #    rotation above passed for an unrelated reason.
    for i in range(len(claims)):
        def break_anchor(mod, cl, i=i):
            cl[i] = ("this anchor matches nothing at all", cl[i][1])
        must_fail(f"q{i + 1} anchor broken", break_anchor, r"anchor .* not in keyed choice")
    print(f"  control OK  all {len(claims)} anchors fail when replaced by a non-matching phrase")

    # 3. every cell of every table corrupted in turn; each table must be
    #    defended by at least one caught corruption, and the count is printed so
    #    a table check that has stopped reading its table shows as a zero.
    for qi, item in enumerate(module.QUESTIONS, 1):
        table = item.get("table")
        if not table:
            continue
        caught = total = 0
        for r in range(len(table["rows"])):
            for c in range(len(table["rows"][r])):
                total += 1
                mod = _mutant(module)
                mod.QUESTIONS[qi - 1]["table"]["rows"][r][c] = es._corrupt(table["rows"][r][c])
                if _run(mod, claims, table_checks) is not None:
                    caught += 1
        if caught == 0:
            failures.append(f"q{qi} table: no corrupted cell was caught")
        print(f"  control OK  q{qi} table: {caught} of {total} corrupted cells caught")

    # 4. notation. Five illegal forms must raise; two legal strings must not --
    #    including "the table below", which the figure-language patterns must
    #    leave alone or every data question in the bank becomes unwritable.
    banned = [
        ("A rise of \\frac{1}{2}", r"backslash"),
        ("A rise of 2^3 units", r"caret"),
        ("The 1945-1991 confrontation", r"digit-hyphen-digit"),
        ("A share of 3/4 of the total", r"digit-slash-digit"),
        ("A cost of $40 per ton", r"dollar sign"),
    ]
    for bad, expect in banned:
        def inject(mod, cl, bad=bad):
            mod.QUESTIONS[0]["choices"][0] = bad
        must_fail(f"notation {bad!r}", inject, expect)
    for legal in ("A confrontation lasting from 1945 to 1991",
                  "The pattern set out in the table below"):
        mod = _mutant(module)
        mod.QUESTIONS[0]["choices"][0] = legal
        buf = io.StringIO()
        try:
            with contextlib.redirect_stdout(buf):
                history_style(mod, claims)
        except AssertionError as exc:
            failures.append(f"the style gate rejected legal prose {legal!r}: {exc}")
    print("  control OK  every banned notation form raises; legal prose and "
          "'the table below' do not")

    # 5. figure language, injected into a stem and into a choice.
    def figure_stem(mod, cl):
        mod.QUESTIONS[0]["q"] = "The map shown here records the following. " + mod.QUESTIONS[0]["q"]

    def figure_choice(mod, cl):
        mod.QUESTIONS[1]["choices"][0] = "The trend depicted in the graph above"

    must_fail("figure language in a stem", figure_stem, r"figure language")
    must_fail("figure language in a choice", figure_choice, r"figure language")
    # positive control for the same gate: the two phrases the brief records as
    # FALSE positives elsewhere must still pass.
    for innocent in ("It offers the fullest picture of the period available",
                     "An age structure diagram used as an analytical concept"):
        mod = _mutant(module)
        mod.QUESTIONS[0]["choices"][0] = innocent
        buf = io.StringIO()
        try:
            with contextlib.redirect_stdout(buf):
                history_style(mod, claims)
        except AssertionError as exc:
            failures.append(f"the figure gate rejected innocent prose {innocent!r}: {exc}")
    print("  control OK  figure language raises; 'the fullest picture of' and "
          "'age structure diagram' do not")

    # 6. the citation rule, in a why and in a claim.
    def uncited_why(mod, cl):
        mod.QUESTIONS[3]["why"] = ("This is true because the historical record of the "
                                   "twentieth century plainly shows that it is true.")

    def uncited_claim(mod, cl):
        cl[4] = (cl[4][0], "This rests on what any well prepared student already knows "
                           "about the twentieth century and needs no further support.")

    must_fail("a why with no CED citation", uncited_why, r"cites no KC code")
    must_fail("a claim with no CED citation", uncited_claim, r"cites no KC code")
    print("  control OK  an uncited why and an uncited claim both raise")

    # 7. the structural gates inherited from cg_check.
    def duplicate_choice(mod, cl):
        mod.QUESTIONS[0]["choices"][-1] = mod.QUESTIONS[0]["choices"][0]

    def thin_why(mod, cl):
        mod.QUESTIONS[1]["why"] = "KC-6.2.II."

    def letter_reference(mod, cl):
        mod.QUESTIONS[2]["why"] = ("Option B is wrong, and KC-6.2.IV.D settles the rest "
                                   "of the reasoning without any further argument.")

    must_fail("a distractor made identical to the key", duplicate_choice,
              r"duplicate choice|contained in choice")
    must_fail("a why cut below the minimum length", thin_why, r"why too thin")
    must_fail("a why naming an option by letter", letter_reference, r"names an option by letter")
    print("  control OK  duplicate choice, thin why and letter reference all raise, "
          "each for its own reason")

    if failures:
        raise SystemExit(f"CONTROL FAILED for {code}:\n  " + "\n  ".join(failures))
    print(f"all negative controls raised as required for {code}.")


def run(module, claims, table_checks=None, argv=()):
    """The two lines every World History verifier ends with."""
    if "--selftest" in argv:
        selftest(module, claims, table_checks)
    history_style(module, claims)
    cg.check(module, claims, table_checks=table_checks)
