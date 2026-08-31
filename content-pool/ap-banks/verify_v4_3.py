"""Structural gate for AP U.S. Government 4.3 Changes in Ideology.

gov345_check plus the four usgov_anchor helpers, plus two content gates.

  _effects   EK 4.3.A.1's two parentheses differ by what the experience BELONGS
             TO -- "experiences shared by people of a COMMON AGE" against
             "experiences a person encounters during different LIFE STAGES" --
             and swapping them is the error this whole topic exists to prevent.
             It is also completely invisible to an anchor: a key that defines
             generational effects using the life cycle parenthesis still sits in
             its own choice and still matches its own substring. The gate reads
             every key that names one of the two terms and refuses any that
             gives it the other's definition, attributing a definition to the
             term NEAREST BEFORE IT so that item 4, whose key correctly
             contrasts both in one sentence, is not reported.

  _no_verdict EK 4.3.A.1 says both effects CONTRIBUTE to the development of a
             person's political ideology, and stops. It does not say which is
             stronger, which ideology either produces, or what any actual
             generation believes. All three are things a confident author would
             supply, and any of them would reach a student with the framework's
             own authority. The gate refuses them, which is also why every table
             in this module measures an unnamed "particular position" rather
             than a real one -- naming a position would smuggle the empirical
             claim in through the stimulus instead of the key.

WHY THE TABLES ARE A MATCHED PAIR
---------------------------------
Items 22 to 24 and 25 to 27 present the same underlying question -- older
respondents hold a position more often -- in two data shapes that a single
cross section could not tell apart. In the first, cohorts keep their levels as
they age, so the difference travels with the people: generational. In the
second, age brackets keep their levels while their occupants turn over, so the
difference stays with the stage: life cycle. Item 12 states the reason a single
survey can never separate them, and item 30 states the reason repeated cross
sections still cannot follow an individual. Those two refusals are what make the
rest of the module's data claims honest, so the checks below assert the shapes
rather than trusting the prose: q22 asserts each row is FLAT across years while
the rows differ, and q25 asserts each COLUMN climbs while the rows stay flat.
"""
import gov345_check as gc
import usgov_anchor as ua
import v4_3

ANCHORS = {
 1: "Experiences shared by people of a common age",
 2: "Experiences a person encounters during different life stages",
 3: "Contribute to the development of a person's political ideology",
 4: "while a life cycle effect attaches to a stage of life that every cohort reaches",
 5: "because the experience is shared by people of a common age",
 6: "encountered at a particular life stage rather than by one cohort",
 7: "Because the framework says both contribute, without ranking them",
 8: "whether by age or by life stage",
 9: "so the distinctiveness moves up the age ladder over time",
 10: "even though the people occupying them have changed",
 11: "stays with the same age brackets or travels with the same cohorts",
 12: "every age group is also a single birth cohort",
 13: "since it is an experience encountered during a life stage",
 14: "since the experience was shared by people who reached a common point at the same",
 15: "an experience of schooling that people of other ages did not have",
 16: "it does not say which ideology results",
 17: "one through contributors such as family and media and the other through shared",
 18: "the views belong to the stage and the group will hold different ones",
 19: "travel with those people as they age, or stay attached to the ages themselves",
 20: "are separated by the shape of data over time",
 21: "Which of the two effects has the greater influence on political ideology",
 22: "each one's share is nearly unchanged across the twenty years",
 23: "because the differences stay attached to the birth cohorts as those cohorts age",
 24: "would move toward the level held by older cohorts as that cohort aged",
 25: "The share rises steadily with age within each survey year",
 26: "because the pattern stays attached to the age brackets even though different",
 27: "would show the distinctive figures moving up the age ladder over time",
 28: "every age group's turnout is highest in the second election",
 29: "rather than a change in any one group's life stage",
 30: "rather than the same individuals over time",
}

GROUNDING = {
 1: "EK 4.3.A.1's first parenthesis, verbatim: generational effects are 'experiences shared by "
    "people of a common age.'",
 2: "EK 4.3.A.1's second parenthesis, verbatim: life cycle effects are 'experiences a person "
    "encounters during different life stages.'",
 3: "EK 4.3.A.1's shared verb: both 'contribute to the development of a person's political "
    "ideology.' Contribution rather than determination.",
 4: "EK 4.3.A.1's two parentheses set against each other. They differ in what the experience "
    "belongs to -- people of a common age, or a life stage -- and the rest follows.",
 5: "EK 4.3.A.1's first parenthesis applied. What matters is that the experience belongs to "
    "the group that lived it rather than to the stage they were at.",
 6: "EK 4.3.A.1's second parenthesis applied. The phrase WHATEVER DECADE THEY WERE BORN IN is "
    "what rules out the cohort explanation.",
 7: "EK 4.3.A.1 names both effects in one sentence with one verb and supplies no weighting. A "
    "key asserting that either dominates would state a conclusion the framework declines.",
 8: "LO 4.3.A's phrase SOCIAL FACTORS against both parentheses, each of which describes an "
    "experience held in common rather than an idiosyncratic one.",
 9: "EK 4.3.A.1's first parenthesis read as a testable signature: a difference tied to people "
    "of a common age travels with that cohort rather than staying at an age.",
 10: "EK 4.3.A.1's second parenthesis read as a testable signature: a difference tied to a life "
     "stage stays with the stage while its occupants turn over.",
 11: "EK 4.3.A.1's two effects are consistent with the same single cross section, because at "
     "one moment a cohort and an age bracket contain the same people. Only repeated "
     "measurement separates them.",
 12: "The identity of age and birth year at a single moment, which is why EK 4.3.A.1's "
     "distinction cannot be drawn from one observation.",
 13: "EK 4.3.A.1's second parenthesis applied to approaching retirement, a stage every cohort "
     "reaches in turn.",
 14: "EK 4.3.A.1's first parenthesis applied. The detail that the views persist REGARDLESS OF "
     "CURRENT AGE is what locates them in the cohort rather than in a stage.",
 15: "Brown v. Board of Education (1954), required case, which the CED attaches to 4.3.A. CED "
     "holding: race-based school segregation violates the equal protection clause of the "
     "Fourteenth Amendment. Used to APPLY EK 4.3.A.1's definition of a generational effect -- "
     "a change in schooling reaches those of school age and not others -- and not to assert "
     "any claim about what a generation concluded.",
 16: "EK 4.3.A.1's verb CONTRIBUTE, and the absence from the framework of any named ideology "
     "or named generation.",
 17: "EK 4.2.A.1's contributors against EK 4.3.A.1's two effects: the same developmental "
     "process described from different angles.",
 18: "EK 4.3.A.1's life cycle parenthesis, which makes the experience belong to a stage and so "
     "predicts change as a group ages rather than persistence.",
 19: "LO 4.3.A's object, how social factors impact political ideology, together with the only "
     "observation that separates EK 4.3.A.1's two effects.",
 20: "The CED's assignment of skill 3.B (describe patterns and trends in data) to this topic "
     "rather than a concept skill, which follows from the two definitions being "
     "indistinguishable in any single description of a finding.",
 21: "EK 4.3.A.1 read for what it omits. Every other option restates part of its one sentence; "
     "a comparison of magnitude is the thing that sentence does not contain.",
 22: "Data item, CED skill 3.B. Every row's movement and every between-row gap is recomputed.",
 23: "EK 4.3.A.1's generational signature located in data: the difference travels with the "
     "cohort. Recomputed below.",
 24: "EK 4.3.A.1's life cycle definition applied counterfactually to the same table.",
 25: "Data item, CED skill 3.B. The age gradient and each row's flatness are recomputed below.",
 26: "EK 4.3.A.1's life cycle signature located in data, with the stem's statement that "
     "different individuals were interviewed each time doing the necessary work.",
 27: "Data item: the generational reading tested against the same table and refuted, since the "
     "levels do not move up the age ladder. Recomputed below.",
 28: "Data item, CED skill 3.B. The age gradient and the common second-election peak are both "
     "recomputed below.",
 29: "A movement common to all four age groups fits neither of EK 4.3.A.1's effects, since one "
     "belongs to a stage and the other to a cohort.",
 30: "The stem's own statement that different individuals were surveyed after each election. "
     "Repeated cross sections cannot follow a person, which is the error that makes EK "
     "4.3.A.1's two effects look interchangeable.",
}

Y1, Y11, Y21 = "Survey year 1 (%)", "Survey year 11 (%)", "Survey year 21 (%)"
E1, E2, E3 = "First election (%)", "Second election (%)", "Third election (%)"


def _rows(t):
    """Each row as (label, [numbers])."""
    return [(r[0], [gc.num(c) for c in r[1:]]) for r in t["rows"]]


def _cols(t):
    """Each data column as a list of numbers, top to bottom."""
    return [[gc.num(r[j]) for r in t["rows"]] for j in range(1, len(t["headers"]))]


def q22(t):
    """Rows are flat across years; the rows differ sharply from one another."""
    rows = _rows(t)
    for name, vals in rows:
        assert max(vals) - min(vals) <= 2, f"cohort {name!r} moves {max(vals) - min(vals):.0f}"
    means = [sum(v) / len(v) for _, v in rows]
    gaps = [abs(a - b) for a, b in zip(means, means[1:])]
    assert min(gaps) > 10, f"two cohorts sit within {min(gaps):.1f} points of each other"
    assert means == sorted(means, reverse=True), "the cohorts are not ordered by birth decade"
    return ("each cohort flat within 2 points across twenty years; cohort levels "
            + ", ".join(f"{m:.0f}" for m in means)
            + f", nearest gap {min(gaps):.0f} points")


def q23(t):
    """The generational signature: level travels with the cohort, not the year."""
    rows = _rows(t)
    within = max(max(v) - min(v) for _, v in rows)
    between = max(sum(v) / len(v) for _, v in rows) - min(sum(v) / len(v) for _, v in rows)
    assert between > 5 * within, \
        f"between-cohort spread {between:.1f} is not far above within-cohort movement {within:.1f}"
    return (f"between-cohort spread {between:.0f} points against at most {within:.0f} points "
            "of movement within any cohort -- the difference travels with the cohort")


def q24(t):
    """The cohorts do NOT converge, which is what the counterfactual asks about."""
    rows = _rows(t)
    first_spread = max(v[0] for _, v in rows) - min(v[0] for _, v in rows)
    last_spread = max(v[-1] for _, v in rows) - min(v[-1] for _, v in rows)
    assert last_spread >= first_spread - 1, \
        f"the cohorts converge from {first_spread:.0f} to {last_spread:.0f}, so the key's " \
        "counterfactual is already what the table shows"
    return (f"spread between cohorts {first_spread:.0f} points in the first year and "
            f"{last_spread:.0f} in the last -- no convergence to describe")


def q25(t):
    """Every column climbs with age; every row is flat across years."""
    for j, col in enumerate(_cols(t)):
        assert col == sorted(col), f"column {j} does not rise with age: {col}"
        assert len(set(col)) == len(col), f"column {j} has a tie: {col}"
    for name, vals in _rows(t):
        assert max(vals) - min(vals) <= 2, f"age group {name!r} moves {max(vals) - min(vals):.0f}"
    col0 = _cols(t)[0]
    return (f"first column climbs {', '.join(f'{c:.0f}' for c in col0)}, a rise of "
            f"{col0[-1] - col0[0]:.0f} points; every row flat within 2 points")


def q26(t):
    """The gradient is by age and not by year, which is the life cycle signature."""
    cols = _cols(t)
    by_age = max(cols[0]) - min(cols[0])
    by_year = max(max(v) - min(v) for _, v in _rows(t))
    assert by_age > 10 * by_year, \
        f"the age gradient {by_age:.0f} is not far above the year movement {by_year:.0f}"
    return (f"age gradient {by_age:.0f} points against at most {by_year:.0f} points across "
            "years -- the pattern stays with the bracket")


def q27(t):
    """The youngest bracket's level does not reappear one bracket up twenty years later."""
    rows = _rows(t)
    young_first = rows[0][1][0]
    next_last = rows[1][1][-1]
    assert abs(next_last - young_first) > 10, \
        (f"the youngest first-year level {young_first:.0f} does reappear in the next bracket "
         f"at {next_last:.0f}, which would be the generational signature the key denies")
    return (f"youngest bracket starts at {young_first:.0f}; the next bracket up reads "
            f"{next_last:.0f} twenty years later, not {young_first:.0f} -- no cohort carry")


def q28(t):
    """Turnout climbs with age in every election, and the second election leads every row."""
    for j, col in enumerate(_cols(t)):
        assert col == sorted(col), f"election {j + 1} turnout does not rise with age: {col}"
    j2 = t["headers"].index(E2) - 1
    for name, vals in _rows(t):
        assert vals[j2] == max(vals), f"{name!r} does not peak in the second election: {vals}"
    return ("turnout rises with age in all three elections; the second election is the "
            f"highest figure in all {len(t['rows'])} rows")


def q29(t):
    """Every row moves the same way, which no single-group explanation covers."""
    rows = _rows(t)
    j2 = t["headers"].index(E2) - 1
    gains = [vals[j2] - vals[0] for _, vals in rows]
    assert all(g > 0 for g in gains), f"not every group rises into the second election: {gains}"
    assert max(gains) - min(gains) <= 4, f"the gains differ too widely to call common: {gains}"
    return ("every age group gains into the second election, by "
            + ", ".join(f"{g:.0f}" for g in gains) + " points -- a common movement")


def q30(t):
    """Four distinct age brackets, three elections, and no row is a person."""
    names = [r[0] for r in t["rows"]]
    assert len(names) == len(set(names)) == 4, f"the rows are {names}"
    assert all("Age" in n for n in names), f"a row is not an age bracket: {names}"
    assert len(t["headers"]) - 1 == 3, "there are not three elections"
    return f"{len(names)} age brackets across 3 elections -- brackets, never individuals"


# --- module-specific content gates -------------------------------------------

_GEN, _LIFE = "generational effect", "life cycle effect"
_GEN_DEF = ("shared by people of a common age", "common age", "birth cohort", "cohort",
            "born around the same time", "reached a common point at the same")
_LIFE_DEF = ("different life stages", "a life stage", "life stage", "as they age",
             "every cohort reaches in turn", "particular life stage")


def _nearest_term(text, at):
    """Whichever of the two term names sits nearest before an offset."""
    g, l = text.rfind(_GEN, 0, at), text.rfind(_LIFE, 0, at)
    if g < 0 and l < 0:
        return None
    return _GEN if g > l else _LIFE


def _effects(module):
    """Neither term may be given the other's definition."""
    bad = []
    for i, item in enumerate(module.QUESTIONS, 1):
        key = item["choices"][item["ans"]].lower()
        if _GEN not in key and _LIFE not in key:
            continue
        for defn in _LIFE_DEF:
            at = key.find(defn)
            while at >= 0:
                if _nearest_term(key, at) == _GEN:
                    bad.append(f"q{i} key: defines a GENERATIONAL effect with the life cycle "
                               f"parenthesis ({defn!r}); EK 4.3.A.1 says generational effects "
                               "are experiences SHARED BY PEOPLE OF A COMMON AGE")
                    break
                at = key.find(defn, at + 1)
        for defn in ("shared by people of a common age", "born around the same time"):
            at = key.find(defn)
            if at >= 0 and _nearest_term(key, at) == _LIFE:
                bad.append(f"q{i} key: defines a LIFE CYCLE effect with the generational "
                           f"parenthesis ({defn!r}); EK 4.3.A.1 says life cycle effects are "
                           "experiences encountered DURING DIFFERENT LIFE STAGES")
    q1 = module.QUESTIONS[0]
    if "shared by people of a common age" not in q1["choices"][q1["ans"]].lower():
        bad.append("q1: the key no longer carries EK 4.3.A.1's generational parenthesis")
    q2 = module.QUESTIONS[1]
    if "different life stages" not in q2["choices"][q2["ans"]].lower():
        bad.append("q2: the key no longer carries EK 4.3.A.1's life cycle parenthesis")
    if bad:
        print(f"FAIL {module.__name__} effects")
        for b in bad:
            print("  -", b)
        raise SystemExit(1)
    print(f"OK  {module.__name__} effects: no key gives either of EK 4.3.A.1's two terms the "
          "other's parenthesis, and both definitions survive in the items that state them")


_VERDICTS = (
    "generational effects always outweigh", "life cycle effects always outweigh",
    "generational effects are stronger than", "life cycle effects are stronger than",
    "the framework names the ideology each generation holds",
    "is the more important of the two",
)


def _no_verdict(module):
    """EK 4.3.A.1 ranks nothing and names no ideology; no key may."""
    bad = []
    for i, item in enumerate(module.QUESTIONS, 1):
        key = item["choices"][item["ans"]].lower()
        for v in _VERDICTS:
            if v in key:
                bad.append(f"q{i} key: states {v!r}. EK 4.3.A.1 says both effects CONTRIBUTE "
                           "to the development of a person's political ideology and supplies "
                           "no weighting, no ideology and no generation")
    # No table may name a real position, party or generation: doing so would put
    # the empirical claim in the stimulus, where no key-level gate would see it.
    named = ("liberal", "conservative", "libertarian", "democrat", "republican",
             "baby boom", "millennial", "generation x", "abortion", "gun", "immigration")
    for i, item in enumerate(module.QUESTIONS, 1):
        t = item.get("table")
        if not t:
            continue
        cells = [c.lower() for c in t["headers"]] + [c.lower() for r in t["rows"] for c in r]
        for cell in cells:
            for n in named:
                if n in cell:
                    bad.append(f"q{i} table: the cell {cell!r} names {n!r}. Every stimulus in "
                               "this module measures an unnamed 'particular position', because "
                               "naming one would assert an empirical claim EK 4.3.A.1 does not "
                               "make -- and it would do it in the stimulus, where a key-level "
                               "check would never look")
    q7 = module.QUESTIONS[6]
    if "without ranking them" not in q7["choices"][q7["ans"]].lower():
        bad.append("q7: the key no longer records that EK 4.3.A.1 declines to rank its two "
                   "effects")
    q21 = module.QUESTIONS[20]
    if "greater influence" not in q21["choices"][q21["ans"]].lower():
        bad.append("q21: the key no longer identifies the comparison of magnitude as the thing "
                   "EK 4.3.A.1 does not state")
    if bad:
        print(f"FAIL {module.__name__} no verdict")
        for b in bad:
            print("  -", b)
        raise SystemExit(1)
    print(f"OK  {module.__name__} no verdict: no key ranks EK 4.3.A.1's two effects or names an "
          "ideology, and no table names a real position, party or generation")


ua.shape(v4_3)
ua.check(v4_3, ANCHORS, GROUNDING)
ua.notation(v4_3)
_effects(v4_3)
_no_verdict(v4_3)
gc.check(v4_3, arith={22: q22, 23: q23, 24: q24, 25: q25, 26: q26, 27: q27,
                      28: q28, 29: q29, 30: q30})
