"""Structural gate for AP U.S. Government 3.4 First Amendment: Freedom of the Press.

gov345_check plus the four usgov_anchor helpers, following verify_v3_3.py.

ONE SENTENCE, THREE LOAD-BEARING PARTS
----------------------------------------
EK 3.4.A.1 is the smallest essential-knowledge base in this half of the course:
"The Supreme Court bolstered the freedom of the press, affirming support for a
heavy presumption against prior restraint even in cases involving national
security." Three things have to survive intact, and each has a check or an item
built for it:

  PRIOR RESTRAINT     government stopping publication BEFORE it happens, which
                      is not the same as punishing what has been published.
                      _prior_restraint below fails the module if any key or
                      rationale treats the holding as immunity from consequences
                      generally. That is the single most common error about this
                      case and item 27 exists to correct it.
  HEAVY PRESUMPTION   a burden, not a bar. _presumption asserts no key upgrades
                      it into an absolute prohibition, because doing so makes
                      LO 3.4.A's question about the EXTENT of the commitment
                      unanswerable.
  EVEN IN CASES INVOLVING NATIONAL SECURITY
                      an a fortiori clause, not an exception. Items 7 and 16
                      turn on the direction it runs, since reading it as a
                      carve-out inverts the sentence.

SKILL 4.D WITH NO CARTOON
--------------------------
The CED's visual sources for this topic are cartoons, maps and infographics,
and this bank cannot ship a cartoon. What a table CAN carry honestly is the
part of 4.D about ARRANGEMENT: items 22 and 25 ask what the grouping invites a
reader to compare and what it leaves out, and item 26 asks what a reader would
wrongly infer from the layout. The timing infographic is deliberately sorted so
the burden column is constant within each block, which is the doctrinal point
made visible -- and q25's arithmetic asserts that sort order, so reshuffling the
rows fails the file rather than quietly destroying the item.
"""
import gov345_check as gc
import usgov_anchor as ua
import v3_4

ANCHORS = {
 1: "A heavy presumption against prior restraint, even in cases involving national security",
 2: "stopping material from being published in the first place",
 3: "a mistaken restraint is invisible",
 4: "the action comes after publication and is therefore not a prior restraint",
 5: "since the order stops publication before it occurs",
 6: "may still seek a prior restraint and will usually fail",
 7: "so a presumption that survives it is strong everywhere else",
 8: "bore a heavy burden to justify stopping publication and did not meet it",
 9: "because it also involved a request to stop publication on national security grounds",
 10: "report what officials would prefer to conceal",
 11: "identifies a specific form of abridgement, restraint before publication",
 12: "A criminal prosecution brought after an article appears",
 13: "made and almost always denied",
 14: "so the restraint operates without any court order",
 15: "the ability to report it beyond that place is what makes the concern possible",
 16: "embarrassment is a far weaker interest",
 17: "the publisher's liberty to publish and the public's ability to learn",
 18: "since the harm cannot be prevented in advance",
 19: "concerns WHEN the government may act against expression",
 20: "whatever its approval rate",
 21: "succeeded in a small minority of cases under every interest asserted",
 22: "none of it speaks to what happens afterward",
 23: "operates against prior restraint even where national security is asserted",
 24: "face a heavy presumption, and the two taken afterward face an ordinary one",
 25: "the burden follows the timing rather than the severity",
 26: "An ordinary presumption is still a burden",
 27: "a publisher may still face suits or prosecution",
 28: "strong on the specific question of advance suppression",
 29: "how often did it succeed, and on what interests did it rely",
 30: "whether government may act before publication",
}

GROUNDING = {
 1: "EK 3.4.A.1, verbatim: the Court affirmed support for 'a heavy presumption against prior "
    "restraint even in cases involving national security.'",
 2: "EK 3.4.A.1's phrase PRIOR restraint: the restraint operates before publication, which is "
    "what places an action inside the presumption.",
 3: "EK 3.4.A.1 read for why the presumption is heaviest at this stage: suppressed material "
    "leaves nothing for the public to weigh.",
 4: "EK 3.4.A.1's presumption applied by TIMING: an action after publication is subject to "
    "ordinary rules, which is not the same as being permitted.",
 5: "EK 3.4.A.1: a judicial order forbidding publication is the paradigm prior restraint. The "
    "distractors name EK 3.3.A.2 categories, which topic 3.3 owns.",
 6: "EK 3.4.A.1's word PRESUMPTION -- a burden the government carries and usually fails to "
    "meet, rather than a bar on trying.",
 7: "EK 3.4.A.1's clause 'even in cases involving national security', read as the a fortiori "
    "it is: a presumption surviving the strongest interest survives weaker ones.",
 8: "New York Times Co. v. United States (1971), required case, which the CED attaches to "
    "3.4.A. CED holding: bolstered freedom of the press, establishing a heavy presumption "
    "against prior restraint even in cases involving national security.",
 9: "New York Times Co. v. United States (1971) as a SCOTUS comparison; the non-required "
    "case's facts are printed in the stem per CED p. 29.",
 10: "LO 3.4.A's commitment to individual liberty read for its consequence: no advance "
     "approval means officials cannot decide what the public learns.",
 11: "U.S. Constitution, First Amendment, quoted verbatim. The text forbids abridgement in "
     "general terms; EK 3.4.A.1 identifies the form most strongly presumed against.",
 12: "EK 3.4.A.1's timing test, applied by exclusion: four options operate before publication "
     "and one after.",
 13: "EK 3.4.A.1 operationalized: a presumption does work when the government tries and loses, "
     "so attempts as well as outcomes must be counted.",
 14: "EK 3.4.A.1 tested by rebuttal, CED skill 5.D: the framework constrains GOVERNMENT "
     "action, so self-censorship suppresses publication outside what it covers.",
 15: "'Letter from a Birmingham Jail' (required document), 'Injustice anywhere is a threat to "
     "justice everywhere,' quoted verbatim; the CED attaches the Letter to 3.4.A.",
 16: "EK 3.4.A.1's national security clause as an a fortiori argument applied to a weaker "
     "asserted interest.",
 17: "LO 3.4.A's 'commitment to individual liberty': the liberty runs to the publisher and to "
     "the reader alike.",
 18: "EK 3.4.A.1's cost, read against EK 3.3.A.2's balance of social order and individual "
     "freedom: a presumption against advance suppression lets some harm through.",
 19: "EK 3.4.A.1 (timing) against EK 3.3.A.2 (type of expression) -- two independent axes, "
     "which is why the framework gives them separate topic codes.",
 20: "EK 3.4.A.1's presumption attaches to the STRUCTURE of advance approval; the power to "
     "decide in advance is itself the restraint.",
 21: "Data item on a labelled hypothetical infographic; all four success rates are recomputed "
     "below.",
 22: "CED skill 4.D, arrangement: grouping by asserted interest puts the interests side by "
     "side, and the whole table is confined to prior restraints.",
 23: "EK 3.4.A.1 measured: two successes in twenty-three national security attempts.",
 24: "Data item on a labelled hypothetical infographic; the timing/burden pairing is "
     "recomputed below.",
 25: "CED skill 4.D, arrangement: sorting by timing makes the burden column constant within "
     "each block, which is the doctrinal point stated visually.",
 26: "CED skill 3.E and 4.D together: the column reads Ordinary rather than None, and reading "
     "a lighter burden as no burden is the inference the layout invites.",
 27: "EK 3.4.A.1's scope: the presumption is against PRIOR restraint, not immunity from every "
     "consequence. The most common error about this holding.",
 28: "LO 3.4.A's 'extent to which', answered against a sentence that is precise about what it "
     "covers -- reading more or less into it both misstate it.",
 29: "EK 3.4.A.1 operationalized: count attempts, outcomes and the interests asserted.",
 30: "EK 3.4.A.1 against EK 3.3.A.2: government action sorted by timing rather than expression "
     "sorted by type, so neither topic subsumes the other.",
}

ATTEMPTS_H, SUCCEEDED = "Attempts to block publication", "Attempts that succeeded"
SECURITY = "National security"
TRIAL = "Protecting an ongoing trial"
REPUTATION = "Protecting a person's reputation"
EMBARRASS = "Preventing embarrassment to an agency"
WHEN, BURDEN = "Before or after publication", "Presumption the government must overcome"


def _cell(t, label, header):
    j = t["headers"].index(header)
    for r in t["rows"]:
        if r[0] == label:
            return r[j]
    raise KeyError(label)


def _col(t, header):
    j = t["headers"].index(header)
    return [r[j] for r in t["rows"]]


def _rate(t, label):
    return gc.num(_cell(t, label, SUCCEEDED)) / gc.num(_cell(t, label, ATTEMPTS_H))


def q21(t):
    """Every asserted interest fails far more often than it succeeds."""
    rates = {r[0]: _rate(t, r[0]) for r in t["rows"]}
    assert all(v < 0.5 for v in rates.values()), f"a row succeeds in a majority: {rates}"
    assert max(rates, key=lambda k: gc.num(_cell(t, k, ATTEMPTS_H))) == REPUTATION, \
        "reputation is not the most frequently asserted interest"
    assert rates[EMBARRASS] == 0.0, "the embarrassment row is not zero"
    assert rates[EMBARRASS] < rates[SECURITY], \
        "embarrassment succeeds at least as often as national security"
    return ("success rates " + ", ".join(f"{k.split()[0].lower()} {v:.0%}"
                                         for k, v in rates.items()))


def q22(t):
    """The arrangement groups by asserted interest and covers only prior restraints."""
    assert t["headers"][0].startswith("Interest asserted"), \
        "the table is no longer grouped by asserted interest"
    assert "block publication" in ATTEMPTS_H, \
        "the count column no longer says these are attempts to BLOCK publication"
    assert not any("after" in h.lower() for h in t["headers"]), \
        "a column now reports action after publication, which the item says is absent"
    return "grouped by asserted interest; every row is an attempt made before publication"


def q23(t):
    """The security row is the one EK 3.4.A.1's clause is about."""
    assert SECURITY in _col(t, t["headers"][0]), "no national security row"
    assert _rate(t, SECURITY) < 0.15, \
        f"security attempts succeed {_rate(t, SECURITY):.0%}, too often to show the presumption"
    return (f"national security: {gc.num(_cell(t, SECURITY, SUCCEEDED)):.0f} of "
            f"{gc.num(_cell(t, SECURITY, ATTEMPTS_H)):.0f} attempts succeeded")


def q24(t):
    """Burden follows timing: Before is Heavy, After is Ordinary, without exception."""
    pairs = list(zip(_col(t, WHEN), _col(t, BURDEN)))
    assert all(b == "Heavy" for w, b in pairs if w == "Before"), "a Before row is not Heavy"
    assert all(b == "Ordinary" for w, b in pairs if w == "After"), \
        "an After row is not Ordinary"
    assert _col(t, WHEN).count("Before") == 2 and _col(t, WHEN).count("After") == 2, \
        f"the timing column is {_col(t, WHEN)}"
    return "two Before rows both Heavy, two After rows both Ordinary"


def q25(t):
    """The sort order is what makes the doctrine visible, so it is asserted."""
    assert _col(t, WHEN) == ["Before", "Before", "After", "After"], \
        f"the rows are no longer sorted by timing: {_col(t, WHEN)}"
    assert _col(t, BURDEN) == ["Heavy", "Heavy", "Ordinary", "Ordinary"], \
        "the burden column is no longer constant within each timing block"
    return "rows sorted Before, Before, After, After, so the burden column runs in two blocks"


def q26(t):
    """An ordinary presumption is still a presumption, which the wording must preserve."""
    assert "Ordinary" in _col(t, BURDEN), "the lighter burden is no longer labelled"
    assert "None" not in _col(t, BURDEN), \
        "a row now reads None, which would make the item's correction false"
    assert "Presumption" in BURDEN, \
        "the column no longer says the government must overcome a presumption"
    return "the lighter burden reads Ordinary rather than None, so a burden remains"


def _prior_restraint(module):
    """No key may treat the holding as immunity from consequences after publication."""
    bad = []
    for i, item in enumerate(module.QUESTIONS, 1):
        for label, s in (("key", item["choices"][item["ans"]]), ("why", item["why"])):
            low = s.lower()
            for phrase in ("without consequence", "immune from suit", "may publish anything",
                           "never be sued", "never be prosecuted"):
                if phrase in low and not any(n in low for n in ("not ", "still", "rather than",
                                                               "may still")):
                    bad.append(f"q{i} {label}: {phrase!r} treats EK 3.4.A.1 as immunity from "
                               "consequences; the presumption is against PRIOR restraint only")
    if bad:
        print(f"FAIL {module.__name__} prior restraint")
        for b in bad:
            print("  -", b)
        raise SystemExit(1)
    print(f"OK  {module.__name__} prior restraint: no key or rationale treats the holding as "
          "immunity from suits or prosecution after publication")


def _presumption(module):
    """A heavy presumption is a burden, not a bar."""
    bad = []
    for i, item in enumerate(module.QUESTIONS, 1):
        key = item["choices"][item["ans"]].lower()
        if "prior restraint" not in key:
            continue
        for phrase in ("absolute prohibition", "may never seek", "is barred from seeking",
                       "prohibited from ever"):
            if phrase in key:
                bad.append(f"q{i} key: upgrades EK 3.4.A.1's heavy PRESUMPTION into an "
                           f"absolute bar ({phrase!r})")
    if bad:
        print(f"FAIL {module.__name__} presumption")
        for b in bad:
            print("  -", b)
        raise SystemExit(1)
    print(f"OK  {module.__name__} presumption: no key states EK 3.4.A.1's heavy presumption as "
          "an absolute prohibition")


ua.shape(v3_4)
ua.check(v3_4, ANCHORS, GROUNDING)
ua.notation(v3_4)
_prior_restraint(v3_4)
_presumption(v3_4)
gc.check(v3_4, arith={21: q21, 22: q22, 23: q23, 24: q24, 25: q25, 26: q26})

# WHAT THE REVIEW FOUND
# ---------------------
# No wrong key. What is worth recording is how a topic with ONE essential-
# knowledge sentence was kept from becoming thirty rewordings of it.
#
# The sentence has three separable parts -- prior restraint, heavy presumption,
# even in national security cases -- and each supports a different kind of
# error, so each gets its own block of items and its own guard. A student can
# know the case and still think it means the press cannot be sued (items 4, 12,
# 27), or that the government may not even ask (items 6, 20), or that national
# security is the exception rather than the hardest case the rule survives
# (items 7, 16). Those are three different misunderstandings of one sentence,
# and a module that only asked "what did the Court hold" would catch none of
# them.
#
# The other decision is the 4.D one. The CED's visual sources here are cartoons,
# maps and infographics, and no bank of this kind can ship a cartoon. Rather
# than skip the skill, the two stimuli are infographics whose items ask about
# ARRANGEMENT -- what the grouping invites you to compare, what it excludes,
# what the layout makes a reader wrongly infer. q25 asserts the timing table's
# sort order for that reason: the doctrine is visible only because the rows are
# blocked Before, Before, After, After, and a reshuffle would leave every number
# intact while destroying the point.
