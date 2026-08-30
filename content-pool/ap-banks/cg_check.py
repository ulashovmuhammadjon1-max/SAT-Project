"""Shared structural + key checks for the AP Comparative Government topic banks.

There is no sympy here. A comparative-politics key rests on a *claim* -- a
sentence in the Course and Exam Description -- so every ``verify_k<u>_<n>.py``
supplies a CLAIMS list with one entry per question:

    (anchor, claim)

``anchor`` is a distinctive substring that MUST appear in the keyed choice and
in none of the distractors. That is the part a computer can check: if a key
index is off by one, or a choice list is reordered while editing, the anchor
stops matching and the module fails. ``claim`` is the sentence stating what the
key rests on -- normally an essential-knowledge code plus the framework
assertion -- written for a human to audit. An unstated assertion is how a wrong
key ships.

WHAT THIS CANNOT DO, stated plainly so nobody mistakes a pass for a warrant:
it cannot tell whether the politics is right. It gates structure, key/anchor
agreement, and the arithmetic of data questions. The politics is gated by the
CLAIMS text and by the rule in SOCIAL_BRIEF.md that a key must be traceable to
the CED.

TABLE ARITHMETIC
----------------
A quantitative item carries ``table=dict(headers=[...], rows=[[...]])``. Its
verifier must supply a callable in ``table_checks`` that recomputes, from that
table alone, whatever the keyed choice asserts -- a difference, a rank, a ratio,
a direction of change. ``check`` FAILS if a question has a table and no such
callable, so a data question cannot ship unverified by being forgotten.

The helpers below read the table by header name and row label rather than by
index, so inserting a column cannot silently repoint a check at the wrong
numbers.

NO \\b ANYWHERE. A digit and a letter are both word characters, so ``\\b`` is
silently not a boundary exactly where it looks like one -- this project has paid
for that four separate times. Every phrase match here uses explicit lookarounds.
"""
import re
import unicodedata

_NUM = re.compile(r"-?\d+(?:\.\d+)?")


def normalize(text):
    """Lowercase, strip accents, drop punctuation, collapse whitespace."""
    t = unicodedata.normalize("NFKD", str(text))
    t = "".join(c for c in t if not unicodedata.combining(c)).lower()
    t = t.replace("’", "'").replace("‘", "'")
    t = t.replace("–", "-").replace("—", "-").replace("−", "-")
    t = re.sub(r"[^a-z0-9'%-]+", " ", t)
    return re.sub(r"\s+", " ", t).strip()


def contains_phrase(haystack, phrase):
    """``phrase`` present in ``haystack``, delimited by non-alphanumerics.

    Explicit lookarounds, never ``\\b``.
    """
    p = re.escape(normalize(phrase))
    return re.search(r"(?<![a-z0-9])" + p + r"(?![a-z0-9])", normalize(haystack)) is not None


# ---------------------------------------------------------------- table helpers

def num(text):
    """The single number in a cell, as a float. Percent signs and commas ignored."""
    hits = _NUM.findall(str(text).replace(",", ""))
    if len(hits) != 1:
        raise AssertionError(f"cell {text!r} does not hold exactly one number")
    return float(hits[0])


def col(table, header):
    """Every value in the named column, as floats, in row order."""
    try:
        j = [normalize(h) for h in table["headers"]].index(normalize(header))
    except ValueError:
        raise AssertionError(
            f"no column {header!r}; headers are {table['headers']}"
        ) from None
    return [num(r[j]) for r in table["rows"]]


def labels(table):
    """The first column, as strings -- normally the country names."""
    return [str(r[0]) for r in table["rows"]]


def cell(table, row_label, header):
    """One value, found by row label and column header."""
    rows = [i for i, lab in enumerate(labels(table))
            if normalize(lab) == normalize(row_label)]
    if len(rows) != 1:
        raise AssertionError(f"row {row_label!r} appears {len(rows)} times")
    return col(table, header)[rows[0]]


def ranked(table, header, reverse=True):
    """Row labels ordered by the named column; highest first by default."""
    pairs = list(zip(labels(table), col(table, header)))
    return [lab for lab, _ in sorted(pairs, key=lambda p: p[1], reverse=reverse)]


# ---------------------------------------------------------------- the main gate

# An option named by letter in a ``why`` or a ``claim`` rots the moment
# export_units.py shuffles the choices. Requires an explicit marker word, so the
# article "A" starting a sentence cannot match -- the LETTER_REF bug this
# project shipped three times.
_LETTER_REF = re.compile(
    r"(?<![A-Za-z])(?:[Cc]hoice|[Oo]ption|[Aa]nswer)\s+\(?([A-E])\)?(?![A-Za-z])"
)


def check(module, claims, table_checks=None, per_topic=30, n_choices=5):
    """Run every structural, key and table check. Raises AssertionError on failure."""
    table_checks = table_checks or {}
    code, title, unit = module.TOPIC
    qs = module.QUESTIONS
    assert len(qs) == per_topic, f"{code}: {len(qs)} questions, expected {per_topic}"
    assert len(claims) == per_topic, f"{code}: {len(claims)} claims, expected {per_topic}"

    n_tables = 0
    for i, (item, (anchor, claim)) in enumerate(zip(qs, claims), 1):
        ch, ans = item["choices"], item["ans"]
        assert len(ch) == n_choices, f"{code} q{i}: {len(ch)} choices, expected {n_choices}"
        assert 0 <= ans < n_choices, f"{code} q{i}: answer index {ans} out of range"
        assert len(set(ch)) == n_choices, f"{code} q{i}: duplicate choice strings"
        assert item["q"].strip(), f"{code} q{i}: empty stem"
        assert len(item["why"].split()) >= 8, f"{code} q{i}: why too thin: {item['why']!r}"

        for field, text in (("why", item["why"]), ("claim", claim)):
            hit = _LETTER_REF.search(text)
            assert not hit, (
                f"{code} q{i}: {field} names an option by letter ({hit.group(0)!r}); "
                "the exporter shuffles choices -- refer to the option by its content"
            )
        assert len(claim.split()) >= 8, f"{code} q{i}: claim too thin to audit: {claim!r}"

        # No choice may be wholly contained in another: if one option's entire
        # assertion sits inside a second option, a student who accepts the
        # shorter one has no ground to reject the longer, and the item has two
        # defensible answers.
        norms = [normalize(c) for c in ch]
        for a in range(n_choices):
            for b in range(n_choices):
                if a != b and norms[a] and norms[a] in norms[b]:
                    raise AssertionError(
                        f"{code} q{i}: choice {a} is contained in choice {b}: "
                        f"{ch[a]!r} inside {ch[b]!r}"
                    )

        # The anchor pins the key to its TEXT, so an off-by-one index fails here.
        assert contains_phrase(ch[ans], anchor), (
            f"{code} q{i}: anchor {anchor!r} not in keyed choice {ch[ans]!r}"
        )
        also = [k for k in range(n_choices) if k != ans and contains_phrase(ch[k], anchor)]
        assert not also, f"{code} q{i}: anchor {anchor!r} also matches choice(s) {also}"

        table = item.get("table")
        if table:
            n_tables += 1
            assert table["headers"] and table["rows"], f"{code} q{i}: empty table"
            width = len(table["headers"])
            for r in table["rows"]:
                assert len(r) == width, f"{code} q{i}: row {r} is not {width} wide"
            fn = table_checks.get(i)
            assert fn, (
                f"{code} q{i}: carries a table but no table_checks[{i}] recomputing it"
            )
            note = fn(table, item)
            assert isinstance(note, str) and len(note.split()) >= 4, (
                f"{code} q{i}: table check must return a sentence saying what it recomputed"
            )
        else:
            assert i not in table_checks, (
                f"{code} q{i}: table_checks[{i}] supplied but the question has no table"
            )

    for i in table_checks:
        assert 1 <= i <= per_topic, f"{code}: table_checks[{i}] is out of range"

    # No two stems inside one topic may open the same way.
    heads = {}
    for i, item in enumerate(qs, 1):
        h = normalize(item["q"])[:80]
        assert h not in heads, f"{code}: q{i} opens like q{heads[h]}"
        heads[h] = i

    print(f"OK  {code} {title} (unit {unit}): {len(qs)} questions, "
          f"{len(claims)} claims stated, {n_tables} data question(s) recomputed.")
