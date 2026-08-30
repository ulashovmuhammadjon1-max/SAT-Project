"""Structural gate for the AP Comparative Government Units 4-5 modules.

Every ``verify_k<unit>_<n>.py`` imports this. It cannot check the politics --
there is no sympy for a claim about Nigeria's Senate -- so it checks exactly
what a machine can check, and the authoring brief is explicit that this is the
whole job of the verifier:

* the module carries EXACTLY the required number of questions (30);
* every question has exactly five choices, pairwise distinct after
  normalisation, so "The Guardian Council." and "the Guardian Council" collide;
* no choice is a substring of another choice in the same item. A choice that is
  contained in a longer choice is the shape of an unanswerable question: if the
  longer one is keyed, the shorter one is usually also true;
* the key index is in range;
* ``why`` is present and is a reason, not a stub -- length is the only proxy a
  machine has, so the floor is deliberately low and the human is still the gate;
* no two stems in the module repeat;
* every question carrying a ``table`` has a recomputation function supplied by
  the verifier, and every recomputation function corresponds to a question that
  actually has a table. That second half matters: without it a table question
  can escape the arithmetic check by having its entry deleted, and a checker
  that silently checks nothing is the failure mode this project has paid for
  more than once.

The normalisation used for the distinctness and containment tests strips
punctuation and case and collapses whitespace. It deliberately does NOT strip
stopwords: "China and Iran" and "China or Iran" are different answers, and a
checker that over-matches is worse than no checker.
"""
import re
import sys

_PUNCT = re.compile(r"[^a-z0-9 ]+")
_WS = re.compile(r"\s+")


def norm(text):
    """Lowercase, strip punctuation, collapse whitespace."""
    return _WS.sub(" ", _PUNCT.sub(" ", text.lower())).strip()


_NUM = re.compile(r"-?\d+(?:\.\d+)?")


def nums(text):
    """Every number in ``text`` as floats, with thousands separators removed."""
    return [float(t) for t in _NUM.findall(str(text).replace(",", ""))]


def cell(table, row_label, col_label):
    """The cell at (row whose first entry is ``row_label``, column ``col_label``).

    Looks the row and column up by their printed labels rather than by index, so
    a verifier cannot silently drift out of alignment when a table is edited.
    """
    col = table["headers"].index(col_label)
    for row in table["rows"]:
        if row[0] == row_label:
            return row[col]
    raise KeyError(f"no row labelled {row_label!r}")


def column(table, col_label):
    """Every value in a column, in row order, as printed strings."""
    col = table["headers"].index(col_label)
    return [row[col] for row in table["rows"]]


def check(module, tables=None, per_topic=30, n_choices=5):
    """Run the structural gate over ``module``; exit non-zero on any finding."""
    tables = dict(tables or {})
    name = module.__name__
    code, title, unit = module.TOPIC
    qs = module.QUESTIONS
    bad = []

    def fail(msg):
        bad.append(msg)

    if not re.fullmatch(r"\d+\.\d+", code):
        fail(f"TOPIC code {code!r} is not of the form <unit>.<n>")
    if code.split(".")[0] != str(unit):
        fail(f"TOPIC code {code!r} disagrees with unit {unit}")
    if not title.strip():
        fail("TOPIC title is empty")

    if len(qs) != per_topic:
        fail(f"{per_topic} questions required, found {len(qs)}")

    stems = {}
    for i, item in enumerate(qs, 1):
        q, choices, ans, why = item["q"], item["choices"], item["ans"], item["why"]

        if not q.strip():
            fail(f"q{i}: empty stem")
        key = norm(q)
        if key in stems:
            fail(f"q{i}: stem repeats q{stems[key]}")
        stems[key] = i

        if len(choices) != n_choices:
            fail(f"q{i}: {n_choices} choices required, found {len(choices)}")
        normed = [norm(c) for c in choices]
        if any(not c for c in normed):
            fail(f"q{i}: an empty choice")
        if len(set(normed)) != len(normed):
            fail(f"q{i}: duplicate choices after normalisation")
        for a in range(len(normed)):
            for b in range(len(normed)):
                if a != b and normed[a] and normed[a] in normed[b]:
                    fail(f"q{i}: choice {a + 1} is contained in choice {b + 1}")

        if not isinstance(ans, int) or not 0 <= ans < len(choices):
            fail(f"q{i}: answer index {ans!r} out of range")

        if not why or len(why.strip()) < 40:
            fail(f"q{i}: 'why' is missing or too short to be a reason")

        has_table = bool(item.get("table"))
        if has_table:
            t = item["table"]
            width = len(t["headers"])
            if width < 2 or not t["rows"]:
                fail(f"q{i}: table needs at least two columns and one row")
            for r, row in enumerate(t["rows"], 1):
                if len(row) != width:
                    fail(f"q{i}: table row {r} has {len(row)} cells, header has {width}")
            fn = tables.pop(i, None)
            if fn is None:
                fail(f"q{i}: has a table but no recomputation function")
            else:
                try:
                    fn(item)
                except Exception as exc:
                    # Deliberately broad. A recomputation function that raises
                    # ValueError because a cell stopped being a number is
                    # reporting the same defect as one that raises
                    # AssertionError, and letting it escape as a traceback
                    # would hide the other questions' findings behind it.
                    fail(f"q{i}: table arithmetic disagrees -- {type(exc).__name__}: {exc}")
        elif i in tables:
            fail(f"q{i}: recomputation function supplied but the question has no table")
            tables.pop(i)

    for leftover in sorted(tables):
        fail(f"q{leftover}: recomputation function supplied for a question that does not exist")

    if bad:
        print(f"FAIL {name} ({code} {title}, unit {unit})")
        for line in bad:
            print("  " + line)
        sys.exit(1)
    n_tab = sum(1 for it in qs if it.get("table"))
    print(f"OK {name}: {code} {title} (unit {unit}) -- {len(qs)} questions, "
          f"{n_choices} choices each, {n_tab} with recomputed tables")
