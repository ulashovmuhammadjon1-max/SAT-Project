"""Shared structural + key checks for the AP Human Geography topic banks.

There is no sympy here. A geography key rests on a *claim* -- what the CED's
essential knowledge actually says, what a named model actually predicts, or what
a set of numbers actually shows -- so each `verify_g<unit>_<n>.py` supplies a
CLAIMS list with one entry per question, in module order:

    (anchor, claim)              for a question with no data stimulus
    (anchor, claim, recompute)   for a question carrying a `table=`

`anchor` is a distinctive substring that MUST appear in the keyed choice and in
none of the distractors. That is the part a machine can check: if a key index is
off by one, or a choice list is reordered during an edit, the anchor stops
matching and the module fails. `claim` is the sentence stating what the key
rests on, written for a human to audit -- an unstated assertion is how a wrong
key ships.

`recompute` is REQUIRED on every question that has a table, and it is the one
genuinely computational gate in this bank. It receives the question's own table
as `dict(headers=[...], rows=[[...]])` and must recompute, from those cells, the
arithmetic the key depends on. It returns either:

    True   -- the function asserted everything itself
    a str  -- a value that must appear in the keyed choice

Returning False, or a string that is not in the keyed choice, fails the module.
A table question with no recompute function fails too: that is the whole point.
The failure mode being prevented is a stimulus table whose numbers drifted away
from the answer during editing, which no amount of reading catches reliably.

WHY EXPLICIT LOOKAROUNDS AND NEVER \\b
--------------------------------------
This project has produced a word-boundary own-goal in every build: `\\bpi` never
matched because a digit and a letter are both word characters; a LETTER_REF
pattern matched the article "A"; a setting check matched the "fen" inside
"fence". Every substring test below is delimited with explicit
`(?<![a-z0-9])` / `(?![a-z0-9])` lookarounds. A boundary-free substring match in
a checker is worse than no check, because it trains you to ignore the output.
"""
import re
import unicodedata

# Pairs (or larger sets) of MULTI-WORD phrases that name the same thing. Two
# choices in one question drawn from the same class make the question
# unanswerable, which is a defect no "duplicate string" check would see.
#
# Only genuine synonyms belong here. "Periphery" and "less developed country"
# are NOT in the list: in this course they come from different frameworks
# (Wallerstein's world-systems vs. a development-measure ranking) and a question
# may legitimately offer both.
SYNONYM_CLASSES = [
    # --- Unit 1: maps, data, space, region ---
    {"perceptual region", "vernacular region"},
    {"geographic information system", "geographic information systems", "gis"},
    {"absolute location", "coordinate location"},
    {"time-space compression", "time space compression"},
    {"thematic map", "statistical map"},
    {"formal region", "uniform region", "homogeneous region"},
    {"functional region", "nodal region"},
    # --- Unit 2: population and migration ---
    {"crude birth rate", "cbr"},
    {"crude death rate", "cdr"},
    {"total fertility rate", "tfr"},
    {"infant mortality rate", "imr"},
    {"rate of natural increase", "natural increase rate", "rni"},
    {"arithmetic density", "arithmetic population density", "crude density"},
    {"physiological density", "physiologic density"},
    {"dependency ratio", "age dependency ratio"},
    {"pronatalist policy", "pro-natalist policy"},
    {"antinatalist policy", "anti-natalist policy"},
    {"internally displaced person", "internally displaced persons"},
    {"population pyramid", "age-sex pyramid", "age-sex structure diagram"},
    {"demographic transition model", "dtm"},
    {"replacement level fertility", "replacement-level fertility"},
    # --- Unit 3: culture and diffusion ---
    {"contagious diffusion", "contagious expansion diffusion"},
    {"hierarchical diffusion", "hierarchical expansion diffusion"},
    {"stimulus diffusion", "stimulus expansion diffusion"},
    {"relocation diffusion", "diffusion by physical movement of people"},
    {"cultural landscape", "built landscape", "anthropogenic landscape"},
    {"universalizing religion", "proselytizing religion"},
    {"lingua franca", "common language of trade and commerce"},
    {"toponym", "place name"},
    {"placemaking", "place-making"},
]


def normalize(text):
    """Lowercase, strip accents and punctuation, collapse whitespace.

    Hyphens and apostrophes survive, because `anti-natalist` and `antinatalist`
    must stay distinguishable for the synonym classes to have anything to say.
    """
    t = unicodedata.normalize("NFKD", str(text))
    t = "".join(c for c in t if not unicodedata.combining(c)).lower()
    t = t.replace("’", "'").replace("–", "-").replace("—", "-")
    t = re.sub(r"[^a-z0-9'/-]+", " ", t)
    return re.sub(r"\s+", " ", t).strip()


def _contains_phrase(haystack_norm, phrase):
    p = re.escape(normalize(phrase))
    return re.search(r"(?<![a-z0-9])" + p + r"(?![a-z0-9])", haystack_norm) is not None


def synonym_conflicts(choices):
    """Pairs of choices in one question that name the same thing."""
    norms = [normalize(c) for c in choices]
    problems = []
    for i in range(len(norms)):
        for j in range(i + 1, len(norms)):
            if norms[i] == norms[j]:
                problems.append((i, j, "identical after normalization"))
                continue
            for cls in SYNONYM_CLASSES:
                hit_i = [p for p in cls if _contains_phrase(norms[i], p)]
                hit_j = [p for p in cls if _contains_phrase(norms[j], p)]
                if hit_i and hit_j and set(hit_i) != set(hit_j):
                    problems.append(
                        (i, j, f"same construct: {sorted(hit_i)} vs {sorted(hit_j)}")
                    )
                    break
    return problems


def superset_conflicts(choices):
    """A choice that wholly contains another choice.

    "Spanish" alongside "Spanish and Portuguese" gives a student a defensible
    argument for two options at once. The containment is tested with the same
    explicit delimiters used everywhere else, and only for a contained phrase of
    at least three words -- a shorter one is ordinary shared vocabulary
    ("the government", "a city") and flagging it would be the over-matching
    failure this file exists to avoid.
    """
    norms = [normalize(c) for c in choices]
    problems = []
    for i, a in enumerate(norms):
        for j, b in enumerate(norms):
            if i == j or len(b.split()) < 3 or len(b) >= len(a):
                continue
            if _contains_phrase(a, b):
                problems.append((j, i, f"choice {j} is contained whole in choice {i}"))
    return problems


def num(cell):
    """The number in a table cell, ignoring commas, currency, units and %.

    Returns a float. Raises ValueError if the cell holds no number, which is the
    right behaviour: a recompute function reaching for a number that is not
    there should fail loudly rather than silently score zero.
    """
    s = str(cell).replace(",", "").replace("−", "-").replace("–", "-")
    m = re.search(r"-?\d+(?:\.\d+)?", s)
    if not m:
        raise ValueError(f"no number in table cell {cell!r}")
    return float(m.group(0))


def column(table, header):
    """Every cell of the column whose header equals `header`, as written."""
    try:
        k = [normalize(h) for h in table["headers"]].index(normalize(header))
    except ValueError:
        raise ValueError(
            f"no column {header!r}; headers are {table['headers']}"
        ) from None
    return [row[k] for row in table["rows"]]


def numcol(table, header):
    """`column`, converted to floats."""
    return [num(c) for c in column(table, header)]


def rowdict(table, row):
    """One table row as {header: cell}."""
    return dict(zip(table["headers"], row))


LETTER_REF = re.compile(
    r"(?<![A-Za-z])(?:[Cc]hoice|[Oo]ption|[Aa]nswer)\s+\(?([A-E])\)?(?![A-Za-z])"
)


def check(module, claims, per_topic=30, n_choices=5):
    """Run every structural and key check. Raises AssertionError on failure."""
    code, title, unit = module.TOPIC
    qs = module.QUESTIONS
    assert len(qs) == per_topic, f"{code}: {len(qs)} questions, expected {per_topic}"
    assert len(claims) == per_topic, f"{code}: {len(claims)} claims, expected {per_topic}"
    assert code.split(".")[0] == str(unit), f"{code}: code does not sit in unit {unit}"

    tables_checked = 0
    for i, (item, entry) in enumerate(zip(qs, claims), 1):
        anchor, claim = entry[0], entry[1]
        recompute = entry[2] if len(entry) > 2 else None
        ch, ans = item["choices"], item["ans"]

        assert len(ch) == n_choices, f"{code} q{i}: {len(ch)} choices, expected {n_choices}"
        assert isinstance(ans, int) and 0 <= ans < n_choices, (
            f"{code} q{i}: answer index {ans!r} out of range"
        )
        assert len(set(ch)) == n_choices, f"{code} q{i}: duplicate choice strings"
        assert all(str(c).strip() for c in ch), f"{code} q{i}: an empty choice"
        assert item["q"].strip(), f"{code} q{i}: empty stem"
        assert len(item["why"].split()) >= 8, (
            f"{code} q{i}: `why` too thin to be a reason: {item['why']!r}"
        )
        # A `why` that only restates the keyed choice explains nothing. Flag the
        # case where the whole keyed choice is quoted back with nothing else.
        assert normalize(item["why"]) != normalize(ch[ans]), (
            f"{code} q{i}: `why` merely restates the answer"
        )

        assert len(claim.split()) >= 6, f"{code} q{i}: claim too thin to audit: {claim!r}"
        m = LETTER_REF.search(claim)
        assert not m, (
            f"{code} q{i}: claim names an option by letter ({m.group(0)!r}); "
            "export_units.py shuffles the choices -- name the option by its content"
        )
        m = LETTER_REF.search(item["why"])
        assert not m, (
            f"{code} q{i}: `why` names an option by letter ({m.group(0)!r}); "
            "export_units.py shuffles the choices -- name the option by its content"
        )

        # The anchor pins the key to its TEXT, so an off-by-one index fails here.
        assert _contains_phrase(normalize(ch[ans]), anchor), (
            f"{code} q{i}: anchor {anchor!r} not in keyed choice {ch[ans]!r}"
        )
        also = [k for k in range(n_choices)
                if k != ans and _contains_phrase(normalize(ch[k]), anchor)]
        assert not also, f"{code} q{i}: anchor {anchor!r} also matches choice(s) {also}"

        for a, b, reason in synonym_conflicts(ch):
            raise AssertionError(f"{code} q{i}: choices {a} and {b} -- {reason}")
        for a, b, reason in superset_conflicts(ch):
            raise AssertionError(f"{code} q{i}: {reason}")

        table = item.get("table")
        if table is not None:
            assert table["headers"] and table["rows"], f"{code} q{i}: empty table"
            width = len(table["headers"])
            for r, row in enumerate(table["rows"]):
                assert len(row) == width, (
                    f"{code} q{i}: table row {r} has {len(row)} cells, header has {width}"
                )
            assert recompute is not None, (
                f"{code} q{i}: has a table but no recompute function; every arithmetic "
                "claim in a data question must be recomputed from the table itself"
            )
            result = recompute(table)
            if isinstance(result, str):
                assert _contains_phrase(normalize(ch[ans]), result), (
                    f"{code} q{i}: recomputed {result!r} is not in the keyed choice "
                    f"{ch[ans]!r}"
                )
            else:
                assert result is True, (
                    f"{code} q{i}: recompute returned {result!r}, expected True or a string"
                )
            tables_checked += 1
        else:
            assert recompute is None, (
                f"{code} q{i}: a recompute function was supplied but the question has "
                "no table"
            )

    # No two stems inside one topic may open the same way.
    heads = {}
    for i, item in enumerate(qs, 1):
        h = normalize(item["q"])[:80]
        assert h not in heads, f"{code}: q{i} opens like q{heads[h]}"
        heads[h] = i

    print(
        f"OK  {code} {title} (unit {unit}): {len(qs)} questions, {len(claims)} claims, "
        f"{tables_checked} table(s) recomputed, no synonym or superset collisions."
    )
