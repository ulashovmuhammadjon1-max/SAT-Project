"""Structural gate for AP U.S. Government 4.8 Ideology and Policymaking.

gov345_check plus the four usgov_anchor helpers, plus three content gates.

  _participate  EK 4.8.A.1's working clause is "citizens WHO CHOOSE TO
                PARTICIPATE in politics at that time". Drop it and the sentence
                becomes "policies reflect the attitudes of citizens" -- a
                different and much weaker claim, and one the framework was
                careful not to make. What it actually says is that policy
                reflects a SUBSET, and that the subset is not the population.
                The first table is built to show that gap directly (the same
                age group is 22 percent of adults, 31 percent of voters and 37
                percent of those contacting a legislator), and the gate refuses
                any key that generalizes the claim to all citizens.

  _dynamic      EK 4.8.A.2 says the balancing of individual liberty against
                government efforts to promote stability and order "has been
                reflected in policy debates AND THEIR OUTCOMES OVER TIME". Three
                droppable things: it is ongoing rather than settled, it appears
                in outcomes as well as in argument, and NEITHER SIDE IS SAID TO
                PREVAIL. The third matters most, because letting either side win
                would state a political position as course content. The second
                table is built with the liberty side leading one question, the
                order side two, and one near even, and the gate refuses any key
                asserting a consistent winner in either direction.

  _no_attributed_visual
                Skill 4.D asks about a cartoon, map or infographic, and this
                bank is text. A DESCRIBED cartoon is an honest stimulus: the
                visual elements are stated, so the student can reason about them
                exactly as the skill requires. An invented cartoon attributed to
                a real cartoonist or publication would not be, and it is the
                same failure mode as a fabricated quotation in 4.4 -- nothing
                downstream could catch it, because a made-up attribution reads
                exactly like a real one. So every visual stimulus here opens
                "A hypothetical" and names no artist and no publication, and the
                gate checks both halves: that the visual items are labelled
                hypothetical, and that none carries an attribution line.
"""
import re

import gov345_check as gc
import usgov_anchor as ua
import v4_8

ANCHORS = {
 1: "Citizens who choose to participate in politics at that time",
 2: "so which of them policy reflects depends on who takes part",
 3: "rather than about the subset that takes part",
 4: "which is what the framework says policy reflects",
 5: "can change from one period to another",
 6: "the thing that determines whose attitudes policy reflects",
 7: "reflect the views of the people who took part in politics at that moment",
 8: "The balancing dynamic of individual liberty and government efforts to promote",
 9: "ongoing and unsettled rather than resolved in favor of either",
 10: "it locates the tension in what governments actually did",
 11: "balancing dynamic of individual liberty and government efforts to promote stability",
 12: "one in policy debates and the other in constitutional doctrine",
 13: "what it is meant to achieve, and how it is carried out",
 14: "list of individualism, equality of opportunity, free enterprise, and the rule of law",
 15: "since scales show two considerations weighed against each other",
 16: "reflects the attitudes of citizens who choose to participate",
 17: "while the empty chairs represent people whose views are not being registered",
 18: "with neither consideration prevailing throughout",
 19: "how the visual elements illustrate or relate to a political principle",
 20: "a permanent condition that a political system has to operate within",
 21: "which is one of the cultural commitments policy debates draw on",
 22: "clause that policy reflects the attitudes of citizens who choose to participate",
 23: "Which of the two considerations should prevail in a policy debate",
 24: "shape what this policy was meant to achieve and how it was carried out",
 25: "with the gap wider among those who contacted a legislator than among voters",
 26: "reflect the attitudes and beliefs of citizens who choose to participate in politics",
 27: "and their age composition differs from that of all adults",
 28: "each side leads two, and one of the four is close to even",
 29: "is reflected in policy debates",
 30: "so the preference is not consistent across the four questions",
}

GROUNDING = {
 1: "EK 4.8.A.1, verbatim: policies 'reflect the attitudes and beliefs of citizens who choose "
    "to participate in politics at that time.' The subject is a subset of the population.",
 2: "EK 4.8.A.1's premise clause, 'a democracy with a diverse society', read together with the "
    "participation clause: if everyone held the same views, who takes part would not change "
    "the result.",
 3: "EK 4.8.A.1 with its clause removed, which yields a claim about all citizens that the "
    "framework does not make.",
 4: "EK 4.8.A.1 applied to a gap between the population and the participating group, which is "
    "the framework's claim operating rather than a counterexample.",
 5: "EK 4.8.A.1's double timing -- policies AT ANY GIVEN TIME, participants AT THAT TIME -- "
    "which is what LO 4.8.A's phrase OVER TIME depends on.",
 6: "EK 4.8.A.1's clause read as a link to Unit 5. The framework says CHOOSE TO PARTICIPATE "
    "rather than naming voting alone, so other forms of participation count too.",
 7: "EK 4.8.A.1 restated with all three working parts: the diversity premise, the timing, and "
    "the participation clause.",
 8: "EK 4.8.A.2, verbatim: 'The balancing dynamic of individual liberty and government efforts "
    "to promote stability and order has been reflected in policy debates and their outcomes "
    "over time.'",
 9: "EK 4.8.A.2's noun DYNAMIC, a continuing interaction, attached to debates and outcomes "
    "OVER TIME. The framework names no winner.",
 10: "EK 4.8.A.2's phrase AND THEIR OUTCOMES, which locates the tension in policies adopted "
     "rather than only in the argument around them.",
 11: "EK 4.8.A.2's two considerations in their usual arrangement: a restriction on individual "
     "action against a government effort to reduce risk.",
 12: "EK 3.8.A.1, which records that some government interests may justify restricting "
     "individual rights with public safety as its example, against EK 4.8.A.2's naming of the "
     "same pair. One tension in two settings.",
 13: "LO 4.8.A's three named stages: FORMATION, GOALS, and IMPLEMENTATION.",
 14: "LO 4.8.A's parenthetical, which points back to EK 4.1.A.1's four core values and EK "
     "4.2.A.2's statement that U.S. political culture is defined by them.",
 15: "CED skill 4.D on a described hypothetical cartoon. Scales are the visual form of two "
     "considerations weighed against each other, and a hand adding weight shows the balance "
     "as adjustable -- EK 4.8.A.2's word DYNAMIC rendered as an image.",
 16: "CED skill 4.D. The two lines make the participating group different from the "
     "population, and the legislator reading what THE VOTERS want completes the link to "
     "policy: EK 4.8.A.1's clause presented visually.",
 17: "CED skill 4.D. Empty chairs at a table labelled for policy picture decisions made by "
     "those who show up, which is EK 4.8.A.1. Nothing in the image indicates who was invited.",
 18: "CED skill 4.D on a described infographic. EK 4.8.A.2 places the dynamic in outcomes over "
     "time, and an alternating pattern across decades is that claim in visual form.",
 19: "Skill 4.D's own wording: explain how the visual elements ILLUSTRATE OR RELATE TO "
     "political principles, institutions, processes, policies and behaviors.",
 20: "Federalist No. 10 (required document), quoted verbatim; the CED attaches it to 4.8.A. "
     "Madison locates the causes of faction in human nature and in the circumstances of civil "
     "society, and EK 4.8.A.1 begins from a diverse society. Both take difference as given.",
 21: "Adam Smith, 'The Wealth of Nations' (required document), quoted verbatim; the CED "
     "attaches it to 4.8.A. EK 4.1.A.1.iii names free enterprise as a core value and sources "
     "it to this work, and LO 4.8.A asks how core values influence policy formation.",
 22: "EK 4.8.A.1's clause against a claim about the will of the majority of citizens. A "
     "majority of the population and a majority of participants need not agree.",
 23: "EK 4.8.A.2 read for what it omits: a dynamic described, and no winner named.",
 24: "LO 4.8.A's three stages, of which goals and implementation are two. The distractors are "
     "procedural facts bearing on none of them.",
 25: "Data item, CED skill 4.D. Every column share and both gaps are recomputed below.",
 26: "EK 4.8.A.1's clause located in data: the population column and the participant columns "
     "differ in composition.",
 27: "Data item: reading a participant column as the population. The largest divergence is "
     "recomputed below.",
 28: "Data item, CED skill 4.D. Which side leads each question is recomputed below.",
 29: "EK 4.8.A.2's balancing dynamic shown as data, with neither side leading throughout.",
 30: "Data item: reading two leads out of four as a consistent preference. Question 1's split "
     "is recomputed below.",
}

ADULTS, VOTERS, CONTACTS = ("Share of all adults (%)", "Share of those who voted (%)",
                            "Share of those who contacted a legislator (%)")
LIBERTY, ORDER, UNDECIDED = ("Favored the individual liberty side (%)",
                             "Favored the stability and order side (%)", "Undecided (%)")


def _col(t, header):
    j = t["headers"].index(header)
    return [gc.num(r[j]) for r in t["rows"]]


def _labels(t):
    return [r[0] for r in t["rows"]]


def q25(t):
    """Oldest over-represented, youngest under-, and the gap grows from voting to contacting."""
    labels = _labels(t)
    ad, vo, co = _col(t, ADULTS), _col(t, VOTERS), _col(t, CONTACTS)
    for name, c in (("adults", ad), ("voters", vo), ("contacts", co)):
        assert sum(c) == 100, f"the {name} column totals {sum(c):.0f}, not 100"
    old, young = labels.index("Age 65 and older"), labels.index("Ages 18 to 29")
    assert vo[old] > ad[old] and co[old] > vo[old], "the oldest group is not increasingly over-represented"
    assert vo[young] < ad[young] and co[young] < vo[young], "the youngest group is not increasingly under-represented"
    assert co[old] - ad[old] > vo[old] - ad[old], "the gap does not widen from voting to contacting"
    return (f"oldest {ad[old]:.0f} of adults, {vo[old]:.0f} of voters, {co[old]:.0f} of "
            f"contacts; youngest {ad[young]:.0f}, {vo[young]:.0f}, {co[young]:.0f}; "
            f"oldest excess {vo[old] - ad[old]:.0f} then {co[old] - ad[old]:.0f} points")


def q26(t):
    """The population column and the participant columns are not the same distribution."""
    ad, vo, co = _col(t, ADULTS), _col(t, VOTERS), _col(t, CONTACTS)
    assert ad != vo and ad != co, "a participant column matches the population exactly"
    assert max(abs(a - c) for a, c in zip(ad, co)) >= 10, \
        "the population and contacting columns differ by less than 10 points everywhere"
    return (f"largest population-to-contacts divergence "
            f"{max(abs(a - c) for a, c in zip(ad, co)):.0f} points")


def q27(t):
    """The divergence is large enough that a participant column cannot stand in for adults."""
    ad, vo, co = _col(t, ADULTS), _col(t, VOTERS), _col(t, CONTACTS)
    worst = max(max(abs(a - v) for a, v in zip(ad, vo)),
                max(abs(a - c) for a, c in zip(ad, co)))
    assert worst >= 15, f"the largest divergence is {worst:.0f} points, under the 15 keyed"
    assert len(t["headers"]) == 4, "the table no longer carries all three populations"
    return f"largest divergence between the population and a participant column: {worst:.0f} points"


def _leads(t):
    lib, ord_ = _col(t, LIBERTY), _col(t, ORDER)
    return ["liberty" if l > o else "order" for l, o in zip(lib, ord_)]


def q28(t):
    """Liberty leads one, order two, and one question is close."""
    leads = _leads(t)
    lib, ord_ = _col(t, LIBERTY), _col(t, ORDER)
    assert leads.count("liberty") == 2, f"liberty leads {leads.count('liberty')} questions"
    assert leads.count("order") == 2, f"order leads {leads.count('order')} questions"
    close = [i for i, (l, o) in enumerate(zip(lib, ord_)) if abs(l - o) <= 5]
    assert len(close) == 1, f"{len(close)} questions are close, not one"
    assert leads[close[0]] == "liberty", "the close question is not the near-even liberty lead"
    majorities = [l for l in lib if l > 50]
    assert len(majorities) == 1, f"the liberty side reaches a majority on {len(majorities)} questions"
    for row in t["rows"]:
        assert sum(gc.num(c) for c in row[1:]) == 100, f"row {row[0]!r} does not total 100"
    return (f"leads {', '.join(leads)} -- two each; one question within "
            f"{abs(lib[close[0]] - ord_[close[0]]):.0f} points; rows total 100")


def q29(t):
    """Both sides lead somewhere, which is what makes it a dynamic rather than a trend."""
    leads = _leads(t)
    assert "liberty" in leads and "order" in leads, f"one side leads every question: {leads}"
    return f"both sides lead at least one question: {', '.join(leads)}"


def q30(t):
    """Question 1 is a clear liberty lead, so the preference is not consistent."""
    lib, ord_ = _col(t, LIBERTY), _col(t, ORDER)
    assert lib[0] == 58 and ord_[0] == 31, \
        f"question 1 reads {lib[0]:.0f} against {ord_[0]:.0f}, not the 58 and 31 keyed"
    assert lib[0] > ord_[0], "question 1 does not favour the liberty side"
    assert _leads(t).count("order") >= 2, "the order side does not lead at least two questions"
    return (f"question 1: liberty {lib[0]:.0f} against order {ord_[0]:.0f}, while order leads "
            f"{_leads(t).count('order')} of {len(lib)} questions")


# --- module-specific content gates -------------------------------------------

_GENERALIZED = (
    "all citizens equally", "the attitudes of every citizen",
    "the will of the majority of citizens", "reflect the views of every citizen",
    "whether they participate or not",
)


def _participate(module):
    """EK 4.8.A.1's clause may not be generalized to all citizens."""
    bad = []
    for i, item in enumerate(module.QUESTIONS, 1):
        key = item["choices"][item["ans"]].lower()
        stem = item["q"].lower()
        withholds = "not state" in stem or "qualifies the claim" in stem
        for g in _GENERALIZED:
            if g in key and not withholds:
                bad.append(f"q{i} key: generalizes EK 4.8.A.1 to {g!r}. The framework says "
                           "policies reflect citizens WHO CHOOSE TO PARTICIPATE in politics "
                           "at that time, which is a subset and not the population")
    # "took part" is the same clause in plainer words, and item 7's key uses it
    # deliberately -- it is a restatement item. A check demanding the literal
    # stem "particip" reported that correct key, which is the fifth over-match
    # of this build and the same lesson every time: match the claim, not a word.
    def _states_participation(text):
        return any(w in text for w in ("particip", "took part", "take part", "takes part"))

    for n in (1, 7):
        key = module.QUESTIONS[n - 1]["choices"][module.QUESTIONS[n - 1]["ans"]].lower()
        if not _states_participation(key):
            bad.append(f"q{n}: the key no longer carries EK 4.8.A.1's participation clause, "
                       "which is the whole content of the statement")
    turn = sum(1 for item in module.QUESTIONS
               if _states_participation(item["choices"][item["ans"]].lower()))
    if turn < 5:
        bad.append(f"only {turn} keys turn on participation; EK 4.8.A.1's clause is what "
                   "distinguishes this topic from a general claim about democracy")
    if bad:
        print(f"FAIL {module.__name__} participate")
        for b in bad:
            print("  -", b)
        raise SystemExit(1)
    print(f"OK  {module.__name__} participate: EK 4.8.A.1's WHO CHOOSE TO PARTICIPATE survives "
          f"in every key that states the claim, {turn} keys turn on it, and no key generalizes "
          "it to all citizens")


_WINNERS = (
    "liberty has permanently prevailed", "order has permanently prevailed",
    "the liberty side leads all four", "the order side leads all four",
    "consistently prefers order", "consistently prefers liberty",
    "steadily expanded at the expense of",
)


def _dynamic(module):
    """EK 4.8.A.2 names no winner, and no key may."""
    bad = []
    for i, item in enumerate(module.QUESTIONS, 1):
        key = item["choices"][item["ans"]].lower()
        stem = item["q"].lower()
        withholds = "not state" in stem or "correction" in stem
        for w in _WINNERS:
            if w in key and not withholds:
                bad.append(f"q{i} key: asserts a winner ({w!r}). EK 4.8.A.2 calls the "
                           "relationship a BALANCING DYNAMIC reflected in debates and their "
                           "outcomes over time, and names no side as prevailing")
    q8 = module.QUESTIONS[7]
    k8 = q8["choices"][q8["ans"]].lower()
    for part in ("balancing dynamic", "individual liberty", "stability and order"):
        if part not in k8:
            bad.append(f"q8: the key has dropped {part!r} from EK 4.8.A.2's own sentence")
    q10 = module.QUESTIONS[9]
    if "actually did" not in q10["choices"][q10["ans"]].lower():
        bad.append("q10: the key no longer records that EK 4.8.A.2 places the dynamic in "
                   "OUTCOMES as well as in debates")
    q23 = module.QUESTIONS[22]
    if "should prevail" not in q23["choices"][q23["ans"]].lower():
        bad.append("q23: the key no longer identifies the question of which side should "
                   "prevail as the thing EK 4.8.A.2 does not state")
    if bad:
        print(f"FAIL {module.__name__} dynamic")
        for b in bad:
            print("  -", b)
        raise SystemExit(1)
    print(f"OK  {module.__name__} dynamic: EK 4.8.A.2's balancing dynamic keeps both "
          "considerations and its reach into outcomes, and no key asserts that either side "
          "prevails")


_ATTRIBUTION = re.compile(r"^\s*[—-]\s*\S", re.MULTILINE)
_VISUAL = ("cartoon", "infographic", "map")
# The two documents the CED attaches to 4.8.A are genuinely quoted, so an
# attribution line is correct in those items. The refusal is specific: a VISUAL
# stimulus may not carry one, because there is no real cartoon behind it.
_QUOTED_DOCS = ("federalist no. 10", "the wealth of nations")


def _no_attributed_visual(module):
    """Every visual stimulus is labelled hypothetical and attributed to no one."""
    bad = []
    visual_items = 0
    for i, item in enumerate(module.QUESTIONS, 1):
        stem = item["q"]
        low = stem.lower()
        # An item that PRESENTS a visual stimulus describes one: it needs both a
        # visual noun and a presenting verb. Item 19 mentions a cartoon while
        # asking what skill 4.D requires of an analysis -- it presents no image,
        # so there is nothing to label hypothetical, and a noun-only test
        # reported it. Sixth over-match of this build.
        # A stimulus item names the visual noun and IMMEDIATELY presents it:
        # "cartoon shows", "infographic shows". Item 19 mentions a cartoon while
        # asking what skill 4.D requires of an analysis -- it presents no image,
        # so there is nothing to label hypothetical. Requiring the noun and verb
        # to be adjacent is what separates presenting from referring; a
        # noun-only test and then a noun-plus-verb-anywhere test each reported
        # item 19. Sixth over-match of this build, and the same lesson: make the
        # pattern say what you actually mean.
        if not any(f"{v} shows" in low for v in _VISUAL):
            continue
        visual_items += 1
        if "hypothetical" not in low:
            bad.append(f"q{i}: describes a {[v for v in _VISUAL if v in low][0]} without "
                       "labelling it hypothetical. This bank is text, so a described visual "
                       "is honest only if it is not presented as a real one")
        if _ATTRIBUTION.search(stem) and not any(d in low for d in _QUOTED_DOCS):
            bad.append(f"q{i}: attributes a visual source. An invented cartoon credited to a "
                       "real cartoonist or publication is the same failure as a fabricated "
                       "quotation -- nothing downstream can catch it, because a made-up "
                       "attribution reads exactly like a real one")
    if visual_items < 3:
        bad.append(f"only {visual_items} items carry a visual stimulus; the suggested skill "
                   "for this topic is 4.D, which is about cartoons, maps and infographics")
    if bad:
        print(f"FAIL {module.__name__} visual sources")
        for b in bad:
            print("  -", b)
        raise SystemExit(1)
    print(f"OK  {module.__name__} visual sources: {visual_items} described visual stimuli, "
          "every one labelled hypothetical and none attributed to an artist or publication")


ua.shape(v4_8)
ua.check(v4_8, ANCHORS, GROUNDING)
ua.notation(v4_8)
_participate(v4_8)
_dynamic(v4_8)
_no_attributed_visual(v4_8)
gc.check(v4_8, arith={25: q25, 26: q26, 27: q27, 28: q28, 29: q29, 30: q30})
