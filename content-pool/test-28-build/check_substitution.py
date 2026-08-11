#!/usr/bin/env python3
"""Substitute every choice into every blank and read the seam.

The defect this exists to catch: a choice whose text runs PAST the blank and
collides with the words the passage already supplies on the other side of it.
Test 28 drafted four of them, and one was in a KEY, not a distractor:

    B7  "quarter; yet the"          + "the custom was never..."  -> "yet the the custom"
    B2  "ground; the amended bill and" + "was published..."      -> "bill and was published"
    B3  "wall; in"                  + "in the loose boxes..."    -> "wall; in in the loose"
    B12 "years; the"                + "the remaining five..."    -> "years; the the remaining"

Reading the option list alone will never show any of them - each option is
well formed in isolation. Only substitution does, which is why this is
mechanical and runs over all four options of every item rather than the key.

Three design notes, all learned the hard way in this repo:

  * The seam is the only place worth checking. A first cut ran its patterns
    over the whole substituted passage and reported 97 findings, 93 of them
    ordinary compound predicates ("stood tied and faced", "walks steadily and
    will make") that have nothing to do with the blank. A check that
    over-matches trains you to ignore its output.
  * Narrowing to a window around the insert was not enough either - it still
    caught compound predicates that merely sat near the blank. DOUBLE and
    DANGLE therefore require the match to STRADDLE the edge of the inserted
    text: one word from the choice, one from the passage. That is the defect,
    stated exactly, and it drops the false positives to zero.
  * Doubling has to tolerate punctuation between the two words, because the
    collision that matters is "years; the the" - the choice supplies both the
    mark and the word.

Checks, per substituted sentence:
  DOUBLE   the same word twice running across the seam, punctuation allowed
  DANGLE   a coordinating conjunction left across the seam before a finite verb
  DUPSTOP  doubled punctuation (,, ;; . ,)
  SPACEDOT whitespace in front of a full stop or comma
  IDENT    two options that substitute to exactly the same sentence
"""
import re
import sys

from rw_test28 import QUESTIONS

BLANK = "_____"

FINITE = (r"was|were|is|are|had|has|have|did|does|do|went|came|paid|took|"
          r"stood|ran|cost|made|passed|carried|published|charged|left|gave")
# Must straddle the edge of the inserted choice: one side from the choice, the
# other from the passage.
STRADDLE = (
    ("DOUBLE", re.compile(r"\b([A-Za-z]+)\b[\s,;:.]+\1\b", re.I)),
    ("DANGLE", re.compile(rf"\b(?:and|or|but|yet|nor)\s+(?:{FINITE})\b", re.I)),
)
# Typography; anywhere in the substituted sentence is a finding.
ANYWHERE = (
    ("DUPSTOP", re.compile(r"[,;:.]\s*[,;:.]")),
    ("SPACEDOT", re.compile(r"\s+[,.;:]")),
)


def plain(html):
    t = re.sub(r"<[^>]+>", " ", html)
    t = t.replace("&ldquo;", '"').replace("&rdquo;", '"')
    t = t.replace("&pound;", "GBP")
    return re.sub(r"\s+", " ", t).strip()


def seams(q):
    """Yield (letter, sentence, insert_start, insert_end) for each choice.

    Only items with an inline blank are yielded: for a Central Ideas or
    Synthesis item the choice is a free-standing sentence with no seam at all,
    and running the seam patterns over it reports its ordinary compound verbs.
    """
    passage = q["passage"]
    if BLANK not in passage:
        return
    # Mark the blank, normalise ONCE, then split on the mark, so the passage
    # keeps its own spacing around the blank. Stripping head and tail
    # separately and rejoining with spaces invents a gap that is not in the
    # source - an early cut of this file reported 28 SPACEDOT findings that
    # were all its own punctuation.
    head, _, tail = plain(passage.replace(BLANK, "\x00")).partition("\x00")
    for letter, choice in zip("ABCD", q["choices"]):
        ins = plain(choice)
        yield letter, head + ins + tail, len(head), len(head) + len(ins)


def main(verbose=False):
    findings = 0
    for q in QUESTIONS:
        seen = {}
        for letter, sentence, lo_ins, hi_ins in seams(q):
            seen.setdefault(sentence, []).append(letter)
            if verbose:
                print(f"  {q['num']:4} {letter}  {sentence[max(0,lo_ins-55):hi_ins+55]}")
            for name, pat in STRADDLE + ANYWHERE:
                for m in pat.finditer(sentence):
                    straddles = m.start() < lo_ins < m.end() or \
                                m.start() < hi_ins < m.end()
                    if (name, pat) in STRADDLE and not straddles:
                        continue
                    lo, hi = max(0, m.start() - 45), m.end() + 45
                    print(f"{name:9} {q['num']:4} {letter}  "
                          f"...{sentence[lo:hi]}...")
                    findings += 1
        for sentence, letters in seen.items():
            if len(letters) > 1:
                print(f"IDENT     {q['num']:4} {'/'.join(letters)}  "
                      "substitute to the same sentence")
                findings += 1

    n_blank = sum(BLANK in q["passage"] for q in QUESTIONS)
    print(f"\n{len(QUESTIONS)} items, {n_blank} with an inline blank, "
          f"{findings} findings")
    return 1 if findings else 0


if __name__ == "__main__":
    sys.exit(main(verbose="-v" in sys.argv))
