"""Structural gate for AP U.S. Government 3.11 Government Responses to Social
Movements.

gov345_check plus the four usgov_anchor helpers, plus two content gates.

  _scopes    EK 3.11.A.1 names three statutes and gives each a scope in the
             framework's own sentence:
                 Civil Rights Act of 1964   public places, integration of
                                            schools and other public
                                            facilities, employment
                 Title IX (1972)            SEX discrimination in an education
                                            program or activity RECEIVING
                                            FEDERAL FINANCIAL ASSISTANCE
                 Voting Rights Act of 1965  RACIAL discrimination in VOTING
             Giving one statute another's subject is a clean falsehood that
             reads as a reasonable summary -- "the Civil Rights Act protects
             voting rights" is the sort of thing a student writes in an FRQ and
             loses the point for. It is invisible to an anchor, because a key
             naming the wrong statute still matches its own substring. This
             check reads every key that names a statute and refuses any that
             attaches a subject the framework assigns elsewhere. It also pins
             Title IX's funding condition, which is the single most droppable
             clause in this topic: without it the statute appears to reach every
             school in the country, which is a different law.

  _channels  EK 3.11.A.1's conjunction is "court rulings AND/OR policies". Three
             of its four items are statutes, so compressing the topic to "the
             courts responded" drops most of the content. The check refuses any
             key that names the channels while giving only one of them, and pins
             the two items that count the statutes and identify the judicial one.

WHY THE DOCUMENT ITEMS ARE SHAPED THE WAY THEY ARE
--------------------------------------------------
The suggested skill is 2.B: relate a required case to a foundational document.
That is a relation, not a derivation, so item 21 exists to refuse the natural
overreach -- a student who has been told to connect the Gettysburg Address to
Brown will happily go on to cite the Address as the legal authority. It is
required course content and it states a national proposition; the enforceable
text is the Fourteenth Amendment. Getting that boundary right is most of what
skill 2.B is testing.
"""
import gov345_check as gc
import usgov_anchor as ua
import v3_11

ANCHORS = {
 1: "Court rulings and policies, either separately or together",
 2: "Three",
 3: "set a rule for conduct the court was never asked about",
 4: "both channels of government response being used on one subject",
 5: "provides for the integration of schools and other public facilities",
 6: "Public places, the integration of schools and other public facilities, and employment",
 7: "which prohibits discrimination in public places",
 8: "which makes employment discrimination illegal",
 9: "Sex discrimination in any education program or activity receiving federal financial",
 10: "That the education program or activity receives federal financial assistance",
 11: "how Congress reaches programs it does not otherwise administer",
 12: "Racial discrimination in voting",
 13: "The Voting Rights Act of 1965",
 14: "the allegation concerns sex discrimination in an education program",
 15: "Supreme Court decisions declaring that race-based school segregation",
 16: "arriving through the judicial channel",
 17: "extending it to other institutions may require further litigation",
 18: "as a violation of a national constitutional guarantee",
 19: "gives that commitment a specific legal consequence in public schooling",
 20: "tend to follow sustained demands rather than to arise on their own",
 21: "the legal authority for an equal protection claim is the Fourteenth Amendment",
 22: "The Voting Rights Act of 1965 with racial discrimination in voting",
 23: "so the subjects the 1964 act covers do not include it",
 24: "over a period of years rather than in a single act",
 25: "fewest actions opened had the largest share",
 26: "since each row names an act of Congress rather than a court decision",
 27: "so it is not the least used",
 28: "passed the number without a plan between the fifth and tenth years",
 29: "whose general realization takes years of further action",
 30: "well under a fifth of them",
}

GROUNDING = {
 1: "EK 3.11.A.1, verbatim: 'The government can respond to social movements through court "
    "rulings and/or policies.' The conjunction is what makes both channels available.",
 2: "EK 3.11.A.1's four items counted: three statutes (1964, 1965, 1972) against one item "
    "about Supreme Court decisions on school segregation.",
 3: "EK 3.11.A.1's two channels read for how they differ in reach. A judgment binds the "
    "parties before the court; EK 3.11.A.1.ii's statute 'makes employment discrimination "
    "illegal' generally.",
 4: "EK 3.11.A.1's 'and/or', which contemplates both channels on one subject -- as the "
    "framework's own list does, pairing school segregation decisions with the 1964 act.",
 5: "EK 3.11.A.1.ii, verbatim: the Civil Rights Act of 1964 'prohibits discrimination in "
    "public places, provides for the integration of schools and other public facilities, and "
    "makes employment discrimination illegal.'",
 6: "EK 3.11.A.1.ii's three subjects, listed. A summary that keeps one of the three "
    "understates what the framework says the statute does.",
 7: "EK 3.11.A.1.ii's first subject, public places, applied to a restaurant open to the "
    "public. The Fourteenth Amendment's clauses are addressed to a State (EK 3.10.A.1), which "
    "is why a statute is the instrument that reaches a private business.",
 8: "EK 3.11.A.1.ii's third subject, employment discrimination, applied to private hiring.",
 9: "EK 3.11.A.1.iii, verbatim: Title IX 'prohibits sex discrimination in any education "
    "program or activity receiving federal financial assistance.' Both halves matter.",
 10: "EK 3.11.A.1.iii's condition. Dropping it turns the framework's sentence into a claim "
     "about every school in the country, which is a different statute.",
 11: "EK 3.11.A.1.iii's condition read for its mechanism: attaching an obligation to accepted "
     "federal funds is how Congress reaches programs it neither created nor administers.",
 12: "EK 3.11.A.1.iv, verbatim: 'The Voting Rights Act of 1965 prohibits racial discrimination "
     "in voting.' One characteristic, one activity.",
 13: "EK 3.11.A.1.iv applied to a rule that keeps voters of one race from registering, which "
     "is exactly that combination of characteristic and activity.",
 14: "EK 3.11.A.1.iii applied with all three of its elements present: sex, an education "
     "program or ACTIVITY, and receipt of federal financial assistance.",
 15: "EK 3.11.A.1.i, the one judicial item in the framework's list of four.",
 16: "Brown v. Board of Education (1954), required case, which the CED attaches to 3.11.A. CED "
     "holding: race-based school segregation violates the equal protection clause of the "
     "Fourteenth Amendment -- EK 3.11.A.1.i's class of decision exactly.",
 17: "EK 3.11.A.1's two channels read for the judicial one's limit: a court decides the case "
     "before it, which the desegregation table in this module shows unfolding over years.",
 18: "'Letter from a Birmingham Jail' (required document), quoted verbatim; the CED attaches "
     "the Letter to 3.11.A. Skill 2.B: the Letter makes a local wrong a general concern and "
     "Brown makes a local practice a national constitutional question.",
 19: "Gettysburg Address (required document), quoted verbatim; the CED attaches it to 3.11.A. "
     "Skill 2.B: the Address states a proposition, the holding supplies a legal consequence.",
 20: "'Letter from a Birmingham Jail', quoted verbatim. Read for implications, it asserts that "
     "change follows demand -- which is why this topic's title calls the government's action a "
     "RESPONSE.",
 21: "Skill 2.B's boundary: a required case RELATES to a foundational document; the document "
     "is not the rule of decision. The Address is required content and states a proposition; "
     "the enforceable text for an equal protection claim is the Fourteenth Amendment.",
 22: "EK 3.11.A.1.ii, iii and iv checked against each other. Each alternative gives a named "
     "statute the subject the framework assigns to a different one.",
 23: "EK 3.11.A.1.ii's three subjects against EK 3.11.A.1.iv's one. The framework lists them "
     "as separate items because their subjects differ, voting being absent from the 1964 act.",
 24: "EK 3.11.A.1's list read as a whole: two channels, four instruments, dated 1954, 1964, "
     "1965 and 1972.",
 25: "Data item, CED skill 2.B. Every finding rate is recomputed below.",
 26: "EK 3.11.A.1's channel distinction located in the table: every row is a statute. Where an "
     "action is filed does not change which instrument created the obligation.",
 27: "Data item: a ranking error. The three counts are recomputed and ordered below.",
 28: "Data item. Both columns and the crossing point are recomputed below.",
 29: "EK 3.11.A.1.i read against the table: a ruling sets a requirement, and this one spreads "
     "across fifteen years. Both the never-moves and the moves-at-once readings are refuted.",
 30: "Data item: the first row's share, recomputed below, against a claim of immediate "
     "compliance.",
}

OPENED, FOUND = "Enforcement actions opened", "Actions resolved with a finding of violation"
PLAN, NOPLAN = ("Districts operating under a desegregation plan", "Districts with no plan in place")
YEAR = "Year after the ruling"


def _col(t, header):
    j = t["headers"].index(header)
    return [r[j] for r in t["rows"]]


def _row(t, needle):
    hits = [r for r in t["rows"] if needle in r[0]]
    assert len(hits) == 1, f"{needle!r} matches {len(hits)} rows, not one"
    return hits[0]


def q25(t):
    """The smallest row has the highest finding rate; Title IX is not the smallest."""
    stats = {r[0]: (gc.num(r[1]), gc.pct(gc.num(r[2]), gc.num(r[1]))) for r in t["rows"]}
    fewest = min(stats, key=lambda k: stats[k][0])
    highest = max(stats, key=lambda k: stats[k][1])
    assert fewest == highest, f"fewest actions on {fewest!r} but highest rate on {highest!r}"
    tix = _row(t, "Title IX")
    vra = _row(t, "Voting Rights Act")
    assert gc.num(tix[1]) > gc.num(vra[1]), "Title IX has fewer actions than the Voting Rights Act"
    return ("; ".join(f"{k.split(',')[0]} {n:.0f} actions at {p} percent"
                      for k, (n, p) in stats.items())
            + f" -- fewest and highest rate are both {fewest.split(',')[0]!r}")


def q26(t):
    """Every row names a statute, so every row is the policy channel."""
    names = _col(t, "Statute invoked")
    assert all("Act" in n for n in names), f"a row does not name an act of Congress: {names}"
    assert not any("v." in n for n in names), f"a row names a case: {names}"
    assert len(names) == 3, f"{len(names)} rows, not three"
    return "all three rows name acts of Congress: " + "; ".join(n.split(",")[0] for n in names)


def q27(t):
    """Title IX sits in the middle when the three rows are ranked by actions opened."""
    order = sorted(t["rows"], key=lambda r: -gc.num(r[1]))
    ranked = [r[0].split(",")[0] for r in order]
    assert "Title IX" in ranked[1], f"the middle row is {ranked[1]!r}, not Title IX"
    tix, vra = gc.num(_row(t, "Title IX")[1]), gc.num(_row(t, "Voting Rights Act")[1])
    assert tix == 530 and vra == 240, f"the key's counts are {tix:.0f} and {vra:.0f}"
    return f"ranked by actions opened: {', '.join(ranked)} -- Title IX in the middle"


def q28(t):
    """Plan column rises throughout and crosses the no-plan column between rows 2 and 3."""
    plan = [gc.num(c) for c in _col(t, PLAN)]
    nop = [gc.num(c) for c in _col(t, NOPLAN)]
    assert plan == sorted(plan) and len(set(plan)) == len(plan), f"the plan column is {plan}"
    assert nop == sorted(nop, reverse=True), f"the no-plan column is {nop}"
    crossings = [i for i in range(len(plan) - 1)
                 if plan[i] < nop[i] and plan[i + 1] > nop[i + 1]]
    assert crossings == [1], f"the columns cross between rows {crossings}, not between 1 and 2"
    years = _col(t, YEAR)
    return (f"plan {', '.join(f'{p:.0f}' for p in plan)} against no plan "
            f"{', '.join(f'{n:.0f}' for n in nop)}; crossing between the "
            f"{years[1].lower()} and {years[2].lower()} years")


def q29(t):
    """The requirement spreads but does not arrive at once."""
    plan = [gc.num(c) for c in _col(t, PLAN)]
    total = gc.num(_col(t, PLAN)[0]) + gc.num(_col(t, NOPLAN)[0])
    assert plan[0] < total / 2, "a majority is already under a plan in the first row"
    assert plan[-1] > plan[0], "the plan column does not grow, so the ruling appears inert"
    assert plan[-1] < total, "every district is under a plan by the end, removing the gap"
    for r in t["rows"]:
        assert gc.num(r[1]) + gc.num(r[2]) == total, \
            f"row {r[0]!r} does not total {total:.0f} districts"
    return (f"every row totals {total:.0f} districts; plan column {plan[0]:.0f} at the start "
            f"and {plan[-1]:.0f} at the end, still short of all of them")


def q30(t):
    """The first row is well under a fifth."""
    first = t["rows"][0]
    plan, nop = gc.num(first[1]), gc.num(first[2])
    total = plan + nop
    share = gc.pct(plan, total)
    assert plan == 18 and total == 160, f"the first row is {plan:.0f} of {total:.0f}"
    assert share < 20, f"the first row is {share} percent, not well under a fifth"
    return f"first year {plan:.0f} of {total:.0f} districts under a plan, {share} percent"


# --- module-specific content gates -------------------------------------------

# Each statute mapped to the subjects the framework assigns SOMEWHERE ELSE. A
# key naming the statute may not attach one of these to it.
_FOREIGN_SUBJECTS = {
    "civil rights act of 1964": (("racial discrimination in voting",
                                  "sex discrimination in any education",
                                  "sex discrimination in education",
                                  "federal financial assistance"),
                                 "EK 3.11.A.1.ii gives it public places, integration of schools "
                                 "and other public facilities, and employment"),
    "title ix": (("racial discrimination in voting", "discrimination in public places",
                  "discrimination in public accommodations",
                  "employment discrimination"),
                 "EK 3.11.A.1.iii gives it SEX discrimination in an education program or "
                 "activity RECEIVING FEDERAL FINANCIAL ASSISTANCE"),
    "voting rights act of 1965": (("sex discrimination", "employment discrimination",
                                   "discrimination in public places",
                                   "discrimination in public accommodations",
                                   "federal financial assistance"),
                                  "EK 3.11.A.1.iv gives it RACIAL discrimination in VOTING"),
}


def _scopes(module):
    """No key may attach one statute's subject to another."""
    bad = []
    for i, item in enumerate(module.QUESTIONS, 1):
        key = item["choices"][item["ans"]].lower()
        for statute, (foreign, note) in _FOREIGN_SUBJECTS.items():
            at = key.find(statute)
            if at < 0:
                continue
            # Only the clause that follows this statute's name, up to the next
            # statute name, describes THIS statute. A key that correctly
            # contrasts two statutes names both, and attributing every subject
            # in the sentence to every statute in it is the over-match this
            # project keeps rediscovering.
            ends = [key.find(o, at + len(statute)) for o in _FOREIGN_SUBJECTS
                    if key.find(o, at + len(statute)) > 0]
            stop = min(ends) if ends else len(key)
            seg = key[at:stop]
            for f in foreign:
                if f in seg:
                    bad.append(f"q{i} key: attaches {f!r} to the {statute}; {note}")
    q9 = module.QUESTIONS[8]
    k9 = q9["choices"][q9["ans"]].lower()
    if "receiving federal financial assistance" not in k9 or "sex discrimination" not in k9:
        bad.append("q9: the Title IX key no longer carries both halves of EK 3.11.A.1.iii, SEX "
                   "discrimination and RECEIVING FEDERAL FINANCIAL ASSISTANCE")
    q12 = module.QUESTIONS[11]
    if "racial discrimination in voting" not in q12["choices"][q12["ans"]].lower():
        bad.append("q12: the Voting Rights Act key no longer states EK 3.11.A.1.iv's subject")
    q5 = module.QUESTIONS[4]
    k5 = q5["choices"][q5["ans"]].lower()
    for part in ("public places", "integration of schools", "employment discrimination"):
        if part not in k5:
            bad.append(f"q5: the Civil Rights Act key has dropped {part!r}, one of the three "
                       "subjects EK 3.11.A.1.ii names in a single sentence")
    if bad:
        print(f"FAIL {module.__name__} scopes")
        for b in bad:
            print("  -", b)
        raise SystemExit(1)
    print(f"OK  {module.__name__} scopes: no key attaches one statute's subject to another, "
          "Title IX keeps its federal funding condition, and the Civil Rights Act keeps all "
          "three of the subjects EK 3.11.A.1.ii names")


def _channels(module):
    """EK 3.11.A.1's two channels stay two."""
    bad = []
    q1 = module.QUESTIONS[0]
    k1 = q1["choices"][q1["ans"]].lower()
    if "court ruling" not in k1 or "policies" not in k1:
        bad.append("q1: the key no longer names both of EK 3.11.A.1's channels, court rulings "
                   "and policies")
    q2 = module.QUESTIONS[1]
    if q2["choices"][q2["ans"]].strip().lower() != "three":
        bad.append("q2: the count of statutes among EK 3.11.A.1's four items is no longer "
                   "three (the 1964, 1965 and 1972 acts against one judicial item)")
    q15 = module.QUESTIONS[14]
    if "supreme court decisions" not in q15["choices"][q15["ans"]].lower():
        bad.append("q15: the key no longer identifies EK 3.11.A.1.i as the judicial item")
    for i, item in enumerate(module.QUESTIONS, 1):
        key = item["choices"][item["ans"]].lower()
        if "only" in key and "court ruling" in key and "polic" not in key:
            bad.append(f"q{i} key: makes court rulings the only channel; EK 3.11.A.1 says "
                       "'court rulings and/or policies' and three of its four items are "
                       "statutes")
    if bad:
        print(f"FAIL {module.__name__} channels")
        for b in bad:
            print("  -", b)
        raise SystemExit(1)
    print(f"OK  {module.__name__} channels: EK 3.11.A.1's two response channels both survive, "
          "the statute count stays three, and no key makes the judiciary the only channel")


ua.shape(v3_11)
ua.check(v3_11, ANCHORS, GROUNDING)
ua.notation(v3_11)
_scopes(v3_11)
_channels(v3_11)
gc.check(v3_11, arith={25: q25, 26: q26, 27: q27, 28: q28, 29: q29, 30: q30})
