"""Structural gate for AP U.S. Government 5.13 Changing Media.

gov345_check plus the four usgov_anchor helpers, plus two content gates and a
negative control for each.

  _uncommitted
      This topic's two load-bearing words are both deliberately uncommitted, and
      both are ones a student and an author already hold an opinion about.

      EK 5.13.A.2's noun is DEBATES: the growth of outlets "led to DEBATES OVER
      media bias and the impact of media ownership and partisan news sites". The
      framework does not say the media are biased and does not say they are not.
      So no key may assert either; a key that touches bias must keep it as a
      debate, a question, or a thing respondents SAY.

      EK 5.13.A.3's verb is AFFECTED, with no direction: "The nature of
      democratic debate and the level of political knowledge among citizens IS
      AFFECTED BY" its four factors. Not raised, not lowered. So no key may
      attach a direction to either quantity.

      Neither restraint is visible to any structural check. An item asserting
      that increased choice lowers political knowledge is well formed, plausible
      and confidently wrong about what the course says, which is precisely the
      class of defect this subject has no computation to catch.

  _lists
      The framework enumerates twice -- EK 5.13.A.1's three forms of media
      output (coverage, ANALYSIS, commentary) and EK 5.13.A.3's four factors --
      and the items that enumerate them must keep every member. A key that drops
      "analysis" from the triple still reads as a complete answer, and an anchor
      pinned to a surviving fragment of the same choice would not notice. So the
      membership is asserted directly.

THE ARITHMETIC
--------------
Items 25 to 27 share a hypothetical survey grouping respondents by how many news
sources they use regularly; items 28 to 30 share a hypothetical survey grouping
them by the kind of outlet they mainly use.

Both tables are HYPOTHETICAL and say so in the stems, and the second reports
only what respondents SAY. That is the design rather than a caption: EK 5.13.A.2
is about debates, so a survey of opinion is evidence within the debate and not a
finding about any outlet. Item 30's key rests on exactly that, and the
recomputation checks it structurally -- every data header in that table must
begin with "Say", so the claim is a property of the table rather than a promise
in the stem.

The first table is built so it cannot be read one way. Political knowledge,
participation AND self reinforcing source selection all rise together, which is
why item 27 can refuse a direction without denying the pattern. The
recomputation asserts that all three rise, because if an edit reversed the third
column the item's correction would collapse while still reading correctly.

NEGATIVE CONTROLS
-----------------
Every gate below is run against a deliberately corrupted copy and must fail. A
checker that cannot fail is worse than none. The controls corrupt: a key
settling the bias debate, a key attaching a direction to political knowledge, a
key dropping ANALYSIS from EK 5.13.A.1's triple, a table figure that reverses
the reinforcement column item 27 depends on, and a header that turns a
self report into a claim about outlet content.
"""
import contextlib
import io
import types

import gov345_check as gc
import usgov_anchor as ua
import v5_13

ANCHORS = {
 1: "Political participation",
 2: "Coverage, analysis, and commentary",
 3: "meaning what citizens do rather than how they come by information",
 4: "Debates over media bias and the impact of media ownership",
 5: "An ideologically diverse audience",
 6: "which reports a dispute rather than settling it",
 7: "The nature of democratic debate and the level of political knowledge",
 8: "Increased media choices, ideologically oriented programming, consumer driven outlets",
 9: "Reinforcing existing beliefs",
 10: "The credibility of news sources and information",
 11: "Ideologically oriented programming",
 12: "does not say in which direction",
 13: "Political institutions and behavior",
 14: "Consumer driven outlets and emerging technologies that reinforce existing beliefs",
 15: "Uncertainty over the credibility of news sources and information",
 16: "Ideologically oriented programming",
 17: "which names debates over the impact of media ownership",
 18: "relates to a relevant political principle, institution, process, policy, or behavior",
 19: "disputes about what they publish are argued out among citizens",
 20: "because a heavy presumption runs against stopping publication in advance",
 21: "because political spending by corporations was held to be protected speech",
 22: "That the growth was directed by government policy or by a decision of any single owner",
 23: "Whether increased media choices have raised or lowered the level of political knowledge",
 24: "from increasing demand to increased choices",
 25: "including the share saying most of their sources share their own point of view",
 26: "and outlets and technologies that reinforce existing beliefs",
 27: "without saying in which direction, and this table's third column rises alongside the first",
 28: "the most likely to say media bias is a serious problem",
 29: "which names debates over media bias and the impact of media ownership",
 30: "so the table is evidence about a debate rather than a finding about any outlet",
}

GROUNDING = {
 1: "EK 5.13.A.1's own words: POLITICAL PARTICIPATION is influenced by a variety of media "
    "coverage, analysis, and commentary on political events.",
 2: "EK 5.13.A.1's three named forms of media output, which differ in kind: what happened, what "
    "it means, and what should be thought of it.",
 3: "EK 5.12.A.1 against EK 5.13.A.1. The earlier statement's object is how citizens routinely "
    "acquire political information; this one's object is political participation.",
 4: "EK 5.13.A.2's own words: the rapidly increasing demand has LED TO DEBATES OVER media bias "
    "and the impact of media ownership and partisan news sites.",
 5: "EK 5.13.A.2's phrase, demand from an IDEOLOGICALLY DIVERSE AUDIENCE, which locates the "
    "driver of the growth in what audiences want.",
 6: "EK 5.13.A.2's noun DEBATES. The framework records that an argument exists and takes no side "
    "in it, so neither side may be keyed as course content.",
 7: "EK 5.13.A.3's two named subjects: the NATURE OF DEMOCRATIC DEBATE and the LEVEL OF "
    "POLITICAL KNOWLEDGE among citizens.",
 8: "EK 5.13.A.3's four listed factors, in the order the framework gives them.",
 9: "EK 5.13.A.3.iii: consumer driven media outlets and emerging technologies THAT REINFORCE "
    "EXISTING BELIEFS.",
 10: "EK 5.13.A.3.iv: uncertainty over THE CREDIBILITY OF NEWS SOURCES AND INFORMATION, which "
     "is a state of doubt in the audience rather than a measured property of a source.",
 11: "EK 5.13.A.3.ii, the only one of the four factors describing what a program contains rather "
     "than how many options exist, what technologies do, or what audiences are unsure of.",
 12: "EK 5.13.A.3's verb, IS AFFECTED BY, with no direction attached to any of the four factors. "
     "Supplying one adds to the course content rather than reading it.",
 13: "LO 5.13.A's object: increasingly diverse choices of media and communication outlets "
     "influence POLITICAL INSTITUTIONS AND BEHAVIOR.",
 14: "EK 5.13.A.3.iii applied to a recommendation shaped by what the viewer already accepts.",
 15: "EK 5.13.A.3.iv applied to a reader unable to judge a site's reliability.",
 16: "EK 5.13.A.3.ii applied to programming argued consistently from one ideological standpoint.",
 17: "EK 5.13.A.2's named debate over THE IMPACT OF MEDIA OWNERSHIP, applied to an argument "
     "about concentrated ownership in one market.",
 18: "CED skill 2.D as stated (p. 14 and p. 116) and assigned to this topic. Skill 2.C compares "
     "a required case with a non-required one and 2.A describes a case, which are different.",
 19: "New York Times Co. v. United States (1971), required case. CED holding (p. 30): a heavy "
     "presumption against prior restraint even in cases involving national security, related "
     "under skill 2.D to the growth of outlets EK 5.13.A.2 describes.",
 20: "The same holding related under skill 2.D to a BEHAVIOR: a citizen acting on the "
     "uncertainty EK 5.13.A.3.iv names by asking government to block publication in advance.",
 21: "Citizens United v. Federal Election Commission (2010), required case. CED holding (p. 30): "
     "political spending by corporations, associations and labor unions is a form of protected "
     "speech under the First Amendment, related under skill 2.D to a state policy.",
 22: "EK 5.13.A.2's causal direction. The framework attributes the growth to demand from an "
     "ideologically diverse audience, which is an explanation running from audiences to outlets "
     "rather than from government or owners to audiences.",
 23: "The limit of EK 5.13.A.3. It states that the level of political knowledge is affected and "
     "attaches no direction, so neither a rise nor a fall is course content.",
 24: "LO 5.13.A's INCREASINGLY DIVERSE CHOICES, EK 5.13.A.2's RAPIDLY INCREASING DEMAND and EK "
     "5.13.A.3.i's INCREASED MEDIA CHOICES, all three of which describe a direction of change.",
 25: "Recomputed from the table: all three columns rise at every step, including the share "
     "saying most of their sources share their own point of view.",
 26: "EK 5.13.A.3's level of political knowledge and its factor iii on reinforcement, matched to "
     "the two columns that measure each.",
 27: "EK 5.13.A.3's directionless verb, checked against the table: knowledge and self "
     "reinforcing source selection rise together, so no single direction can be read out of it.",
 28: "Recomputed from the table: the opinion oriented group holds the highest bias share and the "
     "lowest share encountering disagreement.",
 29: "EK 5.13.A.2's named debates over media bias and over the impact of media ownership, "
     "matched to the two columns, which peak in different groups.",
 30: "Recomputed from the table's own headers: every data column reports what a group SAYS, so "
     "the table is evidence within EK 5.13.A.2's debate rather than a finding about an outlet.",
}


# --- content gate 1: the two words the framework leaves uncommitted -----------
_BIAS_SETTLED = ("the media are biased", "the media are not biased",
                 "outlets are biased", "outlets are not biased",
                 "media is biased", "media is not biased",
                 "the press is biased", "the press is not biased")
_BIAS_OK = ("debate", "debates", "dispute", "question", "say", "says", "whether",
            "argued", "argument")
_DIRECTION = ("raised", "raise", "raises", "lowered", "lower", "lowers",
              "increased", "increases", "improved", "improves",
              "reduced", "reduces", "worsened", "worsens", "degraded")
_SUBJECTS = ("political knowledge", "democratic debate")
# INCREASED MEDIA CHOICES is EK 5.13.A.3's own factor name, so the word
# "increased" inside it is the framework's, not a direction the author supplied.
# It is stripped before the direction scan; nothing else is.
_FACTOR_NAME = "increased media choices"
# Two constructions state the ABSENCE of a direction and must therefore be
# allowed to contain direction words. Both are spelled out in full rather than
# keyed on a single word like "whether", because "whether X matters is settled:
# it raised Y" contains "whether" and asserts a direction anyway -- control 6
# corrupts a key to exactly that shape and requires the gate to still fire.
_DISCLAIMERS = ("does not say in which direction", "raised or lowered",
                "without saying in which direction")


def _uncommitted(module):
    """No key may settle EK 5.13.A.2's debate or give EK 5.13.A.3's verb a direction."""
    bad = []
    for i, item in enumerate(module.QUESTIONS, 1):
        key = item["choices"][item["ans"]]
        norm = gc.normalize(key)
        for settled in _BIAS_SETTLED:
            if gc.normalize(settled) in norm:
                bad.append(f"q{i}: the key asserts {settled!r}. EK 5.13.A.2 names DEBATES over "
                           "media bias and takes no side in them")
        if "bias" in norm and not any(f" {w} " in f" {norm} " for w in _BIAS_OK):
            bad.append(f"q{i}: the key mentions bias without keeping it a debate, a question or "
                       "a thing respondents say")
        scan = norm.replace(_FACTOR_NAME, " ")
        disclaimed = any(d in norm for d in _DISCLAIMERS)
        if any(s in norm for s in _SUBJECTS) and not disclaimed:
            for word in _DIRECTION:
                # Padded so containment is measured on whole words: "raise"
                # must not match inside "raised", each is listed separately.
                if f" {word} " in f" {scan} ":
                    bad.append(f"q{i}: the key attaches {word!r} to one of EK 5.13.A.3's two "
                               "subjects. The framework's verb is AFFECTED, with no direction")
    # The two items whose whole point is the missing direction must say so.
    for i in (12, 27):
        norm = gc.normalize(module.QUESTIONS[i - 1]["choices"][module.QUESTIONS[i - 1]["ans"]])
        if "in which direction" not in norm and "affected" not in norm:
            bad.append(f"q{i}: the key no longer records that the framework withholds a "
                       "direction, which is the whole content of the item")
    if bad:
        print(f"FAIL {module.__name__} uncommitted")
        for b in bad:
            print("  -", b)
        raise SystemExit(1)
    print(f"OK  {module.__name__} uncommitted: no key settles EK 5.13.A.2's bias debate and no "
          "key gives EK 5.13.A.3's AFFECTED a direction")


# --- content gate 2: the framework's two enumerations survive intact ----------
_TRIPLE = ("coverage", "analysis", "commentary")
_FOUR = ("increased media choices", "ideologically oriented programming",
         "reinforce existing beliefs", "credibility of news sources")


def _lists(module):
    """The enumerating items must keep every member of the framework's lists."""
    bad = []
    k2 = gc.normalize(module.QUESTIONS[1]["choices"][module.QUESTIONS[1]["ans"]])
    for member in _TRIPLE:
        if member not in k2:
            bad.append(f"q2: the key drops {member!r} from EK 5.13.A.1's three forms of media "
                       "output. A shortened list still reads as a complete answer")
    k8 = gc.normalize(module.QUESTIONS[7]["choices"][module.QUESTIONS[7]["ans"]])
    for member in _FOUR:
        if gc.normalize(member) not in k8:
            bad.append(f"q8: the key drops {member!r} from EK 5.13.A.3's four factors")
    if bad:
        print(f"FAIL {module.__name__} lists")
        for b in bad:
            print("  -", b)
        raise SystemExit(1)
    print(f"OK  {module.__name__} lists: EK 5.13.A.1's three forms and EK 5.13.A.3's four "
          "factors are each complete in the key of the item that enumerates them")


# --- the arithmetic -----------------------------------------------------------
KNOW = "Can name their own representative (%)"
PART = "Took part in a political activity (%)"
SAME = "Say most sources share their own point of view (%)"
BIASCOL = "Say media bias is a serious problem (%)"
OWNCOL = "Say they can usually tell who owns their main outlet (%)"
DISAGREE = "Say they regularly encounter views they disagree with (%)"


def _col(table, header):
    """Column by header NAME, keyed by row label. Never by index -- inserting a
    column must not silently repoint a check at different numbers."""
    j = table["headers"].index(header)
    return {r[0]: gc.num(r[j]) for r in table["rows"]}


def _rising(table):
    order = [r[0] for r in table["rows"]]
    out = {}
    for header in (KNOW, PART, SAME):
        col = _col(table, header)
        vals = [col[k] for k in order]
        assert all(b > a for a, b in zip(vals, vals[1:])), (
            f"{header} does not rise at every step: {vals}")
        out[header] = vals
    return order, out


def q25(table):
    order, cols = _rising(table)
    return (f"all three columns rise at every step: knowledge {cols[KNOW][0]:.0f}% to "
            f"{cols[KNOW][-1]:.0f}%, participation {cols[PART][0]:.0f}% to {cols[PART][-1]:.0f}%, "
            f"and agreeing sources {cols[SAME][0]:.0f}% to {cols[SAME][-1]:.0f}%")


def q26(table):
    order, cols = _rising(table)
    assert len(order) >= 3, order
    return ("the knowledge column and the agreeing sources column both rise across the same "
            "groups, which is EK 5.13.A.3's political knowledge and its reinforcement factor "
            "measured side by side")


def q27(table):
    order, cols = _rising(table)
    # The correction is only available because the third column rises WITH the
    # first. Reverse it and the item's own reasoning disappears.
    assert cols[SAME][-1] > cols[SAME][0], cols[SAME]
    assert cols[KNOW][-1] > cols[KNOW][0], cols[KNOW]
    return ("knowledge and self reinforcing source selection rise together, so the table "
            "supports no single direction for EK 5.13.A.3's effect")


def _says(table):
    """Every data column of the audience table reports a self report."""
    for header in table["headers"][1:]:
        assert header.startswith("Say "), (
            f"data column {header!r} does not report what respondents SAY, so the table would be "
            "a claim about outlet content rather than evidence within a debate")
    return _col(table, BIASCOL), _col(table, OWNCOL), _col(table, DISAGREE)


def q28(table):
    bias, own, dis = _says(table)
    op = "An opinion oriented outlet"
    assert max(bias, key=bias.get) == op, f"highest bias share is {max(bias, key=bias.get)}"
    assert min(dis, key=dis.get) == op, f"lowest disagreement share is {min(dis, key=dis.get)}"
    return (f"{op} holds the highest bias share ({bias[op]:.0f}%) and the lowest share "
            f"encountering disagreement ({dis[op]:.0f}%)")


def q29(table):
    bias, own, dis = _says(table)
    assert max(bias, key=bias.get) != max(own, key=own.get), (
        "the bias and ownership columns peak in the same group, so they do not read as two "
        "separate debates")
    return (f"the bias column peaks in {max(bias, key=bias.get)!r} and the ownership column in "
            f"{max(own, key=own.get)!r}, so EK 5.13.A.2's two named debates move separately")


def q30(table):
    bias, own, dis = _says(table)
    return (f"all {len(table['headers']) - 1} data columns report what a group says, so the "
            "table is evidence within EK 5.13.A.2's debate rather than a measurement of any "
            "outlet's content")


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
    # 1. A key settling the debate EK 5.13.A.2 only records.
    m = _copy(v5_13)
    m.QUESTIONS[5]["choices"][0] = "The framework states that the media are biased against one side"
    _must_fail("a key settling EK 5.13.A.2's bias debate", lambda: _uncommitted(m))

    # 2. A key attaching a direction to EK 5.13.A.3's AFFECTED.
    m = _copy(v5_13)
    m.QUESTIONS[11]["choices"][0] = (
        "The framework says increased media choices have lowered the level of political knowledge")
    _must_fail("a key giving EK 5.13.A.3's AFFECTED a direction", lambda: _uncommitted(m))

    # 3. A member dropped from EK 5.13.A.1's triple.
    m = _copy(v5_13)
    m.QUESTIONS[1]["choices"][0] = "Coverage and commentary"
    _must_fail("a key dropping ANALYSIS from EK 5.13.A.1's three forms", lambda: _lists(m))

    # 4. A table figure reversing the column item 27's correction rests on.
    m = _copy(v5_13)
    for item in m.QUESTIONS[24:27]:
        rows = item["table"]["rows"]
        for row, val in zip(rows, ("70", "61", "52", "44")):
            row[3] = val          # the agreeing sources column now falls
    _must_fail("a figure reversing the reinforcement column item 27 depends on",
               lambda: q27(m.QUESTIONS[26]["table"]))

    # 5. A header that turns a self report into a claim about outlet content.
    m = _copy(v5_13)
    for item in m.QUESTIONS[27:30]:
        item["table"]["headers"][1] = "Share of stories showing bias (%)"
    _must_fail("a header turning a self report into a claim about outlet content",
               lambda: q30(m.QUESTIONS[29]["table"]))

    # 6. A direction asserted inside a sentence that merely LOOKS like a
    #    disclaimer. This is the hole a one-word "whether" exemption would open,
    #    which is why the disclaimers are spelled out as whole constructions.
    m = _copy(v5_13)
    m.QUESTIONS[11]["choices"][0] = (
        "Whether media choices matter is settled: they have raised the level of political "
        "knowledge among citizens")
    _must_fail("a direction asserted behind a disclaimer-shaped opening",
               lambda: _uncommitted(m))


ua.shape(v5_13)
ua.check(v5_13, ANCHORS, GROUNDING)
ua.notation(v5_13)
_uncommitted(v5_13)
_lists(v5_13)
gc.check(v5_13, arith={25: q25, 26: q26, 27: q27, 28: q28, 29: q29, 30: q30})
_controls()
