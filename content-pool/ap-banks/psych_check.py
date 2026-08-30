"""Shared structural + synonym checks for the AP Psychology topic banks.

There is no sympy here. A psychology key rests on a *claim* -- a definition, a
named study's actual result, or what a theory actually predicts -- so each
verify_p<unit>_<topic>.py supplies a CLAIMS list with one entry per question:

    (anchor, claim)

`anchor` is a distinctive substring that MUST appear in the keyed choice. That
is the part a computer can check: if a key index is off by one, or a choice list
is reordered during editing, the anchor stops matching and the module fails.
`claim` is the sentence stating what the key rests on, written for a human
reader to audit. An unstated assertion is how a wrong key ships.

SYNONYM CLASSES
---------------
In psychology the real duplicate-answer defect is not two identical strings, it
is two phrasings of the same construct -- "client-centered therapy" and
"person-centered therapy" in one choice list makes a question unanswerable.
Every class below is a set of MULTI-WORD technical phrases, matched with
explicit non-letter delimiters rather than \\b, because a boundary-free
substring match in a checker is worse than no check at all.
"""
import re
import unicodedata

SYNONYM_CLASSES = [
    # --- attribution ---
    {"fundamental attribution error", "correspondence bias"},
    {"dispositional attribution", "internal attribution", "personal attribution"},
    {"situational attribution", "external attribution"},
    # --- personality ---
    {"emotional stability", "low neuroticism"},
    {"neuroticism", "emotional instability"},
    {"openness to experience", "openness"},
    {"self-efficacy", "belief in one's own capability", "belief in her own capability"},
    # --- therapy names ---
    {"person-centered therapy", "client-centered therapy", "rogerian therapy"},
    {"rational-emotive behavior therapy", "rebt"},
    {"dialectical behavior therapy", "dbt"},
    {"electroconvulsive therapy", "ect"},
    {"transcranial magnetic stimulation", "tms"},
    {"applied behavior analysis", "aba"},
    {"exposure therapy", "exposure-based therapy"},
    # --- drugs ---
    {"antipsychotic medication", "neuroleptic medication"},
    {"antianxiety medication", "anxiolytic medication"},
    {"psychoactive medication", "psychotropic medication"},
    # --- disorders and symptoms ---
    {"flat affect", "blunted affect", "diminished emotional expression"},
    {"major depressive disorder", "unipolar depression", "clinical depression"},
    {"attention-deficit/hyperactivity disorder", "adhd"},
    {"autism spectrum disorder", "asd"},
    {"generalized anxiety disorder", "gad"},
    {"posttraumatic stress disorder", "ptsd"},
    {"obsessive-compulsive disorder", "ocd"},
    {"dissociative identity disorder", "did"},
    {"delusion", "false belief"},
    {"hallucination", "false perception"},
    # --- stress and health ---
    {"general adaptation syndrome", "gas"},
    {"eustress", "motivating stress"},
    {"problem-focused coping", "problem-focused strategy"},
    {"emotion-focused coping", "emotion-focused strategy"},
    # --- motivation ---
    {"intrinsic motivation", "internal motivation"},
    {"extrinsic motivation", "external motivation"},
    {"drive-reduction theory", "drive reduction theory"},
    {"self-determination theory", "sdt"},
]


def normalize(text):
    """Lowercase, strip accents and punctuation, collapse whitespace."""
    t = unicodedata.normalize("NFKD", text)
    t = "".join(c for c in t if not unicodedata.combining(c)).lower()
    t = t.replace("’", "'").replace("–", "-").replace("—", "-")
    t = re.sub(r"[^a-z0-9'/-]+", " ", t)
    return re.sub(r"\s+", " ", t).strip()


def _contains_phrase(choice_norm, phrase):
    """Phrase present in the choice, delimited by non-letters on both sides.

    Explicit lookarounds, never \\b: a digit and a letter are both word
    characters, so \\b silently fails to be a boundary exactly where it looks
    like one.
    """
    p = re.escape(normalize(phrase))
    return re.search(r"(?<![a-z0-9])" + p + r"(?![a-z0-9])", choice_norm) is not None


def synonym_conflicts(choices):
    """Pairs of choices in one question that name the same construct."""
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


def check(module, claims, per_topic=25, n_choices=5):
    """Run every structural and key check. Raises AssertionError on failure."""
    code, title, unit = module.TOPIC
    qs = module.QUESTIONS
    assert len(qs) == per_topic, f"{code}: {len(qs)} questions, expected {per_topic}"
    assert len(claims) == per_topic, f"{code}: {len(claims)} claims, expected {per_topic}"

    for i, (item, (anchor, claim)) in enumerate(zip(qs, claims), 1):
        ch, ans = item["choices"], item["ans"]
        assert len(ch) == n_choices, f"{code} q{i}: {len(ch)} choices, expected {n_choices}"
        assert 0 <= ans < n_choices, f"{code} q{i}: answer index {ans} out of range"
        assert len(set(ch)) == n_choices, f"{code} q{i}: duplicate choice strings"
        assert item["q"].strip() and item["why"].strip(), f"{code} q{i}: empty stem or why"

        # The claim must be a real sentence, not a placeholder.
        assert len(claim.split()) >= 6, f"{code} q{i}: claim too thin to audit: {claim!r}"

        # The anchor pins the key to its TEXT, so an off-by-one index fails here.
        assert normalize(anchor) in normalize(ch[ans]), (
            f"{code} q{i}: anchor {anchor!r} not in keyed choice {ch[ans]!r}"
        )
        # ...and the anchor must not also match a distractor, or it pins nothing.
        others = [k for k in range(n_choices)
                  if k != ans and normalize(anchor) in normalize(ch[k])]
        assert not others, f"{code} q{i}: anchor {anchor!r} also matches choice(s) {others}"

        for a, b, reason in synonym_conflicts(ch):
            raise AssertionError(f"{code} q{i}: choices {a} and {b} -- {reason}")

    # No two stems inside one topic may open the same way.
    heads = {}
    for i, item in enumerate(qs, 1):
        h = normalize(item["q"])[:80]
        assert h not in heads, f"{code}: q{i} opens like q{heads[h]}"
        heads[h] = i

    print(f"OK  {code} {title} (unit {unit}): {len(qs)} questions, "
          f"{len(claims)} claims stated, no synonym collisions.")
