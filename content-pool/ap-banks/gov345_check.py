"""Structural audit shared by the AP U.S. Government Units 3-5 topic modules.

There is no sympy here, and there is no way for a script to know whether
Wisconsin v. Yoder came out the way a question says it did. So this file does
not pretend to check the politics. It checks the things a machine can actually
settle, and it is deliberately strict about them, because everything it does
NOT check has to be carried by a human reading the module.

WHAT IT CHECKS
--------------
* exactly 30 questions, five choices each, a valid key index
* no two choices in one question identical after normalization
* no choice that is a SUPERSET of another -- if one choice's text contains
  another's whole text, the shorter one is true whenever the longer one is and
  the question has two defensible keys
* a non-empty stem and a non-empty `why`, and a `why` long enough to be a reason
* a `why` may not name an option BY LETTER. export_units.py redistributes the
  key across A-E, so "option C" in an explanation points at whatever landed in
  that slot -- and it rots silently the moment a distractor is edited
* no two stems in a topic open the same way
* every `table` is rectangular, and every table question must have an entry in
  the verifier's ARITH map that RECOMPUTES its arithmetic from the table itself

THE DIGIT-HYPHEN-DIGIT RULE, which is not a style preference
------------------------------------------------------------
export_units.py runs every string through mathfmt.convert on the way out.
Measured on this subject's own prose, that converter reads an ASCII hyphen
between two digits as a MINUS SIGN:

    "In a 5-4 decision"       ->  "In a \\(5 - 4\\) decision"
    "voters aged 18-24"       ->  "voters aged \\(18 - 24\\)"
    "the 2020-2024 cycle"     ->  "the \\(2020 - 2024\\) cycle"

A U.S. Government bank is full of vote splits and age brackets, so this would
have fired on a large fraction of the questions in Units 3 and 5 and produced
typeset subtraction where a student expects a Court's margin. Write "5 to 4",
"ages 18 to 24", or an EN DASH (18-24 with U+2013), all three of which the
converter leaves alone. This check enforces it so the rule cannot quietly lapse.
"""
import re
import unicodedata

# Explicit lookarounds, never \b: a digit and a letter are both word characters,
# so \b is silently not a boundary in exactly the places it looks like one.
LETTER_REF = re.compile(
    r"(?<![A-Za-z])(?:[Cc]hoice|[Oo]ption|[Aa]nswer)\s+\(?([A-E])\)?(?![A-Za-z])"
)
# An ASCII hyphen with a digit on each side. The character class is spelled out
# rather than using \d so that it cannot match a non-ASCII digit and confuse the
# error message.
DIGIT_HYPHEN = re.compile(r"[0-9]-[0-9]")


def normalize(text):
    """Lowercase, strip accents, drop punctuation, collapse whitespace."""
    t = unicodedata.normalize("NFKD", str(text))
    t = "".join(c for c in t if not unicodedata.combining(c)).lower()
    t = t.replace("’", "'").replace("–", "-").replace("—", "-")
    t = re.sub(r"[^a-z0-9']+", " ", t)
    return re.sub(r"\s+", " ", t).strip()


def _strings(item):
    """Every author-written string in a question, labelled for error messages."""
    out = [("stem", item["q"]), ("why", item["why"])]
    out += [(f"choice {k}", c) for k, c in enumerate(item["choices"])]
    t = item.get("table")
    if t:
        out += [(f"table header {k}", h) for k, h in enumerate(t["headers"])]
        for r, row in enumerate(t["rows"]):
            out += [(f"table cell r{r}c{k}", c) for k, c in enumerate(row)]
    return out


def check(module, arith=None, per_topic=30, n_choices=5):
    """Run every structural check. Raises AssertionError on the first failure.

    `arith` maps a 1-based question number to a function f(table) that
    recomputes, from the table alone, whatever arithmetic that question's stem
    or keyed choice asserts, and returns a one-line description of what it
    recomputed. Every question carrying a `table` must appear in the map; a
    question whose table supports no arithmetic claim says so in its return
    string, so the absence of a claim is a decision on the record rather than
    an omission.
    """
    arith = dict(arith or {})
    code, title, unit = module.TOPIC
    qs = module.QUESTIONS

    assert re.fullmatch(r"[345]\.\d{1,2}", code), f"bad topic code {code!r}"
    assert unit == int(code.split(".")[0]), f"{code}: unit {unit} contradicts the code"
    assert title.strip() == title and title, f"{code}: title not clean"
    assert len(qs) == per_topic, f"{code}: {len(qs)} questions, expected {per_topic}"

    table_qs = set()
    for i, item in enumerate(qs, 1):
        ch, ans, why = item["choices"], item["ans"], item["why"]
        where = f"{code} q{i}"

        assert len(ch) == n_choices, f"{where}: {len(ch)} choices, expected {n_choices}"
        assert isinstance(ans, int) and 0 <= ans < n_choices, (
            f"{where}: answer index {ans!r} out of range"
        )
        assert item["q"].strip(), f"{where}: empty stem"
        assert why.strip(), f"{where}: empty why"
        assert len(why.split()) >= 8, f"{where}: why too thin to be a reason: {why!r}"

        ref = LETTER_REF.search(why)
        assert not ref, (
            f"{where}: why names an option by letter ({ref.group(0)!r}); the "
            "exporter redistributes the key across A-E, so name it by content"
        )

        norms = [normalize(c) for c in ch]
        for a in range(n_choices):
            assert norms[a], f"{where}: choice {a} is empty after normalization"
        for a in range(n_choices):
            for b in range(n_choices):
                if a == b:
                    continue
                if a < b and norms[a] == norms[b]:
                    raise AssertionError(f"{where}: choices {a} and {b} are identical")
                # Padded so containment is measured on whole words, not on a
                # word that merely starts the same way ("vote" inside "voter").
                if norms[a] != norms[b] and f" {norms[a]} " in f" {norms[b]} ":
                    raise AssertionError(
                        f"{where}: choice {a} is contained in choice {b}; the "
                        f"shorter one is true whenever the longer one is\n"
                        f"    {ch[a]!r}\n    {ch[b]!r}"
                    )

        for label, s in _strings(item):
            hit = DIGIT_HYPHEN.search(s)
            assert not hit, (
                f"{where} {label}: {hit.group(0)!r} is a digit-hyphen-digit run, "
                "which mathfmt.convert typesets as a minus sign on export. "
                'Write "5 to 4" or use an en dash.'
            )

        t = item.get("table")
        if t is not None:
            table_qs.add(i)
            assert t["headers"] and t["rows"], f"{where}: empty table"
            w = len(t["headers"])
            for r, row in enumerate(t["rows"]):
                assert len(row) == w, (
                    f"{where}: table row {r} has {len(row)} cells, headers have {w}"
                )
            assert len(t["rows"]) >= 2, f"{where}: a one-row table is not a stimulus"

    missing = sorted(table_qs - set(arith))
    assert not missing, (
        f"{code}: questions {missing} carry a table with no recomputation in ARITH"
    )
    stray = sorted(set(arith) - table_qs)
    assert not stray, f"{code}: ARITH names questions {stray}, which have no table"

    recomputed = []
    for i in sorted(arith):
        note = arith[i](qs[i - 1]["table"])
        assert isinstance(note, str) and note.strip(), (
            f"{code} q{i}: the ARITH function returned nothing to record"
        )
        recomputed.append(f"    q{i}: {note}")

    heads = {}
    for i, item in enumerate(qs, 1):
        h = normalize(item["q"])[:80]
        assert h not in heads, f"{code}: q{i} opens exactly like q{heads[h]}"
        heads[h] = i

    print(f"OK  {code} {title} (unit {unit}): {len(qs)} questions, "
          f"{n_choices} choices each, {len(table_qs)} data stimulus.")
    for line in recomputed:
        print(line)


def pct(part, whole, places=1):
    """A percentage recomputed from two counts, for ARITH functions."""
    return round(100.0 * part / whole, places)


def num(cell):
    """The number in a table cell, ignoring %, commas and a leading currency."""
    s = str(cell).replace(",", "").replace("%", "").replace("$", "").strip()
    return float(s)
