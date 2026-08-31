"""Structural gate for AP U.S. Government 3.10 Social Movements and Equal
Protection.

gov345_check plus the four usgov_anchor helpers, plus two content gates.

  _three_sources  EK 3.10.A.1 names THREE sources of civil rights in one
                  sentence: the due process clause, the equal protection
                  clause, "as well as ACTS OF CONGRESS". The third is the one
                  that drops out of a paraphrase, and dropping it is not a
                  harmless simplification -- the Fourteenth Amendment's clauses
                  are addressed to "any State", so the statutory source is the
                  only one of the three that reaches PRIVATE conduct. Item 8
                  turns on exactly that, and this check refuses any key that
                  states the sources of civil rights while naming fewer than the
                  framework does, or that says a constitutional clause reaches
                  private discrimination directly.

  _neutrality     EK 3.10.A.2.iii names "the pro-life and pro-choice movements"
                  together, and the framework's claim is that the equal
                  protection clause CAN SUPPORT AND MOTIVATE movements -- a
                  claim about mobilisation, not about who is right. A bank that
                  quietly took a side on any movement it names would be teaching
                  a position as course content. The check refuses evaluative
                  verdicts in any key: no key may call a named movement correct,
                  mistaken, justified or unjustified. Item 24 makes the
                  framework's even-handedness the question instead.

WHY THE SOURCE ITEMS ASK ABOUT IMPLICATIONS RATHER THAN CONTENT
---------------------------------------------------------------
The suggested skill here is 4.C, which asks what follows from a source's
argument, and LO 3.10.A's verbs are SUPPORTED and MOTIVATED -- effects on people
organising, not on litigation. So the four quoted documents are asked about for
what a movement could DO with them: a local wrong made a national concern, a
just-law test that survives valid enactment, a founding proposition used as a
standard, and a proclamation whose stated geographic limit is itself the
material of a demand. A comprehension question about what each document says
would test the wrong skill and miss the topic.
"""
import gov345_check as gc
import usgov_anchor as ua
import v3_10

ANCHORS = {
 1: "Discrimination based on characteristics such as race",
 2: "Race, national origin, religion, and sex",
 3: "as well as acts of Congress",
 4: "a later Congress could amend",
 5: "The guarantee is not limited to citizens",
 6: "the two clauses EK 3.10.A.1 names",
 7: "A State",
 8: "restrains a State rather than a private business",
 9: "The equal protection clause",
 10: "advocacy for LGBTQ rights",
 11: "a resource that people organize around and argue from",
 12: "properly the concern of people everywhere",
 13: "assessed independently of the fact that it has been enacted",
 14: "lists the Letter and the civil rights movement of the 1960s",
 15: "existing practice had not yet met",
 16: "rather than everywhere in the country",
 17: "gives a movement a stated commitment to demand the completion of",
 18: "a concrete result that a movement could point to",
 19: "Religion is one of the characteristics EK 3.10.A.1 names",
 20: "prevailing against a generally applicable state law",
 21: "The National Organization for Women",
 22: "motivate movements that disagree with one another",
 23: "operates before and apart from any court's ruling",
 24: "were in force long before the movements",
 25: "together account for more than three-quarters",
 26: "list of characteristics such as race, national origin, religion, and sex",
 27: "a higher share than race complaints",
 28: "more than twice as often as the due process clause",
 29: "can support and motivate social movements",
 30: "and 20 petitions here rested on a statute alone",
}

GROUNDING = {
 1: "EK 3.10.A.1, verbatim: 'Civil rights protect individuals from discrimination based on "
    "characteristics such as race, national origin, religion, and sex.'",
 2: "EK 3.10.A.1's four named characteristics. The framework's phrase 'such as' makes the list "
    "illustrative rather than closed, but these four are its own examples.",
 3: "EK 3.10.A.1, verbatim: 'these rights are guaranteed to all persons under the due process "
    "and equal protection clauses of the U.S. Constitution, as well as acts of Congress.' "
    "Three sources in one sentence, the third statutory.",
 4: "EK 3.10.A.1's mixed list read for what it implies: a right resting on a statute is "
    "repealable by the ordinary lawmaking process, a right resting on a constitutional clause "
    "is not. The framework lists both without ranking them.",
 5: "EK 3.10.A.1's phrase 'guaranteed to all persons', which matches the Fourteenth "
    "Amendment's own 'any person within its jurisdiction' rather than a citizenship test.",
 6: "U.S. Constitution, Fourteenth Amendment Section 1, quoted verbatim. The sentence contains "
    "both clauses EK 3.10.A.1 names as constitutional sources of civil rights.",
 7: "Fourteenth Amendment Section 1's grammatical subject, 'any State', which is why this "
    "amendment reaches state and local action and why EK 3.10.A.1 needs a third source.",
 8: "EK 3.10.A.1's third source applied. Because the Fourteenth Amendment's clauses are "
    "addressed to a State, private discrimination is reached by acts of Congress -- which is "
    "why the framework's sentence has three items rather than two.",
 9: "EK 3.10.A.2, verbatim: the three movements are 'evidence of how the equal protection "
    "clause can support and motivate social movements.'",
 10: "EK 3.10.A.2's three named movements: the civil rights movement, the women's rights "
     "movement, and advocacy for LGBTQ rights. Other real movements are not named here.",
 11: "LO 3.10.A's verbs SUPPORTED and MOTIVATED, read against the suggested skill for the "
     "topic (4.C, source analysis). Both point at organising rather than at adjudication.",
 12: "'Letter from a Birmingham Jail' (required document), quoted verbatim; the CED attaches "
     "the Letter to 3.10.A. Read for implications per skill 4.C, the mutuality argument turns "
     "a local injustice into a national concern.",
 13: "'Letter from a Birmingham Jail', quoted verbatim. Splitting legal from moral "
     "responsibility presupposes that a law's justice can be judged apart from its enactment, "
     "which is the premise a movement needs to argue against a valid law.",
 14: "EK 3.10.A.2.i, which pairs the Letter with 'the civil rights movement of the 1960s'. The "
     "Letter is from 1963 and the Fourteenth Amendment was ratified in 1868, so the clause "
     "cannot have been a response to it.",
 15: "Gettysburg Address (required document), quoted verbatim; the CED attaches it to 3.10.A. "
     "Read per skill 4.C, it states a founding proposition rather than a description of "
     "conditions, which is what makes it usable as a standard.",
 16: "Emancipation Proclamation (required document), quoted verbatim; the CED attaches it to "
     "3.10.A. The limitation is on the text's own face -- places 'in rebellion against the "
     "United States'. EK 3.12.A.1.i records the Thirteenth Amendment as the permanent step.",
 17: "LO 3.10.A applied to the Proclamation's stated limit: a measure that invokes a principle "
     "while reaching part of the country supplies both the standard and the visible gap.",
 18: "Brown v. Board of Education (1954), required case, which the CED attaches to 3.10.A. CED "
     "holding: race-based school segregation violates the EQUAL PROTECTION clause of the "
     "Fourteenth Amendment -- the clause EK 3.10.A.2 names, producing a result.",
 19: "Engel v. Vitale (1962), required case, which the CED attaches to 3.10.A. CED holding: "
     "school sponsorship of religious activities violates the ESTABLISHMENT Clause. It belongs "
     "to this topic because RELIGION is one of EK 3.10.A.1's named characteristics.",
 20: "Wisconsin v. Yoder (1972), required case, which the CED attaches to 3.10.A. CED holding: "
     "compelling Amish students to attend school past the eighth grade violates the FREE "
     "EXERCISE Clause. Compulsory attendance is state law, so a state law gave way.",
 21: "EK 3.10.A.2.ii names the National Organization for Women specifically, which makes it "
     "course content rather than a substitutable example.",
 22: "EK 3.10.A.2.iii names 'the pro-life and pro-choice movements' in one item. Listing "
     "opposed movements under a claim about supporting and motivating shows the claim is "
     "about mobilisation and not about which side the clause vindicates.",
 23: "LO 3.10.A's two verbs separated: MOTIVATED describes an effect on people that precedes "
     "any ruling, SUPPORTED describes the clause producing a legal result.",
 24: "EK 3.10.A.1's provisions against EK 3.10.A.2's movements, read against their dates: the "
     "Fourteenth Amendment was ratified in 1868 and the movements the framework names formed "
     "a century later. A written guarantee and its realization are different things.",
 25: "Data item, CED skill 4.C. Both counts and the combined share are recomputed below.",
 26: "EK 3.10.A.1's four named characteristics, located as the rows of the table.",
 27: "Data item: a base-rate error. Both merit rates are recomputed below.",
 28: "Data item. The ratio between the two clause rows is recomputed below.",
 29: "EK 3.10.A.2's claim about the equal protection clause, shown as the table's largest row.",
 30: "EK 3.10.A.1's third source against a reading of the table's smallest row as an empty "
     "one. The count is recomputed below.",
}

FILED, MERIT = "Complaints filed", "Complaints found to have merit"
CHARACTERISTIC = "Characteristic alleged"
BASIS, PETITIONS, SHARE = ("Legal basis principally invoked", "Petitions",
                           "Share of all petitions (%)")


def _col(t, header):
    j = t["headers"].index(header)
    return [r[j] for r in t["rows"]]


def _row(t, needle):
    hits = [r for r in t["rows"] if needle in r[0]]
    assert len(hits) == 1, f"{needle!r} matches {len(hits)} rows, not one"
    return hits[0]


def q25(t):
    """Race and sex together exceed three quarters; religion is smallest."""
    filed = {r[0]: gc.num(r[1]) for r in t["rows"]}
    total = sum(filed.values())
    pair = filed["Race"] + filed["Sex"]
    assert pair / total > 0.75, f"race and sex are {gc.pct(pair, total)} percent, not above 75"
    assert min(filed, key=lambda k: filed[k]) == "Religion", \
        f"the smallest category is {min(filed, key=lambda k: filed[k])!r}, not Religion"
    assert filed["National origin"] < filed["Sex"], "national origin outnumbers sex"
    return (f"race {filed['Race']:.0f} plus sex {filed['Sex']:.0f} is {pair:.0f} of "
            f"{total:.0f}, {gc.pct(pair, total)} percent; religion smallest at "
            f"{filed['Religion']:.0f}")


def q26(t):
    """The rows are exactly EK 3.10.A.1's four characteristics."""
    names = [n.strip().lower() for n in _col(t, CHARACTERISTIC)]
    assert names == ["race", "national origin", "religion", "sex"], \
        f"the rows are {names}, not EK 3.10.A.1's four characteristics in order"
    return "rows are EK 3.10.A.1's four characteristics: " + ", ".join(names)


def q27(t):
    """Religion's merit rate is above race's, so religion is not the lowest."""
    rates = {r[0]: gc.pct(gc.num(r[2]), gc.num(r[1])) for r in t["rows"]}
    assert rates["Religion"] > rates["Race"], \
        f"religion {rates['Religion']} is not above race {rates['Race']}"
    assert min(rates, key=lambda k: rates[k]) != "Religion", \
        "religion IS the lowest merit rate, which the key denies"
    spread = max(rates.values()) - min(rates.values())
    assert spread < 6, f"the merit rates spread {spread} points, too far to call them close"
    return ("merit rates " + ", ".join(f"{k} {v}" for k, v in rates.items())
            + f" -- religion above race, spread {spread:.1f} points")


def q28(t):
    """Equal protection is invoked more than twice as often as due process."""
    ep = gc.num(_row(t, "Equal protection clause")[1])
    dp = gc.num(_row(t, "Due process clause")[1])
    fa = gc.num(_row(t, "First Amendment")[1])
    assert ep > 2 * dp, f"equal protection {ep:.0f} is not above twice due process {dp:.0f}"
    assert ep > fa and dp > fa, "the First Amendment row is not the smallest clause row"
    return (f"equal protection {ep:.0f} against due process {dp:.0f}, a ratio of "
            f"{ep / dp:.2f}; First Amendment {fa:.0f}")


def q29(t):
    """The largest row is the equal protection row, and the shares are consistent."""
    pet = [gc.num(c) for c in _col(t, PETITIONS)]
    total = sum(pet)
    biggest = max(t["rows"], key=lambda r: gc.num(r[1]))
    assert "Equal protection" in biggest[0], f"the largest row is {biggest[0]!r}"
    for r in t["rows"]:
        stated = gc.num(r[2])
        actual = gc.pct(gc.num(r[1]), total, 0)
        assert abs(stated - actual) <= 1, \
            f"{r[0]!r} states {stated} percent, recomputes to {actual}"
    assert sum(gc.num(c) for c in _col(t, SHARE)) == 100, "the stated shares do not total 100"
    return (f"largest row {biggest[0]!r} at {gc.num(biggest[1]):.0f} of {total:.0f}, "
            f"{gc.pct(gc.num(biggest[1]), total)} percent; every stated share recomputes")


def q30(t):
    """The statute row exists and is nonzero, so it is small rather than absent."""
    statute = _row(t, "act of Congress")
    n = gc.num(statute[1])
    assert n > 0, "the act-of-Congress row is zero, so the key's count is wrong"
    assert n == 20, f"the act-of-Congress row is {n:.0f}, not the 20 the key states"
    assert n == min(gc.num(r[1]) for r in t["rows"]), \
        "the act-of-Congress row is not the smallest, which the correction assumes"
    return f"act-of-Congress row is {n:.0f} petitions -- the smallest row, and not empty"


# --- module-specific content gates -------------------------------------------

def _three_sources(module):
    """EK 3.10.A.1 names three sources, and the statutory one may not be lost."""
    bad = []
    for i, item in enumerate(module.QUESTIONS, 1):
        key = item["choices"][item["ans"]].lower()
        stem = item["q"].lower()
        asks_sources = ("guaranteed" in stem and "source" in stem) or "from which sources" in stem
        if asks_sources and "acts of congress" not in key:
            bad.append(f"q{i} key: answers a question about the sources of civil rights without "
                       "naming acts of Congress; EK 3.10.A.1 names three sources and the third "
                       "is statutory")
        # No key may send a Fourteenth Amendment clause directly at private
        # conduct. The clause name merely APPEARING near a private actor is not
        # the defect -- item 8's key correctly reads "the equal protection
        # clause by its terms restrains a State RATHER THAN a private
        # business", and the first draft of this check reported it as a
        # violation. So a hit requires a reaching verb between the two AND no
        # contrastive or negating word in between. Same discipline as the
        # nearest-case-name rule in verify_v3_9.
        for clause in ("equal protection clause", "due process clause"):
            if clause not in key:
                continue
            at = key.index(clause)
            for private in ("private business", "private employer", "private restaurant",
                            "all discrimination of any kind"):
                pat = key.find(private, at)
                if pat < 0 or pat - at > 140:
                    continue
                between = key[at + len(clause):pat]
                reaching = any(v in between for v in ("reaches", "applies to", "binds",
                                                      "restrains", "prohibits", "forbids"))
                contrastive = any(n in between for n in ("rather than", " not ", "cannot",
                                                         "never", "instead of"))
                if reaching and not contrastive:
                    bad.append(f"q{i} key: sends the {clause} directly at {private!r}; the "
                               "Fourteenth Amendment's clauses are addressed to 'any State', "
                               "which is why EK 3.10.A.1 names acts of Congress as well")
    q3 = module.QUESTIONS[2]
    if "acts of congress" not in q3["choices"][q3["ans"]].lower():
        bad.append("q3: the key no longer carries EK 3.10.A.1's third source, acts of Congress")
    q7 = module.QUESTIONS[6]
    if "state" not in q7["choices"][q7["ans"]].lower():
        bad.append("q7: the key no longer names the State as the subject the Fourteenth "
                   "Amendment's clauses restrain")
    if bad:
        print(f"FAIL {module.__name__} three sources")
        for b in bad:
            print("  -", b)
        raise SystemExit(1)
    print(f"OK  {module.__name__} three sources: every key about the sources of civil rights "
          "names acts of Congress alongside the two clauses, and no key sends a Fourteenth "
          "Amendment clause directly at private conduct")


# Verdict words, each paired with the trailing context that would make it a
# judgement ON A MOVEMENT rather than an ordinary use of the word. Checked as
# explicit two-part phrases rather than as bare adjectives, because "justified"
# appears legitimately in EK 3.8.A.1's language about restricting rights and a
# bare-word scan would fire on it. Same discipline as the nearest-case-name rule
# in verify_v3_9: a checker that fires on correct text is worse than no checker.
_MOVEMENTS = ("civil rights movement", "women's rights movement", "lgbtq",
              "pro-life", "pro-choice", "national organization for women")
_VERDICTS = ("was right", "was wrong", "was mistaken", "was correct", "was justified",
             "was unjustified", "should have prevailed", "should not have prevailed",
             "is the correct position", "is the better position")


def _neutrality(module):
    """No key may pass a verdict on any movement EK 3.10.A.2 names."""
    bad = []
    for i, item in enumerate(module.QUESTIONS, 1):
        key = item["choices"][item["ans"]].lower()
        if not any(m in key for m in _MOVEMENTS):
            continue
        for v in _VERDICTS:
            if v in key:
                bad.append(f"q{i} key: passes the verdict {v!r} on a movement EK 3.10.A.2 "
                           "names. The framework's claim is that the equal protection clause "
                           "CAN SUPPORT AND MOTIVATE movements -- including movements that "
                           "oppose each other -- not that one of them is right")
    q22 = module.QUESTIONS[21]
    k22 = q22["choices"][q22["ans"]].lower()
    if "disagree with one another" not in k22 or "mobilization" not in k22:
        bad.append("q22: the key no longer states why EK 3.10.A.2.iii names two opposed "
                   "movements together -- that the claim is about mobilization")
    if bad:
        print(f"FAIL {module.__name__} neutrality")
        for b in bad:
            print("  -", b)
        raise SystemExit(1)
    print(f"OK  {module.__name__} neutrality: no key passes a verdict on any movement EK "
          "3.10.A.2 names, and the item on the framework's even-handedness still states it")


ua.shape(v3_10)
ua.check(v3_10, ANCHORS, GROUNDING)
ua.notation(v3_10)
_three_sources(v3_10)
_neutrality(v3_10)
gc.check(v3_10, arith={25: q25, 26: q26, 27: q27, 28: q28, 29: q29, 30: q30})
