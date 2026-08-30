"""Shared structural checks for the AP Human Geography topic banks (Units 4-7).

There is no sympy here. A geography key rests on a *claim* -- what a model
actually predicts, what a boundary type actually is, what the CED's essential
knowledge actually says -- so nothing in this file can tell you a key is right.
What it CAN do is stop the mechanical failures that have already cost this
project time, and refuse to let a data question make an arithmetic claim that
nobody recomputed.

What each verify_g<unit>_<n>.py supplies
----------------------------------------
ANCHORS
    One short, distinctive substring per question, in module order. It must
    appear in the keyed choice and in NO distractor. That is the part a machine
    can check: if a key index is off by one, or a choice list is reordered
    during an edit, the anchor stops matching and the module fails. It is the
    only guard that survives editing, because export_units.py reshuffles the
    choices on the way out and the written order is not what students see.

TABLE_NOTES
    One entry per question carrying a `table`, keyed by 1-based question number.
    The value is either

        a callable  fn(table) -> str
            which RECOMPUTES the question's arithmetic from the table itself and
            returns a string that must appear in the keyed choice, or

        the exact string "no arithmetic claim"
            for a data question whose key is a pattern reading rather than a
            computation (e.g. "China has a primate city").

    Every table question must be listed, and every listed question must have a
    table. That symmetry is deliberate: the failure mode is not a wrong sum, it
    is a sum nobody looked at, and an optional check is one that gets skipped.

Notes on the checks themselves
------------------------------
Matching uses explicit lookarounds and token-boundary comparison, never `\\b`.
This project has now shipped four separate word-boundary own-goals -- `\\bpi`
never matching because a digit and a letter are both word characters, a
`LETTER_REF` pattern that matched the article "A", a settings check that matched
the "fen" inside "fence", a tag counter that read `<ul` as `<u`. A checker that
under-matches is worse than none, because it trains you to ignore its output.

The superset check compares TOKEN LISTS, not raw substrings, so "ranching" does
not read as contained in "branching" and "state" does not read as contained in
"nation-state". A choice whose whole token sequence sits inside another choice's
is a real defect: the longer option is then strictly more specific and the
shorter one cannot be eliminated on its own terms.

The stimulus check refuses a stem that points at a figure it does not carry.
CLAUDE.md's rule 3 -- "every question needs a real figure, never a prose
description of one" -- exists because a prose description both substitutes for
the picture and leaks the answer. Since this bank can carry a `table` and
nothing else, a stem may not say "the map below" at all.
"""
import re
import unicodedata

# Phrases that promise the student a stimulus. A stem containing one of these
# must carry a `table`; a stem pointing at a map or an image cannot be honoured
# by this bank at all and is rejected outright.
STIMULUS_PHRASES = [
    "the table", "table below", "table above", "the chart", "chart below",
    "the graph", "graph below", "the data below", "the following data",
    "the figure", "figure below", "data in the table", "the data shown",
    "shown below", "the following table",
]
UNSUPPORTED_STIMULUS = [
    "the map below", "map above", "the image below", "the photograph",
    "the satellite image", "the landscape below", "the diagram below",
    "the image above", "the following map", "the following image",
    "the following photograph", "the following diagram",
]

# Pairs of phrasings that name the SAME geographic construct. Two of these in
# one choice list makes the question unanswerable, and it is invisible to a
# duplicate-string check because the strings differ.
SYNONYM_CLASSES = [
    {"least cost theory", "weber's model", "weber model"},
    {"concentric zone model", "burgess model"},
    {"sector model", "hoyt model"},
    {"multiple nuclei model", "harris and ullman model", "harris-ullman model"},
    {"central place theory", "christaller's model"},
    {"world system theory", "world-systems theory", "core-periphery model"},
    {"stages of economic growth", "rostow's model", "modernization model"},
    {"gross national income per capita", "gni per capita"},
    {"human development index", "hdi"},
    {"gender inequality index", "gii"},
    {"exclusive economic zone", "eez"},
    {"united nations convention on the law of the sea", "unclos"},
    {"genetically modified organisms", "gmos"},
    {"community-supported agriculture", "csa"},
    {"special economic zone", "sez"},
    {"shifting cultivation", "swidden agriculture", "slash-and-burn agriculture"},
    {"pastoral nomadism", "nomadic herding"},
    {"metropolitan statistical area", "msa"},
    {"transportation-oriented development", "transit-oriented development"},
    {"squatter settlement", "informal settlement"},
    {"monocropping", "monoculture"},
]


def normalize(text):
    """Lowercase, strip accents, drop punctuation, collapse whitespace."""
    t = unicodedata.normalize("NFKD", str(text))
    t = "".join(c for c in t if not unicodedata.combining(c)).lower()
    t = t.replace("’", "'").replace("–", "-").replace("—", "-")
    t = re.sub(r"[^a-z0-9'%.-]+", " ", t)
    return re.sub(r"\s+", " ", t).strip()


def tokens(text):
    return normalize(text).split()


def _sublist(small, big):
    """True if `small` appears as a contiguous run inside `big`."""
    if not small or len(small) >= len(big):
        return False
    return any(big[i:i + len(small)] == small for i in range(len(big) - len(small) + 1))


def _has_phrase(norm, phrase):
    """Phrase present, delimited by non-alphanumerics on both sides.

    Explicit lookarounds, never \\b: a digit and a letter are both word
    characters, so \\b is silently not a boundary exactly where it looks like
    one.
    """
    p = re.escape(normalize(phrase))
    return re.search(r"(?<![a-z0-9])" + p + r"(?![a-z0-9])", norm) is not None


def synonym_conflicts(choices):
    norms = [normalize(c) for c in choices]
    out = []
    for i in range(len(norms)):
        for j in range(i + 1, len(norms)):
            for cls in SYNONYM_CLASSES:
                hi = [p for p in cls if _has_phrase(norms[i], p)]
                hj = [p for p in cls if _has_phrase(norms[j], p)]
                if hi and hj and set(hi) != set(hj):
                    out.append((i, j, f"same construct: {sorted(hi)} vs {sorted(hj)}"))
                    break
    return out


def check(module, anchors, table_notes=None, per_topic=30, n_choices=5):
    """Run every structural check. Raises AssertionError on the first failure."""
    table_notes = dict(table_notes or {})
    # Counted BEFORE the walk, because the walk pops entries out of the dict as
    # it consumes them -- counting afterwards reported zero every time.
    recomputed = sum(1 for v in table_notes.values() if callable(v))
    code, title, unit = module.TOPIC
    qs = module.QUESTIONS

    assert re.fullmatch(r"\d+\.\d+", code), f"{code!r} is not a topic code"
    assert int(code.split(".")[0]) == unit, f"{code}: code and unit {unit} disagree"
    assert len(qs) == per_topic, f"{code}: {len(qs)} questions, expected {per_topic}"
    assert len(anchors) == per_topic, f"{code}: {len(anchors)} anchors, expected {per_topic}"

    n_tables = 0
    for i, (item, anchor) in enumerate(zip(qs, anchors), 1):
        ch, ans, stem = item["choices"], item["ans"], item["q"]
        where = f"{code} q{i}"

        assert len(ch) == n_choices, f"{where}: {len(ch)} choices, expected {n_choices}"
        assert 0 <= ans < n_choices, f"{where}: answer index {ans} out of range"
        assert len(set(ch)) == n_choices, f"{where}: duplicate choice strings"
        assert len({normalize(c) for c in ch}) == n_choices, (
            f"{where}: two choices identical after normalization")
        assert stem.strip(), f"{where}: empty stem"
        assert item["why"].strip(), f"{where}: empty why"
        assert len(item["why"].split()) >= 8, (
            f"{where}: why is too thin to be a reason: {item['why']!r}")

        # A `why` may not name an option by letter -- export_units.py reshuffles
        # the choices, so "option C" points at whatever lands there.
        letter = re.search(
            r"(?<![A-Za-z])(?:[Cc]hoice|[Oo]ption|[Aa]nswer)\s+\(?([A-E])\)?(?![A-Za-z])",
            item["why"])
        assert not letter, (
            f"{where}: why names an option by letter ({letter.group(0)!r}); "
            "the exporter shuffles choices -- name the option by its content")

        # The anchor pins the key to its TEXT, so an off-by-one index fails here.
        assert normalize(anchor) in normalize(ch[ans]), (
            f"{where}: anchor {anchor!r} not in keyed choice {ch[ans]!r}")
        also = [k for k in range(n_choices)
                if k != ans and normalize(anchor) in normalize(ch[k])]
        assert not also, f"{where}: anchor {anchor!r} also matches choice(s) {also}"

        # No choice may be a token-for-token subsequence of another.
        toks = [tokens(c) for c in ch]
        for a in range(n_choices):
            for b in range(n_choices):
                if a != b and _sublist(toks[a], toks[b]):
                    raise AssertionError(
                        f"{where}: choice {a} is contained in choice {b} "
                        f"({ch[a]!r} inside {ch[b]!r})")

        for a, b, reason in synonym_conflicts(ch):
            raise AssertionError(f"{where}: choices {a} and {b} -- {reason}")

        # A stem may not point at a stimulus it does not carry.
        stem_norm = normalize(stem)
        for phrase in UNSUPPORTED_STIMULUS:
            assert not _has_phrase(stem_norm, phrase), (
                f"{where}: stem promises {phrase!r}, which this bank cannot carry")
        table = item.get("table")
        if any(_has_phrase(stem_norm, p) for p in STIMULUS_PHRASES):
            assert table, f"{where}: stem refers to a stimulus but carries no table"

        if table:
            n_tables += 1
            heads, rows = table["headers"], table["rows"]
            assert heads and rows, f"{where}: table has no headers or no rows"
            for r, row in enumerate(rows):
                assert len(row) == len(heads), (
                    f"{where}: table row {r} has {len(row)} cells, "
                    f"{len(heads)} headers")
            assert i in table_notes, (
                f"{where}: has a table but no TABLE_NOTES entry -- every data "
                "question must either recompute its arithmetic or say in so "
                "many words that it makes no arithmetic claim")
            note = table_notes.pop(i)
            if callable(note):
                got = note(table)
                assert normalize(str(got)) in normalize(ch[ans]), (
                    f"{where}: recomputed {got!r} from the table, but the keyed "
                    f"choice is {ch[ans]!r}")
            else:
                assert note == "no arithmetic claim", (
                    f"{where}: TABLE_NOTES value must be a callable or the exact "
                    f"string 'no arithmetic claim', got {note!r}")
        else:
            assert i not in table_notes, (
                f"{where}: listed in TABLE_NOTES but carries no table")

    assert not table_notes, (
        f"{code}: TABLE_NOTES names questions that do not exist: "
        f"{sorted(table_notes)}")

    # No two stems inside one topic may open the same way.
    heads = {}
    for i, item in enumerate(qs, 1):
        h = normalize(item["q"])[:80]
        assert h not in heads, f"{code}: q{i} opens like q{heads[h]}"
        heads[h] = i

    print(f"OK  {code} {title} (unit {unit}): {len(qs)} questions, "
          f"{n_choices} choices each, {n_tables} with data tables, "
          f"{recomputed} arithmetic claims recomputed.")
