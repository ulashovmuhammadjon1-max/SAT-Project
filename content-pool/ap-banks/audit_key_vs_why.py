"""Find questions whose explanation argues for a choice other than the keyed one.

This exists because of a real defect. Macro 3.1 asked what a decrease in
aggregate demand is, keyed "a higher price level with the same output", and
carried the explanation "a shift means the quantity of real GDP demanded changes
at every possible price level" — which argues for a different choice that was
sitting right there as a distractor. Two independent readers went through 2,100
questions and only one of them caught it.

The signal is mechanical: an explanation is written to justify the correct
answer, so its content words should overlap the key more than any distractor.
Where a distractor overlaps the explanation substantially more, either the key
or the explanation is wrong, and both are worth a person's attention.

This screens; it does not decide. Overlap is a weak proxy — a well-written
explanation often paraphrases rather than echoes — so the output is a reading
list ordered by suspicion, and nothing is changed on its say-so.
"""
import argparse
import importlib
import re
import sys

# Words too common in economics prose to carry any signal about which choice an
# explanation is pointing at.
STOP = {
    "the", "a", "an", "of", "to", "in", "is", "are", "and", "or", "that", "this",
    "it", "its", "as", "at", "by", "for", "on", "with", "from", "be", "been",
    "was", "were", "not", "no", "than", "so", "if", "when", "which", "what",
    "more", "less", "most", "least", "each", "every", "all", "any", "both",
    "will", "would", "can", "could", "may", "might", "must", "should", "does",
    "do", "has", "have", "had", "there", "their", "they", "one", "two", "but",
    "while", "because", "since", "only", "same", "other", "another", "own",
    "means", "meaning", "rather", "into", "over", "under", "up", "down",
}


def words(text: str) -> set[str]:
    """Content words, lowercased. Hyphens are kept so 'short-run' stays one token."""
    return {
        w
        for w in re.findall(r"[a-z][a-z-]+", text.lower())
        if w not in STOP and len(w) > 2
    }


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("modules", nargs="+")
    ap.add_argument(
        "--margin",
        type=int,
        default=2,
        help="report when a distractor beats the key by at least this many shared words",
    )
    args = ap.parse_args()

    rows = []
    for mod_name in args.modules:
        m = importlib.import_module(mod_name)
        code, _title, _unit = m.TOPIC

        for i, item in enumerate(m.QUESTIONS, 1):
            why = words(item["why"])
            if not why:
                continue
            scores = [len(why & words(c)) for c in item["choices"]]
            key_score = scores[item["ans"]]
            best_other = max(
                (s for j, s in enumerate(scores) if j != item["ans"]), default=0
            )
            gap = best_other - key_score
            if gap >= args.margin:
                rows.append((gap, mod_name, code, i, item, scores))

    # Most suspicious first: a person reading from the top should hit the real
    # defects before the noise.
    rows.sort(key=lambda r: -r[0])
    for gap, mod_name, code, i, item, scores in rows:
        j = scores.index(max(scores))
        print(f"[gap {gap}] {mod_name} ({code}) q{i}")
        print(f"    stem : {item['q'][:100]}")
        print(f"    key  : {item['choices'][item['ans']][:90]}")
        print(f"    but  : {item['choices'][j][:90]}")
        print(f"    why  : {item['why'][:110]}")

    print(f"\n{len(rows)} question(s) where a distractor matches the explanation better.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
