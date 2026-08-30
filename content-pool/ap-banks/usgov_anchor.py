"""The anchor-and-grounding gate every AP U.S. Government verifier runs.

``usgov_check.check`` enforces the key-first invariant: ``ans == 0`` on every
question. That guards the INDEX. It does not guard the TEXT, and the text is
what a later edit moves. Reorder a choice list, rewrite the first option, or
sharpen a distractor until it says what the key says, and ``ans`` is still 0 and
every structural check still passes.

So each verifier carries two per-question maps, and this module checks them:

ANCHORS
    A literal substring that must appear in the KEYED choice and in none of the
    other four. Comparison is case-sensitive and literal on purpose -- a
    normalised comparison would let a distractor edited to differ only in
    punctuation slip through. Written against the choice text as it stands, the
    map doubles as a compact record of what each item is keyed on, readable
    without opening the module.

GROUNDING
    The CED essential-knowledge statement, required Supreme Court case,
    foundational document or constitutional provision the key traces back to.
    SOCIAL_BRIEF.md's rule for these subjects is that a key must trace to the
    CED rather than to the author's memory; an unwritten trace is not a trace.
    Writing thirty of them is the review pass, because it cannot be done
    without deciding, item by item, what makes the key true. Every wrong key
    and wrong figure found in this bank so far was found doing it.

Neither map can check the politics. That is stated plainly in usgov_check.py
and it is still true here: nothing mechanical knows that McCulloch is about
federal supremacy. What these maps guarantee is that the human who did know
wrote it down, and that no later edit silently detaches a key from the choice
it was written for.
"""

MIN_GROUNDING = 40


def check(module, anchors, grounding):
    qs = module.QUESTIONS
    bad = []
    for i, item in enumerate(qs, 1):
        anchor = anchors.get(i)
        if not anchor:
            bad.append(f"q{i}: no anchor")
        else:
            key = item["choices"][item["ans"]]
            if anchor not in key:
                bad.append(f"q{i}: anchor {anchor!r} is not in the keyed choice {key!r}")
            for k, c in enumerate(item["choices"]):
                if k != item["ans"] and anchor in c:
                    bad.append(f"q{i}: anchor {anchor!r} also appears in distractor "
                               f"{'ABCDE'[k]}, so it does not identify the key")
        if len(grounding.get(i, "").strip()) < MIN_GROUNDING:
            bad.append(f"q{i}: grounding is missing or too thin to be a citation")
    for i in sorted(set(anchors) | set(grounding)):
        if not 1 <= i <= len(qs):
            bad.append(f"anchor/grounding names q{i}, which does not exist")
    if bad:
        print(f"FAIL {module.__name__} anchors/grounding")
        for b in bad:
            print("  -", b)
        raise SystemExit(1)
    print(f"OK  {module.__name__} anchors: {len(anchors)} keys pinned to a distinctive "
          f"substring of their own choice text; {len(grounding)} keys traced to a CED "
          "statement, required case, foundational document or constitutional provision")
