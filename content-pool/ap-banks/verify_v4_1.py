"""Structural gate for AP U.S. Government 4.1 American Attitudes About
Government and Politics.

gov345_check plus the four usgov_anchor helpers, plus two content gates.

  _glosses         EK 4.1.A.1 supplies a parenthesis for each of its four core
                   values, and each parenthesis carries the whole weight of the
                   value:
                     individualism   shaping a life and destiny THROUGH THE
                                     CHOICES ONE MAKES
                     equality of     an EQUAL CHANCE TO COMPETE -- the starting
                     opportunity     line, not the finish
                     free enterprise self-interest, competition, efficient
                                     allocation, and LIMITED regulation (not
                                     none: EK 4.9.A.1 gives "little or no" to
                                     the libertarian position separately)
                     rule of law     EVEN THOSE IN POWER
                   Two of those clauses are load-bearing in a way nothing
                   structural can see. Equality of opportunity restated as
                   equality of outcome is a different political position wearing
                   the framework's label. And "everyone must obey the law",
                   without "even those in power", describes a regime with an
                   exempt ruling class just as well as it describes the value --
                   so a gloss that drops the clause says nothing at all. The
                   gate refuses both substitutions anywhere in a key.

  _interpretations EK 4.1.A.1's grammatical subject is DIFFERENT
                   INTERPRETATIONS of core values, not the values. That is the
                   topic: it is why near-universal agreement on a value coexists
                   with sharp conflict about what government should do in its
                   name, and it is exactly what a definition-recall bank would
                   flatten into "Americans value individualism". The gate
                   refuses any key claiming a value has a single interpretation
                   or determines an attitude on its own, and refuses any key
                   treating the four named values as a complete list -- the
                   framework's own words are SOME of these core values INCLUDE.

WHY BOTH TABLES ARE BUILT THE WAY THEY ARE
------------------------------------------
Each is EK 4.1.A.1's sentence turned into data, from a different side. The first
shows one population endorsing all four values by large majorities while
splitting far more widely on federal programs in their names -- consensus on the
value, conflict on the role of government. The second shows two groups agreeing
on what equality of opportunity plainly means, agreeing on what it does NOT
mean, and diverging only on what it requires of government. Neither table can be
read as showing Americans hold different values, and items 27 and 30 make that
misreading the thing to correct.
"""
import gov345_check as gc
import usgov_anchor as ua
import v4_1

ANCHORS = {
 1: "Different interpretations of core values",
 2: "and the relationship between citizens and the federal government",
 3: "shape their life and destiny through the choices they make",
 4: "all people are given an equal chance to compete",
 5: "concerns the conditions of competition rather than its results",
 6: "efficient allocation of resources, and limited government regulation",
 7: "even those in power, must follow and is accountable to the same laws",
 8: "examples rather than a complete list",
 9: "it is the interpretation rather than the value that shapes their attitude",
 10: "who agree on a value can still disagree sharply about what government should do",
 11: "can be invoked on opposite sides of the same policy question",
 12: "because the framework's gloss covers even those in power",
 13: "because the framework's gloss is an equal chance to compete",
 14: "The pursuit of self-interest",
 15: "a result no one intended can follow from many people pursuing their own ends",
 16: "the framework identifies him as the source of the position",
 17: "not a provision of law a court applies",
 18: "names LIMITED government regulation of the market rather than none",
 19: "Individualism, with the ability of each person to shape their life",
 20: "locates the variation in different interpretations of those values",
 21: "How do citizens who share a value arrive at different views",
 22: "which is what the framework says affects the relationship between citizens and the",
 23: "How citizens regard and treat one another",
 24: "How core values and attitudes about the role of government are connected",
 25: "while support for a program in its name varies far more widely",
 26: "different interpretations of core values affect the relationship between citizens and",
 27: "so the disagreement the table shows is about what government should do",
 28: "agree most closely about removing formal legal barriers and differ most about public",
 29: "Both groups reject the reading that the value guarantees similar outcomes",
 30: "they differ about what it requires of government",
}

GROUNDING = {
 1: "EK 4.1.A.1's grammatical subject, verbatim: 'Different interpretations of core values "
    "affect the relationship between citizens, as well as between citizens and the federal "
    "government.' The subject is the interpretations, not the values.",
 2: "EK 4.1.A.1's two named relationships. The first, between citizens, is easy to lose next "
    "to the more familiar second one.",
 3: "EK 4.1.A.1.i, verbatim: individualism is 'each person has the ability to shape their life "
    "and destiny through the choices they make.'",
 4: "EK 4.1.A.1.ii, verbatim: equality of opportunity is 'all people are given an equal chance "
    "to compete' -- a statement about the starting line.",
 5: "EK 4.1.A.1.ii read against the outcome substitution. A principle about chances and one "
    "about results generate different policy conclusions from the same words, which is the "
    "disagreement EK 4.1.A.1's opening sentence is about.",
 6: "EK 4.1.A.1.iii, verbatim: 'pursuit of self-interest, competition, efficient allocation of "
    "resources, and limited government regulation of the market.' LIMITED, not none.",
 7: "EK 4.1.A.1.iv, verbatim: 'every person, even those in power, must follow and is "
    "accountable to the same laws that govern all.'",
 8: "EK 4.1.A.1's own introduction, 'SOME of these core values INCLUDE', which marks the four "
    "as illustrative rather than exhaustive.",
 9: "EK 4.1.A.1 applied, CED skill 1.D. Two readings of individualism -- that government "
    "should not intervene, and that people must be equipped to make real choices -- are both "
    "interpretations of one value.",
 10: "EK 4.1.A.1's logic: if the values produced the attitudes, agreement on values would "
     "produce agreement on policy. Locating the variation in interpretation is what lets "
     "consensus on a value coexist with conflict over its application.",
 11: "EK 4.1.A.1's list of four values, unranked, with both sides of the scenario drawing on "
     "it. LO 4.1.A's relationship runs in more than one direction.",
 12: "EK 4.1.A.1.iv's parenthesis applied: EVEN THOSE IN POWER is the clause the scenario "
     "turns on.",
 13: "EK 4.1.A.1.ii applied: removing a barrier to entry is an argument about the conditions "
     "of competition. EK 4.1.A.1.iii's free enterprise favours LIMITED regulation, not none.",
 14: "Adam Smith, 'The Wealth of Nations' (document the CED attaches to 4.1.A), quoted "
     "verbatim. EK 4.1.A.1.iii names the pursuit of self-interest first and attributes the "
     "position to Smith in this work.",
 15: "'The Wealth of Nations', quoted verbatim. The passage separates intention from outcome, "
     "which is the argument behind EK 4.1.A.1.iii's pairing of self-interest with efficient "
     "allocation.",
 16: "EK 4.1.A.1.iii, verbatim: free enterprise 'as espoused by Adam Smith in writings such as "
     "The Wealth of Nations.' The framework cites the text as the source of the position.",
 17: "EK 4.1.A.1.iii's category for the work: the source of a CORE VALUE, not a rule of "
     "decision. The same error as citing the Gettysburg Address as a holding in 3.11.",
 18: "EK 4.1.A.1.iii's LIMITED against EK 4.9.A.1's separate libertarian position, which the "
     "framework describes as favouring little or no regulation. Two different positions.",
 19: "EK 4.1.A.1.i's gloss. Each distractor reverses or negates one of the four parentheses, "
     "including the rule of law's EVEN THOSE IN POWER.",
 20: "EK 4.1.A.1's opening words against the inference that shared values imply shared policy "
     "conclusions.",
 21: "LO 4.1.A's own object, the relationship between core values and attitudes about the role "
     "of government, located by EK 4.1.A.1 in interpretation.",
 22: "EK 4.1.A.1 applied to the rule of law, whose gloss explicitly covers those in power. The "
     "dispute is over what accountability requires, not over whether officials are subject.",
 23: "EK 4.1.A.1's first named relationship, 'the relationship between citizens'.",
 24: "LO 4.1.A, verbatim. The framework supplies no dates, no counts and no constitutional "
     "ranking of the four values.",
 25: "Data item, CED skill 1.D. Both column ranges are recomputed below.",
 26: "EK 4.1.A.1's claim shown as data: near-universal endorsement beside widely varying "
     "support for federal programs in the same values' names.",
 27: "Data item: reading variation in the second column as disagreement about the values in "
     "the first. The minimum endorsement is recomputed below.",
 28: "Data item, CED skill 1.D. All four between-group gaps are recomputed below.",
 29: "EK 4.1.A.1.ii's gloss located in the table's third row: both groups reject the outcome "
     "reading, which is the framework's own distinction shown in data.",
 30: "EK 4.1.A.1's difference of INTERPRETATION against a claim of different values. Both the "
     "shared rows and the divergent ones are recomputed below.",
}

ENDORSE, SUPPORT = "Endorse the value (%)", "Support a federal program in its name (%)"
VALUE = "Core value"
LIB, CON = "Self-described liberals (%)", "Self-described conservatives (%)"
REQUIRES = "What the value is taken to require"


def _col(t, header):
    j = t["headers"].index(header)
    return [gc.num(r[j]) for r in t["rows"]]


def _labels(t):
    return [r[0] for r in t["rows"]]


def q25(t):
    """Program support varies far more widely than endorsement does."""
    e, s = _col(t, ENDORSE), _col(t, SUPPORT)
    er, sr = max(e) - min(e), max(s) - min(s)
    assert sr > er, f"support range {sr:.0f} is not wider than endorsement range {er:.0f}"
    assert min(e) > 75, f"the lowest endorsement is {min(e):.0f}, not above three-quarters"
    names = dict(zip(_labels(t), e))
    assert max(names, key=lambda k: names[k]) == "Rule of law", "rule of law is not the highest"
    assert min(names, key=lambda k: names[k]) == "Free enterprise", \
        "free enterprise is not the lowest endorsed"
    return (f"endorsement {min(e):.0f} to {max(e):.0f}, a range of {er:.0f}; program support "
            f"{min(s):.0f} to {max(s):.0f}, a range of {sr:.0f}")


def q26(t):
    """Four named core values, both columns present, and the columns disagree."""
    names = _labels(t)
    assert len(names) == 4 and len(set(names)) == 4, f"the rows are {names}"
    expected = {"Individualism", "Equality of opportunity", "Free enterprise", "Rule of law"}
    assert set(names) == expected, f"the rows are not EK 4.1.A.1's four values: {names}"
    e, s = _col(t, ENDORSE), _col(t, SUPPORT)
    assert all(x > y for x, y in zip(e, s)), \
        "a value draws more program support than endorsement, which the pattern relies on"
    return "EK 4.1.A.1's four values, endorsement above program support in all four rows"


def q27(t):
    """The lowest endorsement is 78, which is agreement rather than disagreement."""
    e, s = _col(t, ENDORSE), _col(t, SUPPORT)
    assert min(e) == 78, f"the lowest endorsement is {min(e):.0f}, not the 78 the key states"
    assert min(e) > 50, "a value fails to reach a majority, which the correction denies"
    assert len(set(s)) == len(s), "two values draw identical program support"
    return (f"lowest endorsement {min(e):.0f} percent; program support "
            f"{', '.join(f'{x:.0f}' for x in s)} -- all distinct")


def _gaps(t):
    lib, con = _col(t, LIB), _col(t, CON)
    return dict(zip(_labels(t), (abs(a - b) for a, b in zip(lib, con))))


def q28(t):
    """Narrowest gap on removing barriers, widest on public funding."""
    gaps = _gaps(t)
    narrow = min(gaps, key=lambda k: gaps[k])
    wide = max(gaps, key=lambda k: gaps[k])
    assert narrow.startswith("Removing formal"), f"the narrowest gap is on {narrow!r}"
    assert wide.startswith("Public funding"), f"the widest gap is on {wide!r}"
    return ("gaps " + ", ".join(f"{k.split()[0]} {v:.0f}" for k, v in gaps.items())
            + f" -- narrowest {gaps[narrow]:.0f}, widest {gaps[wide]:.0f}")


def q29(t):
    """Both groups reject the outcome reading; neither reaches a majority on it."""
    row = [r for r in t["rows"] if "similar outcomes" in r[0]]
    assert len(row) == 1, "the outcome row is missing or duplicated"
    lib, con = gc.num(row[0][1]), gc.num(row[0][2])
    assert lib < 50 and con < 50, f"a group endorses the outcome reading: {lib}, {con}"
    gaps = _gaps(t)
    assert gaps[row[0][0]] != max(gaps.values()), \
        "the outcome row is the widest disagreement, which the key's last distractor denies"
    return f"outcome reading rejected by both groups: {lib:.0f} and {con:.0f} percent"


def q30(t):
    """Shared at the top and the bottom, divergent in the middle two rows."""
    shared = [r for r in t["rows"] if "Removing formal" in r[0]][0]
    outcome = [r for r in t["rows"] if "similar outcomes" in r[0]][0]
    assert min(gc.num(shared[1]), gc.num(shared[2])) >= 84, \
        f"the shared row is {shared[1]}, {shared[2]}, not both above 84"
    assert max(gc.num(outcome[1]), gc.num(outcome[2])) <= 25, \
        f"the outcome row is {outcome[1]}, {outcome[2]}, not both under 25"
    gaps = _gaps(t)
    assert len(set(gaps.values())) == len(gaps), \
        "two rows show identical gaps, which the key's fourth distractor relies on being false"
    big = [k for k, v in gaps.items() if v > 25]
    assert len(big) == 2, f"{len(big)} rows show a gap above 25 points, not two"
    return (f"agreement above 84 on {shared[0]!r}; both under 25 on the outcome reading; "
            f"two rows diverge by more than 25 points")


# --- module-specific content gates -------------------------------------------

_OUTCOME_SUBSTITUTIONS = (
    "equality of opportunity, with the guarantee that all people reach similar results",
    "equality of opportunity means all people end up",
    "equality of opportunity requires identical income",
    "an equal share of the nation's wealth",
)
_EXEMPT_RULERS = (
    "except those in power", "other than those in power", "exemption of officials",
    "officials are not bound", "does not apply to officials",
)


def _glosses(module):
    """EK 4.1.A.1's four parentheses keep the clauses that make them mean anything."""
    bad = []
    for i, item in enumerate(module.QUESTIONS, 1):
        key = item["choices"][item["ans"]].lower()
        for phrase in _OUTCOME_SUBSTITUTIONS:
            if phrase in key:
                bad.append(f"q{i} key: restates equality of opportunity as an equality of "
                           "OUTCOMES; EK 4.1.A.1.ii's gloss is 'all people are given an equal "
                           "chance to compete', which is the starting line")
        for phrase in _EXEMPT_RULERS:
            if phrase in key:
                bad.append(f"q{i} key: exempts officials from the rule of law; EK 4.1.A.1.iv's "
                           "gloss is 'every person, EVEN THOSE IN POWER'")
        # Free enterprise may not be given the libertarian position.
        at = key.find("free enterprise")
        if at >= 0:
            seg = key[at:at + 160]
            for none in ("eliminating all government regulation", "no government regulation",
                         "without any government regulation"):
                if none in seg:
                    bad.append(f"q{i} key: gives free enterprise a position of NO regulation; "
                               "EK 4.1.A.1.iii says LIMITED government regulation, and EK "
                               "4.9.A.1 assigns 'little or no' to libertarian ideologies")
    pins = {
        3: ("shape their life and destiny through the choices they make", "individualism"),
        4: ("equal chance to compete", "equality of opportunity"),
        6: ("limited government regulation", "free enterprise"),
        7: ("even those in power", "the rule of law"),
    }
    for n, (clause, value) in pins.items():
        key = module.QUESTIONS[n - 1]["choices"][module.QUESTIONS[n - 1]["ans"]].lower()
        if clause not in key:
            bad.append(f"q{n}: the key for {value} no longer carries EK 4.1.A.1's own clause "
                       f"{clause!r}")
    if bad:
        print(f"FAIL {module.__name__} glosses")
        for b in bad:
            print("  -", b)
        raise SystemExit(1)
    print(f"OK  {module.__name__} glosses: equality of opportunity stays a chance to compete, "
          "the rule of law keeps EVEN THOSE IN POWER, free enterprise keeps LIMITED rather "
          "than no regulation, and all four of EK 4.1.A.1's parentheses survive")


_SINGLE_READING = (
    "has only one possible interpretation", "always produces a shared conclusion",
    "every citizen reaches the same policy conclusion",
    "core values determine attitudes toward government by themselves",
    "only these four values exist", "a complete list of american core values",
    "the four values named are all of them",
)


def _interpretations(module):
    """EK 4.1.A.1's subject stays INTERPRETATIONS, and its list stays illustrative."""
    bad = []
    for i, item in enumerate(module.QUESTIONS, 1):
        key = item["choices"][item["ans"]].lower()
        for phrase in _SINGLE_READING:
            if phrase in key:
                bad.append(f"q{i} key: states {phrase!r}. EK 4.1.A.1's subject is DIFFERENT "
                           "INTERPRETATIONS of core values, and its list opens 'SOME of these "
                           "core values INCLUDE'")
    q1 = module.QUESTIONS[0]
    if "different interpretations" not in q1["choices"][q1["ans"]].lower():
        bad.append("q1: the key no longer names EK 4.1.A.1's grammatical subject, DIFFERENT "
                   "INTERPRETATIONS of core values")
    q8 = module.QUESTIONS[7]
    if "complete list" not in q8["choices"][q8["ans"]].lower():
        bad.append("q8: the key no longer records that EK 4.1.A.1's four values are "
                   "illustrative rather than exhaustive")
    q2 = module.QUESTIONS[1]
    k2 = q2["choices"][q2["ans"]].lower()
    if "between citizens" not in k2 or "federal government" not in k2:
        bad.append("q2: the key no longer names both relationships EK 4.1.A.1 lists, between "
                   "citizens and between citizens and the federal government")
    if bad:
        print(f"FAIL {module.__name__} interpretations")
        for b in bad:
            print("  -", b)
        raise SystemExit(1)
    print(f"OK  {module.__name__} interpretations: no key gives a core value a single reading "
          "or treats EK 4.1.A.1's four as a complete list, and both of the framework's named "
          "relationships survive")


ua.shape(v4_1)
ua.check(v4_1, ANCHORS, GROUNDING)
ua.notation(v4_1)
_glosses(v4_1)
_interpretations(v4_1)
gc.check(v4_1, arith={25: q25, 26: q26, 27: q27, 28: q28, 29: q29, 30: q30})
