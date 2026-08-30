"""Shared structural gate for the AP U.S. Government and Politics topic banks.

Every ``verify_v<unit>_<topic>.py`` in this directory calls :func:`check`.

WHAT A CHECKER CAN AND CANNOT DO HERE
-------------------------------------
There is no sympy for constitutional law. Nothing in this file can tell you
that *Shaw v. Reno* is about racial gerrymandering rather than about school
prayer; that is what ``AP_US_GOV_CED.md`` and a human reader are for. What a
checker *can* do is guarantee that the mechanical failures which have shipped
in this project before cannot ship again, and that is all this file claims:

* exactly ``per_topic`` questions, indexes 1..N all present;
* exactly ``n_choices`` choices per question, pairwise distinct after
  normalisation, and none a strict textual superset of another (that pattern
  makes a question unanswerable: if A is contained in B, a student who
  believes A must also believe B);
* a valid key index;
* a non-empty ``why`` that is a reason rather than a stub -- enforced as a
  minimum length, because "it is the definition" is the failure mode;
* no two questions in the module sharing a stem;
* every question whose stem refers to a table/chart/graph/figure actually
  CARRIES a ``table``, and every question that carries a ``table`` has its
  arithmetic recomputed from that table in the module's verifier.

THE KEY-FIRST INVARIANT
-----------------------
Every module in this bank is written key-first: ``ans=0`` on every question,
the same house style as ``p3_1.py``. ``export_units.py`` redistributes the key
across A-E deterministically on the way out, so the shipped bank is balanced
and the source file stays auditable by eye -- the first choice is the answer,
always, so a reader checking 30 keys never has to count choice positions.

That invariant is the substitute for a per-question answer-anchor list. An
anchor list guards against a key index drifting away from the choice it was
written for; ``ans == 0`` on every question is the same guarantee, stated once
and checked mechanically, and it cannot itself be written wrong. A module that
genuinely needs an ordered choice list (a numeric ladder, a chronology) may
pass ``allow_ordered={indexes}``, which exempts exactly those questions and
requires the verifier's author to have thought about each one.

WHY THE SUPERSET CHECK USES NORMALISED WORDS, NOT ``in``
--------------------------------------------------------
A raw substring test reports "Congress" inside "Congressional" and would fire
on half the bank. This project's recurring own-goal is a checker that over- or
under-matches (``\\bpi`` never matching, ``LETTER_REF`` matching the article
"A"), so the containment test here runs over whole normalised WORD SEQUENCES:
choice X is a superset of choice Y only when Y's full word list appears as a
contiguous run inside X's word list. "Congress" and "Congressional" have
different words and do not collide.
"""
import re
import sys
import unicodedata

_FIGURE = re.compile(r"(?<![A-Za-z])(table|chart|graph|figure|infographic)(?![A-Za-z])",
                     re.IGNORECASE)
_NUM = re.compile(r"-?\d+(?:\.\d+)?")


def _norm(text):
    """Casefolded, punctuation-flattened word list for comparison."""
    t = unicodedata.normalize("NFKD", text)
    t = t.replace("’", "'").replace("‘", "'")
    t = t.replace("“", '"').replace("”", '"').replace("—", " ")
    t = re.sub(r"[^0-9a-z']+", " ", t.casefold())
    return t.split()


def _contiguous(small, big):
    """True when the word list ``small`` appears as a contiguous run in ``big``."""
    if not small or len(small) >= len(big):
        return False
    for i in range(len(big) - len(small) + 1):
        if big[i:i + len(small)] == small:
            return True
    return False


# --- helpers a verifier uses to recompute a table's arithmetic ---------------

def number(text):
    """The first number in a cell, with %, $, commas and footnote marks removed."""
    m = _NUM.search(str(text).replace(",", ""))
    if m is None:
        raise ValueError(f"no number in cell {text!r}")
    return float(m.group())


def col(table, header):
    """Every value in the named column, as floats, in row order."""
    j = table["headers"].index(header)
    return [number(row[j]) for row in table["rows"]]


def labels(table):
    """The first column of every row, as written."""
    return [row[0] for row in table["rows"]]


def cell(table, row_label, header):
    """One cell, as a float, addressed by its row label and column header."""
    j = table["headers"].index(header)
    for row in table["rows"]:
        if row[0] == row_label:
            return number(row[j])
    raise KeyError(f"no row labelled {row_label!r}")


# --- the gate ---------------------------------------------------------------

def check(module, table_checks=None, per_topic=30, n_choices=5,
          allow_ordered=frozenset(), min_why=60):
    name = module.__name__
    qs = module.QUESTIONS
    code, title, unit = module.TOPIC
    table_checks = table_checks or {}
    fail = []

    if len(qs) != per_topic:
        fail.append(f"expected {per_topic} questions, found {len(qs)}")
    if not code.startswith(f"{unit}."):
        fail.append(f"TOPIC code {code!r} does not belong to unit {unit}")

    seen_stems = {}
    for i, item in enumerate(qs, 1):
        where = f"q{i}"
        ch = item["choices"]
        if len(ch) != n_choices:
            fail.append(f"{where}: {len(ch)} choices, expected {n_choices}")
            continue
        if not 0 <= item["ans"] < len(ch):
            fail.append(f"{where}: key index {item['ans']} out of range")
            continue
        if item["ans"] != 0 and i not in allow_ordered:
            fail.append(f"{where}: key is not written first (ans={item['ans']}); "
                        "add the index to allow_ordered if the order is deliberate")

        words = [_norm(c) for c in ch]
        if len({" ".join(w) for w in words}) != len(ch):
            fail.append(f"{where}: two choices are the same text")
        for a in range(len(ch)):
            for b in range(len(ch)):
                if a != b and _contiguous(words[a], words[b]):
                    fail.append(f"{where}: choice {'ABCDE'[a]} is contained whole "
                                f"inside choice {'ABCDE'[b]}")
        for k, c in enumerate(ch):
            if not c.strip():
                fail.append(f"{where}: choice {'ABCDE'[k]} is empty")

        why = item.get("why", "")
        if len(why.strip()) < min_why:
            fail.append(f"{where}: why is {len(why.strip())} chars, "
                        f"needs at least {min_why} and must give the reason")

        stem = " ".join(_norm(item["q"]))
        if stem in seen_stems:
            fail.append(f"{where}: stem duplicates q{seen_stems[stem]}")
        seen_stems.setdefault(stem, i)

        table = item.get("table")
        if table is None:
            # A stem that talks about a figure must carry one. Quoting a
            # document that happens to use the word is not a figure reference,
            # so only look outside quoted material.
            unquoted = re.sub(r"[“\"][^”\"]*[”\"]", " ", item["q"])
            if _FIGURE.search(unquoted):
                fail.append(f"{where}: stem refers to a figure but carries no table")
        else:
            if set(table) != {"headers", "rows"}:
                fail.append(f"{where}: table needs exactly headers and rows")
            elif any(len(r) != len(table["headers"]) for r in table["rows"]):
                fail.append(f"{where}: a row's width does not match the headers")
            if i not in table_checks:
                fail.append(f"{where}: carries a table but the verifier "
                            "recomputes nothing from it")

    for i, claims in table_checks.items():
        if not 1 <= i <= len(qs):
            fail.append(f"table check names q{i}, which does not exist")
            continue
        if qs[i - 1].get("table") is None:
            fail.append(f"q{i}: table check on a question with no table")
            continue
        for desc, fn in claims:
            try:
                ok = fn(qs[i - 1]["table"])
            except Exception as exc:                      # noqa: BLE001
                fail.append(f"q{i}: table check {desc!r} raised {exc!r}")
                continue
            if not ok:
                fail.append(f"q{i}: table check failed -- {desc}")

    if fail:
        print(f"FAIL {name} ({code} {title})")
        for f in fail:
            print("  -", f)
        sys.exit(1)
    n_tables = sum(1 for q in qs if q.get("table"))
    n_claims = sum(len(v) for v in table_checks.values())
    print(f"OK {name}: {code} {title} (unit {unit}) -- {len(qs)} questions, "
          f"{n_choices} choices each, {n_tables} data questions, "
          f"{n_claims} arithmetic claims recomputed")
